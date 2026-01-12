import streamlit as st
from newspaper import Article
from groq import Groq

# Secure API key loading
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    groq_api_key = None

if not groq_api_key:
    st.error("""Groq API key not found!

Please add it in one of these places:
• Local: create file .streamlit/secrets.toml in this folder
• Deployed: Settings → Secrets in Streamlit Cloud""")
    st.stop()

client = Groq(api_key=groq_api_key)
st.success("Groq client ready!")

# Fetch article
def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Generate digest
def generate_outputs(article_text):
    if not article_text or len(article_text) < 100:
        return "Article text too short or empty."

    prompt = f"""
Analyze this news article text:

{article_text[:15000]}

Provide **exactly** in this format:

### Neutral Summary
[100-150 word neutral summary]

### Key Facts
- Bullet 1
- Bullet 2
... (8-10 facts)

### Reader FAQs
**Q1:** Question?
**A:** Answer.

... (4-5 FAQs)

Be neutral, factual, no external info.
"""

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant", 
            temperature=0.4,
            max_tokens=900,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

st.title("NewsDigest AI Prototype")
st.markdown("**Make news more accessible:** Get summary, facts & FAQs.")

input_type = st.radio("Input type:", ("URL", "Paste Text"))

if input_type == "URL":
    url = st.text_input("Enter article URL:")
    if st.button("Generate Digest") and url:
        with st.spinner("Fetching..."):
            text = fetch_article_text(url)
            if "Error" in text:
                st.error(text)
            else:
                st.info(f"Length: {len(text):,} chars")
                with st.spinner("Generating..."):
                    result = generate_outputs(text)
                    st.markdown(result)
else:
    text = st.text_area("Paste text:", height=300)
    if st.button("Generate Digest") and text:
        with st.spinner("Generating..."):
            result = generate_outputs(text)
            st.markdown(result)

st.markdown("---")
st.caption("Prototype by Sri Lakshmi • Always verify AI • Groq + Llama 3.1")