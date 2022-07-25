from fibonacci import FibonacciData

def test_divisible_by_5_given_5_should_return_True():
    SUT = FibonacciData()
    return_from_SUT = SUT.divisible_by_5(int_number=5)
    assert return_from_SUT == True
