import secrets, string

# use our own make_random_password method after django 5.1 fully deprecated the functionality (https://django.readthedocs.io/en/stable/releases/5.1.html#:~:text=The%20BaseUserManager.make_random_password()%20method%20is%20removed.)
def make_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))