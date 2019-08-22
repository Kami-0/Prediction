from datetime import datetime as dt
from prediction import prediction as pred 

#Преобразование в html код Head
def generateHead(title):
	head = f"<meta charset='utf-8'><title>{title}</title>"
	return f"<head>{head}</head>"

#Преобразование в html код Body
def generateBody (header,parag):
	body =f"<h1>{header}</h1>"
	for i in parag:
		body+=f"<p>{i}</p>"
	body+='<hr/><a href ="about.html">О реализации</a>&nbsp;<p><a href ="ksu.html">Для моей Ксюши ღ</a></p>'
	return f"<body>{body}</body>"

#Преобразование в html код Page
def generatePage(head, body):
	page = f"<html>{head}{body}</html>"
	return page

#Сохраним в фаил весь код
def savePage(title, header, parag, output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generatePage(
		head=generateHead(title),
		body=generateBody(header=header, parag=parag)
		)
	print(page, file=fp)
	fp.close()


#######################

today=dt.now().date()

savePage(
	title="Prediction",
	header=f"Что готовит нам {today}",
	parag=pred()
	)