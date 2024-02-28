import User

# Will be used to create only one instance of the SocialNetwork.
_instance = None
net_name = ""


class SocialNetwork:
    """
    this class represents a social network.
    """
    users = []

    @staticmethod
    def instance():
        """
        this func is a static method that returns the instance of the social network.
        :return: the instance of the social network
        """
        return _instance

    def __new__(cls, name):
        """
        this func is a singleton implementation of the social network class.
        It will create only one instance of the social network.
        """
        global _instance
        global net_name
        if net_name == "":  # If the _instance is not created, create it.
            _instance = super(SocialNetwork, cls).__new__(cls)
            return _instance
        else:
            return SocialNetwork.instance()

    def __init__(self, name):
        """
        this func is a constructor for the social network.
        it uses the singleton implementation which is implemented in the __new__ method.
        :param name: the name of the social network.
        """
        global net_name
        if net_name == "":
            net_name = name
            print(f"The social network {net_name} was created!\n")

    def sign_up(self, name, password):  # Sign up to the social network.
        """
        this func signs up a new user to the network.
        param name: the new user's name
        param password: the new user's password
        return: the new user
        """
        for user in self.users:  # Go over all the registered users.
            if user.name == name:  # Check if the name is already taken by other user.
                raise RuntimeError('name is not valid')
                # If the name is already taken, you can't create a new user with the same name.
        if 4 <= len(password) <= 8:
            newUser = User.User(name, password)  # name and password are valid, create a new user.
            self.users.append(newUser)  # Add the new user to the list of users of the social network.
            return newUser
        else:
            raise RuntimeError('illegal password')

    def log_in(self, name, password):
        """
        this func allows an existed user to log in from the network
        param name: name of the user who wants to log in
        param password: password of the user who wants to log in
        """
        for user in self.users:  # Go over all the registered users.
            if user.name == name and user.password == password:  # Check if the name and password are
                user.log_in()  # Perform log in (will change the connected status to True).

    def log_out(self, name):
        """
        this func allows an existed user to log out from the network
        param name: name of the user who wants to log in
        """
        for u in self.users:
            if u.name == name:  # Go over all the registered users and find the user with the given name.
                u.log_out()  # Perform log out (will change the connected status to False).

    def __str__(self):
        """
        this func is a Default print method to print the social network parameters.
        """
        str_net = f"{net_name} social network:"
        for user in self.users:
            str_net += "\n" + user.__str__()  # Add the user's string representation to the returned string.
        return str_net
