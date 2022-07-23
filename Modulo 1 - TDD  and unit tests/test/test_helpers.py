from helpers import MathTools

def test_divisible_by_5_given_5_should_return_True():
    SUT = MathTools()
    return_from_SUT = SUT.divisible_by_5(int_number=5)
    assert return_from_SUT == True


def test_divisible_by_5_given_3_should_return_False():
    SUT = MathTools()
    return_from_SUT = SUT.divisible_by_5(int_number=3)
    assert return_from_SUT == False


def test_divisible_by_7_given_7_should_return_True():
    SUT = MathTools()
    return_from_SUT = SUT.divisible_by_7(int_number=7)
    assert return_from_SUT == True
    
def test_divisible_by_7_given_3_should_return_False():
    SUT = MathTools()
    return_from_SUT = SUT.divisible_by_7(int_number=3)
    assert return_from_SUT == False