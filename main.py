from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")




def createfile():
    try:
       readfileandfolder()
       name = input("please tell your fule name:-")
       p = Path(name)
       if not p.exist():
           with open(p,"w") as fs:
               data = input("what you want to write in this file:-")
               fs.write(data)
           print(f"file created succesfully")
       else:
           print("his file already exist. ")
              
    except Exception as err:
       print(f"an erroe as {err}")



print("press 1 for creating a file.")
print("press 2 for reading a file.")
print("press 3 for updating a file.")
print("press 4 for deletion a file.")

check = int(input("please tell your response :-"))

if check ==1:
    createfile()