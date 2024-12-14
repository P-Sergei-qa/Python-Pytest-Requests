import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "158095",
    "name": "Python",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "158095"
}

#Регистрация тренера
respons = requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
print(respons.text)

#Подтверждение почты
respons_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(respons_confirmation.text)

#Создание покемона
respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.text)

#Смена имени покемона
respons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(respons_change.text)


#Поймать покемона в покебол
respons_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(respons_catch.text)

#Попросим программу вывести значение переменной pokemon_id
pokemon_id=respons_create.json()['id']
print(pokemon_id)

#Или запишем значение сообщения полученного
message=respons_create.json()['message']
print(message)


