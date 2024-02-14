import User

# singleton
_instance = None


# Will be used to create only one instance of the SocialNetwork.
# return this instance if someone tries to create new social network
def instance():
    return _instance


class SocialNetwork:
    """
    this class represent a social network.
    """
    users = []

    def __init__(self, name):
        """
        this func is a constructor for the social network.
        **this func implements the singleton design pattern.
        if the static instance of the social network is None,
        the construct will create a new social network with the given name.
        else, the constructor will raise an error that tells the user to call the func "instance" instead.
        param name: the name for the new social network
        """
        if _instance is None:  # If the instance is not created, create it.
            self.name = name
            print(f"The social network {self.name} was created!")
        else:
            raise RuntimeError('Call instance() instead')  # An instance already exists. call instance() instead.

    def sign_up(self, name, password):  # Sign up to the social network.
        """
        this func signs up a new user to the network.
        param name: the new user's name
        param password: the new user's password
        return: the new user
        """
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
        """
        this func allows an exist user to log in from the network
        param name: name of the user who want to log in
        param password: password of the user who want to log in
        """
        for user in self.users:                                    # Go over all the registered users.
            if user.name == name and user.password == password:    # Check if the name and password are
                user.log_in()                              # Perform log in (will change the connected status to True).

    def log_out(self, name):
        """
        this func allows an exist user to log out from the network
        param name: name of the user who want to log in
        """
        for u in self.users:
            if u.name == name:  # Go over all the registered users and find the user with the given name.
                u.log_out()     # Perform log out (will change the connected status to False).

    def __str__(self):
        """
        this func is a Default print method to print the social network parameters.
        """
        str_net = f"{self.name} social network:"
        for user in self.users:
            str_net += "\n" + user.__str__()    # Add the user's string representation to the returned string.
        return str_net
