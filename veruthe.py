str=input("enter a string")
li=list(str)
l=['a','e','i','o','u']
v=0
c=0
for i in li:
    if i in l:
        v=v+1
    else:
       c=c+1
print("no of vowels",v) 
print("no of consonants",c)             