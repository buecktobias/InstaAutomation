import json


class User:
    def __init__(self, name):
        self.name = name
        self.user_name = ""
        self.password = ""
        self.load()

    def load(self):
        auth = json.load(open("/home/tobias/PycharmProjects/InstaAutomation/credentials.json", 'r'))[self.name]["auth"]
        self.user_name = auth["userName"]
        self.password = auth["password"]


