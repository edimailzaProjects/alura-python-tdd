from datetime import date

class Funcionario:
    def __init__(self, nome, data_nasc, salario):
        self._nome = nome
        self._data_nasc = data_nasc
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        #split é um método para formatar strings
        #Eu vou quebrar a string em determinados pontos
        #Daí, eu vou retornar uma lista com os pontos quebrados da string
        #Eu posso passar a string que vou utilizar para fazer a quebra
        # com isso, eu ja terei uma lista com dia mês e ano
        data_nasc_quebrada = self._data_nasc.split('/')
        #Vou criar a variável ano_nasc e vou igualar essa variável ao
        # último item da lista que é a data de nascimento quebrada
        #para isto eu abro o colchetes e coloco [-1]
        #Ele vai pegar o último item da lista que no nosso caso será o ano
        ano_nasc = data_nasc_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nasc) #agora é só chamar aqui

    #Quando uma pessoa coloca o nome e o sobrenome, é comum que exista um espaço entre eles
    #Um caracter em branco antes e depois do nome dela
    # deste modo, utilizaremos o strip para remover os espaços anteriores e posteriores do que foi inserido
    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ') #aqui eu quero que a quebra ocorra no espaço
        #retorne pra mim o último nome da lista quebrado
        return nome_quebrado[-1]

    # NÃO É INTELIGENTE UM MÉTODO QUE FAZ MUITAS COISAS!
    #este método abaixo trabalha o sobrenome e o salário
    #é mais inteligente criar um método que informe se é diretor ou não
    #def decres_salario(self):
    #    sobrenomes = ['Diniz', 'Abrantes', 'Montez'] #lembrando que já existe o método sobrenome
    #    if self._salario >=10000 and (self.sobrenome() in sobrenomes): #o sobrenome deve estar na lista de sobrenomes
    #        dec = self._salario * 0.1
    #        self._salario = self._salario - dec

    def decres_salario(self):
        if (self._eh_diretor() == True): #o sobrenome deve estar na lista de sobrenomes
            dec = self._salario * 0.1
            self._salario = self._salario - dec

    def _eh_diretor(self): #deixe o método privado dado que só o vai ser utilizado nesta classe, não deve ser acessível
        sobrenomes = ['Diniz', 'Abrantes', 'Montez']
        if (self.sobrenome() in sobrenomes):
            return True
        else:
            return False

    #FORMA MAIS ENXUTA DE FAZER
    #def _eh_diretor(self):
    #    sobrenomes = ['Diniz', 'Abrantes', 'Montez']
    #    return (self.sobrenome() in sobrenomes) and (self._salario >= 10000)

    #def decres_salario(self):
    #    if (self._eh_diretor()):  # sem o == True
    #        dec = self._salario * 0.1
    #        self._salario = self._salario - dec

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000: #trabalhando com exception
            raise Exception('Valor muito alto para receber bonus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nasc}, {self._salario})'