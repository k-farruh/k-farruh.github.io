---
title: 'Mastering Generative Ai Run Llama 2 Models On Alibaba Cloud S Pai'
date: 2023-07-26
permalink: /posts/2023-07/Mastering-Generative/
tags:
  - cool posts
  - category1
  - category2
---

Mastering Generative AI: Run Llama 2 Models on Alibaba Cloud’s PAI
 \* {
 font-family: Georgia, Cambria, "Times New Roman", Times, serif;
 }
 html, body {
 margin: 0;
 padding: 0;
 }
 h1 {
 font-size: 50px;
 margin-bottom: 17px;
 color: #333;
 }
 h2 {
 font-size: 24px;
 line-height: 1.6;
 margin: 30px 0 0 0;
 margin-bottom: 18px;
 margin-top: 33px;
 color: #333;
 }
 h3 {
 font-size: 30px;
 margin: 10px 0 20px 0;
 color: #333;
 }
 header {
 width: 640px;
 margin: auto;
 }
 section {
 width: 640px;
 margin: auto;
 }
 section p {
 margin-bottom: 27px;
 font-size: 20px;
 line-height: 1.6;
 color: #333;
 }
 section img {
 max-width: 640px;
 }
 footer {
 padding: 0 20px;
 margin: 50px 0;
 text-align: center;
 font-size: 12px;
 }
 .aspectRatioPlaceholder {
 max-width: auto !important;
 max-height: auto !important;
 }
 .aspectRatioPlaceholder-fill {
 padding-bottom: 0 !important;
 }
 header,
 section[data-field=subtitle],
 section[data-field=description] {
 display: none;
 }
 

Mastering Generative AI: Run Llama 2 Models on Alibaba Cloud’s PAI
==================================================================




Tags:Generative AI, GenAI, AI, PAI, PAI-EAS, Llama 2, Large Language Model, Artificial Intelligence, Machine Learning Platform For AI




---

### Mastering Generative AI: Run Llama 2 Models on the Alibaba Cloud’s PAI

### Introduction

Alibaba Cloud is a cloud computing provider that offers a wide range of cloud products and services, including Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). One of their flagship offerings is the [Machine Learning Platform for AI](https://www.alibabacloud.com/product/machine-learning?spm=a2c65.11461447.0.0.38333bdbbWFwjs), which provides comprehensive AI capabilities to developers and enterprises. PAI-EAS (Elastic Algorithm Service) is a component of PAI that allows users to deploy and manage AI applications easily.

### Llama 2 and Generative AI

[Llama 2](https://github.com/facebookresearch/llama) is an open-source large language model (LLM) developed by Meta. It is a powerful model that can generate text based on a given prompt. Llama 2 has different versions with varying parameters, including 7 billion, 13 billion, and 70 billion. Compared to its predecessor, Llama 1, Llama 2 has more training data and a longer context length, making it more versatile and accurate in generating natural language.

Generative AI is a branch of artificial intelligence that focuses on creating AI models (like Llama 2) capable of generating new content, such as text, images, and music. It is widely used in various applications, including chatbots, virtual assistants, content generation, and more.

### PAI-Blade Accelerator

We will implement Llama on PAI-EAS, which includes the PAI-Blade inference accelerator. Let’s get to know the revolutionary PAI Blade, a game-changer in accelerating LLM inference speed on PAI-EAS.

The PAI Blade is a specially designed hardware accelerator engineered to optimize the performance of LLMs. Leveraging advanced technologies and algorithms allows the PAI Blade to supercharge the inference speed of LLMs up to six times faster than traditional methods. This means you can process more data, generate responses quicker, and achieve enhanced efficiency in your language-based applications.

Now, let’s turn our attention to the cost-saving potential that the PAI Blade brings to the table. With its accelerated inference speed, the PAI Blade enables you to achieve higher throughput while utilizing fewer computing resources. This translates to a reduced need for expensive GPU instances, resulting in significant cost savings for your deployment.

You can witness a remarkable boost in performance without compromising your budget by implementing Llama 2 on PAI-EAS, which harnesses the power of the PAI Blade. The combination of PAI-EAS and the PAI Blade creates a synergy that unleashes the true potential of Llama 2, making it an ideal choice for scenarios with demanding language processing requirements.

Unleash the full potential of Llama 2 on PAI-EAS with the PAI Blade and fuel your language-based applications with unprecedented power, efficiency, and cost-effectiveness.

### Running Llama 2 on PAI-EAS

![](https://cdn-images-1.medium.com/max/800/1*s005Yju-yZK2Bt8buRdAaQ.jpeg)PAI-EAS provides a convenient way to deploy and run AI applications, including Llama 2 models. There are two methods to run Llama 2 on PAI-EAS: WebUI and API. The WebUI method allows you to interact with the model through a web interface, while the API method enables programmatic access to the model for integration with other applications.

### Method 1: Running Llama 2 on PAI-EAS Using WebUI

1. Log into the [Alibaba Cloud Console](https://www.alibabacloud.com/knowledge/developer/login-methods-for-alibaba-cloud-server?spm=a2c65.11461447.0.0.38333bdbbWFwjs), your gateway to powerful cloud computing solutions.

2. Navigate to the PAI page, where the magic of Machine Learning Platform for AI awaits. You can search for it or access it through the [PAI console](https://pai.console.aliyun.com/).

![](https://cdn-images-1.medium.com/max/800/0*IuXyNKJxL12kCyEC.png)3. If you’re new to PAI, fear not! Creating a workspace is a breeze. Just follow the [documentation](https://www.alibabacloud.com/help/en/machine-learning-platform-for-ai/latest/create-a-workspace) provided, and you’ll be up and running in no time.

4. Immerse yourself in the world of workspaces as you click on the name of the specific workspace you wish to operate in. It’s in the left-side navigation pane.

![](https://cdn-images-1.medium.com/max/800/0*sQkxxI-WyftSHqah.png)5. Continue your exploration by delving into the depths of model deployment. Within the workspace page, navigate to **Model Deployment** and select **Model Online Services (EAS).**

6. Click the **Deploy Service** button, beckoning you with promises of innovation and efficiency.

### Visually Appealing-UI

![](https://cdn-images-1.medium.com/max/800/1*kWSJzyxguJmoD2gzKoUrJQ.png)### JSON Approach

For those who prefer a simpler approach, I will present the convenience of working with JSON format to configure your EAS deployment settings. Create a JSON file with the desired parameters, and you’re good to go. All you need to do is update the name to suit your preferences. Here’s an example of how your JSON file could look:


```
{  
 "cloud": {  
 "computing": {  
 "instance\_type": "ecs.gn6e-c12g1.3xlarge",  
 "instances": null  
 }  
 },  
 "containers": [  
 {  
 "image": "eas-registry-vpc.cn-hangzhou.cr.aliyuncs.com/pai-eas/chat-llm-webui:1.0",  
 "port": 8000,  
 "script": "python api/api\_server.py --precision=fp16 --port=8000 --model-path=meta-llama/Llama-2-13b-chat-hf"  
 }  
 ],  
 "features": {  
 "eas.aliyun.com/extra-ephemeral-storage": "50Gi"  
 },  
 "metadata": {  
 "instance": 1,  
 "name": "your\_custom\_service\_name",  
 "rpc": {  
 "keepalive": 60000,  
 "worker\_threads": 1  
 }  
 },  
 "name": "your\_custom\_service\_name"  
}
```
Update the **your\_custom\_service\_name** field with your desired custom service name, and you’re all set. Embrace the simplicity and efficiency of working with JSON to streamline your EAS deployment process.

![](https://cdn-images-1.medium.com/max/800/0*GD55kZTTcgSxH11-.png)7. Click the **Deploy** button as the model deployment takes shape before your eyes. Patience is key as you await completion.

8. Start WebUI for model inference:

* Click **View Web application** in the service mode column of the target service.
* On the WebUI page, you can perform model inference verification by entering conversation content in the input interface at the bottom of the dialog box and clicking **Send** to start the conversation.

![](https://cdn-images-1.medium.com/max/800/0*mtWKln9XG1zd1wQG.png)### Method 2: Running Llama 2 on PAI-EAS Using API

In order to extend the capabilities of the Llama 2 model on PAI-EAS, let’s explore the process of deploying it with API support. Follow these steps to harness the power of API-driven deployment:

1. Configure the deployment parameters (following steps 1–3 from the previous method)

2. In the Run command field, use the following command to run the Llama 2 model with API support:

* **Deploying the 13 billion Model with API Support:** `python api/api_server.py --port=8000 --model-path=meta-llama/Llama-2-13b-chat-hf --precision=fp16`
* **Deploying the 7 billion Model with API Support:** `python api/api_server.py --port=8000 --model-path=meta-llama/Llama-2-7b-chat-hf --precision=fp16`

3. Click the **Deploy** button and wait for the model deployment to complete.

![](https://cdn-images-1.medium.com/max/800/0*GXg_HfMYpED-pU3M.png)4. Now, let’s utilize the power of the API for model inference. Send HTTP POST requests to the endpoint URL of the deployed service. The API supports JSON payload for input and output.

### Python Wrapper for API Call

The provided code is a Python implementation to use the *pai\_llama* class for generating responses using the Llama 2 model deployed on PAI-EAS.


```
import websocket  
import json  
import struct  
  
class pai\_llama:  
 def \_\_init\_\_(self, api\_key):  
 self.api\_key = api\_key  
 self.input\_message = ""  
 self.temperature = 0.0  
 self.round = 1  
 self.received\_message = None  
 # host url should begin with "ws://"  
 host = "ws://you\_host\_url"  
 self.host = host  
 def on\_message(self, ws, message):  
 assert self.input\_message in message, "request not in response."   
 self.received\_message = message  
 def on\_error(self, ws, error):  
 print('error happened .. ')  
 print(str(error))  
 def on\_close(self, ws, a, b):  
 print("### closed ###", a, b)  
 def on\_pong(self, ws, pong):  
 print('pong:', pong)  
 def on\_open(self, ws):  
 print('Opening WebSocket connection to the server ... ')  
 params\_dict = {}  
 params\_dict['input\_ids'] = self.input\_message  
 params\_dict['temperature'] = self.temperature  
 params\_dict['repetition\_penalty'] = self.repetition\_penalty  
 params\_dict['top\_p'] = self.top\_p   
 params\_dict['max\_length'] = self.max\_length  
 params\_dict['num\_beams'] = self.num\_beams  
 raw\_req = json.dumps(params\_dict)  
 ws.send(raw\_req)  
 # for i in range(self.round):  
 # ws.send(self.input\_message)  
 ws.send(struct.pack('!H', 1000), websocket.ABNF.OPCODE\_CLOSE)  
 def generate(self, message, temperature=0.95, repetition\_penalty=1, top\_p=0.01, max\_length=2048, num\_beams=1):  
 self.input\_message = message  
 self.temperature = temperature  
 self.repetition\_penalty= repetition\_penalty  
 self.top\_p = top\_p  
 self.max\_length = max\_length  
 self.num\_beams = num\_beams  
 ws = websocket.WebSocketApp(  
 self.host,  
 on\_open=self.on\_open,  
 on\_message=self.on\_message,  
 on\_error=self.on\_error,  
 on\_pong=self.on\_pong,  
 on\_close=self.on\_close,  
 header=[  
 f'Authorization: {self.api\_key}'],  
 )  
 # setup ping interval to keep long connection.  
 ws.run\_forever(ping\_interval=2)  
 return self.received\_message.split('<br/>')[1:]  
  
client = pai\_llama(api\_key="your\_token\_as\_API")  
res = client.generate(  
 message="tell me about alibaba cloud PAI",   
 temperature=0.95  
)  
print(f"Final: {res}")  
print(" ")
```
You need to replace **you\_host\_url** with the actual host URL of your deployed Llama 2 model on PAI-EAS to use this code. Additionally, provide your API key as the api\_key parameter when creating an instance of the *pai\_llama* class. Adjust the input message and other parameters according to your requirements.

Follow these steps to find the host URL and token required for the code:

1. Go to your deployed model on PAI-EAS
2. Click **Service Details** to access the detailed information of the deployed model
3. Look for the **View Endpoint Information** section and click it
4. In the **Public Endpoint** field, you will find the host URL. Copy this URL.
5. Next, locate the **Authorization** field, which contains the token required for authentication. Copy this token.
6. Replace the placeholder **you\_host\_url** in the code with the copied host URL
7. When creating an instance of the pai\_llama class, pass the copied token as the api\_key parameter.

After completing these steps, you will have the correct host URL and token to use in the code, ensuring a successful connection and interaction with your deployed Llama 2 model on PAI-EAS.

![](https://cdn-images-1.medium.com/max/800/0*h3I5HUMJjtnWKLUR.png)### HTTP Call

The HTTP access method is suitable for single-round questions and answers. The specific methods are listed below:


```
curl $host -H 'Authorization: $authorization' --data-binary @chatllm\_data.txt -v
```
Where:

* `$Host`: You need to replace it with the service access address. On the service details page, click View call information to obtain it on the public address call tab.
* `$Authorization`: Replace it with a service Token. You can click View call information on the service details page to obtain the call information on the public IP address call tab.
* `chatllm_data.txt`: Create a chatllm\_data.txt file and enter specific questions in the file

### Extra Capabilities: Mounting a Custom Model on Llama 2 on PAI-EAS

### How Do I Mount a Custom Model?

If you require a custom model for inference (such as a fine-tuned or downloaded model), you can easily mount it on Llama 2 deployed on PAI-EAS. This capability provides the flexibility to leverage your models for specific use cases. Here’s how you can mount a custom model using [Object Storage Service (OSS)](https://www.alibabacloud.com/product/object-storage-service):

1. Configure your custom model and its related configurations in the huggingface or modelscope model format. Store these files in your OSS directory. The file structure should follow the instance file format.

2. Click **Update Service** in the actions column of the EAS service for your Llama 2 deployment.

3. In the model service information section, configure the following parameters:

* **Model Configuration**: Click **Enter Model Configuration** to specify the model configuration. Select **OSS Mount** and set the OSS path to the bucket path you created earlier. For example, oss://bucket-test/data-oss/.
* **Mount Path**: Set the mount path to */llama2-finetune* or any desired path for your custom model
* **Read-only**: Ensure the read-only switch is turned off, allowing read and write access to your custom model

4. In the run command, include the *— model-path=/llama2-finetune* parameter. For example:


```
python webui/webui\_server.py --listen --port=8000 --model-path=/Llama2-finetune
```
Adjust the command according to your specific deployment requirements.

After completing these steps, you can seamlessly integrate your custom model into the Llama 2 deployment on PAI-EAS. This capability empowers you to leverage your fine-tuned or downloaded models, unlocking endless possibilities for personalized and specialized language processing tasks.

### Conclusion

We explained the seamless integration of Llama 2 models on Alibaba Cloud’s PAI-EAS platform by leveraging PAI Blade, which has an incredible speed boost of up to six times faster inference, leading to substantial cost savings for users.

The article also discussed the additional capabilities provided by Llama 2 on PAI-EAS (such as the ability to mount custom models using OSS and the flexibility to customize parameters for generating responses). These features empower developers to tailor their language-based applications to specific requirements and achieve personalized and specialized language-processing tasks.

The author invites readers to learn more about PAI, delve into generative AI projects, and reach out for further discussions. Whether you have questions, need assistance, or are interested in exploring the potential of generative AI, the author encourages readers to [contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) and discover the endless possibilities that await.

Experience the power of Llama 2 on Alibaba Cloud’s PAI-EAS, unlock the efficiency of PAI Blade, and embark on a journey of accelerated performance and cost-savings. [Contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) to explore the world of generative AI and discover how it can transform your applications and business.



By [Dr. Farruh](https://medium.com/@k-farruh) on [July 26, 2023](https://medium.com/p/ca0c57fe4329).

[Canonical link](https://medium.com/@k-farruh/mastering-generative-ai-run-llama-2-models-on-alibaba-clouds-pai-ca0c57fe4329)

Exported from [Medium](https://medium.com) on May 25, 2024.

