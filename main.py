class User:
    def __init__(self, name, id) :
        print("The new user being created...")
        self.name = name
        self.id = id
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1

user_1 = User("hoang", "001")
user_2 = User("Yen", "002")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)