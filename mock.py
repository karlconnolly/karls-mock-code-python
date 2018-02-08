#The websites I used for help are stackoverflow.com, w3schools.com and pythoncentral.io

while True:

    from time import sleep
    import winsound
    import urllib
    #urllib opens up urls

    class Mood:
        happy = "name1"
        sad = "name2"
        scared = "name3"

    print("Welcome to my Mock Code.")
    sleep(2)
    print("We will be going over all the code that I have learned since 1st Year")
    print("including some new code!")
    sleep(4)
    print("Let's listen to some music!")
    sleep(2)

    mood = input("What mood are you in, happy, sad, or scared?: ")
    print("Now playing the", mood, "song twice!");
#I used inputs and classes for the user to choose their song
    if mood == "happy":
        for x in range(0, 2):
            winsound.PlaySound('happy.wav', winsound.SND_FILENAME)

    elif mood == "sad":
        for x in range(0, 2):
            winsound.PlaySound('sad.wav', winsound.SND_FILENAME)

    elif mood == "scared":
        for x in range(0,2):
            winsound.PlaySound('scared.wav', winsound.SND_FILENAME)
#I used for loops and winsound for the song to play twice 



    else:
        print("That is not a mood that I know.")

    
    sleep(1)
    print("Now, onto my github website!")
    sleep(1)
    urllib.request.urlopen(karlmock.github.io)
    
