import requests
from uuid import uuid4

class OnlineSms:
	def __init__(self):
		self.api = "https://api.online-receive-sms.com"
		self.headers = {
			"user-agent": "okhttp/4.9.0"
		}
		self.token = "g7UqlvemG4xQ56FOK9HeNprNmcJ9Js8f"

	def get_countries_list(self):
		data = {
			"token_auth": f"token{self.token}token"
		}
		return requests.post(
			f"{self.api}/countries",
			data=data,
			headers=self.headers).json()

	def get_random_number(self):
		data = {
			"token_auth": f"token{self.token}token"
		}
		return requests.post(
			f"{self.api}/numbers/random",
			data=data,
			headers=self.headers).json()

	def get_numbers_list(self, size: int = 5):
		data = {
			"token_auth": f"token{self.token}token"
		}
		return requests.post(
			f"{self.api}/numbers/{size}",
			data=data,
			headers=self.headers).json()

	def get_number_messages(self, number: int, size: int = 50):
		data = {
			"token_auth": f"token{self.token}token"
		}
		return requests.post(
			f"{self.api}/messages/{number}/{size}",
			data=data,
			headers=self.headers).json()

	def get_numbers_by_country(self, country_code: str):
		data = {
			"token_auth": f"token{self.token}token"
		}
		return requests.post(
			f"{self.api}/country/{country_code}/numbers",
			data=data,
			headers=self.headers).json()
