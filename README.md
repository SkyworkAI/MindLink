# MindLink

[English](README.md) | [中文](README_CN.md)

## Model Description

We introduce **MindLink**, a new family of large language models developed by **Kunlun Inc**. Built on **Qwen**, these models incorporate our latest advances in post-training techniques. MindLink demonstrates strong performance across various common benchmarks and is widely applicable in diverse AI scenarios. We welcome feedback to help us continuously optimize and improve our models.

### 🚀 Model Downloads

<div align="center">

| **🤖 Model** | **📏 Context Length** | **⬇️ Download** |
| :---: | :---: | :---: |
| **MindLink 32B** | `128K` | [🤗 **HuggingFace**](https://huggingface.co/Skywork/MindLink-32B-0801) |
| **MindLink 72B** | `128K` | [🤗 **HuggingFace**](https://huggingface.co/Skywork/MindLink-72B-0801) |

</div>



### 📖 Technical Report
Our training methodology and evaluation: [MindLink](mindlink.pdf)

---

## Highlights

* **Plan-based Reasoning**: Without the "think" tag, MindLink achieves competitive performance with leading proprietary models across a wide range of reasoning and general tasks. It significantly reduces inference cost, and improves multi-turn capabilities.
* **Mathematical Framework**: It analyzes the effectiveness of both **Chain-of-Thought (CoT)** and **Plan-based Reasoning**.
* **Adaptive Reasoning**: it automatically adapts its reasoning strategy based on task complexity: complex tasks produce detailed reasoning traces, while simpler tasks yield concise outputs. 

---

## API Access

📢 We provide developers with a **one-month free trial** of our API for exploring and testing our models. To request access to an **Open WebUI account** (https://sd1svahsfo0m61h76e190.apigateway-cn-beijing.volceapi.com), please contact us at: **[mindlink@skywork.ai](mailto:mindlink@skywork.ai)**

⚠️ Note: If you encounter inconsistent responses during inference, we recommend clearing the session context (history) and retrying.

### 🔧 Usage Instructions

Our Chat API supports OpenAI's format. Simply include your API Key with HTTP POST requests.

#### ✅ Sample Request using `curl`:

```bash
curl -X POST https://sd2690u280c6ft26qcdi0.apigateway-cn-beijing.volceapi.com/v1/chat/completions \
     -H "Authorization: Bearer nc6Dt7DrLJNzLELiqOR1bogO5Oh1qHtO" \
     -H "Content-Type: application/json" \
     -d '{
           "model": "Mind_Link_beta_32B",
           "messages": [
             {"role": "user", "content": "What is the capital of China?"}
           ],
           "temperature": 0.7,
           "max_tokens": 128,
           "stream": false
         }'
```

#### 🐍 Sample Request using Python:

```python
import requests

API_KEY = "nc6Dt7DrLJNzLELiqOR1bogO5Oh1qHtO"
API_URL = "https://sd2690u280c6ft26qcdi0.apigateway-cn-beijing.volceapi.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Mind_Link_beta_32B",
    "messages": [
        {"role": "user", "content": "What is the capital of China?"}
    ],
    "temperature": 0.7,
    "max_tokens": 128,
    "stream": False
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    reply = response.json()
    print("MindLink Response:")
    print(reply["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}: {response.text}")
```

---

### 🌐 API Interface Details

* **Endpoint**: `https://sd2690u280c6ft26qcdi0.apigateway-cn-beijing.volceapi.com/v1/chat/completions`
* **Authentication**: Use your API key via `Authorization: Bearer <api_key>`
* **Request Format**: Compatible with OpenAI's Chat Completion API
* **Supported Fields**: `model`, `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, etc.
* **Model Identifiers**: Use either `"Mind_Link_beta_32B"` or `"Mind_Link_beta_72B"`
* **Public API Key**: We provide the following public API key: `"nc6Dt7DrLJNzLELiqOR1bogO5Oh1qHtO"` (requests via this key enter a queue and have limited request rates; contact us for unlimited access).


---

## Evaluation

The results are shown below:
![Comparison between MindLink (ML) and other frontier models across various benchmarks.](./figure1.png)

---

## License and Usage Information

### Model License and Terms of Use

#### 1. Core License

This model is licensed under the **Apache License 2.0**, granting users the following rights:

✅ Commercial deployment

✅ Source code modification

✅ Patent authorization

✅ Closed-source derivatives

⚠️ Prohibition on using model names/logos for promotion without written authorization

⚠️ No warranties provided

#### 2. Inheritance Declaration

This model is based on improvements from **Qwen** (Apache 2.0 License). You must:

* Retain original Qwen copyright notices in derivative works.
* Clearly document changes made in modification notes.
* Adhere to any additional usage restrictions imposed by Qwen.

If you have any questions, please raise an issue or contact us at mindlink@skywork.ai.



---
