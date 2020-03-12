from loops.loopInp import loInp


def main():
    '''
    Create a function in loops folder that will go from 0 to a user defined number.
    Get the number outside of the function and pass it as an arguement. 
    Test what numbers are divisible by 2 and return them to the user via a print function.

    ////////////////////////////////////////////////////////////////////////

    arr = []

    arr.append(number)

    ////////////////////////////////////////////////////////////////////////

    i = 0 #starting number
    sN = 10 #stopping number

    while i < sN:
        print(i)
        i += 1


    ////////////////////////////////////////////////////////////////////////

    These two functions will be inside the functions folder and called multiCheck and plusArr

    Create two functions.

    Both functions will take two arguements.

    Function 1 - Multiple two numbers together and if it is a modulus of 2 return True

    2 * 5 = 10

    10 % 2 = 0

    return True

    Function 2 - Add two numbers together and return an array from 0 to the two numbers added together

    1+3 = 4

    return [0,1,2,3,4]

    ////////////////////////////////////////////////////////////////////////

    def multiply(number1, number2):
        return number1 * number2
    '''

    loAm = int(input("Please enter number:"))
    arr = loInp(loAm)
    print(arr)


    #Call new functions here


if __name__ == "__main__":
    main()
