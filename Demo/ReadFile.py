# # # #Read File
# # #
# # # file=open("N&P.txt","r")
# # # print(file.read())
# # # print(file.read())
# # #
# # # write file
# #
# # file=open("DN&P.txt","w")
# # file.write("Good Afternoon")
# # file.close()
# # #append File
# # file=open("DN&P.txt","a")
# # file.write("Hello")
# # file.close()
# # file=open("DN&P.txt","r")
# # print(file.read())
#
# #create new File
# file=open("new.txt","x")
# file=open("new.txt","w")
# file.write("Hi")
# file.close()
# file=open("new.txt","r")
# print(file.read())

file=open("new.txt","a")
file.write("hello")
file.close()
file=open("new.txt","r")
print(file.read())