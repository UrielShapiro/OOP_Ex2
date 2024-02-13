import User

# singleton
_instance = None


# Will be used to create only one instance of the SocialNetwork.
def instance():
    return _instance


class SocialNetwork:
    users = []

    def __init__(self, name):
        if _instance is None:  # If the instance is not created, create it.
            self.name = name
            print(f"The social network {self.name} was created!")
        else:
            raise RuntimeError('Call instance() instead')  # An instance already exists. call instance() instead.

    def sign_up(self, name, password):  # Sign up to the social network.
        for user in self.users:         # Go over all the registered users.
            if user.name == name:       # Check if the name is already taken by other user.
                raise RuntimeError('name is not valid')
                # If the name is already taken, you can't create a new user with the same name.
        if 4 <= len(password) <= 8:
            newUser = User.User(name, password) # name and password are valid, create a new user.
            self.users.append(newUser)          # Add the new user to the list of users of the social network.
            return newUser
        else:
            raise RuntimeError('illegal password')

    def log_in(self, name, password):
        for user in self.users:                                    # Go over all the registered users.
            if user.name == name and user.password == password:    # Check if the name and password are
                user.log_in()                              # Perform log in (will change the connected status to True).

    def log_out(self, name):
        for u in self.users:
            if u.name == name:  # Go over all the registered users and find the user with the given name.
                u.log_out()     # Perform log out (will change the connected status to False).

    def __str__(self):  # Default print method to print the social network parameters.
        str_net = f"{self.name} social network:"
        for user in self.users:
            str_net += "\n" + user.__str__()    # Add the user's string representation to the returned string.
        return str_net
