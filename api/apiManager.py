import requests

class ApiManager:
    BASE_URL = "https://rickandmortyapi.com/api/character/"

    def obtener_personaje_api(self, personaje_id):
        url = f"{self.BASE_URL}{personaje_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None