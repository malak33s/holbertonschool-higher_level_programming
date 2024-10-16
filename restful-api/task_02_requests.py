import requests
import csv

# Récupère  enregistre les posts dans un CSV


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()
        with open('posts.csv', 'w', newline='') as f:
            # Ajout de 'userId' dans les fieldnames
            writer = csv.DictWriter
            (f, fieldnames=["userId", "id", "title", "body"])
            writer.writeheader()  # En-tête CSV
            writer.writerows(posts)  # Écrit les posts

# Récupère et affiche les posts


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])
