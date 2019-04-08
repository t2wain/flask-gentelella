from bcrypt import gensalt, hashpw
from flask_login import UserMixin

from app import login_manager


class User(UserMixin):

    id = 0
    username = ""
    email = ""
    password = ""

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            if property == 'password':
                value = hashpw(value.encode('utf8'), gensalt())
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return get_user_temp(id)


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = get_user_temp(username)
    return user if user else None

def get_user_temp(id):
    user = User()
    user.name = 'admin'
    user.password = 'admin'
    return user
