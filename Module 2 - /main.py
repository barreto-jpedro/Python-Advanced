""" Tarefa modulo 2
Desenvolva uma aplicação com as seguintes características:
- Crie um objeto que gere uma sequência de Fibonacci.
- O objeto recebe o número de elementos da sequência Fibonacci que serão gerados.
- O objeto deve ser inicializado em a variável "anterior" com o valor zero, a variável
"proximo" com o valor um e a variável "iteracao" com o valor recebido.
- O objeto criado deve ser um iterator e a cada iteração as seguintes instruções devem
ocorrer:
- É verificado se o valor da variável "iteracao" é zero, caso positivo, a iteracação é
encerrada.
- Os dois valores são somados e o resultado é armazenado em uma variável.
- O valor da variável "anterior" é atualizado com o valor da variável "proximo"
- O valor da variável "proximo" é atualizado com o valor da soma que foi armazenado na
variável criada
- O valor da variável "iteracao" é decrementado em uma unidade
- O valor da variável "proximo" é retornado pelo iterator
- O iterator criado deve ser iterado em um dict comprehension onde a chave é a posição do
valor na sequência Fibonacci que recebe o valor do elemento na sequência. Dica: Use a
função enumerate para gerar as chaves.
- Utilize ambiente virtual para o desenvolvimento
- Crie os testes unitários para as funções desenvovidas.
- Siga as boas práticas de desenvolvimento. """