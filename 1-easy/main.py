from inputP.stringF import nameF
from outputP.getName import getName
from conditionals.ifStatement import checkName


def main():
    name = getName()
    print(nameF(name))
    print(checkName(name))


if __name__ == "__main__":
    main()
