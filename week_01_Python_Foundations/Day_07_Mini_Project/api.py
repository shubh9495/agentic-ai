import requests



class AIClient:
    def __init__(self, api_url:str):
        self.api_url = api_url
    def ask(self, question:str)->dict:
        response = requests.post(
            self.api_url,
            json={
                "question":question
            }
        )
        requests.raise_for_status()
        return response.json()