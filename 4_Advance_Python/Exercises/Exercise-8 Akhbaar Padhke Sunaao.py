'''
                            * Akhbaar Padhke Sunaao *
'''

import imp


def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == "__main__":
    speak("You are my best friend. I will never forget you in my life. You and me, we together can make a history.")
