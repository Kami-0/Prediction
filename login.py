from db import list_users, query_user_last_seen
from datetime import datetime as dt
from datetime import timedelta as tDelta

timeToSleep=2
listUsers=list_users()


#Проверяем корректность email
def validLogin ():
	count=3
	email = input ("Введите логин у вас 3 попытки: ")
	while  email.find("@") == -1 :
		print("ancorret email")
		if count == 1:
			print("Подождите 10 сек..")
			time.sleep(timeToSleep)
			count=4
		else:
			count=count-1	
			print( f"Введите логин у вас {count} попытки: " )
			email = input()	
	print("success")
	return email

#Отделить от email доменую часть
def getLogin (email):
	login = email.split("@")[0].lower()
	return login

#Проверить заходил ли юзер меньше, чем 180 дней
def checkUserIsActive(login):
	delta=dt.now()-query_user_last_seen(login)<tDelta(days=180)
	return delta

#Существует ли юзер в БД
def validDb (login):
	for name in listUsers:
		if name[0] == login and checkUserIsActive(login):
			future = dt.now()+tDelta(days=180)
			print("Ваш аккаунт действителен до", future)
			break
		else:
			print("Вы с нами совсем недавно! Добро пожаловать")
			break
	return 0

