from helpers import MathTools

if "__main__" == __name__:
    int_number = int(input("Type an integer number: "))

    divisible_by_5 = MathTools.divisible_by_5(int_number)
    divisible_by_7 = MathTools.divisible_by_7(int_number)

    if divisible_by_5 and divisible_by_7:
        print("FizzBuzz")

    elif divisible_by_5:
        print("Fizz")

    elif divisible_by_7:
        print("Buzz")

    else:
        print("Miss")
