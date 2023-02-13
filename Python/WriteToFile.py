import os.path

save_path = 'D:\Shihundu\Personal\Data'

name_of_file = "DemoData"

completeName = os.path.join(save_path, name_of_file+".txt")         

try:
    file1 = open(completeName, "w")

    toFile = "This is a simple test"

    file1.write(toFile)
except IOError:
    print("Error: cannot find file or write data")
else:
    print ("Written content in the file successfully")
    file1.close()
