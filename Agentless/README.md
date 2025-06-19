# MindLink (Beta) – Reproduction Guide for SWE-bench Verified

| Item | Value |
|------|-------|
| **Split evaluated** | `SWE-bench_Verified / test` (500 instances) |
| **Resolved instances** | 366 / 500  →  **73 .2 %** |
| **Model endpoint** | `https://sd15vu0fhj5i8uvr669og.apigateway-cn-beijing.volceapi.com/v1` |
| **Model name** | MindLink-Beta|

---

## 1. Quick Start

```bash
# ❶ Clone & create environment
git clone https://github.com/SkyworkAI/MindLink.git
cd MindLink/Agentless
conda env create -n agentless python=3.11
conda activate agentless
pip install -r requirements.txt   # agentless + swe-bench deps

# ❷ Download and extract repo_structures
# Download the preprocessed repository structures from https://github.com/OpenAutoCoder/Agentless/releases/download/v1.5.0/swebench_repo_structure.zip
# Extract it to MindLink/Agentless/repo_structures

# ❸ Set environment variables
export MODEL_NAME="MindLink_Beta"
export BASE_URL="https://sd15vu0fhj5i8uvr669og.apigateway-cn-beijing.volceapi.com/v1"
export API_KEY="<YOUR_API_KEY>"
export PROJECT_FILE_LOC=$(pwd)/repo_structures
export PYTHONPATH=$PYTHONPATH:$(pwd)

# ❹ Run the verification script
bash run_verified.sh
```

## 2. Workflow

The `run_verified.sh` script executes the following steps:

1. **Localization**: Identifies fault locations at the file, function, and line levels.
2. **Repair**: Generates candidate patches for the identified faults.
3. **Patch Validation**: Selects the most appropriate patch based on test outcomes.

These steps align with the Agentless framework's methodology ([github.com](https://github.com/OpenAutoCoder/Agentless)).


## 3. Model Overview

The MindLink series features a family of dense transformer models, scaling from 24B to 123B parameters. This experimental release, MindLink Beta, is built upon [**mistralai/Mistral-Small-24B-Instruct-2501**](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) as the base model with 24B parameters. The post-training pipeline contains three key stages: continued pre-training, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF), with a primary focus on Proximal Policy Optimization (PPO). Our high-quality training dataset comprises over 2 million carefully curated data points. 

In our ongoing research, we have been investigating a potential reasoning methodology for complex problem-solving tasks. We continue to develop additional models within the series and hope to share detailed technical insights through our upcoming research publications. This experimental release aims to collect community feedback while we iteratively enhance our approach.

Please note that current API responses exclude detailed reasoning processes for data security and proprietary considerations. The complete reasoning traces and methodological insights will be made available upon the publication of our technical reports, providing full transparency into our approach and findings.