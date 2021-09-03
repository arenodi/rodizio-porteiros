#coding : utf-8

class Divrss_ccb():
    """Classe para ser utilizada no software
    'tabela de porteiros', com funções diversas"""

    def __init__(self, data_inicial='', data_final=''):
        """Inicia com os valores da string fornecida
        pelo usuario"""

        self.data_inicial = data_inicial
        self.data_final = data_final

    def string_to_int(self):
        """Função para transformar os valores da data
        fornecido pelo usuario de string para int"""

        entrada_inicial = self.data_inicial.replace('/','')
        entrada_final = self.data_final.replace('/','')

        dia_entr_inicial = int(entrada_inicial[:2])
        mes_entr_inicial = int(entrada_inicial[2:4])
        ano_entr_inicial = int(entrada_inicial[4:])

        dia_entr_final = int(entrada_final[:2])
        mes_entr_final = int(entrada_final[2:4])
        ano_entr_final = int(entrada_final[4:])

        # Se numero tiver '0' na frente, pega somente o segundo numero
        # Nota 'int' não aceita 0's na frente
        if (len(entrada_inicial) and len(entrada_final)) == 8:
            if dia_entr_inicial != int and dia_entr_inicial < 10:
                dia_entr_inicial = int(entrada_inicial[1:2])

            if mes_entr_inicial != int and mes_entr_inicial < 10:
                mes_entr_inicial = int(entrada_inicial[3:4])

            if dia_entr_final != int and dia_entr_final < 10:
                dia_entr_final = int(entrada_final[1:2])

            if mes_entr_final != int and mes_entr_final < 10:
                mes_entr_final = int(entrada_final[3:4])

        return dia_entr_inicial, mes_entr_inicial, ano_entr_inicial, \
                dia_entr_final, mes_entr_final, ano_entr_final

    def contadores_check(self,contador, limite):
        """Check os contadores para verificar se
        estão acima ou igual o limite"""
        
        if contador >= limite:
            contador = 0
        else:
            contador
        return contador
    def verif_par_impar(self, data_par_impar):
        """Verifica se o dia é par ou impar"""

        checked_dia = data_par_impar
        # Verifica se o dia é de somente um algarismo
        if checked_dia[1] == '/':
            checked_dia = checked_dia[0]
        else:
            checked_dia = checked_dia[:2]

        checked_dia = int(checked_dia)

        if checked_dia % 2 == 0:
            return 'par'
        else:
            return 'impar'

    def mes_to_string(self, data_mes_string):
        """Retorna o mes em string"""

        mes_texto = data_mes_string

        mes_nomes = [ 'janeiro', 'fevereiro', 'março',
                'abril', 'maio', 'junho', 'julho', 'agosto',
                'setembro', 'outubro', 'novembro', 'dezembro']

        if mes_texto[1] and mes_texto[3] == '/':
            mes_texto = int(mes_texto[2])
        elif mes_texto[1] and mes_texto[4] == '/':
            mes_texto = int(mes_texto[2:4])
        elif mes_texto[2] and mes_texto[4] == '/':
            mes_texto = int(mes_texto[3])
        else:
            mes_texto = int(mes_texto[3:5])

        mes_texto = mes_nomes[mes_texto - 1].title()

        return mes_texto

    def media_trabalho_lista(self, lista_de_dias, lista_de_porteiros):
        """Realiza média de dias de trabalho pelo
        numero de porteiros"""

        lista_dividendo = len(lista_de_dias)
        lista_divisor = len(lista_de_porteiros)

        media_quociente = (lista_dividendo // lista_divisor)

        return media_quociente

    def dias_trabalhado_porteiro(self, tabela_gerada, nome_porteiro):
        """Conta quantas vezes um porteiro trabalha
        pela tabela gerada"""

        contador_trabalho = 0

        for dia_culto in tabela_gerada:
            if nome_porteiro in dia_culto:
                contador_trabalho += 1

        return contador_trabalho
