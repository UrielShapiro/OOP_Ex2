import User

# singleton
_instance = None


# singleton
def instance():
    return _instance


class SocialNetwork:
    users = []

    # singleton
    def __init__(self, name):
        if _instance is None:
            self.name = name
            print(f"The social network {self.name} was created!")
        else:
            raise RuntimeError('Call instance() instead')

    # factory#
    def sign_up(self, name, password):
        for u in self.users:
            if u.name == name:
                raise RuntimeError('name is not valid')
        if 4 <= len(password) <= 8:
            newUser = User.User(name, password)
            self.users.append(newUser)
            return newUser
        else:
            raise RuntimeError('illegal password')

    def log_in(self, name, password):
        for u in self.users:
            if u.name == name and u.password == password:
                u.logIn()

    def log_out(self, name):
        for u in self.users:
            if u.name == name:
                u.logOut()
