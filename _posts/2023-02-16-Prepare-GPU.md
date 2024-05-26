---
title: 'Prepare Gpu Container Environment On The Alibaba Cloud Ecs Part 1'
date: 2023-02-16
permalink: /posts/2023-02/Prepare-GPU/
tags:
  - cool posts
  - category1
  - category2
---
# Prepare GPU-Container Environment on the Alibaba Cloud ECS Part 1
Nowadays, we have an extremely high-speed changing live environment. Most changes come because of Artificial Intelligence (AI).

---

### Prepare GPU-Container Environment on the Alibaba Cloud ECS Part 1

Nowadays, we have an extremely high-speed changing live environment. Most changes come with the thriving of Artificial Intelligence (AI). The revolution started not only because of AI. It comes with other high-tech. One of the high-tech generators is containerization, and containers are part of MLOps. We start our journey to MLOps with easy-to-use containers. This article describes creating and preparing an environment to train or inference the AI model. Since Alibaba Cloud provides comprehensive tools and environments for deploying and using AI models, we will run example code and environment on it.

**Containerization** allows you to quickly and easily replicate your working environment. It makes it possible to initialize MLOps, and quickly reach the technical support L3 level. Moreover, containerizing allows developers to generate the same results repeatedly on a different machine. However, creating containers is time-consuming and requires expert knowledge. As a container, we will use docker images.

![](https://cdn-images-1.medium.com/max/800/1*GT8ICiDdFRHeDlTgicbxLg.png)Docker is a popular open-source platform that helps to automate the deployment, scaling, and management of applications and services. Its container-based approach to software development makes it easy to package and deploy applications consistently and repeatedly.

**Alibaba Cloud** is a leading cloud computing platform that offers a range of services, including Elastic Compute Service (ECS), which allows users to deploy and use Docker on any Operating System (OS). We run ESC with Ubuntu OS as an example. However, ECS supports all OS and even user-defined OS images. Using Docker on ECS, AI developers can build, deploy, and run their applications quickly and efficiently.



---

Using Docker on ECS can bring you several benefits:

1. Allows applications to run in isolated containers, meaning they can be deployed and run on any machine without worrying about dependencies or configuration issues. This makes it easy to move applications from one environment to another and ensures that they can run seamlessly across multiple machines, making it possible to scale them as needed.
2. Provides a range of tools that make it easy to manage applications' deployment, scaling, and maintenance. For example, Docker Compose is a tool that makes it easy to define and run multi-container applications, which means developers can define the dependencies between different containers and manage them as a single unit.
3. Provides a range of platform and AI services, such as machine learning and deep learning algorithms, which can be used to build and deploy intelligent applications. It also provides a range of big data services, such as data warehousing and data analytics, which can be used to analyze vast amounts of data and accurately make predictions.

As an initial step, we [sign-up with an Alibaba Cloud](https://www.alibabacloud.com/help/en/account-management/latest/sign-up-with-alibaba-cloud) account. Run instances that run an Ubuntu 20.04 operating system. For more information, see [Create an instance by using the wizard](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/create-an-instance-by-using-the-wizard#task-vwq-5g4-r2b).

In this article, we have chosen instances to run AI model inference. Developers not only need to consider inference models but also need to evaluate pricing, so an instance with T4 GPU will be an excellent choice to infer most of the AI models.



---

### Deploy Docker

To deploy, the docker image should be connected to the ECS instance, the detailed information regarding [ECS connection methods](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/connection-methods?spm=a2c63.p38356.0.0.42ae461235M4hj#concept-tmr-pgx-wdb) can be found at the following [link](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/connection-methods?spm=a2c63.p38356.0.0.42ae461235M4hj#concept-tmr-pgx-wdb). It's recommended to update the package sources list with the latest versions of the packages in the repositories. Then need to install packages to allow `apt` to use a repository over HTTPS:

![](https://cdn-images-1.medium.com/max/800/1*LPitr6FqCMs75PNkFr5HoQ.png)OS version and related information
```
 apt update  
 apt install \  
 ca-certificates \  
 curl \  
 gnupg \  
 lsb-release
```
It's recommended to have a look at the official documentation before installing any software. Hence here is the official documentation on how to [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). However, we provide whole steps to installing Docker on Ubuntu 20.04.

1. It is recommended to check if does machine already installed Docker. If yes, uninstall existing/old versions:


```
apt remove docker docker-engine docker.io containerd runc
```
2. Add the official GPG key of the Docker and set up the repository:


```
mkdir -m 0755 -p /etc/apt/keyrings  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg  
  
echo \  
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \  
 $(lsb\_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
3. To get newly added repositories, it needs to update `apt` and then install `Docker Engine, containerd, and Docker Compose:`


```
apt update  
apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
The installation of Docker has been done, but we have to verify whether the installation succeeds or not by checking its status of it and running the *hello-world*:


```
systemctl status docker
```
![](https://cdn-images-1.medium.com/max/800/1*DSBfg2TBaqkV528-S55rkg.png)Docker status is running, which means it can go to the next step
```
docker run hello-world
```
![](https://cdn-images-1.medium.com/max/800/1*_7JUUkDNZeWAfCgci-9V9A.png)Docker Image: Hello-WorldThe successful result can be defined by getting a similar response as shown in the pictures.

Let's check what Docker images the machine has:


```
docker images
```
![](https://cdn-images-1.medium.com/max/800/1*t9W2LDtN4UhZmJXsxmtNhw.png)Docker image listWe have installed Docker and tested it. Logically, the next step will be to pull docker images with Tensorflow and Nvidia-Docker, which we will do in the second part.



By [Dr. Farruh](https://medium.com/@k-farruh) on [February 16, 2023](https://medium.com/p/1f16aef0654b).

[Canonical link](https://medium.com/@k-farruh/prepare-gpu-container-environment-on-alibaba-cloud-ecs-instance-1f16aef0654b)

Exported from [Medium](https://medium.com) on May 25, 2024.

