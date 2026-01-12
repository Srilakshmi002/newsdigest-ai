# NewsDigest AI

**A simple Streamlit web application** that makes news articles more accessible by automatically generating:

- Neutral 100–150 word summary  
- 8–10 key facts (bullet points)  
- 4–5 reader-friendly FAQs  

All powered by **Groq AI** (fast, free-tier models) and newspaper3k for article extraction.

### Why this project?

I created this tool to help readers quickly understand complex public-interest stories - like school vouchers, new state laws, policy changes, or elections — without having to read long, dense articles.  
It promotes **accessibility**, **efficiency**, and **civic engagement** in journalism.

### Features

- Two input modes: article URL or pasted text  
- Clean, interactive user interface  
- Secure API key handling (no hardcoding)  
- Fast AI processing with Llama 3.1 model  
- Always verify outputs against original article (human oversight reminder)

### Tech Stack

- **Python**: 3.12  
- **Streamlit** – interactive web UI  
- **Groq API** – fast LLM inference (Llama 3.1 8B model)  
- **newspaper3k** – intelligent article extraction from URLs  
- **requirements.txt** – all dependencies listed

### How to Run Locally

1. Clone the repository
   ```bash
   git clone https://github.com/Srilakshmi002/newsdigest-ai.git
   cd newsdigest-ai
