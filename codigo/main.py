from funcionario import Funcionario

#Aqui não é a forma correta de realizar teste unitário

#edi = Funcionario('Edi Silva', '21/02/1986', 2000)
#print(edi)
#print(edi.idade())

#Assim como no Java, nós colocamos nossos testes unitarios em métodos
def teste_idade():
    funcionario_teste = Funcionario('Teste', '21/02/1986', 1010)
    print(f'Teste = {funcionario_teste.idade()}') #este f é para formatar


#Agora, basta chamar o método
#teste_idade()

# Instale o pytest
# pip freeze > requirements.txt é o comando que cria o txt que exibe quais pacotes estão instalados
# Crie um dir chamado tests - em caixa baixa e em letra minúscula para ser reconhecido pelo pytest
# __nome__ é chamado de dunder no mundo python