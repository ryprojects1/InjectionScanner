import requests
from bs4 import BeautifulSoup
sus_words = [
    # Direct injection commands
    "ignore previous", "ignore all", "disregard previous",
    "forget previous", "override instructions", "bypass instructions",
    "ignore instructions", "disregard instructions",
    
    # System prompt attacks
    "system prompt", "initial prompt", "original instructions",
    "reveal prompt", "show prompt", "print prompt",
    
    # Exfiltration attempts
    "leak", "exfiltrate", "send to", "forward to",
    "secret key", "api key", "password", "credentials",
    
    # Role manipulation
    "you are now", "act as", "pretend to be", "roleplay as",
    "jailbreak", "dan mode", "developer mode",
    
    # Sharded fragments
    "ignore", "previous", "system", "instead",
    "override", "bypass", "disregard", "forget",
    
    # Data extraction
    "repeat after me", "say exactly", "output everything",
    "print everything", "dump", "extract"
]
#sus phrases that python need to detect and raise alert to
# 2. This is a "for loop" - it goes through the list one by one
def scan_localF(file_path):
        print(f"Scanning: {file_path}")
        try:
            # with block, allow python to automatically close after its done reading
            with open(file_path,"r", encoding="utf-8") as f: # r means reading mode (so no modification) , utf-8 makes sure python reads it correctly
                  content = f.read()
            soup = BeautifulSoup(content,'html.parser')
            meta_tags = soup.find_all('meta') #find all tags that contain 'meta'

            found_threat = False
            for tag in meta_tags:
                 tag_text = str(tag).lower() # make everything in the bracket as a string and .lower makes everything lowercase and minimize the chances of crashing
                 #scanning the entire line
                 for phrase in sus_words:
                    if phrase in tag_text:
                         print(f"[!] THREAT DETECTED: Found '{phrase}' in metadata.")
                         print(f"    Full String: {tag_text}")
                         found_threat = True
            if not found_threat:
                 print("[+] File appears safe.") # [+] means success 
        except FileNotFoundError:
             print("Error: The file 'malicious.html' was not found.")
scan_localF("malicious.html") # scan the file
