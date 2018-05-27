# # Objects and Classes
#
# def main():
#     """This is a function docstring"""
#     # Class creation:
#     class Enemy:
#         """This is the enemy class"""
#         life = 3
#
#         def attack(self):
#             """This is the attack method of the enemy class"""
#             self.life -= 1
#             print("OUCH!!!")
#
#         def check_life(self):
#             """This is the check_life method of the enemy class"""
#             if self.life <= 0:
#                 print("Enemy Dead!")
#             else:
#                 print(self.life, 'life left!')
#
#
#     # Creat two objects of the Enemy class:
#     enemy1 = Enemy()
#     enemy2 = Enemy()
#
#     # Call check_life method of Enamy objects:
#     enemy1.check_life()
#     enemy2.check_life()
#
#     print("------------")
#
#     # Call attack method on the first enemy object:
#     enemy1.attack()
#     enemy1.attack()
#     enemy1.attack()
#
#     print("------------")
#
#     # Call check_life method of Enamy objects:
#     enemy1.check_life()
#     enemy2.check_life()
#
#
# main()




# # Objects and Classes (Init Method)
# def main():
#     """This is a function docstring"""
#     # Class creation:
#     class Animal:
#         """This the the animal class"""
#         def __init__(self, name, type):
#             self.name = name
#             self.type = type
#
#         def say_hello(self, hello):
#             print(hello)
#
#
#
#     # Object creation:
#     fido = Animal('Fido', 'dog')
#     squeaky = Animal('Squeaky', 'cat')
#
#     # Call the say_hello method of the Animal class:
#     fido.say_hello('Ruff Ruff!!!')
#     squeaky.say_hello('Meow Meow!!!')
#
# main()



# # Objects and Classes (Class vs Instance Variables)
# def main():
#     """This is a function docstring"""
#     # Class creation:
#     class Animal:
#         """This is the animal class"""
#
#         # Default properties of class (class variables):
#         legs = 4
#         eyes = 2
#
#         # Default methods of class:
#         def say_name(self):
#             print(self.name)
#
#         # Instantiation of class (instance variables)
#         def __init__(self, type_of, name):
#             self.type_of = type_of
#             self.name = name
#
#
#     # Whatever you pass during object creation is
#     # an instance variable:
#     fido = Animal('Dog', 'Fido')
#     blacky = Animal('Cat', 'Blacky')
#
#     # Instance variable:
#     print(fido.type_of)
#     print(fido.name)
#     print("-----------")
#     print(blacky.type_of)
#     print(blacky.name)
#
#     # Class variables:
#     print(fido.legs)
#     print(fido.eyes)
#     print("----------")
#     print(blacky.legs)
#     print(blacky.eyes)
#
# main()




# # Objects and Classes (Inheritance)
# def main():
#     """This is a function docstring"""
#
#     class Parent():
#         def __init__(self, first_name, last_name):
#             self.first_name = first_name
#             self.last_name = last_name
#
#         def display_first_name(self):
#             print(self.first_name)
#
#         def display_last_name(self):
#             print(self.last_name)
#
#     class Child(Parent):
#         def say_hello(self):
#             print("Hello There!")
#
#         # Override last_name method of parent class:
#         def display_last_name(self):
#             print("Whatever!!!")
#
#
#     mom = Parent('Priscilla', 'Atwood')
#     mom.display_first_name()
#     mom.display_last_name()
#
#     print("------------")
#
#     joe = Child('Joseph', 'Atwood')
#     joe.display_first_name()
#     joe.display_last_name()
#
# main()





# # Objects and Classes (Multiple - Inheritance)
# def main():
#     """This is a function docstring"""
#
#     class Mario():
#         def __init__(self, life):
#             self.life = life
#
#         def move(self):
#             print("Mario moves around...")
#
#         def gains_life(self):
#             self.life += 3
#
#     class Shroom():
#         def eat_shroom(self):
#             print("Mario get's bigger!")
#
#     class FastMario():
#         def super_speed(self):
#             print("Mario runs at super speed!!!")
#
#     # Inherits from multiple classes:
#     class SuperMario(Mario, Shroom, FastMario):
#         pass
#
#     # Creat object:
#     mario1 = SuperMario(5)
#
#     # Has access to methods of parent classes:
#     print(mario1.life)
#     mario1.move()
#     mario1.eat_shroom()
#     mario1.gains_life()
#     print(mario1.life)
#     mario1.super_speed()
#
# main()
