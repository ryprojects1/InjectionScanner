import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime

sus_words = ["ignore", "previous", "system", "instead", "leak", 
              "system prompt", "instead, do", "secret key", "ignore previous"]
DANGER = 3

def scan_text(content):
    content = content.lower()
    found_fragments =  []
    for word in sus_words:
        if word in content:
            found_fragments.append(word)
    score = len(found_fragments)
    return score, found_fragments

def scan_url(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tags = soup.find_all('meta')
        all_text = " ".join([str(tag) for tag in meta_tags]).lower()
        score, found_fragments = scan_text(all_text)
        return score, found_fragments
    except Exception as e:
        return None, str(e)

def log_scan(source, score, threats):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("security_audit.log","a") as log_file:
        log_file.write(f"[{timestamp}] SCAN: {source}\n")
        log_file.write(f"RISK SCORE: {score}\n")
        log_file.write(f"THREATS: {', '.join(threats) if threats else 'None'}\n")
        log_file.write("-" * 30 + "\n")

st.set_page_config(page_title="PromptGuard", page_icon="!")
st.title("PromptGuard")
st.subheader("Prompt Injection Detection Tool")
st.write("Detect prompt injection attacks in URLs or HTML content instantly.")

tab1, tab2 = st.tabs(["Scan URL", "Scan Text/ HTML"])

with tab1:
    st.markdown("### Paste a URL to scan")
    url_input = st.text_input("Enter URL", placeholder = "https://example.com")
    if st.button("Scan URL"):
        if url_input:
            with st.spinner("Scanning URL..."):
                score, result = scan_url(url_input)
            if score is None:
                st.error(f"Error scanning URL: {result}")
            else:
                log_scan(url_input, score, result)
                st.markdown("---")
                if score >= DANGER:
                    st.error(f"HIGH RISK - Prompt Injection Detected!")
                elif score > 0:
                    st.warning(f" LOW RISK - Suspicious fragements found")
                else:
                    st.success("SAFE - No injection detected")
                st.metric("Risk Score", score)
                if result:
                    st.markdown("Suspicious fragments found:**")
                    for word in result:
                        st.code(word)
        else:
            st.warning("Please enter a URL")
with tab2:
    st.markdown(" Paste HTML or text content to scan")
    text_input = st.text_area("Paste content here", height=200,
                              placeholder= "Paste any HTML or text content...")
    if st.button("Scan Text"):
        if text_input:
            score,result = scan_text(text_input)
            log_scan("manual_text_input", score, result)
            st.markdown("---")
            if score >= DANGER:
                st.error(f"HIGH RISK - Prompt Injection Detected!")
            elif score > 0:
                st.warning(f"LOW RISK - Suspicious fragements found")
            else:
                st.success("SAFE - No injection detected")
            st.metric("Risk Score", score)
            if result:
                st.markdown("Suspicious fragments found:**")
                for word in result:
                    st.code(word)
        else:
            st.warning("Please paste some content first")

st.markdown("---")
st.markdown(" Recent Scans")
try:
    with open("security_audit.log", "r") as f:
        logs = f.read()
    if logs:
        st.code(logs[-2000:])
    else:
        st.info("No scans logged yet")
except FileNotFoundError:
    st.info("No scans logged yet")