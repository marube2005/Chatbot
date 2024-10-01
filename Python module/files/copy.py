#copyfile( ) = copies contet of a file.
#copy() = copyfile() + permission mode + destination can be a directory'
#copy2() =copy() + copies + metadata (file's creation and modification timess)

import shutil

shutil.copyfile('C:\\Users\\emaru\\OneDrive\\Desktop\\Python module\\strings\\text.txt','copy.txt') #source,dst