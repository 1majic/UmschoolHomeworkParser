import os
import sqlite3

from sqlalchemy import create_engine

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def make_file(user, password, file):
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user=user, password=password)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    sql_create_database = cursor.execute(f'create database {file}')
    # Закрываем соединение
    cursor.close()
    connection.close()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def addHomework(self, name, checked, tasks):
        with self.connection:
            self.cursor.execute("INSERT ", (name, checked, tasks))

    def addTask(self, taskNum, taskType, Data, variants, correct, answer):
        with self.connection:
            self.cursor.execute("INSERT ", (taskNum, taskType, Data, variants, correct, answer,))

    def delHomework(self):
        pass

    def delTask(self):
        pass

    def addAnswer(self):
        pass