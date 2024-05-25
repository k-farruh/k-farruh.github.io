---
title: 'Run Machine Learning Model On Alibaba Cloud With Docker'
date: 2023-03-04
permalink: /posts/2023-03/Run-Machine/
tags:
  - cool posts
  - category1
  - category2
---

Run Machine Learning Model on Alibaba Cloud with Docker
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
 

Run Machine Learning Model on Alibaba Cloud with Docker
=======================================================




Previously, we prepared an ECS instance and Docker environment at the ECS instance here and here. Now it’s time to run the Machine Learning…




---

### Run Machine Learning Model on Alibaba Cloud with Docker

Previously, we prepared an ECS instance and Docker environment at the ECS instance [here](https://medium.com/@k-farruh/prepare-gpu-container-environment-on-alibaba-cloud-ecs-instance-1f16aef0654b) and [here](https://medium.com/@k-farruh/nvidia-tensorflow-docker-image-on-the-alibaba-cloud-ecs-part-2-b3476c19493c). Now it’s time to run the Machine Learning Model on Docker and get results. Let’s take on image classification tasks as an example. These tasks are well-studied and have a lot of benefits in terms of business values. Moreover, it is fundamental to attempt to comprehend an entire image.

![](https://cdn-images-1.medium.com/max/800/0*UwPoNHxXN2u39aUx.png)### Image Classification

Image classification categorizes and labels groups of pixels or vectors within an image based on specific rules within an image. The categorization law can be devised using one or more spectral or textural characteristics. Two general methods of classification are ‘supervised’ and ‘unsupervised.’ The goal is to classify the image by assigning it to a specific label. Typically, Image Classification deals with images in which only one object appears and being analyzed.

Inspired by [nidolow](https://github.com/nidolow), we will get a pre-trained [model](https://github.com/k-farruh/image-classification) for image classification and put it in Docker. To run a TensorFlow program developed in the host machine within a container, mount the host directory and change the container’s working directory (-v hostDir:containerDir -w workDir). In our example, it will be `-v $PWD:/classification -w /classification`, *PWD* is a current directory, so the codes should be in this directory.


```
docker run --gpus all -it --rm -v $PWD:/classification -w /classification tf.2.1.0-gpu-cat\_dog:v0.0.1 bash
```
After running the above command, we will be in the docker image and can start to prepare the python environment.


```
pip install -r requirements.txt
```
Now the environment is ready, and we can run the pre-trained model to test it.


```
python src/predict.py -m models/model-2a05ce2.mdl -d data/samples/ -o output\_file.csv
```
If, as a result, we can see the similar `output_file.csv` , then congrats, you have succeeded in preparing the model.

![](https://cdn-images-1.medium.com/max/800/1*y2bRXweNcePxvt4K5CuXzA.png)The docker image can be prepared to upload [docker hub](https://hub.docker.com/) or Alibaba Cloud [Container Registry](https://www.alibabacloud.com/product/container-registry). Container Registry allows you to manage images throughout the image lifecycle, and it provides an optimized solution for using Docker in the cloud.

Firstly, let’s create an image from the container. To create an image from the container, we can use the following command syntax: `docker commit <Container ID or container name> [<Repository name>[:<Tag>]]`. Run the image and derive a new image with a simple name for testing and restoration purposes.


```
docker commit f1bc11\* tf.2.1.0-gpu-cat\_dog:v0.0.2
```
![](https://cdn-images-1.medium.com/max/800/1*o2_vQaVJ8a_7vpa7xRMu4w.png)Here is [documentation](https://docs.docker.com/docker-hub/repos/) on how to push the docker image to the docker hub. In a simplified way, it needs to run the below command (please put your information).


```
docker push <hub-user>/<repo-name>:<tag>
```
Another way is to create a docker image file, which will be part of MLOps and help decrease unnecessary work in the future. Later on, we will have an article that will be created the whole ML production lifecycle with MLOps.



---

### Create a Docker Image

Dockerfile is a simple text file with instructions to build Docker images. Let’s start with the preparation of the Dockerfile. First, we create the Dockerfile in the working directory.


```
vim Dockerfile
```
By pressing the key “I,” it can be entered the edit mode and add the following content to the file:


```
#Declare a base image.   
FROM tensorflow/tensorflow:latest-py3  
#Update and Upgrade apt   
RUN apt-get update  
RUN apt-get upgrade -y  
#Specify the commands that you want to run before the container starts. You must append these commands to the end of the RUN command. Dockerfile can contain up to 127 lines. If the total length of your commands exceeds 127 lines, we recommend that you write these commands to a script.   
  
RUN pip install --upgrade pip  
RUN pip install pandas==1.0.5  
RUN pip install scikit\_learn==0.23.1  
RUN pip install pillow==8.4.0  
  
RUN \   
 cd / \  
 &&\   
 git clone https://github.com/k-farruh/image-classification.git \  
 &&\   
 cd image-classification
```
In the same manner, press the key “Esc,” enter `:wq` and press the key “Enter” key to save and exit Dockerfile. Then create an image.


```
docker build -t tf.2.1.0-gpu-cat\_dog:v0.0.3 . #Use Dockerfile to create an image. . at the end of the command line specifies the path of Dockerfile and must be provided.   
docker images #Check whether the image is created.
```
Run the container and check its state.


```
docker run -d webalinux3:v1 #Run the container in the background.   
docker ps #Query the containers that are in the running state.   
docker ps -a #Query all containers, including those in the stopped state.   
docker logs CONTAINER ID/IMAGE #If the container does not appear in the query results, check the startup log to troubleshoot the issue based on the container ID or name.
```
By default, the image is pushed to Docker Hub. You must log on to Docker, add a tag to the image, and then name the image in the `<Docker username>/<Image name>:<Tag>` format. Then, the image is pushed to the remote repository.


```
docker login --username=dtstack\_plus registry.cn-shanghai.aliyuncs.com #Enter the password of the image repository after you run this command.   
docker tag [ImageId] registry.cn-shanghai.aliyuncs.com/dtstack123/test:[Tag]   
docker push registry.cn-shanghai.aliyuncs.com/dtstack123/test:[Tag]
```
However, we recommend alternatives to the Docker Hub, the [Alibaba Cloud Container Registry](https://www.alibabacloud.com/product/container-registry). Here is how to use the [Container Registry to build the docker image](https://www.alibabacloud.com/help/en/container-registry/latest/quick-start-use-container-registry-enterprise-edition-instances-to-build-images). Since we have prepared every step and will be another paper regarding the container register, we press the button to create a docker image or wait until the scheduler creates a docker image.

![](https://cdn-images-1.medium.com/max/800/0*u7mcAyli0nzX1lUA.png)### What to do next?

Since our long-term goal is to make fully automated MLOps, an emerging field, MLOps is rapidly gaining momentum amongst Data Scientists, ML Engineers, and AI enthusiasts. We start our journey by preparing the docker image for inference of the machine learning model. Little by little, we will be closer to our goal and make easy MLOps with the lowest cost and time spent on the model lifecycle.



By [Dr. Farruh](https://medium.com/@k-farruh) on [March 4, 2023](https://medium.com/p/8cc577ae3e4c).

[Canonical link](https://medium.com/@k-farruh/run-machine-learning-model-on-alibaba-cloud-with-docker-8cc577ae3e4c)

Exported from [Medium](https://medium.com) on May 25, 2024.

