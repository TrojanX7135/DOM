import pyttsx3

print("Pass: ")
passWord = input()
while passWord != "1111" :
    print("Password False !")
    print("Pass:")
    passWord = input()

print("Your name: ")
ten = input()

you = input()
while you != "exit" :
    #try:
        you = input()
        if you == "":
            trojan_brain = "I can't hear you"
        if you == "hello":
            trojan_brain = "hello Boss, I'm hear"
        if you == "who are you":
            trojan_brain = "I'm Trojan, slave of you"
        if you == "do you know me":
            trojan_brain =  "You is" + ten +" , my Master"
    #except:
        #trojan_brain =  "I don't understand, what's happend ?"


    print(trojan_brain)

    trojan_mount = pyttsx3.init() #thông số vào
    trojan_mount.say(trojan_brain) #kích hoạt nói
    trojan_mount.runAndWait()