---
title: 'O Properly Use The Gpu Within A Docker Container'
date: draft_How-
permalink: /posts/draft_H/How-to/
tags:
  - cool posts
  - category1
  - category2
---

How to Properly Use the GPU within a Docker Container
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
 

How to Properly Use the GPU within a Docker Container
=====================================================




Note: we have also published how to use GPUs in Docker on our blog. In this post, we walk through the steps required to access your…




---

### 

### How to Properly Use the GPU within a Docker Container

### 

### Note: we have also published [how to use GPUs in Docker](https://blog.roboflow.ai/use-the-gpu-in-docker/) on our blog. In this post, we walk through the steps required to access your machine’s GPU within a Docker container.

### 

Configuring the GPU on your machine can be immensely difficult. The configuration steps change based on your machine’s operating system and the kind of NVIDIA GPU that your machine has. To add another layer of difficulty, when Docker starts a container — it starts from almost scratch. Certain things like the CPU drivers are pre-configured for you, but **the GPU is not configured when you run a docker container**. Luckily, you have found the solution explained here. It is called the **NVIDIA Container Toolkit**!

![]()Nvidia Container Toolkit ([Citation](https://github.com/NVIDIA/nvidia-docker))

### Potential Errors in Docker

When you attempt to run your container that needs the GPU in Docker, you might receive any of the following errors.

Error: Docker does not find Nvidia drivers


```
docker: Error response from daemon: Container command 'nvidia-smi' not found or does not exist..
```
Error: tensorflow cannot access GPU in Docker


```
I tensorflow/stream\_executor/cuda/cuda\_diagnostics.cc:150] kernel reported version is: 352.93  

```
Error: pytorch cannot access GPU in Docker


```
RuntimeError: cuda runtime error (100) : no CUDA-capable device is detected at /pytorch/aten/src/THC/THCGeneral.cpp:50
```
Error: keras cannot access GPU in Docker


```
The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
```
You may receive many other errors indicating that your Docker container cannot access the machine’s GPU. In any case, if you have any errors that look like the above, you have found the right place here.

### First, Make Sure Your Base Machine Has GPU Drivers

You must first install NVIDIA GPU drivers on your base machine before you can utilize the GPU in Docker. As previously mentioned, this can be difficult given the plethora of distribution of operating systems, NVIDIA GPUs, and NVIDIA GPU drivers. The exact commands you will run will vary based on these parameters. Here are some resources that you might find useful to configure the GPU on your base machine.

* [NVIDIA’s official toolkit documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
* [Installing NVIDIA drivers on Ubuntu guide](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
* [Installing NVIDIA drivers from the command line](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/)

Once you have worked through those steps, you will know you are successful by running the **nvidia-smi** command and viewing an output like the following.

![]()I have successfully installed GPU drivers on my Google Cloud Instance

Now that we can assure we have successfully assure that the NVIDIA GPU drivers are installed on the base machine, we can move one layer deeper to the Docker container.

### Next, Exposing the GPU Drivers to Docker

In order to get Docker to recognize the GPU, we need to make it aware of the GPU drivers. We do this in the image creation process. Docker image creation is a series of commands that configure the environment that our Docker container will be running in.

**The Brute Force Approach —**The brute force approach is to include the same commands that you used to configure the GPU on your base machine. When docker builds the image, these commands will run and install the GPU drivers on your image and all should be well. The brute force approach will look something like this in your Dockerfile (Code credit to [stack overflow](https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-container)):


```
FROM ubuntu:14.04  

```
**The Downsides of the Brute Force Approach —**First of all, every time you rebuild the docker image you will have to reinstall the image, slowing down development. Second, if you decide to lift the docker image off of the current machine and onto a new one that has a different GPU, operating system, or you would like new drivers — you will have to re-code this step every time for each machine. This kind of defeats the purpose of build a Docker image. Third, you might not remember the commands to install the drivers on your local machine, and there you are back at configuring the GPU again inside of Docker.

**The Best Approach —**The best approach is to use the NVIDIA Container Toolkit. The NVIDIA Container Toolkit is a docker image that provides support to automatically recognize GPU drivers on your base machine and pass those same drivers to your Docker container when it runs. So if you are able to run **nvidia-smi**, on your base machine you will also be able to run it in your Docker container (and all of your programs will be able to reference the GPU). In order to use the NVIDIA Container Toolkit, you simply pull the NVIDIA Container Toolkit image at the top of your Dockerfile like so — **nano Dockerfile**:


```
FROM nvidia/cuda:10.2-base  
CMD nvidia-smi
```
**This is all the code you need to expose GPU drivers to Docker**. In that Dockerfile we have imported the NVIDIA Container Toolkit image for 10.2 drivers and then we have specified a command to run when we run the container to check for the drivers. Now we build the image like so with **docker build . -t nvidia-test**:

![]()Building the docker image and calling it “nvidia-test”

Now we run the container from the image by using the command **docker run — gpus all nvidia-test.** Keep in mind, we need the **— gpus all** or else the GPU will not be exposed to the running container.

![]()Success! Our docker container sees the GPU drivers

From this base state, you can develop your app accordingly. In my case, I use the NVIDIA Container Toolkit to power experimental deep learning frameworks. The layout of a fully built Dockerfile might look something like the following (where /app/ contains all of the python files):


```
FROM nvidia/cuda:10.2-base  
CMD nvidia-smi#set up environment  
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl  
RUN apt-get install unzip  
RUN apt-get -y install python3  
RUN apt-get -y install python3-pipCOPY app/requirements\_verbose.txt /app/requirements\_verbose.txtRUN pip3 install -r /app/requirements\_verbose.txt#copies the applicaiton from local path to container path  
COPY app/ /app/  
WORKDIR /appENV NUM\_EPOCHS=10  
ENV MODEL\_TYPE='EfficientDet'  
ENV DATASET\_LINK='HIDDEN'  
ENV TRAIN\_TIME\_SEC=100CMD ["python3", "train\_and\_eval.py"]
```
The above Docker container trains and evaluates a deep learning model based on specifications using the base machines GPU. Pretty cool!

### Need Different base image in Dockerfile

Let’s say you have been relying on a different base image in your Dockerfile. Then, you can [install NVIDIA container runtime](https://docs.docker.com/config/containers/resource_constraints/#gpu).


```
apt-get install nvidia-container-runtime  
docker run -it --rm --gpus all ubuntu nvidia-smi
```
Now you can run other base images with nvidia container runtime (here we run ubuntu base).

### The Power of the NVIDIA Container Toolkit

Now that you have you written your image to pass through the base machine’s GPU drivers, you will be able to lift the image off the current machine and deploy it to containers running on any instance that you desire.

### Update: Need CuDNN and NVCC cuda toolkit on Docker?

The `nvidia/cuda:10.2-base` will only get you `nvidia-smi.` If you need `cuDNN` or `nvcc --version` you can pull from other NVIDIA Docker base images, namely: `nvidia/cuda:10.2-devel-ubuntu18.0.` (gets you nvcc cuda toolkit) and`nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04.` (gets you cuDNN).

### Conclusion

Congratulations! Now you know how to expose GPU Drivers to your running Docker container using the NVIDIA Container Toolkit.

Want to use your new Docker capabilities to do something awesome? You might enjoy our other posts on [training a state of the art object detection model](https://blog.roboflow.ai/training-efficientdet-object-detection-model-with-a-custom-dataset/), [training a state of the art image classification model](https://models.roboflow.ai/classification/resnet-32), or simply by looking into some [free computer vision data](https://public.roboflow.ai/)!



[View original.](https://medium.com/p/9c450df9fe9c)

Exported from [Medium](https://medium.com) on May 25, 2024.

