# function to allow user to continue loop or not

def con():

    cont = True

    while cont:
        val = input("\nWould you like to run another analysis (yes/no)? ")
        if val.lower() == "yes":
            return True
            cont = False
        elif val.lower() == "no":
            return False
            cont = False
        else:
            print("invalid value")

