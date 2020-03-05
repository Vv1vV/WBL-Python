from inputP.stringf import namef
from outputP.getName import getName
from conditionals.ifStatement import checkName




def main():
    name = getName()
    print(namef(name))
    print(checkName(name))
    



if __name__ == "__main__":
    main()
