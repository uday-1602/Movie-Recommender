# 🎬 Serverless AI Movie Recommender (Cost-Optimized RAG System)

**Live Demo:** [Click here to try the AI](https://movie-recommender-woad.vercel.app/)

A full-stack, serverless web application that provides highly personalized, conversational movie recommendations using **Retrieval-Augmented Generation (RAG)**. 

### 🏗️ Architecture & Cost Optimization
This project was specifically architected to bypass the high idle costs of traditional managed vector databases (like Amazon OpenSearch). By decoupling the storage layer and migrating the vector index to **Pinecone Serverless**, the system maintains enterprise-grade retrieval speeds while operating entirely on free-tier and pay-per-request infrastructure. 

Additionally, the frontend utilizes a **Vercel Serverless Function proxy** to securely route requests, ensuring no AWS API Gateway endpoints or keys are ever exposed to the client browser.



## 🛠️ Tech Stack

**Frontend & Edge Proxy:**
* **Vanilla UI:** HTML5, CSS3, JavaScript (ES6+) with dynamic Markdown-to-HTML parsing.
* **Vercel:** Hosting the frontend and providing Serverless API Routes (Node.js) to securely proxy requests to AWS.

**Backend & Cloud Infrastructure (AWS & Pinecone):**
* **Amazon Bedrock (Knowledge Bases):** Orchestrates the RAG pipeline and text embeddings (Titan Text Embeddings).
* **Anthropic Claude 3.5 Sonnet:** The core LLM generating the conversational responses.
* **Pinecone (Serverless):** Third-party vector database storing the dimensional movie embeddings.
* **AWS Secrets Manager:** Securely stores and injects the Pinecone API key into Bedrock.
* **AWS Lambda:** Serverless compute running Python (boto3) to execute the Bedrock RetrieveAndGenerate API.
* **Amazon API Gateway:** REST API with strict rate-limiting (Usage Plans) to prevent throttling and abuse.
* **Amazon S3:** Data lake for the raw `.csv` movie datasets.

## 📂 Project Structure
```text
aws-movie-recommender/
│
├── index.html                 # Main UI structure
├── css/
│   └── style.css              # Dark-theme styling
├── js/
│   └── app.js                 # Frontend logic and API integration
├── backend/
│   └── lambda_function.py     # AWS Lambda Python script
├── data/
│   └── cleaned_movies.csv     # Sample dataset for vector search
└── README.md                  # Project documentation
```


## 👥 Author
Uday Salathia Computer Engineering Student | Aspiring Specialist Programmer

If you found this project helpful, feel free to leave a ⭐!
