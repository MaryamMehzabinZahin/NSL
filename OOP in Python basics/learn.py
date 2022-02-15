class Computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print(self.cpu,self.ram)


com1=Computer('i5',16)
com2=Computer("ryzen 3",8)

com1.config()
com2.config()