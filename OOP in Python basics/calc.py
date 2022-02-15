def add():
    print("res 1 is", __name__)


def sub():
    print('res 2 is')


def main():
    print("in calc main")
    add()
    sub()

if __name__=="__main__":
    main()
