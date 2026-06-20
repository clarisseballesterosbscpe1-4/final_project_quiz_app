# Quiz App OOP

## Project Overview

This project is a Python-based Quiz Application that demonstrates the four fundamental Object-Oriented Programming (OOP) principles:

* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

The application allows users to answer True/False questions and receive a final score at the end of the quiz.

This project was modified from an existing GitHub project to demonstrate how OOP concepts can be applied in a real-world application.

---

## Original Source

Original Project Repository:

https://github.com/garimasingh128/awesome-python-projects/tree/master/QUIZ%20APP

The original project was enhanced to demonstrate additional OOP principles required for this activity.

---

## Objectives

The objective of this project is to:

1. Analyze an existing Python project.
2. Identify implemented OOP principles.
3. Implement missing OOP principles.
4. Demonstrate the concepts through code execution and documentation.
---

# Features

* Interactive quiz system
* Score tracking
* Multiple questions
* User roles
* Object-Oriented Programming implementation

---

# OOP Principles Implemented

## 1. Encapsulation

Encapsulation is the process of combining data and methods inside a class while restricting direct access to the data.

Example:

```python
class Player(User):

    def __init__(self, name):
        super().__init__(name)
        self._score = 0

    def add_score(self):
        self._score += 1

    def get_score(self):
        return self._score
```

Implementation:

* The player's score is stored in `_score`.
* The score can only be modified through `add_score()`.
* The score can only be accessed through `get_score()`.

Benefits:

* Protects data from accidental modification.
* Improves maintainability.

---

## 2. Inheritance

Inheritance allows a child class to acquire the properties and methods of a parent class.

Example:

```python
class User:
    def __init__(self, name):
        self._name = name


class Player(User):
    def __init__(self, name):
        super().__init__(name)
        self._score = 0
```

Implementation:

* `Player` inherits from `User`.
* `Admin` also inherits from `User`.
* Common functionality is reused rather than duplicated.

Benefits:

* Reduces code duplication.
* Improves code reusability.

---

## 3. Polymorphism

Polymorphism allows multiple classes to use the same method name while producing different results.

Example:

```python
class Admin(User):

    def display_role(self):
        print(f"{self._name} is an Administrator")


class Player(User):

    def display_role(self):
        print(f"{self._name} is a Quiz Player")
```

Implementation:

```python
for user in users:
    user.display_role()
```

Output depends on the object's class.

Benefits:

* Improves flexibility.
* Simplifies code maintenance.

---

## 4. Abstraction

Abstraction hides implementation details and only exposes essential functionality.

Example:

```python
from abc import ABC, abstractmethod

class QuizBase(ABC):

    @abstractmethod
    def still_has_questions(self):
        pass

    @abstractmethod
    def next_question(self):
        pass
```

Implementation:

```python
class QuizBrain(QuizBase):
```

The abstract class defines what a quiz must do, while the child class provides the actual implementation.

Benefits:

* Simplifies complex systems.
* Improves scalability.

---

# Program Flow

1. User enters a name.
2. A Player object is created.
3. Questions are loaded from `data.py`.
4. Question objects are created.
5. QuizBrain manages quiz execution.
6. Player answers questions.
7. Score is updated using encapsulated methods.
8. Final score is displayed.

---

# Sample Output

```text
=== QUIZ APPLICATION ===

Enter your name: Clarisse

Roles:
Professor is an Administrator
Juan is a Quiz Player

Q1: Python is a programming language? (True/False): True
Correct!

Current Score: 1

Q2: HTML is a programming language? (True/False): False
Correct!

Current Score: 2

Quiz Finished!

Clarisse, your final score is 2/2
```

---

# Technologies Used

* Python 3
* Object-Oriented Programming
* Git
* GitHub

---

# Author

Name: Clarisse A. BAllesteros

Course: BSCpE 1-4

Subject: Object-Oriented Programming


# Conclusion

The Quiz App successfully demonstrates the four core principles of Object-Oriented Programming:

* Encapsulation through protected data and getter methods.
* Inheritance through the User, Player, and Admin classes.
* Polymorphism through method overriding.
* Abstraction through the QuizBase abstract class.

These concepts improve code organization, reusability, maintainability, and scalability.
