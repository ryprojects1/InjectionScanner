# PromptGuard

PromptGuard is a python tool to scan HTML files for prompt injection attacks
[🔴 Live Demo](https://promptguard1.streamlit.app)

### What is Prompt Injection?
Prompt injection is when adversaries hide malicious instructions inside meta tags or content where an AI agent will read it as a legitimate prompt and follow it blindly with no sense of security. This is a huge and growing problem — a successful attack can expose your personal details, credentials, and even banking information without you ever knowing.

### What Does PromptGuard Do?
PromptGuard acts as the middleman between an AI agent and the system it's operating in. It detects threats by scanning for dangerous patterns and suspicious wording before any damage is done. Think of it like an IDS — it monitors, alerts, and notifies the user whether a website or HTML content is dangerous or not.
Two ways to use it:
- Paste a URL — PromptGuard fetches and scans the page automatically
- Paste HTML or text — scan any content directly
  
### How Does It Work?
PromptGuard scans the meta tags of a website or pasted content looking for suspicious activity. If anything is detected you get notified instantly.

I also implemented a sharded detection system — instead of looking for one complete phrase, it tracks individual suspicious fragments across the content. If the number of suspicious fragments exceeds a certain threshold it gets flagged as HIGH RISK. The reason there is a threshold is because not all suspicious activity is dangerous — context matters.

Every scan is logged in an audit trail showing what was found, when it was scanned, and the risk score.
Attack patterns detected:
- Direct injection commands (ignore previous, override instructions)
- System prompt extraction attempts (reveal prompt, show prompt)
- Role manipulation attacks (act as, jailbreak, developer mode)
- Sharded/split injection across multiple tags
- Data exfiltration attempts (leak, dump, extract)

### What It Currently Misses
Being realistic — PromptGuard is still in development and there are things we can't currently detect:
- Encoded or obfuscated prompts
- Non-English injection attempts
- Semantic attacks (same meaning, different words)

### What We're Working On Next
- ML based detection instead of keyword matching only
- Support for more file types
- Browser extension version
- Multi-language support
- 
### Run It Locally
Requiremnts:
- Python 3
- Install dependencies
- pip install streamlit requests beautifulsoup4
Run the app:
- streamlit run app.py

Built By

Ching Ho Wong | 1st Year Computer Science Student


