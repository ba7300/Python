'''
                             Healthy Programmer

(9.AM - 5.PM)

Water - water.mp3 (3.5 litres) - Drank - log
Eyes - eyes.mp3 - every 30 minute - EyDone - log
Physical - physical.mp3 - every 45 min - ExDone - log
 
'''
from pip import main
from pygame import init, mixer
from datetime import datetime
from time import time



def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input(" Enter the command: ") 
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("my_logs.txt",'a') as f:
        f.write(f"{msg} :[{datetime.now()}] \n")



if __name__=="__main__":

    # Customize Variables:
    waterMus = 'Water_Drip.mp3'
    eyesMus = 'Ocean_Eyes.mp3'
    physicalMus = 'Time_to_Exercise.mp3'

    input_name = input(" \n Please Enter your name:")
    print(f"\nGood Morning Mr.{input_name.capitalize()}, \nWelecome to office. Have a Great Day.")

    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersec = 40*60    #10
    eyesecs  = 45*60    #15
    exersecs = 30*60    #20

    while True:

        if time() - init_water > watersec:
            print("\n Water drinking time. Enter 'd' to stop the alarm.")
            musiconloop(waterMus,'d')
            init_water = time()
            log_now("Drank water at")

        if time() - init_eyes > eyesecs:
            print("\n Eye exercise time. Enter 'e' to stop the alarm.")
            musiconloop(eyesMus,'e')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exersecs:
            print("\n physical activity time. Enter 'p' to stop the alarm.")
            musiconloop(physicalMus,'p')
            init_exercise = time()
            log_now("Physical activity done at")