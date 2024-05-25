---
title: 'Nvidia Tensorflow Docker Image On The Alibaba Cloud Ecs Part 2'
date: 2023-02-23
permalink: /posts/2023-02/NVIDIA-Tensorflow/
tags:
  - cool posts
  - category1
  - category2
---

NVIDIA-Tensorflow Docker Image on the Alibaba Cloud ECS Part 2
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
 

NVIDIA-Tensorflow Docker Image on the Alibaba Cloud ECS Part 2
==============================================================




Tensorflow runs in the docker and GPU within docker




---

### NVIDIA-Tensorflow Docker Image on the Alibaba Cloud ECS Part 2


> [Tensorflow](https://www.tensorflow.org/install/docker) runs in the docker and [GPU within docker](https://github.com/NVIDIA/nvidia-docker)

[![](https://cdn-images-1.medium.com/max/800/0*NXSo1W5r58qhbD8Y.png)](https://www.alibabacloud.com/blog/power-up-your-journey-to-cloud-with-alibaba-cloud-elastic-compute-service-ecs_595455)In the [previous article](https://medium.com/@k-farruh/prepare-gpu-container-environment-on-alibaba-cloud-ecs-instance-1f16aef0654b), we prepared ECS and Docker environment. Now come to the second part, we will install Nvidia-Docker and pull the Tenforflow GPU docker image and run the image classification pre-trained model on the docker environment.

The code examples are compatible with TensorFlow version 2.1.0 with GPU support, so we pull exactly this version from the docker registry:

First, we will check GPU card availability:


```
lspci | grep -i nvidia
```
Then we verify your `nvidia-docker` Installation:


```
docker run --rm --gpus all nvidia/cuda:10.1-base nvidia-smi
```
In the same manner, we verify GPU-enabled TensorFlow image verification:


```
docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \  
 python -c "import tensorflow as tf; print(tf.reduce\_sum(tf.random.normal([1000, 1000])))"
```
Finally, we pull TensorFlow:


```
docker pull tensorflow/tensorflow:2.1.0-gpu
```
Let’s check the docker images in the machine:`docker images`

![](https://cdn-images-1.medium.com/max/800/1*2G4DaiD7LtYtyeuIHqZ5-A.png)The original name of the docker image has no connection with the current product. Hence, let’s modify tags to make them related to a related project. Here as an example, we use dog and cat classification tasks, so we name them like `machine learning library name-its version-project name:the tag will be the version of the docker image`. It gives us an opportunity to quickly identify and understand when we will have a dozen or more docker images in the machine.


```
docker tag tensorflow/tensorflow:2.1.0-gpu tf.2.1.0-gpu-cat\_dog:v0.0.1  
docker images
```
Change the tag and view existing images.

![](https://cdn-images-1.medium.com/max/800/1*9L04ZvTX6aaPLW8NcbCu2A.png)Now we have two containers with different tags but the same image\_id, and it’s better to untag the redundant one and print the list of docker images again:


```
docker rmi -f tensorflow/tensorflow:2.1.0-gpu  
docker images
```
![](https://cdn-images-1.medium.com/max/800/1*osARAkAN4sSzB5aqysmAZQ.png)#### Manage Containers

Congratulations, now you have a running container with installed TensorFlow and supports GPU, and the next step is to access the container. PreviousRun the `docker images` command to obtain the **ImageId** value, which is `cb908459d986`. Then, run the `docker run` command to access the container. To keep the container running in the background, we run it with `--detach` (or `-d`) argument. Usually, Docker gives a random sweet name to the container. We can give the name of the container by ourselves. For this need to add the `--name` parameter to the command to specify `cat_dog` the container name.


```
docker run -t -d --name cat\_dog cb908459d986 /bin/bash
```
By the running command `docker ps -a` we can see the list of containers

![](https://cdn-images-1.medium.com/max/800/1*uEPVsPYuN1Lm_I59cUVIrQ.png)Container with the specified nameLet’s access the container that runs in the background.


```
docker exec -it cat\_dog /bin/bash
```
![](https://cdn-images-1.medium.com/max/800/1*q78lpXHYvcHzQSBnY4GvXQ.png)To from the container bash, run the `exit`.



---

Now we have the ready environment to run the inference model on this machine. Alibaba Cloud ECS instances with Docker are a fantastic platform for deploying and using AI technologies. The combination of Docker and Alibaba Cloud ECS instances provides a range of benefits, including the ability to run applications in isolated containers, manage the lifecycle of applications, and access a range of AI and big data services. With these tools, developers can build and deploy intelligent applications with ease and efficiency, solving complex problems and making tasks faster, easier, and more efficient. The following article will be about how to run a Machine Learning model on Docker under the Alibaba Cloud environment.



By [Dr. Farruh](https://medium.com/@k-farruh) on [February 23, 2023](https://medium.com/p/b3476c19493c).

[Canonical link](https://medium.com/@k-farruh/nvidia-tensorflow-docker-image-on-the-alibaba-cloud-ecs-part-2-b3476c19493c)

Exported from [Medium](https://medium.com) on May 25, 2024.

