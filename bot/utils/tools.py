import random
import string


def generate_email() -> str:
    """
       Generates random email address to register user
    """
    email = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    return email + '@gmail.com'


def generate_name() -> str:
    """
       Generates random name or surname to register user
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(5))


def generate_password() -> str:
    """
        Generates random password to register user
    """
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


def generate_post_name() -> str:
    """
        Generate random name of post
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(15))


def generate_post_description() -> str:
    """
        Generate random description to post
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(100))
