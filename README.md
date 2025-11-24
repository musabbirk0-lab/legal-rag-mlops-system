

# Legal Document RAG System

An end-to-end **Retrieval-Augmented Generation (RAG)** system for legal documents, with **full MLOps integration** including Docker, Kubernetes, Airflow, and CI/CD.

---

## **Features**

### 1. Web Scraping & PDF Download

* Automatically downloads legal documents from websites and repositories.
* Supports HTML scraping and PDF download.
* Can be scheduled for automatic updates via Airflow DAGs.

### 2. PDF Ingestion & Text Extraction

* Reads and extracts text from PDFs.
* Cleans and preprocesses text for embeddings.
* Splits large documents into chunks for better semantic search.

### 3. Embeddings & Vector Store

* Converts text chunks to vector embeddings using:

  * OpenAI embeddings
  * Sentence-Transformers local models
* Stores vectors in FAISS or Chroma.
* Supports semantic search and returns top matches with metadata.

### 4. Query & API

* FastAPI endpoints:

  * `/upload` → Upload PDFs and optionally trigger ingestion.
  * `/query` → Submit legal questions; get top relevant document chunks.
* Integrates with LLMs via LangChain for full-text answers.

### 5. MLOps Integration

* **Docker**: Containerized application for consistency.
* **Kubernetes**: Deployment manifests for scaling & service exposure.
* **Airflow**: DAGs for scheduled scraping and ingestion pipelines.
* **GitHub Actions (CI/CD)**: Automatic testing, image build, and deployment.

### 6. Testing & QA

* Unit tests for scraper, ingestion pipeline, and API endpoints.
* Ensures reliability of parsing, embeddings, vector search, and API responses.

---

## **Directory Structure**

```
legal-docs-rag/
├── README.md
├── app/
│   ├── app.py
│   ├── scrape.py
│   ├── ingest.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── utils.py
│   ├── requirements.txt
│   └── Dockerfile
├── airflow/
│   └── dags/
│       ├── scrape_dag.py
│       └── ingest_dag.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── tests/
│   ├── test_scrape.py
│   ├── test_ingest.py
│   └── test_app.py
├── scripts/
│   └── deploy_k8s.sh
└── data/
    ├── pdfs/
    └── vstore/
```



## **MLOps Notes**

* **Airflow DAGs**: Schedule scraping and ingestion periodically.
* **Kubernetes**: Deploy Docker containers with scaling support.
* **CI/CD**: GitHub Actions pipeline runs tests, builds images, and deploys.

---

## **Optional Enhancements**

* OCR support for scanned PDFs.
* Multi-language support for international legal documents.
* Logging and monitoring with Prometheus/Grafana.

---



