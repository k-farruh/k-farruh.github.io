---
title: 'Ontainer Registry As Part Of Mlop'
date: draft_The-
permalink: /posts/draft_T/The-Container/
tags:
  - cool posts
  - category1
  - category2
---

The Container Registry — As Part of MLOps
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
 

The Container Registry — As Part of MLOps
=========================================




Container Registry Enterprise Edition allows you to build images from source code. This is a secure, high concurrent, stable, and efficient…




---

### The Container Registry — As Part of MLOps

Container Registry Enterprise Edition allows you to build images from source code. This is a secure, high concurrent, stable, and efficient continuous integration (CI) process. Container Registry Enterprise Edition automates the building and delivery of images from source code repositories to Container Registry repositories based on Dockerfiles. When the source code is updated, Container Registry Enterprise Edition automatically builds an image by using a Dockerfile and uploads the image to a Container Registry repository. This topic describes how to build images by using Container Registry Enterprise Edition instances.

### Prerequisites

### 

* An instance of Container Registry Enterprise Edition is created. For more information, see [Use a Container Registry Enterprise Edition instance to push and pull images](https://www.alibabacloud.com/help/en/container-registry/latest/use-a-container-registry-enterprise-edition-instance-to-push-and-pull-images#section-ngl-swv-bde).
* A Dockerfile is created.

### Background information

### 

The image building service of Container Registry features security, stability, and high efficiency:

* Security: During image building, the system distributes each image building task to a new, exclusive, and isolated environment. This ensures the security of code and image assets.
* Stability: If you use a source code repository to build multiple images, the time used for each image building task is stable because each image building task is run on an exclusive environment.
* Intelligent acceleration:
* By default, the system uses the efficient building tool BuildKit. BuildKit has robust building capabilities, especially for multi-stage building scenarios, and supports rich building features.
* The system hosts common base images. During image building, the system can use the base images without the need to pull images. The base images help reduce the building time.
* The system can use remote caches to accelerate image building.
* 

The image building service of Container Registry supports features such as multiple code hosting platforms and accelerated image generation.

* Code hosting platforms: The following table lists the supported code hosting platforms.Code hosting platformEditionAuthentication method for bindingLimit on triggering image buildingGiteeAllOAuth authenticationNoneGitHubGitHub developer versionOAuth authenticationNoneGitLabAllPersonal access tokenNone
* Accelerated image generation: The system allows you to load resources of a container image on demand. The accelerated version of the container image is automatically generated after the container image is pushed. For more information, see [Load resources of a container image on demand](https://www.alibabacloud.com/help/en/container-registry/latest/load-resources-of-a-container-image-on-demand#task-1955391).

### Step 1: Bind your instance to a source code hosting platform

### 

Before you build images, you must bind your instance to a source code hosting platform. For more information, see [Bind a source code hosting platform](https://www.alibabacloud.com/help/en/container-registry/latest/image-build-bind-a-source-code-hosting-platform#task-2038492).

**Important**

* You cannot build images from an on-premises image repository.
* For information about how to access private GitLab code repository in a VPC, see [Build a container image in VPC mode](https://www.alibabacloud.com/help/en/container-registry/latest/anquangoujianmoshi#task-2224804).

### Step 2: Create a namespace

### 

1. Log on to the [Container Registry console](https://cr.console.aliyun.com/).
2. In the top navigation bar, select a region.
3. In the left-side navigation pane, click **Instances**.
4. On the **Instances** page, click the Container Registry Enterprise Edition instance for which you want to create a namespace.
5. In the left-side navigation pane of the management page of the Container Registry Enterprise Edition instance, choose **Repository > Namespace**.
6. On the **Namespace** page, click **Create Namespace**.
7. In the **Create Namespace** dialog box, set the **Namespace**, **Automatically Create Repository**, and **Default Repository Type** parameters. Click **Confirm**.

### Step 3: Create an image repository

### 

Create an image repository and bind it to a code repository. All images that are generated from the code repository are pushed to the image repository.

1. Log on to the [Container Registry console](https://cr.console.aliyun.com/).
2. In the top navigation bar, select a region.
3. In the left-side navigation pane, click **Instances**.
4. On the **Instances** page, click the Enterprise Edition instance that you want to manage.
5. On the management page of the Container Registry Enterprise Edition instance, choose **Repository > Repositories** in the left-side navigation pane.
6. On the **Repositories** page, click **Create Repository**.
7. In the **Repository Info** step, set the **Namespace**, **Repository Name**, **Repository Type**, **Tags**, **Accelerated Image**, **Summary**, and **Description** parameters, and click **Next**.
8. In the **Code Source** step, set the **Code Source**, **Build Settings**, and **Build Rules** parameters, and then click **Create Repositories**.
9. ParameterDescriptionCode sourceThe code source.Build Settings
* Automatically Build Images When Code Changes: An image is automatically built when code is committed from a branch.
* Build With Servers Deployed Outside Chinese Mainland: Images are built on servers outside the Chinese mainland and then pushed to a repository in the specified region. If the Dockerfile used in your project must be downloaded from a site outside the Chinese mainland but the cross-border network connection is unstable, you can enable **Build With Servers Deployed Outside Chinese Mainland**.
* Build Without Cache: The system pulls the base image from the source code repository each time an image is built. This may increase the building time. You can disable **Build Without Cache** to accelerate the image building.
1. 
2. On the **Repositories** page, click the created image repository. If you can view **Build** in the left-side navigation pane of the repository management page, the image repository is bound to the source code repository.
3. 

### Step 4: Build an image

### 

**Note** If you cannot find **Build** on the repository management page, the code source hosting platform fails to be bound to the image repository. You can refer to [Step 1](https://www.alibabacloud.com/#section-m5z-ykv-ye6) to rebind the source code hosting platform.

1. Log on to the [Container Registry console](https://cr.console.aliyun.com/).
2. In the top navigation bar, select a region.
3. In the left-side navigation pane, click **Instances**.
4. On the **Instances** page, click the Enterprise Edition instance that you want to manage.
5. In the left-side navigation pane of the management page of the Container Registry Enterprise Edition instance, choose **Repository > Repositories**.
6. On the **Repositories** page, find the created image repository and click **Manage** in the **Actions** column.
7. In the left-side navigation pane, click **Build**. In the **Build Rules** section, click **Add Build Rule**. In the **Build Information** step of the Add Build Rule wizard, set the following parameters and click **Next**.
8. ParameterDescription**Type**The type of the source code repository. Valid values: Branch and Tag.**Branch/Tag**Select or enter a branch or a tag. Regular expressions are supported. If you specify the release-(?<imageTag>\w\*) regular expression, the system automatically builds an image of V1 when the source code in the release-v1 branch is updated. The image cannot be built immediately. For more information about how to specify regular expressions, see [Use regular expressions in named capturing groups](https://developer.aliyun.com/article/683079).
9. **Note** After you specify regular expressions, images can be built only by the system. You cannot manually build images.
10. 
11. **Dockerfile Directory**The directory of the Dockerfile. This is a subdirectory of the branch or tag directory. For example, if the branch directory is master and the Dockerfile is in the master directory, the value is master/Dockerfile**Dockerfile Filename**The name of the Dockerfile. The default name is Dockerfile.
12. 
13. In the **Tag** step, configure the following parameters, click **Save**, and then click **Next**.
14. **Note** Click **Add Configuration** to add an image tag. You can specify up to three image tags.
15. 
16. ParameterDescription**Image Tag**The tag of the image. Example: latest. You can enable named capturing groups. For example, if you specify a named capturing group for **Branch/Tag**, you can use the captured content.**Build Time**The time when source code is pushed. The time is in UTC+8 format. Example: 20201015 or 202010151613.
17. **Note** This parameter is optional. If you set this parameter, images can be built only by the system. You cannot manually build images.
18. 
19. **Commit ID**The number of characters to be obtained from the commit ID of the most recently pushed code. By default, the first six characters are used. You can adjust the slider to change the number of characters.
20. **Note** This parameter is optional. If you set this parameter, images can be built only by the system. You cannot manually build images.
21. 
22. 
23. 
24. In the **Build Configurations** step, set the following parameters and click **Confirm**.
25. ParameterDescription**Build Architecture**The architecture for which you want to build images. You can select multiple architectures. If you select multiple architectures, multiple container images for the architectures are built for each image tag.**Build Parameters**The runtime parameters of the image building. Each building parameter is a case-sensitive key-value pair. You can set a maximum of 20 building parameters. You can set a building parameter to modify the environment variables in a Dockerfile to make the same Dockerfile show different status.
26. 
27. Trigger the image building rule.
28. You can use one of the following methods to trigger an image building rule:
* In the **Build Rules** section of the **Build** page, find the image building rule and click **Build** in the **Actions** column.
* Submit code to the master branch of the source code repository to trigger the building rule.
1. **Note**
* In the **Build Log** section of the **Build** page, find the triggered image building task and click **Cancel** in the **Actions** column to cancel the image building task.
* In the **Build Log** section of the **Build** page, find the triggered image building task and click **Log** in the **Actions** column to view the image building log.
1. 
2. 
3. 
4. In the left-side navigation pane, click **Image Tag**. If the image that you created is displayed, the image is built.
5. 

### Example 1: Build an image based on the branch that is named main (you can manually build images)

### 

Configure the building rule based on the following settings:

* **Type**: Branch
* **Branch/Tag**: main
* **Dockerfile Directory**: /
* **Dockerfile Filename**: Dockerfile
* **Image Tag**: latest

When you click Build or the source code in the main branch is updated, the system builds an image. The file named Dockerfile in the / directory of the main branch is used to build the image. The tag of the created image is latest. The following figure shows the configuration of the building rule.

![](https://cdn-images-1.medium.com/max/800/0*z77-QdiP2vzKhVKe.png)### Example 2: Build an image based on the branch that matches a regular expression (you cannot manually build images)

### 

Configure the building rule based on the following settings:

* **Type**: Branch
* **Branch/Tag**: release-(?<imageTag>\w\*)
* **Dockerfile Directory**: /
* **Dockerfile Filename**: Dockerfile
* **Image Tag**: ${imageTag}
* **Build Time**: yyyyMMddHHmm
* **Commit ID**: 30

When the source code is updated in the branch whose name starts with `release-`, the system automatically builds an image. The file named **Dockerfile** in the / directory of the branch is used to build the image.

For example, if the source code in the branch named `release-v1` is updated, the regular rule `release-(?<imageTag>\w*)` captures the `v1` in the branch name, sends the v1 to the variable `imageTag`, and uses v1 in the image tag. In this example, the tag of the created image is `v1-202010151625-d4ef3dc3b77a011a5779eec7efdd45`. The following figure shows the configuration of the building rule.

![](https://cdn-images-1.medium.com/max/800/0*M4tqxqUN9qBQzLjv.png)### What to do next

### 

You can perform the following operations after the image is built:

* You can pull the image from Container Service for Kubernetes (ACK) clusters without using secrets. For more information, see [Use the aliyun-acr-credential-helper component to pull images without a password](https://www.alibabacloud.com/help/en/container-registry/latest/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-a-password#task-2456294).
* You can use the image to create applications in ACK clusters. For more information, see [Create a stateless application by using a Deployment](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/create-a-stateless-application-by-using-a-deployment#task-p2s-2rl-vdb).
* You can use the P2P acceleration feature in ACK clusters to improve the image pulling speed. For more information, see [Use the P2P acceleration feature in ASK and ACK clusters](https://www.alibabacloud.com/help/en/container-registry/latest/use-the-p2p-acceleration-feature-in-ask-and-ack-clusters#task-2058972).

### Use images of Container Registry to deploy applications in other cloud services

### 

Updated at: 2022–05–19 14:51

You can use images of Container Registry to deploy applications in Container Service for Kubernetes (ACK), Enterprise Distributed Application Service (EDAS), Serverless App Engine (SAE), and Function Compute. This topic describes how to use images of Container Registry to deploy applications in ACK, EDAS, SAE, and Function Compute.

### Use Container Registry to deploy applications in ACK

### 

1. An instance of Container Registry Enterprise Edition is created. For more information, see [Create a Container Registry Enterprise Edition instance](https://www.alibabacloud.com/help/en/container-registry/latest/create-a-container-registry-enterprise-edition-instance#task488 "Container Registry Enterprise Edition allows enterprises to manage and distribute Open Container Initiative (OCI) artifacts such as container images, Helm charts, and Operators in a secure and efficient way. Container Registry Enterprise Edition can distribute large-scale application artifacts in the production environment and distribute application artifacts across global regions. Container Registry Enterprise Edition also allows enterprises to efficiently build DevSecOps environments. Before you use Container Registry Enterprise Edition, you must create a Container Registry Enterprise Edition instance to manage and distribute your cloud-native assets.").
2. Use the instance that you created to build an image. Alternatively, push an image to the instance. For more information, see [Use Container Registry Enterprise Edition to build images](https://www.alibabacloud.com/help/en/container-registry/latest/quick-start-use-container-registry-enterprise-edition-instances-to-build-images#task-2035247 "Container Registry allows you to build images from source code with the following features: continuous integration, security, high concurrency, stability, and high efficiency. This topic describes how to build images by using Container Registry Enterprise Edition.") and [Use a Container Registry Enterprise Edition instance to push and pull images](https://www.alibabacloud.com/help/en/container-registry/latest/use-a-container-registry-enterprise-edition-instance-to-push-and-pull-images#task-2023726).
3. Enable ACK to pull the image without a password. For more information, see [Use the aliyun-acr-credential-helper component to pull images without a password](https://www.alibabacloud.com/help/en/container-registry/latest/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-a-password#task-2456294 "Container Registry provides the aliyun-acr-credential-helper component for you to pull private images without a password from Container Registry Enterprise Edition or Personal Edition. This component is automatically installed in Container Service for Kubernetes (ACK) clusters. This topic describes how to use the aliyun-acr-credential-helper component to pull a private image without a password in different scenarios.").
4. Use the image to deploy an application in ACK. For more information, see [Create a stateless application by using a Deployment](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/create-a-stateless-application-by-using-a-deployment#task-p2s-2rl-vdb "You can deploy a stateless application by using a Deployment. A Deployment can be created by using an image, an orchestration template, or kubectl commands. Container Service for Kubernetes (ACK) allows you to use Secrets to pull images by using a web interface. This topic describes how to create a stateless NGINX application by using an image, an orchestration template, and kubectl commands.").

### Use Container Registry to deploy applications in EDAS

### 

1. An instance of Container Registry Enterprise Edition is created. For more information, see [Create a Container Registry Enterprise Edition instance](https://www.alibabacloud.com/help/en/container-registry/latest/create-a-container-registry-enterprise-edition-instance#task488 "Container Registry Enterprise Edition allows enterprises to manage and distribute Open Container Initiative (OCI) artifacts such as container images, Helm charts, and Operators in a secure and efficient way. Container Registry Enterprise Edition can distribute large-scale application artifacts in the production environment and distribute application artifacts across global regions. Container Registry Enterprise Edition also allows enterprises to efficiently build DevSecOps environments. Before you use Container Registry Enterprise Edition, you must create a Container Registry Enterprise Edition instance to manage and distribute your cloud-native assets.").
2. Use the instance that you created to build an image. Alternatively, push an image to the instance. For more information, see [Use Container Registry Enterprise Edition to build images](https://www.alibabacloud.com/help/en/container-registry/latest/quick-start-use-container-registry-enterprise-edition-instances-to-build-images#task-2035247 "Container Registry allows you to build images from source code with the following features: continuous integration, security, high concurrency, stability, and high efficiency. This topic describes how to build images by using Container Registry Enterprise Edition.") and [Use a Container Registry Enterprise Edition instance to push and pull images](https://www.alibabacloud.com/help/en/container-registry/latest/use-a-container-registry-enterprise-edition-instance-to-push-and-pull-images#task-2023726 "Container Registry Enterprise Edition is an enterprise-class platform designed to manage the lifecycle of cloud-native application artifacts, including container images, Helm charts, and Open Container Initiative (OCI) artifacts. You can manage images in a Container Registry Enterprise Edition instance to facilitate application creation by using images. This topic describes how to use a Container Registry Enterprise Edition instance to push and pull images.").
3. Use the image to deploy an application in EDAS. For more information, see [Use an image to deploy an application in a](https://www.alibabacloud.com/help/en/enterprise-distributed-application-service/latest/use-an-image-to-deploy-an-application-in-an-ack-cluster#task-tu6-g7m-khn "Enterprise Distributed Application Service (EDAS) fully integrates with on the basis of cloud-native Kubernetes. EDAS supports the full lifecycle management of Kubernetes containerized applications. A is embedded with the capabilities of Alibaba Cloud in virtual machines, storage, networking, and security, and provides an excellent runtime environment for Kubernetes containerized applications. This topic describes how to use an image to deploy an application in a .").

### Use Container Registry to deploy applications in Function Compute

### 

1. An instance of Container Registry Enterprise Edition is created. For more information, see [Create a Container Registry Enterprise Edition instance](https://www.alibabacloud.com/help/en/container-registry/latest/create-a-container-registry-enterprise-edition-instance#task488 "Container Registry Enterprise Edition allows enterprises to manage and distribute Open Container Initiative (OCI) artifacts such as container images, Helm charts, and Operators in a secure and efficient way. Container Registry Enterprise Edition can distribute large-scale application artifacts in the production environment and distribute application artifacts across global regions. Container Registry Enterprise Edition also allows enterprises to efficiently build DevSecOps environments. Before you use Container Registry Enterprise Edition, you must create a Container Registry Enterprise Edition instance to manage and distribute your cloud-native assets.").
2. Use the instance that you created to build an image. Alternatively, push an image to the instance. For more information, see [Use Container Registry Enterprise Edition to build images](https://www.alibabacloud.com/help/en/container-registry/latest/quick-start-use-container-registry-enterprise-edition-instances-to-build-images#task-2035247 "Container Registry allows you to build images from source code with the following features: continuous integration, security, high concurrency, stability, and high efficiency. This topic describes how to build images by using Container Registry Enterprise Edition.") and [Use a Container Registry Enterprise Edition instance to push and pull images](https://www.alibabacloud.com/help/en/container-registry/latest/use-a-container-registry-enterprise-edition-instance-to-push-and-pull-images#task-2023726 "Container Registry Enterprise Edition is an enterprise-class platform designed to manage the lifecycle of cloud-native application artifacts, including container images, Helm charts, and Open Container Initiative (OCI) artifacts. You can manage images in a Container Registry Enterprise Edition instance to facilitate application creation by using images. This topic describes how to use a Container Registry Enterprise Edition instance to push and pull images.").
3. Use the image to deploy an application in Function Compute. For more information, see [Create a function](https://www.alibabacloud.com/help/en/function-compute/latest/create-a-function#task-2559807 "This topic describes how to create a custom container function in the Function Compute console or by using Funcraft.").

  


  




[View original.](https://medium.com/p/1430f832f26)

Exported from [Medium](https://medium.com) on May 25, 2024.

