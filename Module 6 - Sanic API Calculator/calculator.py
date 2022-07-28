async def calculator(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "/":
        return first_number / second_number
    elif operation == "*":
        return first_number * second_number
    else:
        return "This operation is not possible."
