from bs4 import BeautifulSoup #doing this rather just import, allow easier access and more efficient
html_doc = "<html><body><h1>Hello World</h1><p class=' description'>This is a test.</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print(f"The headline is:{soup.h1.string}") #f tells python to look inside those curly brackets
print(f"The description is:{soup.find('p', class_= 'description').text}") # its class_ to avoid naming collision
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) #User agent is like an id card, and M... is the content of the card
# it allows website to treat the scipt as like a normal browser
# goes and get the page
soup = BeautifulSoup(response.text, 'html.parser')
#response.text is  everthing thats on that url
for tag in meta_tags:
    # Most meta tags use 'name' and 'content' attributes
    #have a loop that output the name and contents of the hidden tags
    name = tag.get('name', 'N/A')
    content = tag.get('content', 'N/A')
    print(f"Name: {name} | Content: {content}")
#The url we are targeting
print(f"I found {len(meta_tags)} hidden tags on this page!\n")
 tag_text = str(tag.get('content', '')).lower() # make everything in the bracket as a string and .lower makes everything lowercase and minimize the chances of crashing
                 for phrase in sus_words: