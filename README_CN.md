
# MindLink

[English](README.md) | [中文](README_CN.md)

## 模型介绍

我们推出了全新的大语言模型系列 **MindLink**，由**昆仑万维** 开发。我们使用了最新的后训练（post-training）技术来改进了 **Qwen** 模型的效果，在多个通用基准测试中，MindLink 展现了较强的性能，能够广泛应用于多种 AI 场景。我们欢迎各方反馈，以帮助我们不断优化和改进模型。

### 🚀 模型下载

<div align="center">

| **🤖 模型** | **📏 上下文长度** | **⬇️ 下载** |
| :---: | :---: | :---: |
| **MindLink 32B** | `128K` | [🤗 **HuggingFace**](https://huggingface.co/Skywork/MindLink-32B-0801) |
| **MindLink 72B** | `128K` | [🤗 **HuggingFace**](https://huggingface.co/Skywork/MindLink-72B-0801) |

</div>


### 📖 技术报告
详细训练方法和评估: [MindLink](mindlink.pdf)

---

## 模型亮点

* 推出全新推理大模型，新的推理范式:Plan-based Reasoning，去掉了"think"标签，减少了推理成本和增强了多轮对话能力，增强了推理过程的可读性和相关性。

* 提出一套数学方法，尝试分析CoT和Plan-based Reasoning的有效性。

* 提出一套自适应的推理机制，根据任务难度，整合推理和非推理的生成长度。

* MindLink模型，是基于Qwen3-32B和Qwen2.5-72B，进行了后训练，提高了原本模型能力，未来会开源更多尺寸模型。

## API 接入

📢 我们为开发者提供了一个月的免费 API 调用额度来探索与测试我们的模型。同时如需申请 Open WebUI 的账户（https://sd1svahsfo0m61h76e190.apigateway-cn-beijing.volceapi.com）， 请发送邮件联系我们~ **[mindlink@skywork.ai](mailto:mindlink@skywork.ai)**。

### 🔧 使用说明

我们的聊天 API 支持 OpenAI 格式，使用时只需将 API Key 加入到 HTTP POST 请求即可。

⚠️ 注意： 如果模型返回的结果出现异常或不符合预期，建议清除上下文历史记录（history）后重新尝试。

#### ✅ 使用 `curl` 发起请求的示例：

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

#### 🐍 使用 Python 发起请求的示例：

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
    print("MindLink 响应内容：")
    print(reply["choices"][0]["message"]["content"])
else:
    print(f"请求错误 {response.status_code}: {response.text}")
```

---

### 🌐 API 接口详情

* **接口地址**：`https://sd2690u280c6ft26qcdi0.apigateway-cn-beijing.volceapi.com/v1/chat/completions`
* **认证方式**：使用您的 API Key，以 `Authorization: Bearer <api_key>` 格式认证
* **请求格式**：兼容 OpenAI 的聊天（Chat Completion）API 格式
* **支持字段**：`model`、`messages`、`temperature`、`top_p`、`max_tokens`、`stream`、`stop` 等
* **模型标识符**：模型名选项： `"Mind_Link_beta_32B"`、`"Mind_Link_beta_72B"`
* **API Key**：我们公开如下的 API Key 以供更便捷地使用我们的模型：`"nc6Dt7DrLJNzLELiqOR1bogO5Oh1qHtO"`（通过该API Key发送的请求会进入队列并且限制请求速率，如需更快的访问速率，请邮件联系我们申请单独的API Key~）


---

## 模型评估

结果如下:
![MindLink和各大先进模型对比](./figure1.png)

---

## 许可证与使用信息

## 模型许可证与使用条款

### 1. 核心许可证
本模型采用 **Apache License 2.0** 授权，用户享有以下权利：

✅ 商业部署 

✅ 修改源代码

✅ 专利授权

✅ 闭源衍生  

⚠️ 禁止使用模型名称/logo进行推广（需书面授权）  

⚠️ 不提供任何担保

### 2. 继承声明
本模型基于 **Qwen**（Apache 2.0 协议）改进开发，您必须：
- 在衍生作品中保留原始Qwen版权声明
- 在修改说明中清晰标注变动内容
- 遵守Qwen模型的附加使用限制

