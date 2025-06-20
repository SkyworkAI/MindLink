DATASET="princeton-nlp/SWE-bench_Verified"
OUTPUT_FOLDER="results/MindLink_Beta"

export MODEL_NAME="MindLink_Beta"
export BASE_URL=""
export API_KEY="xxxxx"
export API_KEY=""

export PYTHONPATH=$PYTHONPATH:$(pwd)
export PROJECT_FILE_LOC=repo_structures


# python agentless/fl/localize.py --file_level \
#         --output_folder $OUTPUT_FOLDER/file_level \
#         --num_threads 100 \
#         --dataset $DATASET \
#         --model $MODEL_NAME \
#         --skip_existing 

# python agentless/fl/localize.py --related_level \
#         --output_folder $OUTPUT_FOLDER/related_elements \
#         --top_n 3 \
#         --compress_assign \
#         --compress \
#         --start_file $OUTPUT_FOLDER/file_level/loc_outputs.jsonl \
#         --num_threads 100 \
#         --skip_existing \
#         --model $MODEL_NAME \
#         --dataset $DATASET 

# python agentless/fl/localize.py --fine_grain_line_level \
#         --output_folder $OUTPUT_FOLDER/edit_location_samples \
#         --top_n 3 \
#         --compress \
#         --temperature 0.00001 \
#         --num_samples 1 \
#         --start_file $OUTPUT_FOLDER/related_elements/loc_outputs.jsonl \
#         --num_threads 100 \
#         --skip_existing \
#         --model $MODEL_NAME \
#         --dataset $DATASET

# python agentless/fl/localize.py --merge \
#         --output_folder $OUTPUT_FOLDER/edit_location_individual \
#         --top_n 3 \
#         --num_samples 1 \
#         --start_file $OUTPUT_FOLDER/edit_location_samples/loc_outputs.jsonl 


python agentless/repair/repair.py --loc_file $OUTPUT_FOLDER/edit_location_individual/loc_merged_0-0_outputs.jsonl \
        --output_folder $OUTPUT_FOLDER/repair_sample_1 \
        --loc_interval \
        --top_n=3 \
        --context_window=10 \
        --max_samples 1  \
        --cot \
        --diff_format \
        --gen_and_process \
        --num_threads 100 \
        --model $MODEL_NAME \
        --dataset $DATASET
