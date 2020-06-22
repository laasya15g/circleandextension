import os
file_name=input("enter the filename")
extension=file_name.split(".")
if extension[-1]=='py':
    print("python")
elif extension[-1]=='txt':
    print("text")
elif extension[-1]=='png':
    print("portable network graphics")
else:
    print("none")
