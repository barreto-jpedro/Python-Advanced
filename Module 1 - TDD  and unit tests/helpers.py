class MathTools:
    def __init__(self) -> None:
        pass

    def divisible_by_5(self, int_number=5):
        return int_number % 5 == 0

    def divisible_by_7(self, int_number: int):
        return int_number % 7 == 0
