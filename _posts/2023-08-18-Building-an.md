---
title: 'Building An Exciting Journey For Your Genai Application With Llama 2 Analyticdb Pai Eas And '
date: 2023-08-18
permalink: /posts/2023-08/Building-an/
tags:
  - cool posts
  - category1
  - category2
---
# Building an Exciting Journey for Your GenAI Application with Llama 2, AnalyticDB, PAI-EAS, and…
Explore the integration of AnalyticDB for PostgreSQL with large language models on Alibaba Cloud’s PAI platform, empowering businesses…

### Building an Exciting Journey for Your GenAI Application with Llama 2, AnalyticDB, PAI-EAS, and Alibaba Cloud

[AnalyticDB for PostgreSQL](https://www.alibabacloud.com/product/hybriddb-postgresql), offered by Alibaba Cloud, is an exceptional solution that combines the speed and efficiency of the fastest vector database with the power of PostgreSQL. This technology empowers developers to process, store, and analyze massive volumes of structured and unstructured data at unprecedented speeds.

![](https://cdn-images-1.medium.com/max/800/1*KCDRf4iaP5Q6ru-Ilx1Hkg.jpeg)With AnalyticDB for PostgreSQL, you can supercharge your GenAI applications on [Alibaba Cloud PAI](https://www.alibabacloud.com/product/machine-learning). Whether you are working on recommendation systems, natural language processing, or image recognition, this solution provides the performance boost you need to take your applications to the next level.

In this tutorial, we will guide you through the process of harnessing AnalyticDB for PostgreSQL’s amazing capabilities in combination with Alibaba Cloud PAI. You will learn how to seamlessly integrate language models, query vector data, and leverage the advanced features of AnalyticDB for PostgreSQL.

Join us on this exciting journey and unlock the full potential of your GenAI applications with AnalyticDB for PostgreSQL and Alibaba Cloud PAI.

Note: Before proceeding with the steps mentioned below, ensure that you have an Alibaba Cloud account and have access to the Alibaba Cloud Console.

### 1. Prepare AnalyticDB for the PostgreSQL Environment

1. [Logon](https://www.alibabacloud.com/knowledge/developer/login-methods-for-alibaba-cloud-server) to Alibaba Cloud Console and [create an instance](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/create-an-instance) of AnalyticDB for PostgreSQL.

2. We chose the following for test purposes:

* Compute Node Specifications: 4 Cores, 16 GB Memory
* Compute Nodes: 2
* Compute Node Storage Capacity: 50 GB
* Configuration Information Summary: 16 Cores, 64 GB Memory, 100 GB ESSD PL1 Total Physical Storage (Single-Copy)

3. [Create](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/create-a-privileged-account) an account to connect to DB

4. We must enable “Vector Engine Optimization” to use the vector database.

![](https://cdn-images-1.medium.com/max/800/0*9huUzYth1GHXtZRe.png)5. We recommend using ECS, where they will be installed: [UI Configure an IP address whitelist](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/configure-an-ip-address-whitelist-1), which will be created in the next section. If ECS and AnalyticDB are in on VPC (Virtual Private Cloud), you can put the Primary Private IP Address. If not, then a public IP address requires to be put.

![](https://cdn-images-1.medium.com/max/800/0*y1-e8ExF7AILnUoK.png)Now it’s time to work on an ECS instance.

### 2. ECS Instance

1. Assume the user has already login to Alibaba Cloud Console (following section 1.1)

2. [Create an ECS instance](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/create-and-manage-an-ecs-instance-by-using-the-ecs-console). We recommend at least ecs.g7.2xlarge with the parameters for testing purposes:

* Hardware: 8vCPU(s) 32 GiB
* Operating System: Ubuntu 22.04 64-bit

![](https://cdn-images-1.medium.com/max/800/0*w367O6u3yEcn9FAk.png)* For Logon Credential, we recommend using “Key Pair.”

![](https://cdn-images-1.medium.com/max/800/0*ThmTqlwBY6p61Ld2.png)3. We need to add port 5000 to the security group by following this [documentation](https://www.alibabacloud.com/help/en/ecs/user-guide/add-a-security-group-rule):

![](https://cdn-images-1.medium.com/max/800/0*wtCx2UaaXrxtzVeh.png)### 2.1. Environment and Dependencies

### Connect with SSH and Install NVIDIA Driver

1. Once the ECS instance is created, navigate to the “Instances” section in the Alibaba Cloud Console.
2. Find the newly created instance and click on the “Connect” button.
3. Follow the instructions to download the private key (.pem) file.
4. Open a terminal on your local machine and navigate to the directory where the private key file is downloaded.
5. Run the following command to set the correct permissions for the private key file:


```
chmod 400 key\_pair.pem
```
6. Use the SSH command to connect to the ECS instance using the private key file:


```
ssh -i key\_pair.pem root@<ECS\_Instance\_Public\_IP>
```
### Install Docker.io

1. Run the following commands to install Docker.io on the ECS instance:


```
apt -y update  
apt -y install docker.io
```
2. Start the Docker service:


```
systemctl start docker
```
### Start the Docker Container

1. Run the following command to start the Docker container:


```
sudo docker run -t -d --network host --name llm\_demo hackathon-registry.ap-southeast-5.cr.aliyuncs.com/generative\_ai/langchain:llm\_langchain\_adbpg\_v02
```
It takes around 15–25 minutes to download, depending on network speed. This image will be available only during the Generative AI Hackathon event period. If you want to use this image, please, feel free to [contact us](https://www.alibabacloud.com/solutions/generative-ai/contact-us?spm=a2c65.11461447.0.0.29d540141XRsk0).

2. Enter the Docker container:


```
docker exec -it llm\_demo bash
```
### Configure config.json

1. Use a text editor to open the config.json file:


```
nano config.json
```
To fill the config file, please follow the instructions below:

2. Open a text editor or IDE of your choice.

3. Edit and save it with the name *config.json*.

4. Copy the following JSON structure into the file.  
The embedding part does not require change. Feel free to modify other embedding models if you want to use them.


```
{  

```
5. Replace the placeholder values with your specific configuration details as described below:

* *embedding.model\_dir:* Specify the directory path where the embedding model is stored. By default `/code/`
* *embedding.embedding\_model:* Provide the name of the embedding model file (e.g.,`SGPT-125M-weightedmean-nli-bitfit`).
* *embedding.embedding\_dimension:* Enter the dimension of the embedding model (e.g., 768).
* *EASCfg.url:* Add the URL of the llama2\_model API endpoint. Details on how to create PAI-EAS with Llama 2 model you can find [here](https://www.alibabacloud.com/blog/600229).
* *EASCfg.token:* Insert the access token for the chatglm2\_model API endpoint.
* *ADBCfg.PG\_HOST:* Enter the hostname of your AnalyticDB for PostgreSQL instance.
* *ADBCfg.PG\_USER:* Provide the username for accessing your AnalyticDB for PostgreSQL instance.
* *ADBCfg.PG\_PASSWORD:* Fill in the password for your AnalyticDB for PostgreSQL instance.
* *create\_docs.chunk\_size:* Specify the desired chunk size for indexing the knowledge base.
* *create\_docs.chunk\_overlap:* Set the chunk overlap value (if required).
* *create\_docs.docs\_dir:* Specify the directory path where your knowledge base files are located.
* *create\_docs.glob:* Define the file pattern for the knowledge base files.
* *query\_topk:* Set the number of relevant results to be returned by the query.
* *prompt\_template:* Customize the template for generating prompts while answering user questions.

6. Save the changes to the config.json file.

Ensure that you provide accurate and valid information in the configuration file to ensure the proper functioning of your application.

### 3. Run API Service on the Docker

1. You can start to run need run the Flask application by the below command:


```
nohup python3 app.py
```
![](https://cdn-images-1.medium.com/max/800/0*2E9tT-xkkiAhvDmo.png)If successful, you will get a similar response as shown above figure. Then the terminal can be closed.

2. Test the running API:


```
<your public IP address>:5000
```
Replace *<your public IP address>* with the actual IP address or hostname of your machine running the Docker container.

![](https://cdn-images-1.medium.com/max/800/0*41Oc-0ay-nJmKmDw.png)3. Make any necessary modifications to the index.html file or connect your application using the provided API endpoints:

* To upload a text document file: `<your public IP address>:5000/upload`
* To query or ask a question: `<your public IP address>:5000/query`

Ensure that you update the URLs in your application code or any other relevant places to use the correct API endpoints.

Here is an examples CURL to check services for query and upload:


```
curl -X POST -H "Authorization: Bearer <JWT\_TOKEN>" -F "file=@/path/to/file.txt" <your public IP address>:5000/upload  
  
curl -X POST -H "Authorization: Bearer <JWT\_TOKEN>" -H "Content-Type: application/json" -d '{"query": "Your query here"}' <your public IP address>:5000/upload
```
Congratulations! You have successfully completed the step-by-step tutorial for setting up and running the LLM demo on Alibaba Cloud using ECS, PAI-EAS, AnalyticDB for PostgreSQL, and the Llama 2 project.

### Conclusion

We have explored the capabilities of AnalyticDB for PostgreSQL in conjunction with large language models on Alibaba Cloud’s PAI platform. By leveraging the power of AnalyticDB for PostgreSQL, developers can efficiently store, process, and analyze massive amounts of data while seamlessly integrating large language models for advanced language processing tasks.

Combining AnalyticDB for PostgreSQL, large language models, and Alibaba Cloud’s PAI platform opens up many possibilities for businesses and developers. The high performance and scalability of AnalyticDB for PostgreSQL ensure efficient data handling while integrating large language models enabling sophisticated language processing capabilities.

This powerful solution allows businesses to extract valuable insights, improve natural language understanding, and develop innovative applications across various domains, such as recommendation systems, sentiment analysis, chatbots, and more. Alibaba Cloud’s PAI platform also provides a user-friendly environment for easily managing, deploying, and scaling these applications.

We invite you to explore the potential of AnalyticDB for PostgreSQL, large language models, and Alibaba Cloud’s PAI platform. Leverage the power of these cutting-edge technologies to enhance your language processing capabilities, gain valuable insights from data, and drive innovation in your business.

Unlock the full potential of AnalyticDB for PostgreSQL, large language models, and Alibaba Cloud’s PAI platform to revolutionize your language-driven applications and stay ahead in the digital landscape. [Contact Alibaba Cloud](https://www.alibabacloud.com/solutions/generative-ai/contact-us?spm=a2c65.11461447.0.0.29d540141XRsk0) to embark on an exciting journey and unleash the power of data and language processing.



By [Dr. Farruh](https://medium.com/@k-farruh) on [August 18, 2023](https://medium.com/p/c3c4b117ea0c).

[Canonical link](https://medium.com/@k-farruh/building-an-exciting-journey-for-your-genai-application-with-llama-2-analyticdb-pai-eas-and-c3c4b117ea0c)

Exported from [Medium](https://medium.com) on May 25, 2024.

