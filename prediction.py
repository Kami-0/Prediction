import random as rt

def lists (fileName) :
	list=[]
	with open(fileName,'r',encoding = 'utf-8') as f:
		for line in f:
			list.append(line.replace("\n",""))
	return list

times = lists(fileName="times.txt")
advices = lists(fileName="advices.txt")
promises = lists(fileName="promises.txt")
phraza=[]

def prediction () :
	for i in range(0,5) :
		rTimes=times[rt.randrange(0,len(times))]
		rAdvices=advices[rt.randrange(0,len(advices))]
		rPromises=promises[rt.randrange(0,len(promises))]
		phraza.append(f"{rTimes.title()} {rAdvices} {rPromises}.")
	return phraza
