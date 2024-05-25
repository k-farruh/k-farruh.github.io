---
title: 'Empowering Generative Ai With Alibaba Cloud Pai S Advanced Llm And Langchain Features'
date: 2023-11-23
permalink: /posts/2023-11/Empowering-Generative/
tags:
  - cool posts
  - category1
  - category2
---

Empowering Generative AI with Alibaba Cloud PAI’s Advanced LLM and LangChain Features
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
 

Empowering Generative AI with Alibaba Cloud PAI’s Advanced LLM and LangChain Features
=====================================================================================




Are you ready to dive into the world of Generative AI (GenAI) and witness the magic of Large Language Models (LLM)? Meet Alibaba Cloud…




---

### **Empowering Generative AI with Alibaba Cloud PAI’s Advanced LLM and LangChain Features**

![](https://cdn-images-1.medium.com/max/800/1*Z4ed4Wi3G0VMhoIYwnwvcw.jpeg)Are you ready to dive into the world of **Generative AI** (GenAI) and witness the magic of Large Language Models (LLM)? Meet [Alibaba Cloud Platform for AI](https://www.alibabacloud.com/product/machine-learning) (PAI). This cutting-edge platform combines the advanced capabilities of AI (Artificial Intelligence) with the groundbreaking features of Langchain and LLM to revolutionize the field of GenAI.

![](https://cdn-images-1.medium.com/max/800/0*wJ49qdrUWmZ7vNQs.png)PAI offers plenty of exciting features that will leave you awe-inspired. Let’s explore some of its key highlights:

1. **Seamless Langchain Integration:** PAI seamlessly integrates with Langchain, an open platform. With Langchain’s powerful tools and resources, PAI employs the full potential of language models, enabling you to create dynamic and contextually-aware AI-generated content.
2. **Advanced LLM Capabilities:** PAI leverages state-of-the-art LLM technology to provide unparalleled text generation performance. Whether you’re looking to generate natural language responses or creative stories or engage in multi-turn conversations, PAI can handle it with unprecedented accuracy and fluency.
3. **Real-time Streaming Output:** Say goodbye to waiting for AI-generated responses! PAI offers real-time streaming output, ensuring instant and dynamic feedback. Experience the thrill of watching the AI-generated content unfold before your eyes, making your interactions with the model more engaging and interactive.
4. **Template-based Access:** PAI introduces an innovative template-based access feature. With the help of *DSW Gallery*, you can easily create your own GenAI or AI model based on templates for your business tasks. This empowers you to tailor the AI model for specific areas or create an **Industry-Specific LLM,** providing an industry and contextually relevant experience.
5. **Knowledge Base System (KBS) or Retrieval Augmented Generation (RAG):** Unlock the power of PAI’s KBS feature within LLM. Seamlessly retrieve relevant information from vast knowledge bases to enhance the quality and accuracy of AI-generated responses. Leverage the extensive knowledge stored in PAI to make LLM an intelligent and reliable companion.
6. **Interactive Agent Capabilities:** Transform your AI-driven conversations with PAI into an interactive and immersive experience. With PAI as the platform, you can establish your multi-agent system to engage in lifelike and multi-turn dialogues. Witness an AI companion that understands your queries, responds intelligently, and adapts to your conversation flow.

Covering all features in one publication will be challenging. Hence, we will publish articles related to LLM on PAI. Let’s start with integration with Langchain.

### Unleashing the Power of Chat Models with AliCloud PAI EAS

### Introduction

### PAI-EAS

![](https://cdn-images-1.medium.com/max/800/0*Y4CN3x2XsYw7zD7Q.png)[PAI-EAS (Platform for AI — Elastic Algorithm Service)](https://www.alibabacloud.com/help/en/pai/user-guide/overview-2) is for online inference of the model. It offers automatic scaling, blue-green deployment, and resource group management. PAI-EAS supports real-time and near-real-time AI inference scenarios and provides a flexible infrastructure, efficient container scheduling, and simplified model deployment. It also enables real-time and near real-time synchronous inference, ensuring high throughput and low latency for various AI applications.

### LangChain

![](https://cdn-images-1.medium.com/max/800/0*76m-LwPQj2_rQoPP)[LangChain](https://python.langchain.com/docs/get_started/introduction) is a robust framework for developing applications powered by language models. It enables context-aware applications that can connect a language model to various context sources, such as prompt instructions, few-shot examples, or content to ground its response in. LangChain allows applications to reason and make decisions based on the provided context, utilizing the capabilities of the language model.

The LangChain framework consists of several components. The LangChain Libraries provide Python and JavaScript libraries with interfaces and integrations for working with language models. These libraries include a runtime for combining features into chains and agents and pre-built implementations of chains and agents for different tasks. The LangChain Templates offer easily deployable reference architectures for various applications.

By using LangChain, developers can simplify the entire application lifecycle. They can develop applications using LangChain libraries and templates, produce them by inspecting and monitoring with LangSmith, and deploy the chains as APIs using LangServe.

LangChain offers standard and extendable interfaces and integrations for modules such as Model I/O, Retrieval, and Agents. It provides many resources, including use cases, walkthroughs, best practices, API references, and a developer’s guide. The LangChain community is active and supportive, offering places to ask questions, share feedback, and collaborate on the future of language model-powered applications.

In this tutorial, we will walk through the steps to set up PAI EAS, deploy a chat model, and run it using different configurations. [Here is the documentation link](https://python.langchain.com/docs/integrations/chat/pai_eas_chat_endpoint).

### Steps to Build LangChain and LLM with PAI-EAS

### Step 1: Setting Up LLM on PAI-EAS

We begin from the lunching LLM on PAI-EAS. [Here, you can find a tutorial](https://www.alibabacloud.com/blog/mastering-generative-ai---run-llama2-models-on-alibaba-clouds-pai-with-ease_600229) or [documentation](https://www.alibabacloud.com/help/en/pai/user-guide/service-deployment/) on how to set up EAS and obtain the PAI-EAS service URL and token. These credentials will be essential for connecting to the EAS service.

![](https://cdn-images-1.medium.com/max/800/0*AApQh4jIz4U7Cye8)Suppose you would like to try the [Qwen](https://github.com/QwenLM/Qwen) model. Feel free to modify the “*Command to Run”* in the number 4 field. Qwen is open-source and has a series of models, including Qwen, the base language models, namely Qwen-7B and Qwen-14B, and Qwen-Chat, the chat models, namely Qwen-7B-Chat and Qwen-14B-Chat.


```
python api/api\_server.py --port=8000 --model-path=Qwen/Qwen-7B-Chat
```
### Step 2: Environment Variables Next

It requires setting the environment variables URL and token from the PAI-EAS. You can export these variables in your terminal or set them programmatically in your code. This will allow your application to access the EAS service securely.

Export variables in the terminal:


```
export EAS\_SERVICE\_URL=XXX  
export EAS\_SERVICE\_TOKEN=XXX
```
To get these variables from the PAI-EAS, you can follow the below steps to find the host URL and token required for the code:

![](https://cdn-images-1.medium.com/max/800/0*ivMMHI1wjcIUC---.png)* Go to your deployed model on PAI-EAS, as shown above.
* Click Service Details to access the detailed information on the deployed model.
* Look for the View Endpoint Information section and click it.

![](https://cdn-images-1.medium.com/max/800/0*LsaYB7h8n_fpslY8)* In the Public Endpoint field, you will find the host URL. Copy this URL.
* Next, locate the Authorization field, which contains the token required for authentication. Copy this token.

![](https://cdn-images-1.medium.com/max/800/0*SQ1oBOvtm5OyF0qR.png)### Step 3: Import Dependencies Now

Import the necessary dependencies in your code. This includes the *PaiEasChatEndpoint* class from the *langchain.chat\_models* module and the *HumanMessage* class from the *langchain.chat\_models.base* module. These modules provide the foundation for running chat models with PAI-EAS.


```
import os  
  
from langchain.chat\_models import PaiEasChatEndpoint  
from langchain.chat\_models.base import HumanMessage  
  
os.environ["EAS\_SERVICE\_URL"] = "Your\_EAS\_Service\_URL"  
os.environ["EAS\_SERVICE\_TOKEN"] = "Your\_EAS\_Service\_Token"  
chat = PaiEasChatEndpoint(  
 eas\_service\_url=os.environ["EAS\_SERVICE\_URL"],  
 eas\_service\_token=os.environ["EAS\_SERVICE\_TOKEN"],  
)
```
### Step 4a: Initializing the Chat Model

Create an instance of the *PaiEasChatEndpoint* class by passing the PAI-EAS service URL and token as parameters. This initializes the connection to the EAS service and prepares it for chat model interactions.


```
output = chat([HumanMessage(content="write a funny joke")])  
print("output:", output)
```
### Step 4b: Running the Chat Model

Utilize the chat model by calling the chat method and passing a *HumanMessage* object with the desired input content. By default, the chat model uses the default settings for inference. However, you can customize the inference parameters by including additional keyword arguments such as *temperature, top\_p, and top\_k*. This allows you to optimize the model’s behavior as per your requirements.


```
kwargs = {"temperature": 0.8, "top\_p": 0.8, "top\_k": 5}  
output = chat([HumanMessage(content="write a funny joke")], \*\*kwargs)  
print("output:", output)
```
Here is the list of other parameters for PaiEasEndpoint:

![](https://cdn-images-1.medium.com/max/800/1*iRpN22gUudzgZzQyu4p2Ig.png)### Step 4c: Stream Response (Optional)

You can run a stream call to obtain a stream response for more dynamic interactions. Set the streaming parameter to *True* when calling the stream method. Iterate over the stream outputs to process each response in real-time.


```
outputs = chat.stream([HumanMessage(content="hi")], streaming=True)  
for output in outputs:  
 print("stream output:", output)
```
### Bonus: a Ready Code to Run


```
import os  
from langchain.llms.pai\_eas\_endpoint import PaiEasEndpoint  
from langchain.prompts import PromptTemplate  
from langchain.chains import LLMChain  
  
# Initialize the EAS service endpoint  
os.environ["EAS\_SERVICE\_URL"] = "EAS\_SERVICE\_URL",  
os.environ["EAS\_SERVICE\_TOKEN"] = "EAS\_SERVICE\_TOKEN"  
llm = PaiEasEndpoint(eas\_service\_url=os.environ["EAS\_SERVICE\_URL"], eas\_service\_token=os.environ["EAS\_SERVICE\_TOKEN"])  
# Accessing EAS LLM services:  
# Access method 1: Direct access  
kwargs = {"temperature": 0.8, "top\_p": 0.8, "top\_k": 5}  
output = llm("Say foo:", \*\*kwargs)  
# Access method 2: Template-based access  
# 2.1 Prepare the question template  
template = """Question: {question}  
Answer: Let's think step by step."""  
prompt = PromptTemplate(template=template, input\_variables=["question"])  
# 2.2 Wrap with LLMChain  
llm\_chain = LLMChain(prompt=prompt, llm=llm)  
# 2.3 Access the service  
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"  
llm\_chain.run(question)
```
### Conclusion

Alibaba Cloud PAI is the perfect blend of cutting-edge platforms, which provides technology and captivating features, creating a transformative experience in the realm of GenAI. Brace yourself for a journey where language becomes a canvas for AI-powered creativity and innovation. Get ready to unlock the true potential of LLM with PAI — your gateway to the future of GenAI!

With Alibaba Cloud PAI-EAS, deploying and running chat models becomes seamless and efficient. Using the above steps and information, you can unlock the full potential of chat models and create intelligent conversational experiences. PAI-EAS empowers developers to harness the capabilities of machine learning with ease while providing high throughput, low latency, and comprehensive operations and maintenance features. Start leveraging chat models within your applications today and embark on a journey of exciting AI-driven conversations.

Experience the power of LLM and LangChain on Alibaba Cloud’s PAI-EAS and embark on a journey of accelerated performance and cost-savings. [Contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) to explore the world of generative AI and discover how it can transform your applications and business.



By [Dr. Farruh](https://medium.com/@k-farruh) on [November 23, 2023](https://medium.com/p/a4f8a7842fb2).

[Canonical link](https://medium.com/@k-farruh/empowering-generative-ai-with-alibaba-cloud-pais-advanced-llm-and-langchain-features-a4f8a7842fb2)

Exported from [Medium](https://medium.com) on May 25, 2024.

