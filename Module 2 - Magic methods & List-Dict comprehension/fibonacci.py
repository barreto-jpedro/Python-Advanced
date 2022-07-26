class FibonacciData():
    def __init__(self, limit) -> None:
        self.limit_counter_interation = limit
        self.interation_counter = 0
        self.prior = 1
        self.before_prior = 1

    def __iter__(self):
        self.number = 1
        return self
        
    def __next__(self):
        if self.interation_counter == self.limit_counter_interation:
            raise StopIteration
        self.interation_counter += 1
        
        self.number = self.prior + self.before_prior
        self.before_prior = self.prior
        self.prior = self.number
        
        return self.number
