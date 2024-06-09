letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input("enter word")
w=[]
w=word.split(" ")
for i in w:
    if i in  letters:
        index=letters.index(i)
        new=index+3
        print(letters[new])

