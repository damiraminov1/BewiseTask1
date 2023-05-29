import requests
import json


class JServiceAPI:
    @staticmethod
    def get_random_quizz_questions(count: int) -> list[dict]:
        try:
            r = requests.get(f"https://jservice.io/api/random?count={count}")
            r.raise_for_status()
        except Exception:
            raise ConnectionError
        else:
            return json.loads(r.text)
