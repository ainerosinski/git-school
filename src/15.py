import requests

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('downloaded_file.txt', 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully!")
    else:
        print(f"Failed to download file from {url}. Status code: {response.status_code}")

# Replace the following URLs with actual file links
download_file("https://example.com/file1.pdf")
