---
title: 'Next Level Conversations Llm Vectordb With Alibaba Cloud Customizable And Cost Efficient'
date: 2023-06-09
permalink: /posts/2023-06/Next-Level/
tags:
  - cool posts
  - category1
  - category2
---

Next-Level Conversations: LLM+VectorDB with Alibaba Cloud, Customizable and Cost-Efficient
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
 

Next-Level Conversations: LLM+VectorDB with Alibaba Cloud, Customizable and Cost-Efficient
==========================================================================================




We recommend using ECS for the backend and front end. If the user will use open-source, the LLM (Large Language Model) can be used GPU-ECS…




---

### Next-Level Conversations: LLM+VectorDB with Alibaba Cloud, Customizable and Cost-Efficient

We recommend using ECS for the backend and front end. If the user will use open-source, the LLM (Large Language Model) can be used GPU-ECS or Platform for AI (Artificial Intelligence). This tutorial will not cover the LLM part; we assume the user has LLM and its API key. The data will be saved in Analytic DB PostgreSQL (ADBPG), below high-level architecture.

![](https://cdn-images-1.medium.com/max/800/1*6UFdUjIdW9qTgfwMYZoYEA.png)### 1. Prepare AnalyticDB PostgreSQL Environment

1. [Login](https://www.alibabacloud.com/knowledge/developer/login-methods-for-alibaba-cloud-server) to Alibaba Cloud Console, then [create](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/create-an-instance) an instance of AnalyticDB for PostgreSQL.
2. For test purposes, could be chosen:
* Compute Node Specifications: 8 Cores, 32 GB Memory;
* Compute Nodes: 2;
* Compute Node Storage Capacity: 50 GB
* Configuration Information Summary: 16 Cores, 64 GB Memory, 100 GB ESSD PL1 Total Physical Storage (Single-copy)

3. [Create](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/create-a-privileged-account) an account to connect DB.

4. We need to create a vector table by following this tutorial: [Create a vector table and index](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/create).

5. We recommend using ECS, where they will be installed: UI [Configure an IP address whitelist](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/configure-an-ip-address-whitelist-1).

6. Prepare ECS

### 2. ECS Instance

1. Assume the user has already login to Alibaba Cloud Console by following section 1.1

2. [Create an ECS instance](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/create-and-manage-an-ecs-instance-by-using-the-ecs-console). For testing purposes, we recommend using ecs.g7.2xlarge with the parameters:

* Hardware: 8vCPU(s) 32 GiB;
* Operating System: Ubuntu 22.04 64-bit.
* [Connect](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/connect-to-a-linux-instance-by-using-an-ssh-key-pair) to the ECS through SSH;

### 2.1. Environment and Dependencies

### 2.1.1. Steps to Create a Virtual Environment on Python

1. Open the command prompt or terminal and navigate to the directory where the virtual environment needs to be created.

2. Install the virtualenv package by typing the following command: pip install virtualenv.

3. Once the installation is complete, create a new virtual environment by running the following command:virtualenv env\_name. Recommended replacing env\_name with the user-created one.

4. Activate the virtual environment by typing the following command: source env\_name/bin/activate.

5. The name of the virtual environment will be displayed in the command prompt or terminal.

6. It can be installed in the environment of any packages or libraries via pip.

7. To exit the virtual environment, type the following command: deactivate.

### 2.1.2. Install psycopg2 Dependencies

1. Make sure it has installed the required dependencies for building *psycopg2*. These dependencies on Ubuntu can be installed using the following command: sudo apt-get install libpq-dev python3-dev.

2. If the user is using a different operating system, consult the *psycopg2* [documentation](https://pypi.org/project/psycopg2/) for information on the required dependencies.

3. Install psycopg2 again using pip: pip install psycopg2-binary.

### 2.2. Install Retrieval Plugin: chatgpt-retrieval-plugin

### 2.2.1. Setup

This app uses Python 3.10 and [Poetry](https://python-poetry.org/) for dependency management.

Install Python 3.10 onto the machine if it still needs to be installed. Depending on the system, the Poetry can be downloaded from the official [Python website](https://www.python.org/downloads/) or with a package manager like Brew or apt. Activate the virtual environment prepared in section 2.2.2.

1. Clone the repository from GitHub:


```
git clone https://github.com/openai/chatgpt-retrieval-plugin.git
```
2. Navigate to the cloned repository directory:


```
cd /path/to/chatgpt-retrieval-plugin
```
3. Install poetry:


```
pip install poetry
```
4. Create a new virtual environment that uses Python 3.10:


```
poetry env use python3.10  
poetry shell
```
5. Install app dependencies using poetry:


```
poetry install
```
**Note:** If adding dependencies to the project. Tool, make sure to run poetry lock and poetry install.

#### 2.2.1.1. General Environment Variables

The API requires the following environment variables to work:

![](https://cdn-images-1.medium.com/max/800/1*elZUuTK_blVdGBz8tyaDnw.png)### 2.3. Running the API Locally

To run the API locally, first required to set the requisite environment variables with the export command:


```
export DATASTORE=<datastore>  
export BEARER\_TOKEN=<bearer\_token>  
export LLM\_API\_KEY=<llm\_api\_key>  
export PG\_HOST=<dbhost>  
export PG\_PORT=5432  
export PG\_DATABASE=<db>  
export PG\_USER=<dbuser>  
export PG\_PASSWORD=<dbuser-password>
```
Or above variables could be written in a global environment via the following instructions:

1. Open the terminal.

2. Type nano *~/.bashrc* to open the bashrc file in the nano text editor.

3. Scroll down to the end of the file or the section where variables must be added.

4. Add variables in the following format: export *VARIABLE\_NAME=value*. Replace *VARIABLE\_NAME* with the name of the variable and value with the value which wanted to assign to it.

5. Save the file by pressing Ctrl + X, Y, and Enter.

6. Finally, to apply the changes, open a new terminal or type source *~/.bashrc* in the terminal to reload the bash file.

Start the API with:


```
poetry run start
```
Append docs to the URL in the terminal and open it in a browser to access the API documentation and try out the endpoints (i.e., [*http://0.0.0.0:8000/docs*](http://0.0.0.0:8000/docs)). Make sure to enter the correct bearer token and test the API endpoints.

**Note:** If added new dependencies to the *project.toml* file, to run poetry lock and poetry install to update the lock file and install the new dependencies.

### 2.4. Upload Data to ADBPG

Within the scripts folder exist scripts built for upserting or processing text documents from various data sources, including JSON files, JSONL files, and zip files. These scripts utilize the plugin’s upsert utility functions, which convert the documents into plain text and divide them into chunks before uploading them to the vector database along with their metadata. Each script folder comes with a README file that outlines how to use the script and the parameters it requires. It is also possible to use the services.pii\_detection module to screen the documents for personally identifiable information (PII) and exclude any documents that contain it to avoid unintentionally uploading sensitive or private data to the vector database.

Furthermore, it can be used the *services.extract\_metadata* module to extract metadata from the document text, which can then be used to enrich the document metadata. It is worth noting that if the user uses incoming webhooks to synchronize data continuously, the user should run a backfill after setting them up to ensure that no data is missed.

The following scripts are available:

* Process\_json: This script processes a file dump of documents in JSON format and stores them in the vector database with metadata. The JSON file format must be a list of JSON objects, where each object represents a document. The JSON object should have a text field and other fields to populate the metadata.
* Process\_jsonl: This script processes a file dump of documents in JSONL format and stores them in the vector database with metadata. The format of the JSONL file should be a newline-delimited JSON file, where each line represents a valid JSON object representing a document. The JSON object should have a text field and other fields to populate the metadata.
* Process\_zip: This script processes a file dump of documents in a zip file and stores them in the vector database with metadata. The zip file format should contain a flat-file folder containing docx, pdf, txt, md, ppt, or CSV files.

All three types of scripts support the custom metadata as a JSON string and enable flags to screen for PII and extract metadata.


```
# Upload prepared zipped \*.md file to the /llm-retrieval-plugin/scripts/process\_zip  
   
 source env\_name/bin/activate  
 poetry shell  
 python scripts/process\_zip/process\_zip.py — filepath srcripts/process\_zip/<upload\_file\_name.zip>
```
### 3.3.1. Verify Uploaded Data

1. Open the terminal or command prompt and type psql -h host -p <server port: default 5432> -U username -d database\_name to connect to the PostgreSQL database. Replace the host with the host server address, username with the PostgreSQL username, and database\_name with the database name that the user wants to connect to.

2. Once established connection. It can count the values on a specific table by typing SELECT COUNT(\*) FROM document\_chunks;

3. To show only one column in the table, it can be used the SELECT statement followed by the name of the column which needed to be shown the SELECT statement can be used. For example, SELECT content FROM document\_chunks;

4. If needed to truncate the table values (i.e., delete all the rows), it can be used the TRUNCATE TABLE document\_chunks; command. This will delete all the rows in the table, so use it with caution.

### 3. Simple WebUI for Test

We offer a simple WebUI, which have done with a flask. This WebUI is only for reference and **can’t be** put in a production environment.

To run a ready website Flask application with Python, follow these steps:

1. Clone or download the website Flask application from its [source code repository](https://github.com/k-farruh/webui-llm)**.**
2. It requires Python and Flask installed on the system. They can be downloaded and installed from their official websites.
3. Open the terminal and navigate to the directory that contains the Flask application.
4. Install any dependencies required by the Flask application by running the following command: *pip install -r requirements.txt*
5. Set the environment variables required by the Flask application. The variables and their values should be listed in a file called .env. Refer to section: 2.2.1.
6. Start the Flask application by running the following command: python app.pyReplace app.py with the name of the Python file that contains the Flask application.
7. Open the web browser and go to <http://localhost:5000/> or the URL specified by the Flask application to see the website in action after it should open a similar page shown below.

Congratulations! Now successfully running LLM+ADBPG with own data in Alibaba Cloud.

We believe that ADBPG in the Generative AI era has the potential to revolutionize the way businesses and organizations analyze and use data. If you’re interested in learning more about our software solution and how it can benefit your organization, please don’t hesitate to [contact us](https://www.alibabacloud.com/solutions/logistics/contact-us). We’re always happy to answer your questions and provide a demo of our software.



By [Dr. Farruh](https://medium.com/@k-farruh) on [June 9, 2023](https://medium.com/p/1936a6bf2629).

[Canonical link](https://medium.com/@k-farruh/next-level-conversations-llm-vectordb-with-alibaba-cloud-customizable-and-cost-efficient-1936a6bf2629)

Exported from [Medium](https://medium.com) on May 25, 2024.

