"""
Day 17 - Creation of classes, attributes and others
"""

class User:
    #Initializing attributes
    #self is the object being initialized or created
    def __init__(self, user_id, name):
        #Creating the attributes
        self.id = user_id
        self.username = name
        #Initial attribute. It's default for everyone.
        self.followers = 0
        self.following = 0
    
    #Defining a new method. Methods always need a self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)