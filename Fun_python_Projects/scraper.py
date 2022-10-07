import requests
import json
from bs4 import BeautifulSoup

link = input("Input the URL:\n")

try:
    r = requests.get(link, headers={'Accept-Language': 'en-US,en;q=0.5'}).text
    soup = BeautifulSoup(r, 'html.parser')
    title = soup.find('h1').text
    des = soup.find('span', {'data-testid': 'plot-xl'}).text
    solution = {"title": title, "description": des}
    print()
    print(json.dumps(solution))



    # print(r.json()['content'])
except AttributeError:
    print("\nInvalid movie page!")
