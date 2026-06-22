# AI Webpage Brochure Generator

## Overview

AI Webpage Brochure Generator is an AI-powered application that analyzes a company's website, identifies the most relevant pages, extracts their content, and automatically generates a professional brochure in Markdown format.

The application uses a multi-step AI workflow:

1. Extract links from a company's homepage.
2. Use an LLM to identify the most relevant company pages.
3. Fetch content from those pages.
4. Generate a brochure for customers, investors, and potential recruits.

---

## Features

* Extract website content automatically
* Discover relevant company pages
* AI-powered link selection
* Generate professional company brochures
* Produce Markdown-formatted output
* Run locally using Ollama and Llama 3.2

---

## Tech Stack

* Python
* Ollama
* Llama 3.2
* OpenAI SDK
* BeautifulSoup
* Requests
* Prompt Engineering

---

## Project Workflow

```text
Company Website
       │
       ▼
Link Extraction
       │
       ▼
LLM Link Selection
       │
       ▼
Content Collection
       │
       ▼
Brochure Generation
       │
       ▼
Markdown Brochure
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/gannuabhinavreddy-ai/ai-webpage-brochure-generator.git
cd ai-webpage-brochure-generator
```

### Create Virtual Environment

```bash
uv venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Start Ollama

```bash
ollama run llama3.2:1b
```

### Run Application

```bash
python app.py
```

---

## Example

Input:

```text
Company: Hugging Face
Website: https://huggingface.co
```

The system:

* Extracts links
* Selects relevant pages
* Downloads content
* Generates a brochure

Output:

```markdown
# Hugging Face

Hugging Face is an open-source AI platform...
```

---


#sample output for HuggingFace - you can try with other companies too!
"""
Selecting relevant links for https://huggingface.co by calling llama3.2:1b
Found 2 relevant links
https://huggingface.co/about
https://endpoints.huggingface.co
Hugging Face: The AI Community Building the Future
Hugging Face is an open-source platform built by a community of researchers and industry leaders to empower the next generation of artificial intelligence. With a mission to facilitate collaborative model development and deployment, Hugging Face has created an incredible array of AI models, datasets, and applications.

Featured Models
Explore our extensive collection of state-of-the-art AI models, covering various domains such as computer vision, natural language processing, and speech recognition.

BERT (Bidirectional Encoder Representations from Transformers) - A widely used pre-trained model for natural language processing.
**ViT-B/32 (Vision Transformer with BERT Pre-Training on ImageNet 1k) - An improved vision transformer architecture integrated with bert pre-training on image_net_1000.
Datasets
Discover an expansive library of high-quality datasets covering text, images, and more. These datasets are crucial for training and deployment of various AI models.

**T5-large-patch-16k-cased-uncased - A pre-trained text model developed for conversational AI applications.
**Llama Mini-maxi - A small-scale mini-maximization version of Llama, designed specifically for exploration in reinforcement learning.
Spaces
Contribute to our ecosystem by collaborating with others on various projects and initiatives. These spaces foster innovation and accelerate progress in artificial intelligence.

**Zero Agents Space - A community-driven space for hosting and contributing zero-shot models and agents developed from scratch.
**Hugging Chat Space - An initiative to explore various conversations, scenarios, and dialogue systems using our existing datasets.
Enterprise Support
Take advantage of enterprise-grade support and deployment services designed specifically for large-scale AI initiatives. Our solutions are optimized for production environments.

**Hugging Face PRO - Enterprise-level access to our platform's full features, including model management, deployment, and more.
**Inference Endpoints by Hugging Face - Secure cloud-based inference endpoints optimized for high-performance AI workloads.
Pricing
Explore our affordable pricing options and customized bundles tailored to meet specific needs of your organization.
 """

## Learning Outcomes

Through this project I learned:

* Multi-step LLM workflows
* Structured JSON outputs
* Prompt engineering techniques
* Web scraping with BeautifulSoup
* Link extraction and filtering
* Content aggregation
* Markdown generation
* Local LLM deployment using Ollama

---

## Future Improvements

* Streamlit web interface
* PDF brochure export
* Brochure templates
* Multiple brochure styles
* Company logo extraction
* Automatic brochure download

---

## Author

Abhinav Reddy Gannu

AI Engineering Learning Journey Project #2
