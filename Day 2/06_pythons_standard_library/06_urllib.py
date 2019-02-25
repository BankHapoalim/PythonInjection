import urllib

# Retrieve content from a URL:

http_response = urllib.request.urlopen("https://www.bankhapoalim.co.il/")
html = http_response.read()

print(str(html[:500], "utf-8"))


# Extract domain name from an URL:
from urllib.parse import urlparse

parsed_url = urlparse('https://www.bankhapoalim.co.il/wps/portal/PoalimPrivate/branches')

print(parsed_url.netloc)