from fibonacci import FibonacciData

obj = FibonacciData(10)

fibonacci = {k:v for k,v in enumerate(obj)}
for k,v in fibonacci.items():
    print(k," : ",v)
    