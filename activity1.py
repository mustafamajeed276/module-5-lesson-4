class myclass:
    __privatevar = 27
    def __privmeth(self):
        print("i'm in class myclass")
    def hello(self):
        print("private variable value is ", myclass.__privatevar)
foo = myclass()
foo.hello()
foo.__privmeth