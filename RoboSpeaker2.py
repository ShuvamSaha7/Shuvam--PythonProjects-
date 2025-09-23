import win32com.client #Import the win32.client module allows python to use windows COM objects,icluding the Speech API

if __name__ == "__main__":

    print("Welcome to Robospeaker 2.0 (win32com version). Created by Shuvam")

    speaker = win32com.client.Dispatch("SAPI.SpVoice") # Creates a Speech API (SAPI) voice object provided by windows
                                                       # SAPI.SpVoice is the built in windows text to speech engine
    speaker.rate = 0  #Rate property(-10 to 10)

    speaker.volume = 100 #Volume property (0 to 100)

    while True:

        text = input("Enter what you want me to pronounce or type 'exit' to quit: ")

        if text.lower() == "exit":

            speaker.Speak("Goodbye!") #say goodbye before quitting

            break

        else:

            speaker.Speak(text) #The program converts the entered text to speech and speaks it out loud