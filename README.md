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

### How to Run Locally

### 1. Clone the repository
   ```bash
   git clone https://github.com/Srilakshmi002/newsdigest-ai.git
   cd newsdigest-ai
   
### 2. Install the required Python packages:
```bash
pip install -r requirements.txt

#### If you don't have requirements.txt, create it with these lines:
textstreamlit
newspaper3k
groq

### Set up your Groq API key (local development)
This is very important — add this section:

```markdown
3. Create a local secrets file for your Groq API key:
```bash
mkdir -p .streamlit
echo 'GROQ_API_KEY = "your_groq_api_key_here"' > .streamlit/secrets.toml

Get your free API key at: https://console.groq.com/keys
Never commit this file to GitHub! (add .streamlit / to .gitignore)

### 4. Run the app
```markdown
4. Launch the app:
```bash
streamlit run app.py

## Tech Stack
- Python 3.12
- Streamlit (UI framework)
- Groq API (fast LLM inference with Llama 3.1 8B model)
- newspaper3k (article parsing)

## Important Notes
- AI outputs are generated for quick understanding — **always verify against the original article**
- No API keys are stored in code — use `st.secrets` only
- Built for accessibility in public-interest journalism

## Author
Sri Lakshmi  
