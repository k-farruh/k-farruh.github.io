---
title: 'Mlops Compare Part 2'
date: draft_Easy
permalink: /posts/draft_E/Easy-MLOps/
tags:
  - cool posts
  - category1
  - category2
---

Easy MLOps: Compare— Part 2
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
 

Easy MLOps: Compare— Part 2
===========================




MLOps uses proven DevOps techniques to automate the creation, deployment, and monitoring of ML pipelines in a production environment. As…




---

### Easy MLOps: Compare— Part 2

MLOps uses proven DevOps techniques to automate the creation, deployment, and monitoring of ML pipelines in a production environment. As the development of MLOps-tools for working with it becomes more — both proprietary and Open Source. From this variety, it is often difficult to choose a stack for your project.

My name is Alexander Volynsky, I am the technical manager of the Cloud ML Platform at VK Cloud. In this article, I will compare Open Source and proprietary approaches to working with MLOps and explain which tools and why we have chosen for the Cloud ML Platform.

A little about MLOps

According to statistics, up to 87% of ML models do not reach production. This is due to the fact that it is difficult to manage the infrastructure for ML and organize work with data at different stages of the life cycle in large projects. Yes, and the transition from experimentation to output to production and building a service creates difficulties: it is one thing to conduct experiments in Jupyter Notebook, and another thing is to pack everything into a Docker image, raise it to Kubernetes, organize monitoring and logging. MLOps helps keep it all in order.

MLOps is a modern approach to working with ML models and managing machine learning projects. He helps:

increase the speed of model deployment;  
improve team productivity;  
reduce risks and costs;  
perform tracking of experiments, feature hyperparameters in the process of model training;  
ensure continuous monitoring and logging of the already deployed model.

MLOps solves these problems using various tools and processes.

What to build MLOps on: proprietary tools vs Open Source

For MLOps, both proprietary and open-source tools can be used. Proprietary software is often chosen to get vendor support, stable updates, and in some cases the ability to influence the roadmap. At the same time, Open-Source tools can be more flexibly adapted to your project, and also easier to master: as a rule, a whole community is built around such solutions, which shares materials, answers questions, and helps solve emerging problems.

There are advantages and disadvantages to each of the approaches. In this article, we will compare the options in several ways.

Code quality

Vendor solutions are often perceived as more reliable and optimized. But even in paid tools there can be bugs and “crutches”, due to which the solution does not work correctly in one scenario or another. At the same time, the user does not have access to the code, cannot fix the error — you have to wait for the bugs to be fixed with updates from the vendor.

In Open Source, the source code of the tools is open and available to everyone. The community reviews the code and fixes bugs to make the tool better. True, this applies only to common software — in a small project it may be different due to a small audience.

Applicability and versatility

In proprietary solutions, the concept of “plug and play” often prevails — with settings out of the box. Each developer strives to introduce new developments and practices into their solutions that can make it better than its competitors. It is convenient and practical. However, if the vendor leaves the market and support is terminated, the expertise in one tool that has been accumulated over the years may turn out to be useless.

Software based on Open Source is often built taking into account generally accepted practices and approaches. Therefore, many Open-Source solutions implement similar functions and capabilities — this simplifies the development of new tools. Moreover, for various reasons, companies and teams more often use Open-Source tools — that is, expertise in such solutions ensures the versatility of the skill and simplifies the search for specialists in the team and their onboarding. True, no one usually expects work “out of the box” for Open Source — the tool will have to be configured.

Modularity

Proprietary software developers often rely on complex multifunctional solutions that can cover most or all of the user’s needs at once. This is practical, but each of the components can independently fail, which will affect the operation of the entire software. Moreover, the monolithic architecture of such solutions makes it difficult to customize them for specific use cases and connect to existing platforms.

Open source software is usually more customizable and more focused on integrating with other platforms. Open-source tools for MLOps are like a constructor: any part can be replaced, added or removed to get a solution specifically for your tasks. True, such adaptation will have to be dealt with separately, which requires certain skills from engineers.

Version stability

One of the advantages of vendor products is regular updates and licensed support. But along with the advantages, it also has several disadvantages. Firstly, vendors may release updates less often, while in Open Source they roll out more often. Secondly, there is no way to roll back to a stable version if suddenly the update does not suit you for some reason: the vendor strives tounification and support two versions of the same product is unlikely to want.

In Open Source, updates must be rolled out to production on their own. This increases the burden on developers working with such solutions. Version stability may vary from product to product. However, bugs are usually quickly fixed. In general, popular Open Source releases tend to come out much more frequently, allowing for quick bug fixes and new functionality.

Let’s summarize

Proprietary solutions are best chosen when:

the team has no experience with Open Source and no expertise in customizing tools;  
the project is large and complex, vendor support is needed;  
there is a budget for a licensed solution for working with data.

MLOps tools based on Open Source are more suitable if:

I want to be among the first to have access to new features, which often appear faster in Open Source;  
you need a solution that can be fully adapted to your tasks and supplemented with the necessary modules;  
a universal solution is required, from which it is easy to switch to an analogue;  
community support is important — even if the Open-Source tool becomes completely unavailable, the community will jointly decide where and how to switch from it;  
the project is small or short-term, it is unprofitable to buy proprietary software;  
it is important to reduce the risks of Vendor Lock-in in case it leaves the market.

Overview of Open-Source Tools for MLOps

A typical task stack in working with ML models comes down to several stages:

collection, preparation, labeling of data;  
model training;  
assessment of the quality of the model;  
bringing the model to production;  
monitoring.

Comprehensive open source solutions allow you to solve these problems. Let me briefly talk about the five main tools.



[View original.](https://medium.com/p/71619c2e6488)

Exported from [Medium](https://medium.com) on May 25, 2024.

