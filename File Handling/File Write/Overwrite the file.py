

f = open("demofile3.txt", "w")
f.write("whoops! I have deleted the content!")
f.close()

#open and read teh file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())