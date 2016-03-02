#Prog asking for english word#
original = raw_input("Enter a word:")
empty_string = ""
if len(original) > 0:
    print original
elif len(empty_string) == 0:
    print "Empty"
else:
    print "Exit"

raw_input("Press Enter to exit, thank you!")
