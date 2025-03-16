import requests

GITHUB_TOKEN = ""  # Replace with your actual token

query = "filename:settings.py"
url = f"https://api.github.com/search/code?q={query}"

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

response = requests.get(url, headers=headers)
data = response.json()

# Format output neatly
for item in data.get("items", []):
    repo_name = item['repository']['full_name']
    file_url = item['html_url']
    print(f"📂 Repository: {repo_name}\n📄 File URL: {file_url}\n{'-'*40}")