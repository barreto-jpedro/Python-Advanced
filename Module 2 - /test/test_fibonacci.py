from fibonacci import FibonacciData
import pytest

FIBONACCI = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

params = [x for x in range(2,11)]
@pytest.mark.parametrize("iterations",params)
def test_FibonacciData_initialized_with_N_should_generate_an_iterable_object_for_N_iterations(iterations):
    SUT = FibonacciData(iterations)
    iteration_counter = iterations
    
    for fibonacci_number, SUT_number in zip(FIBONACCI, SUT):
        iteration_counter-=1
        assert fibonacci_number == SUT_number
        assert iteration_counter >= 0
