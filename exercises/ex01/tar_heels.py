"""An exercise in remainders and boolean logic."""

__author__ = "730333306"


# Begin your solution here...
var: int = input("Enter an int:")
if int(var) % 2 == 0 or int(var) % 7 == 0:
    if int(var) % 2 == 0 and int(var) % 7 != 0:
        print("TAR")
    else:
        if int(var) % 2 != 0 and int(var) % 7 == 0:
            print ("HEELS")
        else:
            if int(var) % 2 == 0 and int(var) % 7 == 0:
                print("TAR HEELS")
else:
    print("CAROLINA")
