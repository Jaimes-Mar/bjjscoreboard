from threading import Timer
def menu():
    print("[1] custom option in seconds.")
    print("[2] 5 minuite option")
    print("[0] exit")


def scoreboard():
    def endscreen():
        print("\n")
        print("---------------")
        print("Match has ended")
        print("Final score is ")
        print("Red corner score: " + str(Rcorner))
        print("Blue corner score: " + str(Bcorner))
        print('type "quit" to return to menu')
    Bcorner=0

    Rcorner = 0
    endtime_input= int(input("enter seconds: "))
    t=Timer (endtime_input,endscreen)
    t.start()
    print("COMBATE")
    while True:
        user_input = input('Enter a number: ')
        if user_input == 'a':
            print('plus 1 red')
            Rcorner+=1
            print("Red corner score: " + str(Rcorner))
        elif user_input == 'j':
            print('plus 1 blue')
            Bcorner+=1
            print("Blue corner score: " + str(Bcorner))
        elif user_input == 'quit':
            t.cancel()
            print("\n")
            print("----------------------------------")
            print("Final score is: ")
            print("Red corner score: " + str(Rcorner))
            print("Blue corner score: " + str(Bcorner))
            print('User typed "quit"...closing program')
            break
        else:
            print("invalid input,  try again")

def FiveMins():
    def endscreen():
        print("\n")
        print("---------------")
        print("Match has ended")
        print("Final score is ")
        print("Red corner score: " + str(Rcorner))
        print("Blue corner score: " + str(Bcorner))
        print('type "quit" to return to menu')
    Bcorner=0

    Rcorner = 0
    endtime_input= 300
    t=Timer (endtime_input,endscreen)
    t.start()
    print("COMBATE")
    while True:
        user_input = input('Enter a number: ')

            # 👇️ Exit when user presses Enter with empty input
        if user_input == 'a':
            print('plus 1 red')
            Rcorner+=1
            print("Red corner score: " + str(Rcorner))
        elif user_input == 'j':
            print('plus 1 blue')
            Bcorner+=1
            print("Blue corner score: " + str(Bcorner))
        elif user_input == 'quit':
            t.cancel()
            print("\n")
            print("----------------------------------")
            print("Final score is: ")
            print("Red corner score: " + str(Rcorner))
            print("Blue corner score: " + str(Bcorner))
            print('User pressed quit...closing program')
            break
        else:
            print("invalid input,  try again")



menu()
option= (input("you selected: "))
while option != "0":
    if option == '1':
        scoreboard()
    if option == '2':
        FiveMins()
    else:
        print("invalid option")
    menu()
    option= (input("you selected "))
print("Thank you ... program closing")        
