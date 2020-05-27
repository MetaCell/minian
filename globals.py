import os

def initialize(path="./demo_movies"):
    global dpath
    if not path:
        path = "./demo_movies"
    dpath = os.path.abspath(path)
