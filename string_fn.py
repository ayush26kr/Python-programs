story='''twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.'''

print("Length of story is : ",(len(story)))  #len()

print(story.endswith("sky"))   #string.endswith()
print(story.endswith("sky."))

print(story.count("t"))  #string.count()

print(story.capitalize())  #string.capitalize --> makes first word capital

print(story.find("star"))  #string.find() --> -1 means word is not present 

print(story.replace("twinkle","spakling"))