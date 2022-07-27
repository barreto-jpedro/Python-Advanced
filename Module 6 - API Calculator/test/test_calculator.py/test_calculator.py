from calculator import calculator


async def test_calculator_multiplication_8_and_4_and_should_return_32():
    SUT_return = await calculator(8, 4, "*")
    expected = 32
    assert SUT_return == expected


async def test_calculator_division_8_and_4_and_should_return_2():
    SUT_return = await calculator(8, 4, "/")
    expected = 2
    assert SUT_return == expected


async def test_calculator_subtraction_8_and_4_and_should_return_4():
    SUT_return = await calculator(8, 4, "-")
    expected = 4
    assert SUT_return == expected


async def test_calculator_sum_8_and_4_and_should_return_12():
    SUT_return = await calculator(8, 4, "+")
    expected = 12
    assert SUT_return == expected
