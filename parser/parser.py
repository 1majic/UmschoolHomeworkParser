from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from selenium_starter import StartUrlDriver
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
from utils import Classes
import os

last_messages_ids = {}


def get_url_drive(url, less_name, cookie, proxy=None):
    driver = StartUrlDriver("https://umschool.net/", proxy, less_name)
    print("Загрузка 1")
    for cookie in pickle.load(open("cookies", "rb")):
        # for cookie in pickle.load(cookie):
        driver.add_cookie(cookie)

    time.sleep(1)
    print("Запуск страницы")
    driver.get(url)

    return driver


def get_homework_from_url(url, less_name, cookie, proxy=None):
    driver = get_url_drive(url, cookie, proxy, less_name)  # https://umschool.net/homework/submissions/69541650/
    homework_exercise = driver.find_element(By.CLASS_NAME, "homework-exercise")
    homework_title = homework_exercise.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "h1").text
    hm = Classes.Homework(name=homework_title)
    tasks = homework_exercise.find_elements(By.CLASS_NAME, "exercise-item")
    completed_tasks = []
    for i in tasks:
        num = str(i.get_attribute("data-loop-counter"))
        parts = i.find_element(By.CLASS_NAME, "fr-view").find_elements(By.TAG_NAME, "p")
        data = []
        for part in parts:
            img = part.find_elements(By.TAG_NAME, "img")
            if not img:
                data.append(part.text)
            else:
                data.append(img[0].get_attribute("src"))

        AnswerBlock = driver.find_element(By.CLASS_NAME, "mt-3").find_element(By.TAG_NAME, "input").get_attribute("name")
        if AnswerBlock == "text-answer":
            taskType = "text-answer"
            variants = []

        elif AnswerBlock == "variant":
            taskType = "variant"
            variants = [{"num": x + 1,
                         "text": j,
                         "correct": None} for x, j in enumerate(driver.find_element(By.CLASS_NAME, "mt-3").find_elements(By.TAG_NAME, "input"))]

        hm.AddTask(Classes.Task(taskNum=num, taskType=taskType, Data=data, variants=variants))
    return hm


async def get_homework_from_pdf(path):
    try:
        pass
    except Exception as e:
        pass


if __name__ == '__main__':
    hm = get_homework_from_url(url="https://umschool.net/homework/submissions/69541650/",
                                cookie=open("cookies", "rb"),
                                less_name="Тест")
    input()
