"""this is an example API module for adding classes"""

class SomeClass:
    """description : this is some class"""
    def __init__(self,arg1,*args,**kwargs):
        print("self.arg1 = {}".format(arg1))
        print("self *args")
        for arg in args:
            print(arg)
        print("self kwargs")
        print(kwargs)

    def printSomething(self):
        """this prints something"""
        print("someting")

def main():
    """main function for this module"""
    print(__name__)

if __name__ == "__main__":
    main()
    