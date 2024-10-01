try:
 with open ('C:\\Users\\emaru\\OneDrive\\Desktop\\Python module\\strings\\text.txt') as f:
    f.write(text('Hello world'))
except FileNotFoundError as F:
  print("That file was not found.")
except NameError as F:
  print("Undefined word found.")
  print(F)
# to apend or write to a file you write this way:
# with open('test_file', 'w') as f:
#   f.write(text('hello world')) # w meaning write into a file.