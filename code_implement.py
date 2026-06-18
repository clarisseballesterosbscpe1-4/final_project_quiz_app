from abc import ABC, abstractmethod

# INHERITANCE

class User:

    def __init__(self, name):
        self.name = name

class Player(User):

    def __init__(self, name):
        super().__init__(name)
        self.score = 0