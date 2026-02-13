# 🚀 End-to-End MLOps Pipeline: Iris Classification

![Build Status](https://github.com/oscartma/Portfolio-MLOps/actions/workflows/calidad_codigo.yml/badge.svg)
![Docker Build](https://github.com/oscartma/Portfolio-MLOps/actions/workflows/docker-publish.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.9-blue)
![Deployment](https://img.shields.io/badge/deploy-Render-success)

## 📋 Project Overview

This project demonstrates a robust **MLOps (Machine Learning Operations)** pipeline that automates the lifecycle of a Machine Learning model. It goes beyond simple model training by implementing **Continuous Integration (CI)**, **Continuous Delivery (CD)**, and **Containerization**.

The system trains a Random Forest classifier on the Iris dataset, packages it into a Docker container, and deploys it as a scalable API to the cloud.

### 🏗️ Engineering Architecture

The following diagram illustrates the automated pipeline triggered by every code push:

```mermaid
graph LR
    A[🧑‍💻 Local Dev] -->|git push| B(🐱 GitHub Repo)
    B --> C{⚙️ GitHub Actions}
    
    subgraph CI - Continuous Integration
    C -->|1. Test| D[🧪 Pytest & Linting]
    C -->|2. Train| E[🤖 Train Model Script]
    E -->|Artifact| F[💾 Model.pkl]
    end
    
    subgraph CD - Continuous Delivery
    C -->|3. Build| G[🐳 Docker Image]
    G -->|Publish| H[📦 GitHub Container Registry]
    end
    
    subgraph Deployment
    H -->|Pull| I[☁️ Render Cloud]
    I -->|Serve| J[🚀 Live API Endpoint]
    end
