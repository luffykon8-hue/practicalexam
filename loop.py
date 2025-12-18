# int
age = 25
print(age + 5)

# float
price = 99.99
tax = price * 0.18
print(tax)

# str
name = "Python"
print(name.upper())

# list (mutable, ordered)
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

# tuple (immutable, ordered)
coordinates = (10, 20)
print(coordinates[0])

# set (unique, unordered)
numbers = {1, 2, 2, 3}
print(numbers)  # duplicates removed

# dict (key-value pairs)
student = {"name": "Alex", "age": 21}
print(student["name"])

# 🔁 Looping Constructs
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 3:
    print(count)
    count += 1

# Nested loop
for i in range(2):
    for j in range(3):
        print(i, j) 
        # 0 0 
        # 0 1
        # 0 2
        # 1 0
        # 1 1 
        # 1 2

# Python Modules
# os
import os

from sqlalchemy import JSON
print(os.getcwd())

# sys
import sys
print(sys.argv)

# datetime
from datetime import datetime
print(datetime.now())

# logging
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")

# argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()

print(f"Hello {args.name}")

# OOP Concepts
# Class and Object
class Car:
    def start(self):
        print("Car started")

c = Car()
c.start()

# Inheritance
class Vehicle:
    def move(self):
        print("Moving")

class Bike(Vehicle):
    pass

b = Bike()
b.move()

# Polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()

# Exception Handling
# try-except
try:
    x = int("abc")
except ValueError:
    print("Conversion error")

# Handling JSON & CSV
# JSON
import json

data = {"name": "John", "age": 30}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    print(json.load(f))

# CSV
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["John", 30])

# 🔐 Security Measures in SDLC (Example)
# • Input validation
# • Password hashing (bcrypt)
# • Secure API keys via environment variables
# • HTTPS
# • Regular security testing
# Example:

import os
SECRET_KEY = os.getenv("SECRET_KEY")

#  Flask Basics
# Simple Flask App
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

app.run(debug=True)

# 🔍 SAST vs DAST
# SAST (Static):
# • Code analysis
# • Finds issues early
# • Example: Bandit

# DAST (Dynamic):
# • Tests running app
# • Finds runtime vulnerabilities
# • Example: OWASP ZAP

# 🔄 CI/CD Pipeline (Simple Flow)
# 1. Developer pushes code
# 2. CI runs tests & linting
# 3. Security scan (SAST)
# 4. Build & deploy


# Example GitHub Actions:
# name: CI
# on: [push]
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - run: python -m unittest

# 🗄 Database Connectivity in Flask
# Flask + SQLite
from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("app.db")

@app.route("/users")
def users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return str(cursor.fetchall())