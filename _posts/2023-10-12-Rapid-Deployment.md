---
title: 'Rapid Deployment Of Ai Painting With Webui On Pai Eas Using Alibaba Cloud'
date: 2023-10-12
permalink: /posts/2023-10/Rapid-Deployment/
tags:
  - cool posts
  - category1
  - category2
---

Artificial Intelligence (AI) Painting or AI Generative Content (AIGC) is a fascinating field within artificial intelligence that focuses on creating visual content using advanced machine learning techniques. These areas of research and development have gained significant attention in recent years as they offer innovative and creative solutions for generating artwork, graphics, and other visual media. One of the foundation models for AIGC is the diffusion model.


### Rapid Deployment of AI Painting with WebUI on PAI-EAS using Alibaba Cloud

### Introduction

Artificial Intelligence (AI) Painting or AI Generative Content (AIGC) is a fascinating field within artificial intelligence that focuses on creating visual content using advanced machine learning techniques. These areas of research and development have gained significant attention in recent years as they offer innovative and creative solutions for generating artwork, graphics, and other visual media. One of the foundation models for AIGC is the diffusion model.

![](https://cdn-images-1.medium.com/max/800/1*Wm8X29dxukZYq_hw3KLaoQ.jpeg)### Diffusion Models

Diffusion models are a class of machine learning models that excel in generating sequential data, such as text or images, by iterative refining and updating the generated output. These models leverage the concept of gradual diffusion, where the generation process starts with a noisy or incomplete initial state and progressively refines it to produce more coherent and accurate results.

The diffusion process in these models involves multiple steps or iterations, with each step refining the generated output. The model estimates the conditional probability distribution of the next step at each iteration, given the current state. By repeatedly sampling from this conditional distribution and updating the state, the model gradually improves the quality and fidelity of the generated data.

Diffusion models are often used in various applications, such as image generation, text generation, and video synthesis. They have gained significant attention due to their ability to generate high-quality, diverse, and realistic samples. Unlike traditional generative models, diffusion models tend to produce more coherent and structured outputs by leveraging the sequential nature of the generation process.

### Stable Diffusion

Stable Diffusion is a specific type of diffusion model that focuses on generating images corresponding to given text prompts. It is an open-source and popular cross-modal generation model that aims to generate visually compelling images based on textual descriptions.

The stable diffusion process employed by this model involves iteratively refining the generated image based on the provided text prompt. Stable Diffusion ensures that the generated visual content accurately represents the intended concepts and ideas described in the prompt by optimizing the generated image to align with the textual input.

One of the critical advantages of Stable Diffusion is its ability to create high-quality and realistic images that closely match the provided text. This model leverages advanced deep learning algorithms and techniques to achieve impressive results. Iteratively updating the generated image progressively enhances the quality, coherence, and fidelity of the final output.

Stable Diffusion has found applications in various domains, ranging from creative content generation to marketing and advertising. It enables automated content creation, allowing marketers and content creators to quickly generate visually engaging graphics and visuals that align with their specific needs and brand messaging.

However, the optimization aspect always arises since the stable diffusion belongs to huge foundation models. One of the ways to optimize or increase the speed of transformers is quantization.

### Quantization

Quantization is an optimization technique in machine learning that reduces the precision of a model’s parameters. It converts data from 32-bit floating point values to 8-bit (int8) values. Quantization can be applied to a trained model or integrated into the training process.

Quantization reduces model size, improves portability, and speeds up computation. It also reduces the memory requirement and computational cost of using neural networks. Quantized neural networks increase power efficiency by reducing memory access costs and increasing computing efficiency.

These days, quantization like LoRA (Low-Rank Adapters) and QLoRA (Quantized Low-Rank Adapters), let’s have a look at those technologies.

### LoRA

LoRA is a method to improve the performance of pre-trained language models by adapting them to specific downstream tasks. It was introduced in a research paper titled “Low-Rank Adapters for Multi-task Learning in Transformers” by Pfeiffer et al. in 2020.

LoRA addresses this problem of efficiency by introducing task-specific adapters. Adapters are small neural networks that are added to the pre-trained model with minimal changes to its architecture. These adapters are task-specific and learn additional parameters that fine-tune the pre-trained model for a particular downstream task.

What makes LoRA unique is the utilization of low-rank parameterization techniques. Significant memory and computational savings can be achieved by imposing low-rank constraints on the adapter parameters. This is particularly useful when dealing with multiple tasks simultaneously, as the low-rank parameterization reduces the overall memory footprint and speeds up training and inference.

LoRA offers several advantages. It allows for efficient multi-task learning, where a single pre-trained model can be adapted to multiple downstream tasks using task-specific adapters. It also avoids catastrophic forgetting, where fine-tuning a pre-trained model on one task erases the learned representations for other tasks. Additionally, LoRA provides a scalable approach that can handle large-scale models and diverse tasks.

### QLoRA

QLoRA is a technique that combines the low-rank approximation of weight updates with quantization. It reduces the memory footprint of the weight updates by quantizing the low-rank matrices Wa and Wb.

In addition to reducing memory requirements, QLoRA introduces quantization to compress the weight updates further. The quantization process involves representing the weight updates with a lower bit-width representation, such as 4 bits. This significantly reduces the memory needed to store the weight updates.

The combination of low-rank approximation and quantization in QLoRA provides a highly memory-efficient solution for deploying and fine-tuning large language models. It efficiently adapts to different tasks or customers without excessive computational resources.

By using techniques like LoRA and QLoRA, ML engineers can optimize the memory usage and computational requirements of large language models, making it more feasible to deploy and customize these models in resource-constrained environments.

### Machine Learning Platform for AI

Alibaba Cloud’s [Machine Learning Platform for AI](https://www.alibabacloud.com/product/machine-learning) offers a comprehensive solution for AI and an example for text and image generation, providing an end-to-end, customizable white box solution. It supports text and image generation functions, allowing users to create intelligent text-image generation models tailored to their business scenarios. Alternatively, users can leverage the default models provided by PAI for model tuning and online deployment to generate diverse images based on different text inputs.

The following components of PAI play a vital role in this process:

1. [PAI-DSW](https://www.alibabacloud.com/help/en/pai/user-guide/dsw-notebook-service/) (Data Science Workshop): It is a collaborative platform designed for data scientists and researchers. PAI-DSW seamlessly integrates with Jupyter Notebook, Visual Studio Code, and OS (Operating System) Terminal, providing pre-installed AI libraries and tools for data analysis. This platform offers scalable computing resources, supports collaboration and sharing, and includes data visualization and experiment tracking capabilities. PAI-DSW simplifies the data science workflow and serves as an efficient choice for developing AI models. Using PAI-DSW, users can fine-tune the Diffusion model and algorithm provided by PAI to build a text-image generation model specific to their scenarios.
2. [PAI-EAS](https://www.alibabacloud.com/help/en/pai/user-guide/eas-model-serving/) (Elastic Algorithm Service): This platform simplifies the deployment and management of machine learning algorithms. PAI-EAS offers elastic scalability, an algorithm marketplace, end-to-end model training and inference, AutoML capabilities, model monitoring, and efficient resource management. Users can deploy the model generated through fine-tuning or utilize PAI’s default Diffusion model as an online service in PAI-EAS to generate corresponding images based on input text.
3. [PAI-DLC](https://www.alibabacloud.com/help/en/pai/user-guide/container-training/) (Deep Learning Container): It provides pre-configured containers for deep learning, streamlining the setup and management of deep learning environments. PAI-DLC includes ready-to-use containers with popular deep learning frameworks like TensorFlow and PyTorch. By leveraging PAI-DLC, users can quickly deploy and utilize deep learning frameworks without manual setup and configuration, saving time and effort in developing and deploying deep learning models.

The architecture of text-to-image model development and deployment on PAI involves utilizing PAI-DSW for fine-tuning the model, PAI-EAS for online deployment and generation of images from text, and PAI-DLC for streamlined deep learning environment setup and management.

### Step-By-Step Tutorial

This step-by-step tutorial will guide you on quickly deploying the AIGC Stable Diffusion WebUI painting AI-web application using Alibaba Cloud’s PAI-EAS. You can deploy the model, start the WebUI for inference, and experience the power of AI-generated content. Let’s dive in!

### Step 1: Model Deployment

1. [Access](https://www.alibabacloud.com/help/en/pai/user-guide/grant-the-permissions-that-are-required-to-use-eas) the [PAI-EAS Model](https://www.alibabacloud.com/help/en/pai/user-guide/overview-2) Online Service page on the Alibaba Cloud platform;

2. [Login](https://www.alibabacloud.com/help/en/pai/user-guide/activate-pai-and-create-the-default-workspace) to the PAI console;

3. Select your default workspace from the left navigation bar;

4. Navigate to Model Deployment > Elastic Algorithm Service (EAS) on the workspace page in a figure number 1;

![](https://cdn-images-1.medium.com/max/800/0*rt-yXpGHqlWdda3G)5. Put “Service Name”, number 2 red rectangle. Further, we will put only numbers in brackets, like [2];

6. Select the image as PAI Image [3] and image “stable-diffusion-webui” with version. Writing this tutorial time, it was version “4.0-standard”;

![](https://cdn-images-1.medium.com/max/800/0*MqOHCH4KYCjls9Qs)7. Then, choosing a GPU virtual machine, at least P100 or above, is recommended, and T4 will be too slow. We tried the GU30 GPU machine, which works pretty well at an economical price.

![](https://cdn-images-1.medium.com/max/800/0*CNRyr48NTNr3qkpQ)8. If one of you is familiar with the configuration code, feel free to change JSON deployment.

9. Click on Deploy Service to start the deployment process.

Now, your WebUI with stable diffusion is ready.

### Step 2: Starting SDWebUI for Model Inference

1. On the PAI-EAS Model Online Service page, click on the View Web Application under the Deployment Method column for the model you deployed.

2. You will be directed to the Stable Diffusion SDWebUI application page.

3. In the Prompt area, input your desired content (e.g., “cute dog”) and click on Generate to initiate the AIGC process.

![](https://cdn-images-1.medium.com/max/800/0*9ehvURT4Wb-ckZZO)4. The generated inference result will be displayed on the page.

### Step 3: Starting the Model Service

If the model service is not called within 30 minutes, the service instance will automatically scale stops, and the model status will change to Stopped. If you need to use the service again, follow these steps:

1. On the PAI-EAS Model Online Service page, click the Start button for the corresponding model under the Deployment Operation column.
2. Wait for the model status to change from Stopped to Running, indicating that the service runs normally.

![](https://cdn-images-1.medium.com/max/800/0*n3g9Iaa-OXK5QeZF)### Conclusion

In this tutorial, we explored the rapid deployment of AI painting with stable diffusion WebUI using Alibaba Cloud’s PAI-EAS. By following the steps described, you were able to deploy the model, start the WebUI for model inference, and experience the power of AI-generated content creation. This demonstrates the ease and efficiency of leveraging AI technologies for automated content generation. This solution allows businesses to enhance their marketing efforts, personalize recommendations, create virtual environments, and engage users with visually stunning graphics.

Moreover, this solution is valuable for creating virtual environments and generating visual content. Whether for gaming, virtual reality experiences, or architectural visualizations, AI Painting with Stable Diffusion models seamlessly generates realistic and immersive graphics. The ability to fine-tune through the web UI interface allows users to customize visuals to their specific requirements, resulting in visually stunning virtual environments.

If you would like to learn more about AI Painting/AIGC and its applications, we encourage you to [contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us) or visit our website at [www.alibabacloud.com](http://www.alibabacloud.com/). Our team of experts is available to provide further information and discuss how this solution can benefit your specific needs. Let’s explore the possibilities of automated content creation, personalized recommendations, chatbots, and virtual environments together.



By [Dr. Farruh](https://medium.com/@k-farruh) on [October 12, 2023](https://medium.com/p/0fb4da398989).

[Canonical link](https://medium.com/@k-farruh/rapid-deployment-of-ai-painting-with-webui-on-pai-eas-using-alibaba-cloud-0fb4da398989)

Exported from [Medium](https://medium.com) on May 25, 2024.

