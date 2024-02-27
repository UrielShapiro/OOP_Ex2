import User

# singleton
_instance = None


# Will be used to create only one instance of the SocialNetwork.


class SocialNetwork:
    """
    this class represent a social network.
    """
    users = []

    @staticmethod
    def instance():
        """
        this func is a static method that returns the instance of the social network.
        :return: the instance of the social network
        """
        global _instance  # This function returns the global variable _instance.
        return _instance

    def __new__(cls, name):
        """
        this func is a singleton implementation of the social network class.
        It will create only one instance of the social network.
        """
        global _instance  # This function changes the global variable _instance.
        if _instance is None:  # If the _instance is not created, create it.
            _instance = super(SocialNetwork, cls).__new__(cls)
        return _instance

    def __init__(self, name):
        """
        this func is a constructor for the social network.
        it uses the singleton implementation which is implemented in the __new__ method.
        :param name: the name of the social network.
        """
        self.name = name
        print(f"The social network {self.name} was created!")

    def sign_up(self, name, password):  # Sign up to the social network.
        """
        this func signs up a new users to the network.
        param name: the new users's name
        param password: the new users's password
        return: the new users
        """
        for user in self.users:  # Go over all the registered users.
            if user.name == name:  # Check if the name is already taken by other users.
                raise ValueError('name is not valid')
                # If the name is already taken, you can't create a new users with the same name.
        if 4 <= len(password) <= 8:
            new_user = User.User(name, password)  # name and password are valid, create a new users.
            self.users.append(new_user)  # Add the new users to the list of users of the social network.
            return new_user
        else:
            raise ValueError('illegal password')

    def log_in(self, name, password):
        """
        this func allows an existed users to log in from the network
        param name: name of the users who want to log in
        param password: password of the users who want to log in
        """
        for user in self.users:  # Go over all the registered users.
            if user.name == name and user.password == password:  # Check if the name and password are matching any
                # users.
                user.log_in()  # Perform log in (will change the connected status to True).

    def log_out(self, name):
        """
        this func allows an existed users to log out from the network
        param name: name of the users who want to log in
        """
        for u in self.users:
            if u.name == name:  # Go over all the registered users and find the users with the given name.
                u.log_out()  # Perform log out (will change the connected status to False).

    def __str__(self):
        """
        this func changes the default print method to print the social network parameters.
        """
        network_str = f"{self.name} social network:"
        for user in self.users:
            network_str += "\n" + user.__str__()  # Add the user's string representation to the returned string.
        return network_str
