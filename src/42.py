import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(e)

def parse_html(html, tag_name):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for item in soup.find_all(tag_name):
        result = {}
        for index, attribute in enumerate(item.attrs):
            if attribute.startswith('data-'):
                del attribute[:attribute.index('=')]
            value = re.sub(r'[^\w\s]','',attribute)
            if '=' not in value:
                value = value.replace('"', '')
            result[attribute] = value
        results.append(result)
    return results

def extract_data(html, tag_name):
    soup = BeautifulSoup(html, 'html.parser')
    data = {}
    for item in soup.find_all(tag_name):
        for attribute, value in zip(item.attrs, item.get_text().strip('data-').split()):
            if attribute.startswith('data-'):
                del attribute[:attribute.index('=')]
            value = re.sub(r'[^\w\s]','',value)
            if '=' not in value:
                value = value.replace('"', '')
            data[attribute] = value
    return data

if __name__ == "__main__":
    url = "http://example.com"
    html = get_html(url)
    parsed_data = parse_html(html, 'h1')
    extracted_data = extract_data(html, 'p')

    for tag_name in ['h1', 'p']:
        print(f"{tag_name} data: {parsed_data[tag_name]}", end="\n\n")
        print(f"Extracted data: {extracted_data[tag_name]}")

