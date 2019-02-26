from urllib import request

# Retrieve content from a URL:

http_response = request.urlopen("https://www.bankhapoalim.co.il/")
html = http_response.read()

print(str(html[:500], "utf-8"))

if True:
    a = 1

# Extract domain name from an URL:
from urllib.parse import urlparse

parsed_url = urlparse('https://www.bankhapoalim.co.il/wps/portal/PoalimPrivate/branches')

print(parsed_url.netloc)
