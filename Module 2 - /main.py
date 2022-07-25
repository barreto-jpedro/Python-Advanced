""" Tarefa modulo 2
Desenvolva uma aplicação com as seguintes características:
- O objeto deve ser inicializado em a variável "anterior" com o valor zero, a variável
"proximo" com o valor um e a variável "iteracao" com o valor recebido.
- O iterator criado deve ser iterado em um dict comprehension onde a chave é a posição do
valor na sequência Fibonacci que recebe o valor do elemento na sequência. Dica: Use a
função enumerate para gerar as chaves."""

from fibonacci import FibonacciData

obj = FibonacciData(1)
result = {k:v for k,v in enumerate(obj)}
for k,v in result.items():
    print(k," : ",v)
    