import requests
import pytest

#assert - я утверждаю,что ответ на этот запрос
# Переменные:
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '21759'

#Тест на cравнение статуса
def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

#Тест на сравнение какой то части ответа, что строчка содержит имя со значением Бульбазавр
def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    #я утверждаю,что ответ на этот запрос? его json содержит имя со значением Бульбазавр.
    assert response_get.json()["data"][0]["name"]=='Бульбазавр'

#Тест, что строчка содержит имя моего тренера (ID 21759) Post12
def test_part_of2_response():
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    #я утверждаю,что ответ на этот запрос, его json содержит имя тренера Post12
    assert response_get.json()["data"][0]["trainer_name"]=='Post12'

#Создали текстуру, обозначили какие параметры будем передавать, в [] передаем значения этих параметров. 
@pytest.mark.parametrize('key, value', [('name','Бульбазавр'), ('trainer_id',TRAINER_ID), ('id','158095')])
#Пишем конву, в которые будут передаваться эти параметры
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    #я утверждаю, что d json в ответе на запрос за списком покемонов у нас есть дата[внутри массив 1 элемент] и по ключу есть значение
    assert response_parametrize.json()["data"][0][key] == value
