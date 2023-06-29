import pyttsx3 #import the library

def textToVoice():
    eng = pyttsx3.init('sapi5') #initialize an instance
    eng.say("This is a demonstration of how to convert text to voice using pyttsx3 library in python.") #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command

if __name__ == "__main__":
    textToVoice()