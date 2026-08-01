import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime

# --- CONFIG ---
st.set_page_config(
    page_title="PromptGuard",
    page_icon="🛡️",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* Background */
    .stApp {
        background-color: #0d1117;
    }
    
    /* Main title */
    .main-title {
        font-size: 3em;
        font-weight: 800;
        color: #ff4444;
        text-align: center;
        padding: 10px 0;
        letter-spacing: 2px;
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 1.1em;
        color: #8b949e;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Risk boxes */
    .high-risk {
        background-color: #3d0000;
        border: 2px solid #ff4444;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        color: #ff4444;
    }
    
    .low-risk {
        background-color: #2d2000;
        border: 2px solid #ffa500;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        color: #ffa500;
    }
    
    .safe {
        background-color: #002d00;
        border: 2px solid #00ff00;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        color: #00ff00;
    }

    /* Stats bar */
    .stat-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        color: #c9d1d9;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNCTIONS ---
sus_words = ["ignore", "previous", "system", "instead", "leak",
             "system prompt", "instead, do", "secret key", "ignore previous"]
DANGER = 3

def scan_text(content):
    content = content.lower()
    found_fragments = []
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
    with open("security_audit.log", "a") as log_file:
        log_file.write(f"[{timestamp}] SCAN: {source}\n")
        log_file.write(f"RISK SCORE: {score}\n")
        log_file.write(f"THREATS: {', '.join(threats) if threats else 'None'}\n")
        log_file.write("-" * 30 + "\n")

def show_result(score, result):
    if score >= DANGER:
        st.markdown('<div class="high-risk">🚨 HIGH RISK — Prompt Injection Detected!</div>',
                    unsafe_allow_html=True)
    elif score > 0:
        st.markdown('<div class="low-risk">⚠️ LOW RISK — Suspicious Fragments Found</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="safe">✅ SAFE — No Injection Detected</div>',
                    unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stat-box"><h3 style="color:#ff4444">{score}</h3>Risk Score</div>',
                    unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-box"><h3 style="color:#ff4444">{len(result)}</h3>Threats Found</div>',
                    unsafe_allow_html=True)

    if result:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**🔍 Suspicious fragments detected:**")
        for word in result:
            st.code(word)

# --- HEADER ---
st.markdown('<div class="main-title">🛡️ PromptGuard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Prompt Injection Detection Tool — Scan URLs or text for malicious prompts instantly</div>',
            unsafe_allow_html=True)

st.markdown("---")

# --- TABS ---
tab1, tab2 = st.tabs(["🌐 Scan URL", "📄 Scan Text/HTML"])

# --- URL SCANNER ---
with tab1:
    st.markdown("### Paste a URL to scan")
    url_input = st.text_input("Enter URL", placeholder="https://example.com")
    if st.button("🔍 Scan URL", key="scan_url"):
        if url_input:
            with st.spinner("Scanning URL for injection attacks..."):
                score, result = scan_url(url_input)
            if score is None:
                st.error(f"Error scanning URL: {result}")
            else:
                log_scan(url_input, score, result)
                st.markdown("---")
                show_result(score, result)
        else:
            st.warning("Please enter a URL first")

# --- TEXT SCANNER ---
with tab2:
    st.markdown("### Paste HTML or text content to scan")
    text_input = st.text_area("Paste content here", height=200,
                               placeholder="Paste any HTML or text content...")
    if st.button("🔍 Scan Text", key="scan_text"):
        if text_input:
            score, result = scan_text(text_input)
            log_scan("manual_text_input", score, result)
            st.markdown("---")
            show_result(score, result)
        else:
            st.warning("Please paste some content first")

# --- AUDIT LOG ---
st.markdown("---")
st.markdown("### 📋 Recent Scans")
try:
    with open("security_audit.log", "r") as f:
        logs = f.read()
    if logs:
        st.code(logs[-2000:])
    else:
        st.info("No scans logged yet")
except FileNotFoundError:
    st.info("No scans logged yet")

# --- FOOTER ---
st.markdown("---")
st.markdown('<div style="text-align:center; color:#8b949e; font-size:0.8em">Built by Ching Ho Wong | Cybersecurity Tool | <a href="https://github.com/ryprojects1/PromptGuard" style="color:#ff4444">GitHub</a></div>',
            unsafe_allow_html=True)