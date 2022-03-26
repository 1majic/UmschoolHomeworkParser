from ..db.init import db


class Homework:
    def __init__(self, name, checked=False):
        self.name = name
        self.checked = checked
        self.Tasks = []

    def AddTask(self, task):
        self.Tasks.append(task)

    def DelTask(self, index):
        self.Tasks.pop(index)


class Task:
    def __init__(self, taskNum, taskType, Data, variants=[], correct=None, answer=0):
        self.taskNum = taskNum
        self.taskType = taskType    # Может быть text-answer, variant
        self.Data = Data
        self.variants = variants
        self.correct = correct
        self.answer = answer

    def addToDb(self):
        db.addTask(self.taskNum, self.taskType, self.Data, self.variants, self.correct, self.answer)

    def addAnswersToDb(self, answer):
        pass

