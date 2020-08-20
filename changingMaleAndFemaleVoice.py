import pyttsx3

engine = pyttsx3.init()    #Object creation

#how many voices the pyttsx3 provides to you
# but you don't know the id no of those voices

sound = engine.getProperty('voices') #list of voices along with id
print(sound)

engine.setProperty('voice',sound[0].id)
engine.say("I will speak this text in male voice")

engine.setProperty('voice',sound[1].id)
engine.say("I will speak this text in female voice")
engine.runAndWait()