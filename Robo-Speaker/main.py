import os
if __name__ == '__main__':
    print("welcome to robo speaker 1.1.Created by Karan")
    while True:
        x = input("enter what you want to say: ")
        if x == "q":
            break
        command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
        os.system(command)





















    #  PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hello');"