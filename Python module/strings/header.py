import os 

path = "C:\\Users\\emaru\\OneDrive\\Desktop\\Python module\\strings\\generatenum.py"
if os.path.exists(path):
    print("path already exists")
    if os.path.isfile(path):
      print("That is a file.") 
    elif os.path.isdir(path):
      print("That is a directory")
    elif os.path.isjunction(path):
      print("That is a junction")
else:
 print("path does not exist")