import wolframalpha 
import wikipedia   #these two module- wikipedia and wolframalpha, will be using to answer the question
from tkinter import *
import speech_recognition as sr

"""
The condition like- hello, how are u etc, comes under the condition of wolframealpha.
The condition like- tell me about bill gates, comes under the condition of wikipedia.
"""

while True:
	r = sr.Recognizer()  #creating an object for recognising the speech

	with sr.Microphone() as source:  #considering microphone as a source
		print("Listening.....")
		audio = r.listen(source) #r is an object of speech_recogniser, storing the souce voice in audio variable
		try:
			print("Regognizing....")
			text = r.recognize_google(audio)  #converting "speech into text" using google recognizer
			print('You said: ' + text)
			if text == "stop":   #if user says stop
				print("Program will exit.")
				break   #out of loop
			else:
				root = Tk()  # tkinter UI will Open 
				root.geometry("700x600")  #giving length and heigth to the UI 
				try:  #for wolframealpha
					app_id = "TLRLXJ-T9J4KKGAH8" #app id, will generate ot rom the website Wolframalpha
					client = wolframalpha.Client(app_id) #here we are genetrating client id....app_id is just an api of wolframalpha
					res = client.query(text) #generating answer
					answer = next(res.results).text#converting answer into text
					print("Answer from Wolfram|Alpha:")
					print(answer) #this answer will be shown in the terminal window
					label1 = Label(root, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')#UI ME DIKHANE KE LIYE
					label1.pack() #packing the label of UI
					root.after(5000, lambda: root.destroy()) #tkinter window will be destroid after certain amount of time
					mainloop()
				except Exception as e:
					print("No results from Wolfram|Alpha. Trying wikipedia...") #for wikipedia
					answer = wikipedia.summary(text)
					print("Answer from Wikipedia:")
					print(answer) #will be shown in terminal window
					label1 = Label(root, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					root.after(500000, lambda: root.destroy())
					mainloop()
		except Exception as e:
			print(e)
			answer = "Sorry we cannt hear you"
			print(answer)