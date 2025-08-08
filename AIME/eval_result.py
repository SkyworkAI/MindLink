"""
Run inference for AIME2024 and AIME2025
python eval_result.py --config config_32B --num_workers 30 --input_json AIME2024.json --output_jsonl test—aime24_32B.jsonl --num_repeat 10
python eval_result.py --config config_72B --num_workers 30 --input_json AIME2024.json --output_jsonl test—aime24_72B.jsonl --num_repeat 10
python eval_result.py --config config_32B --num_workers 30 --input_json AIME2025.json --output_jsonl test—aime25_32B.jsonl --num_repeat 10
python eval_result.py --config config_72B --num_workers 30 --input_json AIME2025.json --output_jsonl test—aime25_72B.jsonl --num_repeat 10

"""

import json
import os
import datetime
from tqdm import tqdm
import openai
from concurrent.futures import ThreadPoolExecutor, as_completed

def load_local_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        item['id'] = i
    return data

def save_to_jsonl(data, file_path):
    with open(file_path, "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")

def clean_non_serializable(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, (dict, list)):
        return (
            {k: clean_non_serializable(v) for k, v in obj.items()}
            if isinstance(obj, dict)
            else [clean_non_serializable(v) for v in obj]
        )
    return obj

def process_single(record, gen_client, judge_client, config, judge_prompt_template, output_path):
    prompt = record["question"]
    reference_answer = str(record["answer"])
    set_name = record.get("set", "")

    messages = [{"role": "user", "content": prompt}]
    gen_response = gen_client.chat.completions.create(
        model=config["GEN_MODEL_NAME"],
        messages=messages,
        timeout=config["TIMEOUT"],
        temperature=config["TEMPERATURE"],
    )
    gen_result = gen_response.choices[0].message.content.strip()
    gen_raw = gen_response.model_dump() if hasattr(gen_response, "model_dump") else gen_response.__dict__

    judge_prompt = judge_prompt_template.replace("{{generate_answer}}", gen_result).replace("{{real_answer}}", reference_answer)
    judge_messages = [{"role": "user", "content": judge_prompt}]
    judge_response = judge_client.chat.completions.create(
        model=config["JUDGE_MODEL_NAME"], messages=judge_messages, timeout=60
    )
    judge_content = (judge_response.choices[0].message.content or "").strip()
    judge_raw = judge_response.model_dump() if hasattr(judge_response, "model_dump") else judge_response.__dict__

    result = {
        "question": prompt,
        "answer": reference_answer,
        "set": set_name,
        "generated": gen_result,
        "judge_result": judge_content,
        "id": record.get("id"),
        "gen_raw": clean_non_serializable(gen_raw),
        "judge_raw": clean_non_serializable(judge_raw),
        "gen_model": config["GEN_MODEL_NAME"],
        "judge_model": config["JUDGE_MODEL_NAME"],
    }
    save_to_jsonl(result, output_path)
    return result, judge_content

if __name__ == "__main__":
    import importlib
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default="config_32B", help="config_32B or config_72B")
    parser.add_argument('--max_count', type=int, default=None)
    parser.add_argument('--num_repeat', type=int, default=1)
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--output_jsonl', type=str, default=None)
    parser.add_argument('--input_json', type=str, default="AIME2025.json", help="Path to AIME2025.json")
    args = parser.parse_args()
    
    CONFIG = importlib.import_module(args.config).CONFIG

    dataset = load_local_json(args.input_json)
    if args.max_count:
        dataset = dataset[:min(args.max_count, len(dataset))]
    output_path = args.output_jsonl if args.output_jsonl else CONFIG["OUTPUT_JSONL"]


    gen_client = openai.OpenAI(api_key=CONFIG["VLLM_API_KEY"], base_url=CONFIG["VLLM_URL"])
    judge_client = gen_client if CONFIG["JUDGE_MODEL_NAME"] == CONFIG["GEN_MODEL_NAME"] else openai.AzureOpenAI(
        api_key=CONFIG["AZURE_OPENAI_KEY"],
        azure_endpoint=CONFIG["AZURE_ENDPOINT"],
        api_version=CONFIG["AZURE_API_VERSION"],
    )

    stats = []
    for repeat_idx in range(args.num_repeat):
        correct, total = 0, 0
        futures = []
        cur_output_path = output_path.replace(".jsonl", f"_{repeat_idx+1}.jsonl")
        if os.path.exists(cur_output_path):
            os.remove(cur_output_path)
            print(f"Removed {cur_output_path}")
        with ThreadPoolExecutor(max_workers=args.num_workers) as executor:
            for record in dataset:
                futures.append(
                    executor.submit(
                        process_single, record, gen_client, judge_client, CONFIG, CONFIG["JUDGE_PROMPT_TEMPLATE_EN"], cur_output_path
                    )
                )
            for f in tqdm(as_completed(futures), total=len(futures), desc=f"Evaluating {args.input_json} ({repeat_idx+1}/{args.num_repeat})"):
                try:
                    _, judge = f.result()
                    total += 1
                    if str(judge).strip() in ["1", "True", "true", "正确"]:
                        correct += 1
                except Exception as e:
                    print("Error:", e)
        acc = correct / total if total else 0.0
        print(f"Run {repeat_idx+1}: total={total}, correct={correct}, acc={acc:.4f}")
        stats.append(acc)

    if args.num_repeat > 1:
        print("\nAverage acc over %d runs: %.4f" % (args.num_repeat, sum(stats)/len(stats)))
    else:
        print(f"\nAccuracy: {stats[0]:.4f}")
