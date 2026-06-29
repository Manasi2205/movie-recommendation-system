import requests

url = "https://api.themoviedb.org/3/movie/550?api_key=4d94021969f7adf7544c17dd9823311f&language=en-US"

try:
    response = requests.get(url, timeout=10)
    print(response.status_code)
    print(response.json()["title"])
except Exception as e:
    print(e)