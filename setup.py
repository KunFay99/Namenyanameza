import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pip2 install requests")
    os.system("git pull")

elif c == "1":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pip2 install requests")
    os.system("git pull")
    
print("Done.")
