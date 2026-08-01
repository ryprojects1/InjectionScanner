# PromptGuard

PromptGuard is a python tool to scan HTML files for prompt injection attacks

### Function
- scan files for suspicious fragments
- score and determine the risk level
- logs findings to an audit file

### Why do we need it?
Prompt injection is a real and growing cybersecurity threat
As AI becomes more common, tools like mine are increasingly important

### How to run it?
- require python3
- command to run: `python3 CheckSharded.py`

### Example: (After scanned result)
Running Scan on: malicious.html 
 Event logged to security_audit.log
Found 4 suspicious fragments: ['ignore', 'previous', 'instead', 'leak']
 HIGH RISK: Sharded Prompt Injection detected (Score: 4)
### Future improvements

- Support more file types
- Web interface
- Live AI integration testing

