class ContaBancaria:
    def __init__(self, nome_banco, saldo_inicial):
        self.nome_banco = nome_banco
        self.saldo = saldo_inicial

    def __str__(self):
        return f'Conta no {self.nome_banco} | Saldo atual: R$ {self.saldo:.2f}'

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return f'Deposito de R$ {valor:.2f} realizado com sucesso!'

    def sacar(self, valor):
        if valor > self.saldo:
            return 'Erro: Saldo insuficiente para realizar o saque.'
        else:
            self.saldo = self.saldo - valor
            return f'Saque de R$ {valor:.2f} realizado com sucesso!'

    def exibir_saldo(self):
        return f'Seu saldo atual é de R$ {self.saldo:.2f}'


pessoa = ContaBancaria('Santander', 300)
print(pessoa)

print(pessoa.depositar(200))
print(pessoa.exibir_saldo())
print(pessoa.sacar(130))
print(pessoa.exibir_saldo())
