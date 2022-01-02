"""
This file have somes
configurations for the project.
"""

from dotenv import load_dotenv
from os import environ

# loading the variable
load_dotenv()

PATH = environ['SQLITE_PATH']
DB_PATH = f'sqlite:///{PATH}'
