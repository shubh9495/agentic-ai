import requests

from models import Question_model
from api import AIClient


def main():
    user_input = input("ask a question")
    question = Question_model(
        question = user_input
    )
    client = AIClient(
        "url"
    )
    try:
        result = client.ask(
            question.question
        )

        print(result)
    except requests.RequestException:
        print("api failed...")

if __name__ == "__main__":
    main()