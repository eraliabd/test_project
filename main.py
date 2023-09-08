import requests
from bs4 import BeautifulSoup

url = 'https://road24.uz/'
response = requests.get(url=url)
print(response)
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    first_h1 = soup.find('h1').get_text()
    print(first_h1)
else:
    print("Failed to fetch the website.")
exit()


