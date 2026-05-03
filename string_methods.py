course="python Programming"
print(course.upper())#gives a new string
print(course.lower())
print(course.title())
print(course.strip())# removes whte spaces
print(course.lstrip())#left strip is same as strip but only removes left white spaces
print(course.rstrip())#right strip is same as strip but only removes right white spaces
print(course.find("Pro"))#gives index of the firstletter of the word if found else gives -1
print(course.find("pro"))
print(course.replace("p","j"))
print("gra"in course)#boolean operator gives true if found else false
print("not"not in course)#boolean operator gives true if not found else false

