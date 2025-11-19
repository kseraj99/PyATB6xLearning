class MobilePhone:

    model = None
    def __init__(self, name, bread):
        print("Print me first")
        self.name = name
        self.bread = bread


    def talk(self):
        print("Hi, I am talking")


iphone = MobilePhone()
iphone.talk()
