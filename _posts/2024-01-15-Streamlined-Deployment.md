---
title: 'Streamlined Deployment And Integration Of Large Language Models With Pai Eas'
date: 2024-01-15
permalink: /posts/2024-01/Streamlined-Deployment/
tags:
  - cool posts
  - category1
  - category2
---

# Streamlined Deployment and Integration of Large Language Models with PAI-EAS
This article provides a comprehensive guide on deploying a large language model (LLM) application using the PAI-EAS (Platform for AI —…


### **Streamlined Deployment and Integration of Large Language Models with PAI-EAS**

This article provides a comprehensive guide on deploying a large language model (LLM) application using the PAI-EAS ([Platform for AI](https://www.alibabacloud.com/product/machine-learning)— [Elastic Algorithm Service](https://www.alibabacloud.com/help/en/pai/user-guide/overview-2)). The deployment process supports both WebUI interface and API calls. Once deployed, the LLM application can be integrated with the LangChain framework to incorporate an enterprise knowledge base, and [details are here](https://www.alibabacloud.com/blog/empowering-generative-ai-with-alibaba-cloud-pais-advanced-llm-and-langchain-features_600577). PAI-EAS also offers inference acceleration engines like BladeLLM and vLLM to achieve high concurrency and low latency.

![](https://cdn-images-1.medium.com/max/800/1*76S245vDyBrIMcPr3Ema5A.png)### Background

The growing popularity of big models such as GPT has made the deployment of LLM applications a sought-after service. There are numerous open-source big models available, each excelling in different specialties. PAI-EAS simplifies the deployment of these models, making it possible to launch an inference service in under five minutes.

### Deploying EAS Services

To deploy an EAS service, follow these steps:

1. Navigate to the PAI-EAS model online service page by signing in to the [PAI console](https://pai.console.aliyun.com/), selecting **workspaces**, and choosing *Model Deployment > Model online services (EAS)*;

![](https://cdn-images-1.medium.com/max/800/0*halSxY8l-CAqvcSP.png)Click *Deploy Service* and configure key parameters such as the service name (e.g., llm\_demo001), deployment method (*Deploy Web App by Using Image*), and *Select Image* (choose from the PAI platform image list).

![](https://cdn-images-1.medium.com/max/800/0*wJnIq7AUF6vy5nA7.png)![](https://cdn-images-1.medium.com/max/800/1*ei-VCoMy3w9loNIHOlsqQg.png)2. Set the run command to launch the desired large model, such as Qwen/Qwen-7B-Chat, for the Universal-7B parameter model.

3. Select the appropriate resource group type and configuration, recommending GPU types like ml.gu7i.c16m60.1-gu30 for optimal performance.

![](https://cdn-images-1.medium.com/max/800/1*iQL5xaVn7M7M2ANbqzlCLg.png)4. Deploy the service and wait for the model deployment to complete.

Creating an inference service will take some time, so let’s go to the next interesting session and start using the service itself.

### Starting WebUI for Model Inference

Once the service is deployed, use the WebUI interface to perform model inference verification. Enter a query like “Please provide a financial learning plan” and click send to interact with the model.

![](https://cdn-images-1.medium.com/max/800/0*oOBxxj0tsMlvBmzE.png)![](https://cdn-images-1.medium.com/max/800/0*hP6X4BsQdNlNfe7i.png)### Common Use-Cases

**Switching Open-Source Models:** PAI-EAS allows easy switching between different models, such as Tongyi Qianwen, Llama2, and chatglm, by updating the run commands and instance specifications accordingly.

**Integrating Business Data with LangChain:** LangChain is a framework that combines LLMs with external data. Select LangChain on the WebUI page to integrate your business data, and follow the prompts to upload and vectorize your knowledge base files.

**Improving Inference Concurrency and Latency:** Add the — backend=vllm parameter to the run command for higher concurrency and lower latency. This is compatible with certain models like qwen, llama2, and baichuan-13B.

**Mounting Custom Models:** To deploy a custom model, mount it using OSS by uploading the model and configuration files to your OSS bucket, updating the service with the appropriate OSS path, and running command parameters.

### Using APIs for Model Inference

**Obtaining Service Access Address and Token:** Access the service details page from the PAI-EAS model online service page to retrieve the service Token and access address.

**HTTP Calls:** Use standard HTTP or SSE methods to call the service by sending string or structured requests with the service Token and access address. You can use Python’s requests package for this purpose.

**WebSocket Calls:** WebSocket can maintain connections and conduct multiple rounds of conversation. Replace the http in the service access address with ws and control the streaming output with the use\_stream\_chat parameter.

This guide outlines the entire process of deploying and using an LLM application with PAI-EAS, addressing common issues and providing solutions for seamless integration and improved performance. Whether you’re using the WebUI interface or calling APIs, this guide ensures a smooth deployment and utilization of LLM applications.

### Usage of LangChain to Integrate with Business Needs

* LangChain features: LangChain is an open-source framework that allows AI developers to combine big language models (LLM) like GPT-4 with external data to achieve better performance and effectiveness with as few computing resources as possible.
* LangChain working principle: Divide a large data source, such as a 20-page PDF file, into blocks and embed them into VectorDB (Vector Database).

LangChain first processes the input user data in natural language and stores it locally as a knowledge base for large models. Each inference user input will first find the answers similar to the input questions in the local knowledge base and input the knowledge base answers with the user input into a large model to generate customized answers based on the local knowledge base.

* Setting method:
1. In the upper-right corner of the WebUI page, select LangChain.
2. In the lower-left corner of the WebUI page, follow the instructions on the interface to pull custom data. You can configure files in txt, md, docx, and pdf formats.

![](https://cdn-images-1.medium.com/max/800/0*h0eIIrzvC-nUDPnk.png)For example, Upload a [README.md](https://raw.githubusercontent.com/alibaba/EasyCV/master/README.md) file. In the lower-left corner, click knowledge base file vectorization. The following result indicates that the custom data is loaded.

![](https://cdn-images-1.medium.com/max/800/0*Q8iuVUqm4_ymF_8s.png)In the input box at the bottom of the WebUI page, enter questions related to business data for a conversation.

For example, enter “What is EasyCV, and how can it be used? Use English to answer my question.” in the input box and click Send. The following figure shows the returned result.

![](https://cdn-images-1.medium.com/max/800/0*kVIlwSxQdjjfWNiV.png)### Ways of Improving Inference Concurrency and Reduce Latency

With one click, the PAI-EAS inference acceleration engine that supports BladeLLM and vLLM can help you enjoy high concurrency and low latency.

1. Click Update Service in the service actions column.
2. In the model service information section, add the parameter — backend = vllm at the end of the run command parameter, and then click deploy. (Note that the current inference acceleration engine only supports the following models: qwen, llama2, baichuan-13B, and baichuan2–13B)

![](https://cdn-images-1.medium.com/max/800/0*UjJp285KBEOncGeD.png)1. Transformers, vllm, and other versions are upgraded. Due to the iterative update of the model, the earlier and the latest released models are incompatible with the version dependencies of transformers, vllm, and other toolkits. Users can freely upgrade toolkits such as transformers and *vllm* according to their actual needs.

![](https://cdn-images-1.medium.com/max/800/0*kciyZCsLRzrXOO9B.png)### How do I mount a custom model?

To deploy a custom model, you can use OSS to mount the custom model. The procedure is as follows:

1. Upload custom models and related configuration files to your OSS Bucket Directory. For more information about how to create buckets and upload files, see [Create a bucket in the console](https://www.alibabacloud.com/help/en/oss/getting-started/console-quick-start) and [Upload files in the console](https://www.alibabacloud.com/help/en/oss/getting-started/console-quick-start).

The sample model file to be prepared is as follows:

![](https://cdn-images-1.medium.com/max/800/0*oeIwcNcV5GI9izLv.png)The configuration file must include a config.json file, and you will need to set up the Config file in accordance with the model formats of [Huggingface](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf/tree/main) or [Modelscope](https://www.modelscope.cn/models/modelscope/Llama-2-7b-chat-ms/files). For details of the example file, please refer to [config.json](https://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/file-manage-files/zh-CN/20230724/mpdm/config.json).

1. Click Update Service in the service actions column.
2. Configure the following parameters in the model service information section and click deploy.

![](https://cdn-images-1.medium.com/max/800/0*tUPaqBGL7v5E6jRm.png)**Parameter**

**Depaint**

Model configuration

Click Enter model configuration to configure the model.

* Select OSS mount for model configuration. Set the OSS path to the OSS path where the custom model file is located. For example, oss:// bucket-test/data-oss/.
* Mount path: set it to/data.
* Read-only: the switch is turned off.

Run command

Add the following parameters to the run command:

* — model-path: Set to/data. The configuration must be consistent with that of the Mount path.
* — model-type: the model type.

For more information about how to configure running commands for different models, see [Mastering Generative AI: Run Llama 2 Models on the Alibaba Cloud’s PAI](https://medium.com/@k-farruh/mastering-generative-ai-run-llama-2-models-on-alibaba-clouds-pai-ca0c57fe4329).

**Run command**

![](https://cdn-images-1.medium.com/max/800/1*5cHEiX2inauyMLH9lGQv3g.png)### API Interface for Model Reasoning

1. Obtain the service access address and Token.
2. Go to the PAI-EAS model online service page. For more information, see [Deploy EAS services](https://www.alibabacloud.com/help/en/pai/use-cases/5-minutes-to-use-the-pai-eas-one-click-deployment-llama2-webui).
3. Click the target service name on this page to go to the service details page.
4. In the basic information section, click View call information to obtain the service Token and access address on the public address call tab.
5. Start the API for model inference.

### Use HTTP to Call Services

* Non-streaming call

The client uses the standard HTTP format. When you call the curl command, you can send the following two types of requests:

* Send a String request


```
curl $host -H 'Authorization: $authorization' --data-binary @chatllm\_data.txt -v
```
Where: **$authorization** needs to be replaced with the service Token, **$host**: needs to be replaced with the service access address, **chatllm\_data.txt**: This file contains the information.

* Send semi-structured requests


```
curl $host -H 'Authorization: $authorization' -H "Content-type: application/json" --data-binary @chatllm\_data.json -v -H "Connection: close"
```
Use the **chatllm\_data.json** file to set inference parameters. The content format of the chatllm\_data.json file is as follows:


```
{  
 "max\_new\_tokens": 4096,  
 "use\_stream\_chat": false,  
 "prompt": "How to install it?",  
 "system\_prompt": "Act like you are programmer with 5+ years of experience."  
 "history": [  
 [  
 "Can you tell me what's the bladellm?",  
 "BladeLLM is an framework for LLM serving, integrated with acceleration techniques like quantization, ai compilation, etc. , and supporting popular LLMs like OPT, Bloom, LLaMA, etc."  
 ]  
 ],  
 "temperature": 0.8,  
 "top\_k": 10,  
 "top\_p": 0.8,  
 "do\_sample": True,  
 "use\_cache": True,  
}
```
The parameters are described as follows. Add and delete them as appropriate.

![](https://cdn-images-1.medium.com/max/800/1*Z8DRiwkJQZRjZKjiQMuWUw.png)You can also implement your own client based on the Python requests package. The sample code is as follows:


```
import argparse  

```
Where:

* host: specifies the service access address.
* authorization: The service Token is configured.
* Streaming call

The HTTP SSE method is used for streaming calls. Other settings are the same as those for non-streaming calls. For more information, see the following code:


```
import argparse  
import json  
from typing import Iterable, List  
  
import requests  
  
def clear\_line(n: int = 1) -> None:  
 LINE\_UP = '\033[1A'  
 LINE\_CLEAR = '\x1b[2K'  
 for \_ in range(n):  
 print(LINE\_UP, end=LINE\_CLEAR, flush=True)  
  
def post\_http\_request(prompt: str,  
 system\_prompt: str,  
 history: list,  
 host: str,  
 authorization: str,  
 max\_new\_tokens: int = 2048,  
 temperature: float = 0.95,  
 top\_k: int = 1,  
 top\_p: float = 0.8,  
 langchain: bool = False,  
 use\_stream\_chat: bool = False) -> requests.Response:  
 headers = {  
 "User-Agent": "Test Client",  
 "Authorization": f"{authorization}"  
 }  
 if not history:  
 history = [  
 (  
 "San Francisco is a",  
 "city located in the state of California in the United States. \  
 It is known for its iconic landmarks, such as the Golden Gate Bridge \  
 and Alcatraz Island, as well as its vibrant culture, diverse population, \  
 and tech industry. The city is also home to many famous companies and \  
 startups, including Google, Apple, and Twitter."  
 )  
 ]  
 pload = {  
 "prompt": prompt,  
 "system\_prompt": system\_prompt,  
 "top\_k": top\_k,  
 "top\_p": top\_p,  
 "temperature": temperature,  
 "max\_new\_tokens": max\_new\_tokens,  
 "use\_stream\_chat": use\_stream\_chat,  
 "history": history  
 }  
 if langchain:  
 pload["langchain"] = langchain  
 response = requests.post(host, headers=headers,  
 json=pload, stream=use\_stream\_chat)  
 return response  
  
def get\_streaming\_response(response: requests.Response) -> Iterable[List[str]]:  
 for chunk in response.iter\_lines(chunk\_size=8192,  
 decode\_unicode=False,  
 delimiter=b"\0"):  
 if chunk:  
 data = json.loads(chunk.decode("utf-8"))  
 output = data["response"]  
 history = data["history"]  
 yield output, history  
  
if \_\_name\_\_ == "\_\_main\_\_":  
 parser = argparse.ArgumentParser()  
 parser.add\_argument("--top-k", type=int, default=4)  
 parser.add\_argument("--top-p", type=float, default=0.8)  
 parser.add\_argument("--max-new-tokens", type=int, default=2048)  
 parser.add\_argument("--temperature", type=float, default=0.95)  
 parser.add\_argument("--prompt", type=str, default="How can I get there?")  
 parser.add\_argument("--langchain", action="store\_true")  
 args = parser.parse\_args()  
 prompt = args.prompt  
 top\_k = args.top\_k  
 top\_p = args.top\_p  
 use\_stream\_chat = True  
 temperature = args.temperature  
 langchain = args.langchain  
 max\_new\_tokens = args.max\_new\_tokens  
 host = ""  
 authorization = ""  
 print(f"Prompt: {prompt!r}\n", flush=True)  
 system\_prompt = "Act like you are programmer with \  
 5+ years of experience."  
 history = []  
 response = post\_http\_request(  
 prompt, system\_prompt, history,  
 host, authorization,  
 max\_new\_tokens, temperature, top\_k, top\_p,  
 langchain=langchain, use\_stream\_chat=use\_stream\_chat)  
 for h, history in get\_streaming\_response(response):  
 print(  
 f" --- stream line: {h} \n --- history: {history}", flush=True)
```
Where:

* host: specifies the service access address.
* authorization: The service Token is configured.

### Use WebSocket to Call Services

To better maintain user conversation information, you can also use WebSocket to maintain the connection with the service to complete one or more rounds of conversation. The code example is as follows:


```
import os  
import time  
import json  
import struct  
from multiprocessing import Process  
import websocket  
  
round = 5  
questions = 0  
  
def on\_message\_1(ws, message):  
 if message == "<EOS>":  
 print('pid-{} timestamp-({}) receives end message: {}'.format(os.getpid(),  
 time.time(), message), flush=True)  
 ws.send(struct.pack('!H', 1000), websocket.ABNF.OPCODE\_CLOSE)  
 else:  
 print("{}".format(time.time()))  
 print('pid-{} timestamp-({}) --- message received: {}'.format(os.getpid(),  
 time.time(), message), flush=True)  
  
def on\_message\_2(ws, message):  
 global questions  
 print('pid-{} --- message received: {}'.format(os.getpid(), message))  
 # end the client-side streaming  
 if message == "<EOS>":  
 questions = questions + 1  
 if questions == 5:  
 ws.send(struct.pack('!H', 1000), websocket.ABNF.OPCODE\_CLOSE)  
  
def on\_message\_3(ws, message):  
 print('pid-{} --- message received: {}'.format(os.getpid(), message))  
 # end the client-side streaming  
 ws.send(struct.pack('!H', 1000), websocket.ABNF.OPCODE\_CLOSE)  
  
def on\_error(ws, error):  
 print('error happened: ', str(error))  
  
def on\_close(ws, a, b):  
 print("### closed ###", a, b)  
  
def on\_pong(ws, pong):  
 print('pong:', pong)  
# stream chat validation test  
def on\_open\_1(ws):  
 print('Opening Websocket connection to the server ... ')  
 params\_dict = {}  
 params\_dict['prompt'] = """Show me a golang code example: """  
 params\_dict['temperature'] = 0.9  
 params\_dict['top\_p'] = 0.1  
 params\_dict['top\_k'] = 30  
 params\_dict['max\_new\_tokens'] = 2048  
 params\_dict['do\_sample'] = True  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 # raw\_req = f"""To open a Websocket connection to the server: """  
 ws.send(raw\_req)  
# end the client-side streaming  
  
# multi-round query validation test  
def on\_open\_2(ws):  
 global round  
 print('Opening Websocket connection to the server ... ')  
 params\_dict = {"max\_new\_tokens": 6144}  
 params\_dict['temperature'] = 0.9  
 params\_dict['top\_p'] = 0.1  
 params\_dict['top\_k'] = 30  
 params\_dict['use\_stream\_chat'] = True  
 params\_dict['prompt'] = "您好！"  
 params\_dict = {  
 "system\_prompt":  
 "Act like you are programmer with 5+ years of experience."  
 }  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
 params\_dict['prompt'] = "请使用Python，编写一个排序算法"  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
 params\_dict['prompt'] = "请转写成java语言的实现"  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
 params\_dict['prompt'] = "请介绍一下你自己？"  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
 params\_dict['prompt'] = "请总结上述对话"  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
  
# Langchain validation test.  
 def on\_open\_3(ws):  
 global round  
 print('Opening Websocket connection to the server ... ')  
 params\_dict = {}  
 # params\_dict['prompt'] = """To open a Websocket connection to the server: """  
 params\_dict['prompt'] = """Can you tell me what's the MNN?"""  
 params\_dict['temperature'] = 0.9  
 params\_dict['top\_p'] = 0.1  
 params\_dict['top\_k'] = 30  
 params\_dict['max\_new\_tokens'] = 2048  
 params\_dict['use\_stream\_chat'] = False  
 params\_dict['langchain'] = True  
 raw\_req = json.dumps(params\_dict, ensure\_ascii=False).encode('utf8')  
 ws.send(raw\_req)  
  
authorization = ""  
host = "ws://" + ""  
  
def single\_call(on\_open\_func, on\_message\_func, on\_clonse\_func=on\_close):  
 ws = websocket.WebSocketApp(  
 host,  
 on\_open=on\_open\_func,  
 on\_message=on\_message\_func,  
 on\_error=on\_error,  
 on\_pong=on\_pong,  
 on\_close=on\_clonse\_func,  
 header=[  
 'Authorization: ' + authorization],  
 )  
 # setup ping interval to keep long connection.  
 ws.run\_forever(ping\_interval=2)  
  
if \_\_name\_\_ == "\_\_main\_\_":  
 for i in range(5):  
 p1 = Process(target=single\_call, args=(on\_open\_1, on\_message\_1))  
 p2 = Process(target=single\_call, args=(on\_open\_2, on\_message\_2))  
 p3 = Process(target=single\_call, args=(on\_open\_3, on\_message\_3))  
 p1.start()  
 p2.start()  
 p3.start()  
 p1.join()  
 p2.join()  
 p3.join()
```
Where:

* authorization: The service Token is configured.
* host: specifies the service access address. Replace the front-end http with ws.
* use\_stream\_chat: this parameter is used to control whether the client is streaming output. The default value is True, indicating that the server returns streaming data.
* See the on\_open\_2 function implementation method in the preceding sample code to implement multiple rounds of conversations.

### Conclusion

The article serves as an in-depth manual for deploying and integrating large language models (LLMs) using Alibaba Cloud’s Platform for AI — Elastic Algorithm Service (PAI-EAS). It addresses the increasing demand for accessible and efficient deployment of sophisticated LLM applications, such as those based on the foundation models’ architecture, emphasizing the capability to establish an inference service rapidly.

Key points covered in the article include:

1. **PAI-EAS Deployment**: The article explains the step-by-step deployment process of LLMs using PAI-EAS. It highlights the convenience of using both the WebUI interface and API calls, which cater to varying user preferences and technical expertise. It also specifies the necessary parameters and recommended resources for optimal model performance, facilitating a tailored setup for different LLM applications.
2. **Integration with LangChain**: The integration with LangChain, an open-source framework, is outlined, showcasing how LLMs can be enhanced with a company’s knowledge base. This significantly improves the model’s output by grounding responses in enterprise-specific information, which is particularly useful for creating more contextual and relevant interactions in business applications.
3. **Inference Acceleration Engines**: The article discusses the use of BladeLLM and vLLM acceleration engines provided by PAI-EAS to improve inference performance. These tools help users achieve higher concurrency and lower latency, which are critical factors in maintaining efficient, responsive LLM services.
4. **Custom Model Deployment**: For users with custom model requirements, the guide explains the process of mounting custom models using OSS, detailing the steps to upload and configure models and their associated files. This flexibility allows businesses to deploy proprietary or specially configured models that fit their unique use cases.
5. **API Utilization for Inference**: The article provides practical insights into obtaining service access credentials and making HTTP or WebSocket calls for model inference. This includes examples of making both streaming and non-streaming calls, thus offering a complete toolkit for developers to effectively integrate PAI-EAS LLM services into their applications.

The content is rich with command examples, parameter descriptions, and model-specific recommendations that enable users to navigate the complexities of LLM deployment confidently. By covering common use cases and providing solutions to typical challenges, the article ensures that readers can not only deploy but also maximize the utility of LLM applications, aligning with their business objectives and technical requirements.

This comprehensive tutorial embodies a critical resource for data scientists, AI developers, and IT professionals aiming to leverage the power of large language models within the Alibaba Cloud ecosystem. [Contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) to explore the world of generative AI and discover how it can transform your applications and business. It bridges the gap between advanced AI technologies and practical business applications, enabling organizations to innovate and extract value from cutting-edge language processing capabilities.



By [Dr. Farruh](https://medium.com/@k-farruh) on [January 15, 2024](https://medium.com/p/bb8da7ec39bd).

[Canonical link](https://medium.com/@k-farruh/streamlined-deployment-and-integration-of-large-language-models-with-pai-eas-bb8da7ec39bd)

Exported from [Medium](https://medium.com) on May 25, 2024.

