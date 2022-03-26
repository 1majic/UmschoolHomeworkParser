from parser.parser import get_homework_from_url

print(get_homework_from_url(url="https://umschool.net/homework/submissions/69541650/",
                            cookie=open("cookies/1/cookies", "rb"),
                            less_name="Тест",
                            proxy=None))
