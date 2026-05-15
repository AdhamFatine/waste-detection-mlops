Waste Detection MLOps Project

Project Overview

This project is an end-to-end MLOps system for waste detection. It uses a trained machine learning model served through a FastAPI backend and a Streamlit frontend for interaction. The whole system is containerized using Docker and managed with docker-compose.

The goal of this project is to demonstrate a full machine learning deployment pipeline from model to production-ready application.

Architecture

Streamlit frontend communicates with FastAPI backend, which loads the trained machine learning model and returns predictions.

Streamlit → FastAPI → Machine Learning Model

Features

- Real-time predictions through REST API
- Simple user interface using Streamlit
- Fully containerized setup using Docker
- Multi-service orchestration with docker-compose
- Easy local deployment

Project Structure

waste-detection-mlops/
├── api/              FastAPI backend
├── app/              Streamlit frontend
├── models/           Trained model files
├── docker-compose.yml
├── requirements.txt
└── README.md

Installation and Run

1. Clone the repository

git clone <your-repo-url>
cd waste-detection-mlops

2. Run the project with Docker Compose

docker-compose up --build

Access the Application

- FastAPI documentation: http://localhost:8000/docs
- Streamlit application: http://localhost:8501

API Endpoints

Health check:
GET /health

Prediction:
POST /predict

Example request:
{
  "data": "sample input"
}

MLOps Workflow

- Model is trained separately and saved in the models folder
- FastAPI loads the trained model
- Streamlit sends input data to API
- API returns prediction results
- Docker ensures consistent deployment across environments

Future Improvements

- Add CI/CD pipeline using GitHub Actions
- Deploy on cloud platforms like Render or AWS
- Add logging and monitoring for predictions
- Implement model retraining pipeline

Author

MLOps / Data Science student project