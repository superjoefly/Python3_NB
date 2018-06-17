"""Sort Objects by Attribute"""


# Import Modules:
from operator import attrgetter


# Define main:
def main():
    """The main function"""

    # Create the User class:
    class User:
        """User Class with two methods"""

        # Initialize objects with name and user_id:
        def __init__(self, name, user_id):
            self.name = name
            self.user_id = user_id

        # String representation of object:
        def __repr__(self):
            return self.name + ':' + str(self.user_id)

    # List of user objects:
    users = [
        User('John', 43),
        User('Craig', 5),
        User('Billy', 61),
        User('Gina', 2),
        User('Jessica', 8)
    ]

    # Display each user:
    for user in users:
        print(user)

    print("-----------------")

    # Display list of users sorted by name:
    for user in sorted(users, key=attrgetter('name')):
        print(user)

    print("-----------------")

    # Display list of users sorted by user_id:
    for user in sorted(users, key=attrgetter('user_id')):
        print(user)


# Call main:
main()
