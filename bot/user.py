import json
import random
import requests

from utils.tools import (
    generate_email,
    generate_name,
    generate_password,
)


class User:

    def __init__(self, api):
        self.API = api
        self.email = generate_email()
        self.first_name = self.last_name = generate_name()
        self.password = generate_password()

        # Registering user
        self.register()
        # Get access token
        self.headers = {
            'Authorization': f'Bearer {self.login()}'
        }

    def get_data(self) -> dict:
        """
            Initial data to create and login user
        :return:
        """
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'confirm_password': self.password,
        }

    def register(self) -> None:
        """
            Registering user into the server to get access token later
        :return: None
        """
        requests.post(
            url=self.API + 'users/register/',
            data=self.get_data(),
        )

    def login(self) -> str:
        """
            Sends request to get access token from server and saving it to the headers variable in __init__
        :return: access token
        """
        response = requests.post(
            url=self.API + 'users/token/',
            data=self.get_data()
        )
        data = json.loads(response.text)
        return data['access']

    def create_post(self) -> None:
        requests.post(
            url=self.API + 'posts/',
            data={
                'name': f'Post created by {self.first_name} {self.last_name}',
                'description': f'Random description'
            },
            headers=self.headers
        )

    def get_posts(self) -> list:
        """
            Sending request to get list of the posts objects and convert it to the list of post ids
        :return: list of post_id
        """
        posts = []
        response = requests.get(
            url=self.API + 'posts/',
            headers=self.headers
        )
        data = json.loads(response.text)
        for post in data:
            posts.append(post['uuid'])
        return posts

    def like_post(self) -> None:
        """
            Get random post and sending request to like it
        :return: None
        """
        posts = self.get_posts()
        post_id = random.choice(posts)
        requests.post(
            url=self.API + f'posts/{post_id}/like/',
            headers=self.headers
        )

    def dislike_post(self) -> None:
        """
            Get random post and sending request to dislike it
        :return: None
        """
        posts = self.get_posts()
        post_id = random.choice(posts)
        requests.post(
            url=self.API + f'posts/{post_id}/dislike/',
            headers=self.headers
        )
