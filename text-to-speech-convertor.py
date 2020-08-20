import pyttsx3

engine = pyttsx3.init()   #object creation
speech = input("Say Something : ")
engine.say(speech)
engine.runAndWait()


