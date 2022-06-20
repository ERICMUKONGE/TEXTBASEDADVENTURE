
def God():
    answer = input("Do you want to play this game:[yes/no]\n")
    if answer == "yes":
        print("Hope you know the second commandement")
        ask = input("Do you mind if i share it with you:[yes/no]\n")
        if ask == "yes":
            print("Love your neighbour as you love yourself")
            start = input("Do you really need any more explanation to this?[yes/no]\n")
            if  start == "yes":
                print("Imagine you in danger and everyone knows about it but just doesnot care, Is that real love?")
                name = input("Do you mind share this good news with others?[yes/no]\n")
                if name == "yes":
                    print("Thanks for spreading the good news")
                elif name == "no":
                    print("Imagine good news bypasses you how does it feel?")
            else:
                print("God will truly love if you share the message!")        
        elif ask == "no":
            print("Nevermind even failure is learning.\nLove your neighbour as you love yourself.Is the second commandement.")
        else:
            print("Please dont cheat yourself,learn something about God.")
    else:
        print("God is watching,please dont cheat yourself,learn something about him.")
God()