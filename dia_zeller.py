#coding: utf-8
# Chama o metodo OrderedDict() para organizar dicionarios.
from collections import OrderedDict

class Datas_dias():
    """Classe para trabalhar com datas"""
    
    def __init__(self, dia, mes, ano,
            dia_fut='', mes_fut='', ano_fut=''):
        """Inicia atributos"""
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.dia_fut = dia_fut
        self.mes_fut = mes_fut
        self.ano_fut = ano_fut

    
    def get_dia_semana(self):
        """Acha qual o dia da semana"""
        
        dias_semana = [
                'Domingo',
                'Segunda-Feira',
                'Terça-Feira',
                'Quarta-Feira',
                'Quinta-Feira',
                'Sexta-Feira',
                'Sábado',
                ]
        
        # Cria variaveis para trabalhar com ano e mes
        ano_semana = self.ano
        mes_semana = self.mes
        
        # Verifica se o mes é janeiro ou fevereiro
        # Se 'true', trabalha como mes 13 ou 14 do ano anterior
        if self.mes <= 2:
            ano_semana = self.ano - 1
            mes_semana = self.mes + 12
        
        # Inicia formula da congruencia de zeller
        cong_zeller = self.dia + (((mes_semana+1)*13)/5)
        cong_zeller += (ano_semana % 100) + ((ano_semana % 100) // 4)
        cong_zeller += ((ano_semana // 100) // 4) + (5 * (ano_semana // 100))
        cong_zeller = int(cong_zeller) % 7
        
        # Gera o index para lista 'dias_semana'
        index_dia_semana = cong_zeller - 1
        
        # Volta com o index da semana
        return (index_dia_semana)
        
    def get_dif_dias(self):
        """Acha a diferença de dias entre datas,
        incluindo a data futura"""
        
        # Cria variaveis para trabalhar com o mes e ano
        ano_dif_atual = self.ano
        mes_dif_atual = self.mes
        dia_dif_atual = self.dia
        ano_dif_futuro = self.ano_fut
        mes_dif_futuro = self.mes_fut
        dia_dif_futuro = self.dia_fut
        
        # Verifica se o mes é janeiro ou fevereiro
        # Se 'true', trabalha como mes 13 ou 14 do ano anterior
        if mes_dif_atual <= 2:
            ano_dif_atual = self.ano - 1
            mes_dif_atual = self.mes + 12
        
        # Verifica se o mes é janeiro ou fevereiro
        # Se 'true', trabalha como mes 13 ou 14 do ano anterior
        if mes_dif_futuro <= 2:
            ano_dif_futuro -= 1
            mes_dif_futuro += 12
        
        # Realize cálculo aritimetico para numero de dias 1
        data_antiga = ((1461 * ano_dif_atual) // 4)
        data_antiga += ((153 * mes_dif_atual) // 5) + dia_dif_atual
        # Realiza cálculo aritimetico para numero de dias 2
        data_futura = ((1461 * ano_dif_futuro) // 4)
        data_futura += ((153 * mes_dif_futuro) // 5) + dia_dif_futuro

        # Subtrai dia 1 de dia 2 (d2-d1)
        total_dias = data_futura - data_antiga

        # Volta com total de dias
        return(int(total_dias))
        
    def get_ano_bissexto(self):
        """Verifica se ano é bissexto e retorna Boolean"""
        # Pega o ano e verifica se é
        # divisível por 4 e não divisivel por 100
        if self.ano %4 == 0 and self.ano %100 != 0:
            se_bissexto = True
        # Se acima = false, verifica se é divisivel por 400
        elif self.ano %400 == 0:
            se_bissexto = True
        # Se acima = false, retorna como ano não bissexto
        else:
            se_bissexto = False
            
        return (se_bissexto)
    
    def get_only_wanted(self, datas_percorrer, index_data_1):
        """Pega somente datas escolhidas"""
        
        # Dicionario de datas guardadas, chamando a function
        # OrderedDict() que lembra a ordem de cada item
        datas_guardadas = OrderedDict()
        
        # Sub_dicionario para datas/ano, chamando a function
        # OrderedDict() que lembra a ordem de cada item
        datas_guardadas_ano = OrderedDict()

        # Sub_dicionario para datas/mes, chamando a function
        # OrderedDict() que lembra a ordem de cada item
        datas_guardadas_mes = OrderedDict()
        
        # Lista com o nome dos meses
        meses_ano = [
                'Janeiro',
                'Fevereiro',
                'Março',
                'Abril',
                'Maio',
                'Junho',
                'Julho',
                'Agosto',
                'Setembro',
                'Outubro',
                'Novembro',
                'Dezembro'
                ]

        # Lista com o nome dos dias da semana
        dias_semana = [
                'Domingo',
                'Segunda-Feira',
                'Terça-Feira',
                'Quarta-Feira',
                'Quinta-Feira',
                'Sexta-Feira',
                'Sábado',
                ]
                
        # lista de filtro dos dias desejados
        dias_desejados = [ 0, 2, 6]
        
        # lista contendo o numero do primeiro dia do mes
        # em relação ao numero total de dias no ano
        primeiro_dia_mes = [
                #Primeiro dia de cada mês
                0, 31, 59, 90,
                120, 151, 181, 212,
                243, 273, 304, 334
                ]
        
        # lista de meses com 30 dias          
        meses_trinta = [ 4, 6, 9, 11 ]
        
        # Esta variavel trará 31 dias para os não
        # estiverem a lista 'meses_trinta'
        numero_dias_mes = 31
        
        # Numero do dia atual
        numero_dia_ano = primeiro_dia_mes[self.mes -1] + self.dia
        
        # Cria variaveis para trabalhar com dia, mes, ano
        # e index para a lista 'dias_semana'
        dia_atual = self.dia
        mes_atual = self.mes
        ano_atual = self.ano
        sendo_dia = index_data_1
        # Variável para ano bissexto
        se_bissexto = False
        # Verifica se ano é bissexto
        if (ano_atual %4 == 0 and ano_atual %100 != 0):
            se_bissexto = True
        elif ano_atual %400 == 0:
            se_bissexto = True
        else:
            se_bissexto = False

        # Nome mes atual
        nome_mes_atual = ''
        
        # Inicia loop para filtrar dias
        for dia_passado in range(0, datas_percorrer + 1):

            #Da nome ao mes
            nome_mes_atual = meses_ano[mes_atual - 1]
                        
            # Verifica se mes atual esta na lista meses_trinta
            # se true, o mes tem 30 dias
            if mes_atual in meses_trinta:
                numero_dias_mes = 30
            # Se o mes atual é = 2 (fevereiro), o mes possui 28 dias
            elif mes_atual == 2:
                numero_dias_mes = 28
                # Porem se for bissexto, o mes tem 29 dias.
                if se_bissexto == True:
                    numero_dias_mes = 29
            else:
                numero_dias_mes = 31
                            
            # Verifica se a data passa no filtro 'dias desejados'
            if sendo_dia in dias_desejados:
                # Concatena chave
                chave_dia_mes = str(dia_atual)
                #chave_dia_mes += '/' + str(mes_atual)
                # Concatena valor
                valor_semana = dias_semana[sendo_dia]
                # Guarda as datas no dicionario mes
                datas_guardadas_mes[chave_dia_mes] = valor_semana

            # Adiciona uma unidade no numero_do_dia
            # na data atual e no index do dia
            numero_dia_ano += 1
            dia_atual += 1
            sendo_dia += 1
            # Cria ou adiciona o dicionario mes no dicionario de ano
            datas_guardadas_ano[nome_mes_atual] = datas_guardadas_mes
            # Cria ou adiciona o dicionario ano no dicionario geral
            datas_guardadas[ano_atual] = datas_guardadas_ano
            
            # Se o index após a adição for > 6, retorna 0
            if sendo_dia > 6:
                sendo_dia = 0
            
            # Se o dia atual for maior que o numero total
            # de dias do mes, retorna dia primeiro do mes seguinte
            if dia_atual > numero_dias_mes:
                dia_atual = 1
                mes_atual += 1
                datas_guardadas_mes = OrderedDict()
                # Se o mes > 12, retorna janeiro, primeiro do ano seguinte
                if mes_atual > 12:
                    mes_atual = 1
                    numero_dia_ano = 1
                    ano_atual += 1
                    datas_guardadas_ano = OrderedDict()
                    # Verifica se ano seguinte é bissexto
                    if (ano_atual %4 == 0 and ano_atual %100 != 0):
                        se_bissexto = True
                    elif ano_atual %400 == 0:
                        se_bissexto = True
                    else:
                        se_bissexto = False
        
        return(datas_guardadas)

