---
title: 'Easy Mlops With Ack Alibaba Cloud Part 1'
date: 2023-03-29
permalink: /posts/2023-03/Easy-MLOps/
tags:
  - cool posts
  - category1
  - category2
---

Easy MLOps with ACK Alibaba Cloud — Part 1
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
 

Easy MLOps with ACK Alibaba Cloud — Part 1
==========================================




Kubernetes is an open-source container-orchestration system that enables teams to deploy, scale, and manage containerized applications. It…




---

![](https://cdn-images-1.medium.com/max/800/1*Q-EJwzSML360lSw8_6i2-Q.png)### Easy MLOps with ACK Alibaba Cloud — Part 1

K**ubernetes** is an open-source container-orchestration system that enables teams to deploy, scale, and manage containerized applications. It handles the scheduling of containers in a cluster and manages workloads so that everything runs as intended.

Enterprise businesses have been rapidly adopting the cloud and various cloud services to modernize their workloads and increase their agility and scalability. Through concepts like containerization and orchestration, companies have found ways to make applications more portable, increase efficiency and address challenges surrounding code deployment.

Alibaba Cloud, the global leader in cloud computing, offers various cloud services, including **A**libaba Cloud **C**ontainer Service for **K**ubernetes (ACK), a fully managed Kubernetes service.

We were running Kubernetes on Alibaba infrastructure before ACK was once a challenge due to several manual configurations which required extensive operational expertise and effort. Now, ACK can be used for various use cases, including machine learning/big data/web applications and others. After the ACK was successfully tested internally, have decided to make as a cloud-native product on Alibaba Cloud.

Moreover, the product is popular and got positive feedback from the user that The Forrester Wave™ was named the Alibaba Cloud, a Leader in Public Cloud Container Platforms.

[![](https://cdn-images-1.medium.com/max/800/1*6S-UwUL2ohwJ5qVmkPkjIQ.jpeg)](https://www.alibabacloud.com/zh/about/forrester-wave-public-cloud-container-platforms-q1-2022)### Dissecting Containerization and Kubernetes Orchestration

First, before diving into ACK, let's go over containerization, orchestration, and Kubernetes.

#### What is Containerization?

**Containerization** enables developers to build and deploy applications faster and with more security. Traditionally, code is developed in a specific environment. When moves to different environments happen, bugs can be introduced. With containerization, this problem is removed since application code, configuration files, and dependencies required for the code to run are all bundled together. This container can stand alone and run on any platform or cloud.

#### What is Orchestration?

**Orchestration** helps IT operations manage complex tasks and workflows by automatically configuring, managing, and coordinating applications, systems, and services. When DevOps have to manage multiple servers and applications, orchestration helps to combine various automated tasks and configurations across groups of systems.

#### What is Kubernetes?

**Kubernetes** is an open-source container-orchestration system that enables teams to deploy, scale, and manage containerized for developing cloud-native applications. It handles the scheduling of containers in a cluster and manages workloads so that everything runs as intended. Kubernetes was designed for software development teams and IT operations to work together, allowing for easy adoption of MLOps workflows. Kubernetes is now maintained by the Cloud Native Computing Foundation (CNCF).

### ACK Benefits

ACK offers the best way to run Kubernetes by taking away the manual effort development teams once had to go through in setting up Kubernetes clusters on Alibaba Cloud. ACK provides a highly-available and scalable control plane that runs across multiple availability zones, eliminating any single points of failure.

Applications managed by ACK are fully compatible with those managed by a standard Kubernetes environment. That's because ACK runs upstream Kubernetes and is also a certified Kubernetes conformant.

Since Kubernetes is open source, the community contributes code to its ongoing development and Alibaba's contributions as part of that community.

* **High Availability**. ACK runs the Kubernetes management infrastructure across multiple Alibaba Cloud Availability Zones. This allows ACK to detect and replace unhealthy control plane nodes automatically, leading to on-demand, zero downtime upgrades and security patches.
* **Security.** The latest security patches are automatically applied to the cluster control plane. Plus, Alibaba leverages and coordinates with the ACK community to resolve critical issues before new releases are deployed to existing clusters.

#### ACK Use Cases

* **Hybrid Deployment.** ACK can be used on Alibaba Outposts to run low-latency containerized applications to on-prem systems. Alibaba Outposts are another fully managed service from Alibaba that extends Alibaba infrastructure, services, tools, and APIs to essentially any related sites. ACK on Outposts allows you to manage on-premise containers as quickly as in the cloud.
* **Batching Processing.** Run sequential or parallel batch work on an ACK cluster using the Kubernetes Jobs API. ACK will allow you to plan, schedule and execute batch workloads across the Alibaba compute services and features, whether using ECS, Fargate, or Spot Instances.
* **Web Apps**. Build web applications that can scale up and down automatically and run in a highly available configuration across multiple Availability Zones. When using ACK, web apps can leverage Alibaba's performance, scalability, availability, and reliability benefits.
* **Big Data.** Kubernetes makes implementing Big Data easier for infrastructure and operations teams to deploy, scale, and manage software and resources flexibly and reliably. Teams responsible for big data platforms and infrastructure already have enough to ensure that data scientists and engineers have access to the data and systems they need, making it essential to have solutions that simplify and streamline infrastructure management.
* **Machine Learning.** Kubernetes are playing an essential role in the evolution of machine learning. Containerized development and deployment are becoming crucial elements for machine learning models. Machine learning models can be easily scaled and scheduled when containerized, and workload performance management can be automated. Containerization offers a consistent state across different servers or cloud environments. With a strong community backing the open-source Kubernetes, it's one of the most popular ways of managing container machine-learning models. With Kubernetes, organizations can embed end-to-end machine-learning workflows within containers.
* **Content Management.** With ACK, Alibaba has made it easier for organizations to deploy cloud-native applications. Having a cloud-native CMS, for instance, allows organizations to leverage the benefits of containers and apply them to running a content management system and CMS-driven web and mobile apps. As companies look for ways to improve the digital customer experience by publishing content to multiple channels, a cloud-native CMS can help in several ways.

The above use cases allow for lower upfront costs compared to on-premise solutions, more accessibility for content authors at any time and on any device, developer-friendly tools and services, and the capacity to scale as required.

ACK allows enterprises to deploy cloud-scalable DevOPS/MLOps environments and serverless digital experience applications quickly and cost-effectively.

### Be Independent

To trust the business and computing environment is not to be taken lightly. It is a significant decision that can seriously impact your enterprise positively and negatively. Choosing the wrong provider can result in lost revenue, missed opportunities, and additional technical complications to your IT infrastructure. Finding the right cloud solution and provider will lead to gains in productivity, increased customer satisfaction, and the ability to use your company's data more effectively.

One of the considerations in choosing a cloud provider is independence. That means you will not be an adjective on cloud vendor technology. How can it be investigated by checking the product's availability in open-source communities? That allows you to be independent and be sure the services from cloud vendors are error-free and mature since the product is tested and used by a dozen thousand developers, usually open-source developers picky and not solidarity to the bugs.

As below shown, the Alibaba Cloud provides its proprietary ASK as open-source and provides container-based DevOps.

[**Aliyun (Alibaba Cloud) Container Service**  
*阿里云容器服务 - ACK (Container Service for Kubernetes) , ASK (Serverless Kubernetes) , ACR (Container Registry Service), ASM…*github.com](https://github.com/AliyunContainerService "https://github.com/AliyunContainerService")[**GitHub - AliyunContainerService/DevOps: 阿里云容器服务持续交付**  
*阿里云容器服务持续交付 基于容器服务的持续集成与云端交付（一）- 交付之禅 基于容器服务的持续集成与云端交付（二）- 多维度打磨交付能力 基于容器服务的持续集成与云端交付（三）- 从零搭建持续交付系统…*github.com](https://github.com/AliyunContainerService/DevOps "https://github.com/AliyunContainerService/DevOps")### Control Everything by Containerizing

In this article, we become acquainted with the theoretical aspects of containerization and how to choose the proper cloud vendor. So we are ready to practice, and the following article will be practiced. Let me know in the below comments what kind of practice cases you would like to observe on ACK.



By [Dr. Farruh](https://medium.com/@k-farruh) on [March 29, 2023](https://medium.com/p/1e83e0da72b9).

[Canonical link](https://medium.com/@k-farruh/easy-mlops-with-ack-alibaba-cloud-part-1-1e83e0da72b9)

Exported from [Medium](https://medium.com) on May 25, 2024.

