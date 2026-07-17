import requests
from bs4 import BeautifulSoup
sus_words= ["ignore previous", "system prompt", "instead, do", "secret key"]
#sus phrases that python need to detect and raise alert to
# 2. This is a "for loop" - it goes through the list one by one
def injection_scanner(url):
        print(f"Scanning: {url}")
        try:
            response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}, timeout=5) 
            # it is fetching the url, if it takes longer than 5 sec then it stop this prevent python to try fetch it forever
            soup = BeautifulSoup(response.text,'html.parser')
            meta_tags = soup.find_all('meta') #find all tags that contain 'meta'
            for tag in meta_tags:
                 name = tag.get('name', 'N/A')
                 content = tag.get('content', 'N/A')
                 print(f"Name: {name} | Content: {content}")
                 for word in sus_words:
                       if word in sus_words:
                             print(f"[!] SECURITY ALERT: sus words found in metadata!")
                             #[!] create a digital flare
                             print(f"Found: '{word}' in content: {content[:50]}")
                             #only show the first 50 characters
                             return True
            print("No injection found. All Safe")
            return False
        except Exception as e: #if there is scanning error it output the error message
              print(f"Error scanning: {e}")
injection_scanner("https://tryhackme.com/paths") #scan the url
