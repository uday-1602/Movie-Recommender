# 🎬 Serverless AI Movie Recommender (RAG System)

A full-stack, serverless web application that provides highly personalized, conversational movie recommendations using **Retrieval-Augmented Generation (RAG)**. 

Unlike standard LLMs that rely purely on pre-trained data, this system connects a custom dataset of movie plots, casts, and genres directly to **Anthropic's Claude 3.5 Sonnet** via **Amazon Bedrock**, ensuring accurate, hallucination-free recommendations based strictly on the provided context.



## 🚀 Features
* **Retrieval-Augmented Generation (RAG):** Uses a custom Knowledge Base (AWS S3 + Bedrock) to ground the AI's responses in factual data.
* **Serverless Architecture:** Fully managed backend utilizing AWS Lambda and API Gateway for zero-maintenance scalability.
* **Prompt Engineering:** Custom generation configurations enforce strict response formatting (e.g., exactly 3 recommendations, 5-line descriptive paragraphs, specific tone) while preventing robotic phrasing.
* **Clean UI/UX:** A responsive, dark-themed (Netflix-inspired) frontend with asynchronous loading states and markdown parsing.
* **Separation of Concerns:** Clean codebase structured with distinct HTML, CSS, JS, and Python backend logic.

## 🛠️ Tech Stack
**Frontend:**
* HTML5, CSS3, Vanilla JavaScript (ES6+)
* Asynchronous Fetch API for backend communication
* Regex for dynamic Markdown-to-HTML parsing

**Backend & Cloud Infrastructure (AWS):**
* **Amazon S3:** Data lake for the raw and cleaned `.csv` movie datasets.
* **Amazon Bedrock (Knowledge Bases):** Handles text embedding and vector database management for semantic search.
* **Claude 3.5 Sonnet (Anthropic):** The core LLM generating conversational responses.
* **AWS Lambda:** Serverless compute running Python (boto3) to orchestrate the RAG pipeline.
* **Amazon API Gateway:** REST API with Lambda Proxy Integration and strict CORS management.

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

Author
Uday Salathia Computer Engineering Student | Aspiring Specialist Programmer

If you found this project helpful, feel free to leave a ⭐!