---
title: 'Unleashing The Creative Potential With Genai Diffusion Graphic Generation Solution From Alibaba '
date: 2023-10-05
permalink: /posts/2023-10/Unleashing-the/
tags:
  - cool posts
  - category1
  - category2
---

Unleashing the Creative Potential with GenAI-Diffusion Graphic Generation Solution from Alibaba…
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
 

Unleashing the Creative Potential with GenAI-Diffusion Graphic Generation Solution from Alibaba…
================================================================================================




Generative AI (GenAI) models have revolutionized the way we create and experience content. These models possess the remarkable ability to…




---

### Unleashing the Creative Potential with GenAI-Diffusion Graphic Generation Solution from Alibaba Cloud

Generative AI (GenAI) models have revolutionized the way we create and experience content. These models possess the remarkable ability to generate text, images, music, and videos that closely resemble human-created content. They have become invaluable tools across industries, enabling creative expression, automation, and problem-solving.

![](https://cdn-images-1.medium.com/max/800/1*7YgFWsBcnUpr1apzEmuoYA.png)In this article, we will explore how you can create your own GenAI model without the need for costly investments or extensive time commitments. While training and utilizing language-based models like [BERT](https://arxiv.org/abs/1810.04805) and [GPT](https://www.alibabacloud.com/blog/599666) can be resource-intensive, we will focus on a stable diffusion text and image generation solution as an example model. This approach offers a cost-effective alternative that delivers impressive results.

The Diffusion Model stands as a powerful technique within the realm of generative AI specifically designed to generate lifelike, high-quality images. It operates on a probabilistic framework, iteratively refining an initial image over multiple steps or time intervals.

During the diffusion process, carefully designed noise sources are applied to the image at each step, gradually degrading its quality. However, through a series of calculated transformations, the model learns to reverse this degradation and restore the image with enhanced quality.

The key concept behind the diffusion model lies in leveraging data-dependent noise sources to encourage the model to capture the underlying structure and intricate patterns present in the training data. By iteratively applying these noise sources and optimizing the model, the diffusion model becomes capable of generating highly realistic and diverse images that closely resemble the training dataset.

This approach has gained significant popularity in domains such as computer vision, art, and creative applications. It empowers the creation of visually captivating images, artistic compositions, and even realistic deepfake content. The diffusion model offers a unique mechanism for generating images abundant in fine details, diverse textures, and coherent structures.

By harnessing the potential of the diffusion model, developers and artists can explore novel frontiers in image generation, content creation, and visual storytelling. It unlocks opportunities for innovative applications in areas like virtual reality, augmented reality, advertising, and entertainment.

The Diffusion text-to-image generation solution provided by Alibaba Cloud’s [Machine Learning Platform for AI (PAI)](https://www.alibabacloud.com/product/machine-learning) product facilitates a streamlined end-to-end construction process. This comprehensive solution supports offline model training, inference, and empowers the generation of images directly from text inputs.

### Overall Architecture

Alibaba Cloud’s machine learning PAI offers a comprehensive solution for AI and an example for text and image generation, providing an end-to-end, customizable white box solution. It supports text and image generation functions, allowing users to create intelligent text-image generation models tailored to their business scenarios. Alternatively, users can leverage the default models provided by PAI for model tuning and online deployment to generate diverse images based on different text inputs.

The following components of PAI play a vital role in this process:

1. PAI-DSW (Data Science Workshop): It is a collaborative platform designed for data scientists and researchers. PAI-DSW seamlessly integrates with Jupyter Notebook, Visual Studio Code, and OS (Operating System) Terminal, providing pre-installed AI libraries and tools for data analysis. This platform offers scalable computing resources, supports collaboration and sharing, and includes data visualization and experiment tracking capabilities. PAI-DSW simplifies the data science workflow and serves as an efficient choice for developing AI models. Using PAI-DSW, users can fine-tune the Diffusion model and algorithm provided by PAI to build a text-image generation model specific to their scenarios.
2. PAI-EAS (Elastic Algorithm Service): This platform simplifies the deployment and management of machine learning algorithms. PAI-EAS offers elastic scalability, an algorithm marketplace, end-to-end model training and inference, AutoML capabilities, model monitoring, and efficient resource management. Users can deploy the model generated through fine-tuning or utilize PAI’s default Diffusion model as an online service in PAI-EAS to generate corresponding images based on input text.
3. PAI-DLC (Deep Learning Container): It provides pre-configured containers for deep learning, streamlining the setup and management of deep learning environments. PAI-DLC includes ready-to-use containers with popular deep learning frameworks like TensorFlow and PyTorch. By leveraging PAI-DLC, users can quickly deploy and utilize deep learning frameworks without manual setup and configuration, saving time and effort in the development and deployment of deep learning models.

The overall architecture of text-to-image model development and deployment on PAI involves utilizing PAI-DSW for fine-tuning the model, PAI-EAS for online deployment and generation of images from text, and PAI-DLC for streamlined deep learning environment setup and management.

### Play around with PAI Diffusion Services

Before we dive into the deployment options, let’s ensure we have everything ready for a smooth process. Here are the preparations you need to complete:

1. Subscription and Workspace: Make sure you have subscribed to PAI (Designer, DSW, EAS) and created a default workspace. If you haven’t done so, follow the instructions in the “[Activate and Create a Default Workspace](https://help.aliyun.com/document_detail/326190.htm)” guide to set it up.
2. OSS Storage Space: You’ll need an OSS storage space (Bucket) to store datasets, model files, and configuration files. If you haven’t created one yet, refer to the “[Creating a Storage Space](https://help.aliyun.com/document_detail/31885.htmhttps://help.aliyun.com/document_detail/31885.htm)” guide for step-by-step instructions.
3. DSW Instance (Optional): If you prefer to use a DSW instance for fine-tuning, ensure that it is created and running smoothly. The “[Creating and Managing a DSW Instance](https://help.aliyun.com/document_detail/163684.htm)” guide will assist you in setting it up correctly.
4. Dedicated Resource Group: Create a dedicated resource group specifically for PAI-EAS. This resource group will be used to deploy your trained model. Refer to the “[Using a Dedicated Resource Group](https://help.aliyun.com/document_detail/120122.htm)” guide for detailed instructions on creating one.
5. Resource Group Machine: The type of machine you choose depends on the deployment option you prefer. If you plan to use PAI’s default Diffusion model, create a resource group machine with an A10 or A100 card type. For fine-tuned models, select resource group machines with card types such as T4, V100, A10, or A100.

By completing these preparations, you’ll be ready to explore the deployment options and choose the one that best suits your needs and preferences. Let’s dive in!

### Deploy on PAI-EAS with EAS

1. Log into the [Alibaba Cloud Console](https://www.alibabacloud.com/knowledge/developer/login-methods-for-alibaba-cloud-server?spm=a2c65.11461447.0.0.38333bdbbWFwjs), your gateway to powerful cloud computing solutions.

2. Navigate to the PAI page, where the magic of Machine Learning Platform for AI awaits. You can search for it or access it through the [PAI console](https://pai.console.aliyun.com/).

![](https://cdn-images-1.medium.com/max/800/0*tJDYfDHfP93-t0Jv)3. If you’re new to PAI, fear not! Creating a workspace is a breeze. Just follow the [documentation](https://www.alibabacloud.com/help/en/machine-learning-platform-for-ai/latest/create-a-workspace) provided, and you’ll be up and running in no time.

4. Immerse yourself in the world of workspaces as you click on the name of the specific workspace you wish to operate in. It’s in the left-side navigation pane.

![](https://cdn-images-1.medium.com/max/800/0*HQP4xi-0sxIXIo_M)5. In the left navigation bar of the workspace page, select Model Deployment > Model Online Service (EAS) to enter the PAI EAS Model Online Service page.  
6. On the Inference Service tab, click Deploy Service .  
7. On the Deploy Service page, configure parameters and click Deploy .

1. Paste the content of the following JSON file into the text box under the corresponding configuration edit .


```
{  

```
* name : need to be replaced with your own service name, you can directly modify this parameter in the console model service information area.
* resource : It needs to be replaced with your own resource group. You can directly modify this parameter in the resource deployment information area of the console.
* illustrate
* A resource group machine with an A10 or A100 card type is required.

### Call the Service

The service provides a RESTful API, and the specific Python call example is as follows.


```
import json  
import sys  
import requests
```

```
import base64  
from io import BytesIO  
from PIL import Image  
import os  
from PIL import PngImagePlugin
```

```
hosts = '<Replace with your service call address>' # Service address, which can be obtained in the call information under the service method column of the target service.  
head = {  
    "Authorization": "<Replace with your service token>" # Service authentication information, which can be obtained in the call information under the service method column of the target service.  
}
```

```
def decode_base64(image_base64, save_file):  
    img = Image.open(BytesIO(base64.urlsafe_b64decode(image_base64)))  
    img.save(save_file)  
  

```

```
datas = json.dumps({  
    "text": "a cat playing the guitar",   
    "skip_translation": False,  
    "num_inference_steps": 20,  
    "num_images": 1,  
      "use_blade": True,  
    }  
)
```

```
r = requests.post(hosts, data=datas, headers=head)  
data = json.loads(r.content.decode('utf-8'))
```

```
text = data["text"]  
images_base64 = data["images_base64"]  
success = data["success"]  
error = data["error"]  
print("text: " + text)  
print("num_images:" + str(len(images_base64)))
```

```
decode_base64(images_base64[0], "./decode_ldm_base64.png")
```
The service call parameters are configured as follows.

![](https://cdn-images-1.medium.com/max/800/0*Vh8maqmmJZVr80sO)The service return parameters are described as follows.

![](https://cdn-images-1.medium.com/max/800/0*xCvHYSFnKEYhnSAP)### Utilizing the Fine-Tuned Diffusion Model Powered by PAI

### Prepare Data

1. Prepare training and validation datasets.

This article uses a subset of a text and image dataset for model training. The specific format requirements of the training data set and the verification data set are as follows.

1) Data: Training dataset; Format: TSV; Columns: text column, Image column (base64 encoded); File: [T2I\_train.tsv](https://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/file-manage-files/zh-CN/20230223/mchs/T2I_train.tsv).  
2) Data: Validation dataset; Format: TSV; Columns: text column, Image column (base64 encoded); File: [T2I\_val.tsv](https://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/file-manage-files/zh-CN/20230223/wuti/T2I_val.tsv)

2. Upload the dataset to the OSS Bucket. For details, see [Uploading Files](https://help.aliyun.com/document_detail/31886.htm) .

### Construct a Text-graph Generation Model

1. Enter DSW Gallery, see [Function Trial: DSW Gallery](https://help.aliyun.com/document_detail/441723.htm) for details .

2. In the Chinese text-image generation area based on the EasyNLP Diffusion model on the Deep Learning tab , click Open in DSW , and follow the console operation instructions to build a text-image generation model, namely the Finetune model.

3. Package the trained model and other related configuration files. Package the trained model and other configuration files into tar.gz format, and upload them to the user’s OSS Bucket. The directory structure for models and configurations is shown in the figure below.

![](https://cdn-images-1.medium.com/max/800/0*K1Re5IsA_g5hMo2-)You can use the following command to pack the directory into tar.gz format.


```
cd finetuned\_model/   

```
finetuned\_model.tar.gz is the packaged model file.

### Deploy and Call Model Service

1. Deploy the model service.

2. Refer to Step 1: Deploy the service, paste the content of the following JSON file into the text box under the corresponding configuration edit, and deploy the Finetune model service.


```
{  

```
in:

* model\_path: It needs to be replaced with the storage path of the packaged model file in the OSS Bucket.
* name: need to be replaced with your own service name. You can directly modify this parameter in the console model service information area.
* resource: It needs to be replaced with your own resource group. You can directly modify this parameter in the resource deployment information area of the console.

illustrate The Finetune model supports resource group machines using card types such as T4, V100, A10, and A100.

3. Call the model service.

Refer to Step 2: Invoke the service to call the Finetune model service. Among them: text only supports Chinese text input; service call parameters do not support configuration skip\_translation.

### Conclusion

The GenAI-Diffusion Graphic Generation Solution offers a wide range of benefits and applications that can revolutionize various industries. With its stable diffusion and webUI interface, this solution enables automated content creation for marketing and advertising, personalized recommendations, chatbots, and virtual environment generation.

One of its key benefits is the ability to automate content creation for marketing and advertising purposes. Marketers can easily generate high-quality graphics and visuals tailored to their specific needs, saving time and resources while ensuring consistency and enhancing brand messaging.

The solution also excels in personalized recommendations and chatbot applications. By leveraging AI and fine-tuning through the webUI interface, businesses can provide personalized recommendations to customers, improving user experiences and increasing customer satisfaction. Additionally, chatbots powered by GenAI-Diffusion can generate visually engaging content, enhancing communication and creating a more interactive conversational experience.

Moreover, this solution is a valuable tool for creating virtual environments and generating visual content. Whether it’s for gaming, virtual reality experiences, or architectural visualizations, GenAI-Diffusion seamlessly generates realistic and immersive graphics. The ability to fine-tune through the webUI interface allows users to customize visuals to their specific requirements, resulting in visually stunning virtual environments.

If you would like to learn more about the GenAI-Diffusion Graphic Generation Solution and its applications, we encourage you to [contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) or visit our website at [www.alibabacloud.com](http://www.alibabacloud.com/). Our team of experts is available to provide further information and discuss how this solution can benefit your specific needs. Together, let’s explore the possibilities of automated content creation, personalized recommendations, chatbots, and virtual environments.



By [Dr. Farruh](https://medium.com/@k-farruh) on [October 5, 2023](https://medium.com/p/805d7d1a2397).

[Canonical link](https://medium.com/@k-farruh/unleashing-the-creative-potential-with-genai-diffusion-graphic-generation-solution-from-alibaba-805d7d1a2397)

Exported from [Medium](https://medium.com) on May 25, 2024.

