"""
4. Напиши функцию на Python, которая возвращает текущий
публичный IP-адрес компьютера
(например, с использованием сервиса ifconfig.me)
"""
import requests

response = requests.get('https://ifconfig.me/')
print(response.text)
