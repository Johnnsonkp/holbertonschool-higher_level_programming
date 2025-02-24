#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        r = requests.get(url)

        if r.status_code == 200:
            posts = r.json()

            print("Status Code: {}".format(r.status_code))

            for post in posts:
                print("{}".format(post['title']))

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


def fetch_and_save_posts():

    def save_to_csv_file(data):
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def fetch_posts():
        url = "https://jsonplaceholder.typicode.com/posts"
        dict = []
        try:
            r = requests.get(url)
            if (r.status_code == 200):
                posts = r.json()
                for post in posts:
                    dict.append(
                        {'id': post['id'], 'title': post['title'], 'body': post['body']})

                save_to_csv_file(dict)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    fetch_posts()
