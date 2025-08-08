CONFIG = {
    "OUTPUT_JSONL": "result_MindLink_72B.jsonl",

    "GEN_MODEL_NAME": "Mind_Link_beta_72B",
    "VLLM_URL": "https://api.com/v1",
    "VLLM_API_KEY": "VLLM_API_KEY",
    "TIMEOUT": 2000,
    "TEMPERATURE": 0.6,
    
    "JUDGE_MODEL_NAME": "gpt-4.1-250414",
    "AZURE_OPENAI_KEY": "AZURE_OPENAI_KEY",
    "AZURE_ENDPOINT": "https://openai.azure.com/",
    "AZURE_API_VERSION": "2025-01-01-preview",

    "JUDGE_PROMPT_TEMPLATE_EN": (
        "Below are the model's generated answer and the reference answer. "
        "Please judge if the generated answer is correct. "
        "Only answer 1 (for correct) or 0 (for incorrect).\n\n"
        "Model's generated answer: {{generate_answer}}\n\n"
        "Reference answer: {{real_answer}}\n"
    )
}