from abc import ABC, abstractmethod

# INHERITANCE

class User:

    def __init__(self, name):
        self.name = name

class Player(User):

    def __init__(self, name):
        super().__init__(name)
        self.score = 0

# POLYMORPHISM

class Admin:

    def display(self):
        print("Admin User")

class QuizPlayer:

    def display(self):
        print("Quiz Player")

users = [Admin(),QuizPlayer()]

for user in users:
    user.display()