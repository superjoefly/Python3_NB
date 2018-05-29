#####################
# Objects and Classes
#####################


def main():
    """Example of Class and Object Creation"""
    # Class creation:
    class Enemy:
        """This is the enemy class"""
        life = 3

        def attack(self):
            """This is the attack method of the enemy class"""
            self.life -= 1
            print("OUCH!!!")

        def check_life(self):
            """This is the check_life method of the enemy class"""
            if self.life <= 0:
                print("Enemy Dead!")
            else:
                print(self.life, 'life left!')


    # Creat two objects of the Enemy class:
    enemy1 = Enemy()
    enemy2 = Enemy()

    # Call check_life method of Enemy objects:
    enemy1.check_life()
    enemy2.check_life()

    print("------------")

    # Call attack method on the first enemy object:
    enemy1.attack()
    enemy1.attack()
    enemy1.attack()

    print("------------")

    # Call check_life method of Enamy objects:
    enemy1.check_life()
    enemy2.check_life()
    print("##################")





    #######################
    # Using the Init Method
    #######################

    # Create Animal Class:
    class Animal:
        """This the the Animal Class"""
        def __init__(self, name, type_of):
            self.name = name
            self.type_of = type_of

        def say_hello(self, hello):
            """Say Hello Method of Animal Class"""
            print(hello)



    # Object creation:
    fido = Animal('Fido', 'dog')
    squeaky = Animal('Squeaky', 'cat')

    # Call the say_hello method of the Animal class:
    fido.say_hello('Ruff Ruff!!!')
    squeaky.say_hello('Meow Meow!!!')
    print("##################")






    #############################
    # Class vs Instance Variables
    #############################
    # Create Animal Class:
    class Beast:
        """This is the Beast class"""

        # Default properties of class (class variables):
        legs = 4
        eyes = 2
        noise = 'Grrraawwww!!!'

        # Default methods of class:
        def make_noise(self):
            """Make Noise Method of Beast Class"""
            print(self.noise)

        # Instantiation of class (instance variables)
        def __init__(self, type_of, name):
            self.type_of = type_of
            self.name = name


    # Whatever you pass during object creation is
    # an instance variable:
    beasty = Beast('Monster', 'Grawl')
    monstey = Beast('Monster', 'Monstro')

    # Instance variable:
    print(beasty.type_of)
    print(beasty.name)
    print("-----------")
    print(monstey.type_of)
    print(monstey.name)


    # Class variables:
    print(beasty.legs)
    print(beasty.eyes)
    print("----------")
    print(monstey.legs)
    print(monstey.eyes)


    # Class method:
    beasty.make_noise()
    monstey.make_noise()
    print("##################")






    ######################
    # Object Inheritance
    ######################
    class Parent():
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def display_first_name(self):
            """Display First Name method of Parent Class"""
            print(self.first_name)

        def display_last_name(self):
            """Display Last Name method of Parent Class"""
            print(self.last_name)

    class Child(Parent):
        """Child Class"""
        def say_hello(self):
            """Say Hello Method of Child Class"""
            print("Hello There!")

        # Override last_name method of parent class:
        def display_last_name(self):
            """Display Last Name method of Child Class"""
            print("Whatever!!!")


    mom = Parent('Priscilla', 'Atwood')
    mom.display_first_name()
    mom.display_last_name()

    print("------------")

    joe = Child('Joseph', 'Atwood')
    joe.display_first_name()
    joe.display_last_name()

    print("##################")




    ########################
    # Multiple - Inheritance
    ########################

    class Mario():
        """Mario Class"""
        def __init__(self, life):
            self.life = life

        def move(self):
            """Move Method"""
            print("Mario moves around...")

        def gains_life(self):
            """Gains Life Method"""
            self.life += 3

    class Shroom():
        """Shroom Class"""
        def eat_shroom(self):
            """Eat Mushroom Method"""
            print("Mario get's bigger!")

    class FastMario():
        """Fast Mario Class"""
        def super_speed(self):
            """Super Speed Method"""
            print("Mario runs at super speed!!!")

    # Inherits from multiple classes:
    class SuperMario(Mario, Shroom, FastMario):
        """Super Mario Class"""
        pass

    # Creat object:
    mario1 = SuperMario(5)

    # Has access to methods of parent classes:
    print(mario1.life)
    mario1.move()
    mario1.eat_shroom()
    mario1.gains_life()
    print(mario1.life)
    mario1.super_speed()


main()
