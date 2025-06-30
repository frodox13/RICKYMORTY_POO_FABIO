import requests

class ApiManager:
    BASE_URL = "https://rickandmortyapi.com/api/"

    def obtener_personaje_api(self, personaje_id):
        url = f"{self.BASE_URL}character/{personaje_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def obtener_episodio_api(self, episodio_id):
        url = f"{self.BASE_URL}episode/{episodio_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def obtener_ubicacion_api(self, ubicacion_id):
        url = f"{self.BASE_URL}location/{ubicacion_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None