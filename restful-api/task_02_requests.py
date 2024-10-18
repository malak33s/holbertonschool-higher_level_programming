#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print('Status code: {}'.format(r.status_code))

    if r.status_code == 200:
        p = r.json()
        for post in p:
            print(post['title'])


def fetch_and_save_posts():
    """ fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        p = r.json()
        for post in p:
            post = [{'id': post['id'], 'title': post['title'],
                     'body': post['body']}]
            module_csv = 'posts.csv'
            with open(module_csv, 'w', encoding="utf-8") as f:
                w = csv.DictWriter(f, ['id', 'title', 'body'])
                w.writeheader()
                w.writerows(post)
