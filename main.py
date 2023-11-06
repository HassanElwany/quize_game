class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0


user_1 = User("001", "Hassan")

print(user_1.followers)
