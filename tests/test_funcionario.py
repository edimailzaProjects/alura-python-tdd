# O nome do arquivo.py deve obrigatoriamente começar com "test_"
# O comando pra executar é python -m pytest
# Se eu escrevo python -m pytest -v ele traz o nome do método com os status Passed e Fail

from codigo.funcionario import Funcionario #esse pontinho é o que separa diretório.classe.py

import pytest
from pytest import mark

class TestClass:
    #para que o teste seja reconhecido, o nome do método obrigatoriamente deve começar com "test_"
    def test_quando_idade_recebe_21_02_1986_deve_retornar_36(self):
        entrada = '21/02/1986'
        esperado = 36

        funcionario_teste = Funcionario('Edi', entrada, 2000)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Edi_Silva_deve_retornar_apenas_Silva(self):
        entrada = "Edi Silva"
        esperado = "Silva"

        funcionario_teste = Funcionario(entrada, '21/02/1986', 2000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_9000(self):
        entrada_salario = 10000
        entrada_nome = 'Raul Montez'
        esperado = 9000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decres_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_mendonza_deve_nao_decrementar(self):
        entrada_salario = 10000
        entrada_nome = 'Raul Mendonza'
        esperado = 10000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decres_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    # marks são formas de tagear os testes
    # semelhante a JUnit @Before @After, etc
    #para rodar tag específica: python -m pytest -v -m calcular_bonus
    #para explorar documentação: python -m pytest --markers
    # se um método estiver tageado, ele será skipado quando o comando python -m pytest -v  for executado
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '21/02/1986', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_salario_10000000_calcular_bonus_deve_lancar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000

            funcionario_teste = Funcionario('Teste', '21/02/1986', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert  resultado

    @mark.preenchidos
    def test_quando_nome_data_nasc_salario_preenchidos_deve_retornar_valores_preenchidos(self):
            entrada_nome = 'Teste'
            entrada_data_nasc = '21/02/2000'
            entrada_sal = 10000

            funcionario_teste = Funcionario(entrada_nome, entrada_data_nasc, entrada_sal)
            resultado = funcionario_teste.__str__()

            print(resultado)

            esperado = 'Funcionario(Teste, 21/02/2000, 10000)'

            assert  resultado == esperado

#COBERTURA DOS TESTES
# pip install pytest-cov
# pip freeze > requirements.txt para atualizar e inserir o pytest-cov
#Para conferir a cobertura, coloque
#python -m pytest --cov
# Stms - quantidade de linhas de códigos
# Miss - quantas linhas não estão cobertas pelos testes
#  python -m pytest --cov=codigo tests/ seleciona classe específica para dar cobertura
#  python -m pytest --cov=codigo tests/ --cov-report term-missing mostra onde está faltando cobertura
# O missing da coluna exibida é a linha do código que falta cobertura

# python -m pytest --cov=codigo tests/ --cov-report html joga o resultado dos testes em um arquivo .html
# Abra o index.html gerado no explorer e, no teclado do lado superior direito, aparecerão os comandos

#ANOTAÇÕES
#Existe uma outra metodologia muito utilizada para a construção do raciocínio de funcionamento de testes chamada
# Arrange-Act-Assert ou simplesmente AAA. Essa metodologia também consiste em 3 etapas para a construção de um teste,
# análogas às etapas do Given-When-Then.

#Arrange:
# A tradução não literal seria algo como organizar. A organização, nesse caso,
# seria focada nos passos preliminares necessários para montar o contexto inicial do teste;
# Act:
# A tradução não literal seria algo como agir. Nesse caso seria a ação que parte
# dos passos organizados na primeira etapa e leva ao que vamos averiguar no final;
# Assert:
# A tradução não literal seria algo como averiguar. Nesse caso, averiguarmos que o
# desfecho trazido pela ação é realmente aquele que esperamos.