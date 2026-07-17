#attackers can use Sharded Exfiltration. This means instead of putting the whole dangerous phrase in one tag, they break it up like a puzzle:

#Tag 1: "Ignore"

#Tag 2: "previous"

# Tag 3: "instructions"

# A simple scanner looks for the whole phrase and misses it.
from bs4 import BeautifulSoup
from audit import log_security
sus_words= ["ignore" , "previous", "system", "instead", "leak"]
DANGER = 3
def sharded_scan_local(file_path):
    print(f" Running Scan on: {file_path} ")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower() #reading everything in lower case
            found_fragments = []
            for word in sus_words:
                if word in content:
                    found_fragments.append(word)
            score = len(found_fragments)
            log_security(file_path, score, found_fragments)
            print(f"Found {score} suspicious fragments: {found_fragments}")
            if score >= DANGER:
                print(f" HIGH RISK: Sharded Prompt Injection detected (Score: {score})")
                return True
            else:
                print("Page score is low, its likely safe")
                return False
    except FileNotFoundError:
        print("File not found")
sharded_scan_local("malicious.html")