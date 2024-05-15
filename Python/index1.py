# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()
# f = open("demo.txt","r")
# data = f.read(5)
# print(data)

# f.close()
###################################
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()
# f = open("demo.txt","a")
# f.write("Then i will move to ReactJS")
# f.close()

#######################################
# f = open("demo.txt","r+")
# f.write("abc")
# f.close()
#######################################
# f = open("demo.txt","+a")
# print(f.read())
# f.write("abc")
# f.close()
########################################
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

#####################################
# import os

# os.remove("demo.txt")

######################################
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/o\n")
    f.write("using Java.\nI like programming in Java.")