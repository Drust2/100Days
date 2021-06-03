import requests
class Questions:
    
    def __init__(self):
        self.response = requests.get(url="https://opentdb.com/api.php?amount=50&category=15&type=boolean")
        self.response.raise_for_status()
        self.question_data = self.response.json()["results"]
        

