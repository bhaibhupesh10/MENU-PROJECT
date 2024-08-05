#!/usr/bin/env python3

import cgi
import cgitb
import requests
from bs4 import BeautifulSoup
import json

cgitb.enable()

print("Content-Type: application/json\n")

def google_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {'q': query, 'num': 10}
    response = requests.get('https://www.google.com/search', headers=headers, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for item in soup.find_all('div', attrs={'class': 'g'}, limit=10):
            title_element = item.find('h3')
            link_element = item.find('a')
            snippet_element = item.find('div', attrs={'class': 'IsZvec'})

            if title_element and link_element:
                title = title_element.text
                link = link_element['href']
                snippet = snippet_element.text if snippet_element else 'No snippet'
                results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })

            if len(results) >= 5:
                break

        return results
    else:
        return None

form = cgi.FieldStorage()
query = form.getvalue('query')
results = google_search(query)

print(json.dumps(results))

