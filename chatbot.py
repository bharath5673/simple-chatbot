import random
import time
import datetime

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?','wassup']
responses = ['Okay',"I'm fine",'nothing much']
random_response = random.choice(responses)

question1 = ['time?','what is time',]
responses1 =("now the time is ",time.asctime())
random_responses1 = random.choice(responses1)


while True:
	userInput = input(">>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	elif userInput in question1:
		print (random_responses1)
	elif userInput == 'quit':
		break
	else:
		print("I did not understand what you said")