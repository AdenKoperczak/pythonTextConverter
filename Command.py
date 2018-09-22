import main

con = True
while con:
    command=input("Command: ")
    if command=="file":
        file=input("File: ")
        tFrom=input("Input Type: ")
        tTo=input("Output Type: ")
        open(file.replace(".","(con)."),"w").write(main.textCon(open(file,"r").read(),tFrom,tTo))
    elif command=="end":
        con=False
    elif command=="text":
        text=input("Text: ")
        tFrom=input("Input Type: ")
        tTo=input("Output Type: ")
        print(main.textCon(text,tFrom,tTo))




























    
