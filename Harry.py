from sys import exit

first_name = input("""What is your name again?
First name: """)
last_name = input("Last name: ")

input("\n")
input("Okay, quick description of the game")
input("""You will have to type in words in the game.
This makes the game a tad more interesting,
and you can die""")
input("So be cautious\n")

input("Sweats ooze into your newly bought robe")
input("Your feet tip toe to the ground anxiously")

def sortingHat():
    print(f"Finally the sorting hat calls '{first_name} {last_name}'")
    input()
    print("""Which situation do you prefer more?
    1. Talking with friends in the hall
    2. Going to an adventure in the woods
    3. Getting good grades in your N.E.W.T
    4. Reading your favorite book""")

    consider1 = 0
    while(consider1 != '1' and consider1 != '2' and consider1 != '3' and consider1 != '4'):
        consider1 = (input(">"))

    print("""Which attribute do you like best?
    1. Well if I know no fear...
    2. If only I know everything there is to know
    3. To always do the right thing
    4. To be great of course""")

    consider2 = 0
    while(consider2 != '1' and consider2 != '2' and consider2 != '3' and consider2 != '4'):
        consider2 = (input(">"))

    print("""What are you?
    1. Muggleborn - Our ministry of magic is a muggleborn
    2. Halfblood - The most powerful wizard ever lived is a halfblood
    3. Pureblood - The most talented wizards are purebloods""")

    consider3 = 0
    while(consider3 != '1' and consider3 != '2' and consider3 != '3' and consider3 != '4'):
        consider3 = (input(">"))
    print("""Which house do you want to be sorted into?
    1. Gryffindor
    2. Hufflepuff
    3. Ravenclaw
    4. Slytherin""")

    consider4 = 0
    while(consider4 != '1' and consider4 != '2' and consider4 != '3' and consider4 != '4'):
        consider4 = (input(">"))

    if (consider1 == '2' and consider2 == '1' or (consider4 == '1' and consider2 == '1')):
        print("Gryffindor!")
        house = "Gryffindor"
        founder = "Godrick Gryffindor"
        headTeacher = "Prof. Longbottom"

    elif (consider1 == '4' and consider2 == '2' or (consider4 == '3' and consider2 == '2')):
        print("Ravenclaw!")
        house = "Ravenclaw"
        founder = "Rowena Ravenclaw"
        headTeacher = "Prof. Warbeck"

    elif (consider1 == '3' and consider2 == '4' and consider3 != '1' or (consider4 == '4' and consider3 != '1')):
        print("Slytherin!")
        house = "Slytherin"
        founder = "Salazar Slytherin"
        headTeacher = "Prof. Zul"

    else:
        print("Hufflepuff!")
        house = "Hufflepuff"
        founder = "Helga Hufflepuff"
        headTeacher = "Prof. Warrington"

    print(f"The house of {house} clap their hands")
    input("A month later...")

    return(house)


def start():
    input("It was rowdy in the great hall\n")
    input("Newspapers are everywhere\n")
    input("You look around...\n")
    input("and everyone looks uneasy\n")
    input()
    input("Harry Potter theme starts\n")
    input("You have finished your first month at Hogwarts\n")
    room()

def dead(why):
    input(f"{why}\n")
    input("You died\n")
    exit(0)

def room():
    input(f"{first_name}, You are now in {house} common room\n")
    input("It is 9:55 pm")
    input("You have a choice to wander and explore wonderful Hogwarts\n")
    input("or perhaps go to sleep")
    input("and experience beautiful dreams that even Muggle can experience\n")
    input("What is your choice")

    while True:
        room = input(">")

        if "wander" in room:
            input("Lumos Maxima!\n")
            input("You start by going through the corridor\n")
            input("Ghosts were screaming at you to turn off the light\n")
            input("Until the caretaker of Hogwarts catches you in action\n")
            input("Detention!\n")
            detention()
        elif "sleep" in room:
            input("Good choice\n")
            input("You stayed out of trouble")

            if 'lytherin' in house:
                input("As expected for a Slytherin")
            elif 'ufflepuff' in house:
                input("Hufflepuff...always doing the right thing")
            elif 'ryffindor' in house:
                input("A bit weird for a Gryffindor")
            elif 'avenclaw' in house:
                input("Ravenclaw... always doing the smart thing")
            else:
                input()

            input("You have defence against the dark arts class tomorrow\n")
            input("Get some rest...\n")
            defenceClass()
        else:
            print("Try again")

def defenceClass():
    input("The next morning...\n")
    input("Prof. Warrington: Okay students, we are going to learn the stunning spell today\n")
    input("This stunning spell is used to...\n")
    input("You listen to Warrington attentively\n")
    input("After the class, you have a question for Prof. Warrington\n")
    input("But, he walked so fast that you can't catch him\n")
    input("You followed his fast pace to his office\n")
    input("He slammed the door before you could call his name\n")
    input("As you are about to knock...\n")
    input("You heard Prof. Warrington screaming and talking to himself\n")
    input("Let me go, let me go! He said\n")
    input("You feel afraid \n ")
    input("What are you going to do?\n")
    while True:
        war = input(">")

        if "barge" in war or "attack" in war or "get in" in war or "knock" in war or "open door" in war:
            input("Professor Warrington noticed you\n")
            input("Prof. Warrington: Diffindo!\n")
            dead("Your body is shreded into pieces\n")
        elif "flee" in war or "away" in war or "avoid" in war:
            input("You walked away\n")
            input("Because of this you start to avoid Prof. Warrington class\n")
            input("Hence, you get detention\n")
            detention()
        else:
            print("Try again")

def detention():
    input("\n")
    input("You and Hagrid walked into the forbidden forest\n")
    input("It was darker than you expected\n")
    input("The fog is ubiquitous\n")
    input("Suddenly\n")
    input("A swarm of Arachnids rushed into you\n")
    input("You have to cast a spell\n")
    while True:
        forestSpell = input(">")
        if "tupefy" in forestSpell or "ictumsempra" in forestSpell:
            input("You stun some of the arachnids\n")
            input("and you take your chance to run\n")
            dragon()
        elif "rania" in forestSpell or "edavra" in forestSpell:
            input("You kill some of arachnids\n")
            input("and you take your chance to run\n")
            dragon()
        elif "protego" in forestSpell or "pelliarmus" in forestSpell:
            input("No effect to the arachnids\n")
            dead("You become arachnids' dinner")
        else:
            print("Try again")

def dragon():
    input("You ran out of stamina\n")
    input("Whilst breathing heavily, you notice a huge shadow lurking about\n")
    input("As you looked above the sky, you see a Ukranian Ironbelly dragon right above you\n")
    input("It landed right in front of you\n")
    input("What are you going to do?\n")
    while True:
        dragonFirst = input(">")
        if "attack" in dragonFirst or "kill" in dragonFirst:
            input("You cast Stupefly to the dragon\n")
            input("It has no effect whatsoever\n")
            input("The dragon breathes fire right to you\n")
            dead("You are now nothing but ashes\n")
        elif "stay" in dragonFirst or "quiet" in dragonFirst or "stand" in dragonFirst:
            input("You stand there unmoving\n")
            input("The dragon bows to you\n")
            finish()
        else:
            print("Try again\n")

def finish():
    input("This is the end of chapter 2\n")
    input("Thank you for playing\n")
    input("To be continued\n")
    exit(0)

house = sortingHat()
start()
