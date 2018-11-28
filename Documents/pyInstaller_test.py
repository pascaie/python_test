text = input("Enter the file name: ") #suggestion: enter 'myfile.txt'
myfile = open(text, "w+") #generate a file with the name given in the input
myfile.close()

#input at the end of the script in order to keep the window open when the .exe file is executed
input("Press Enter to continue...")
