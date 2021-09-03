#coding : utf-8
# Utilizando as funções criadas no arquivo dia_zeller.py
# Inicia chamando a classe Datas_dias
#!/usr/bin/env python
from sys import exit
from dia_zeller import Datas_dias
from func_diversas import Divrss_ccb
from dados_storage import Porteiro

p = Porteiro()      

CADASTRO = True

while CADASTRO:
    p.force_read()
    print ("Insira:\n\t*ver para vizualizar dados\n\t*add para "\
            "adicionar porteiros\n\t*del para deletar\n\t*continuar para"\
            " ir ao gerador de rodízio")
    action = input("\n> ")
    if "add" in action:
        nome_port = input("Nome do Porteiro?\n> ")
        indisp_esp_port = input("Indisponibilidade em dia da semana?\n"\
                "('Terça', 'Sábado', 'Domingo' ou 'nenhum'.)\n> ")
        indisp_dia_port = input("Indisponibilidade de escala?\n" \
                "('Par' ou 'Impar' ou 'nenhum'.)\n> ")
        p.writing(nome_port,indisp_esp_port,indisp_dia_port)
    elif "ver" in action:
        print('\n Digite:*nome do porteiro ou *todos para ver tudo')
        p.reading()
    elif "del" in action:
        print('\n Digite o nome do porteiro que deseja deletar:')
        p.deleting()
    elif "continuar" in action:
        CADASTRO = False


# Mensagem de instrução        
mensagem_instrucao = ' - dd/mm/aaaa, ex:01/12/1991 ou 16/7/1993: '
# Solicita o input da data inicial
entry_inicial = input('Data inicial' + mensagem_instrucao)
# Solicita o input da data futura
entry_final = input('Data final' + mensagem_instrucao)

diversos_fun = Divrss_ccb(entry_inicial, entry_final)

dia_entr_inicial, mes_entr_inicial, ano_entr_inicial, dia_entr_final, \
mes_entr_final, ano_entr_final = diversos_fun.string_to_int()

# Direciona as entradas para iniciar a classe
datas = Datas_dias(dia_entr_inicial, mes_entr_inicial, ano_entr_inicial,
        dia_entr_final,mes_entr_final,ano_entr_final)

# retorna o index do dia da semana da data inicial
index_inicial = datas.get_dia_semana()

# retorna o numero de dias entre data inicial e data futura
qtd_dias = datas.get_dif_dias()

# retorna dicionario contendo as datas como key e
# dia da semana como valor
dicio_dias = datas.get_only_wanted(qtd_dias, index_inicial)
# Cria lista vazia para guardar as datas
lista_data_dia = []

#Transforma dicionario em lista
for ano, meses in dicio_dias.items():
    for mes, dias in meses.items():
        for dia, nome_dia in dias.items():
            lista_data_dia.append(str(dia) + '/' + str(mes) + '/' +
                    str(ano) + ' - ' + nome_dia)
    pass

################ INICIA TESTE DE PORTEIROS ###############

porteiros = p.retorna_dicio()
# Cria tabela para armazenar a "tabela" de porteiros
tabela_porteiros = []
# Flag para o main Loop
flag_loop = True
# Contador de data para ser utilizado no index da lista de datas
contador_data = 0
# Gera lista apartir das keys do dicionario porteiros
lista_porteiros = list(porteiros.keys())
print(lista_porteiros)
# Gera contador para ser utilizado como index na lista de porteiros
contador_port = 0

# Main loop se inicia
while flag_loop:

    # testa se contador data é maior igual ao numero
    # de items da lista de datas
    if contador_data >= len(lista_data_dia):
        # Quebra Main loop
        flag_loop = False
        break
    
    # Data atual é ao valor no index 'contador_data' na 'lista_data_dia'
    data_atual = lista_data_dia[contador_data]
    # Verifica se data atual é par ou impar
    data_atual_par = diversos_fun.verif_par_impar(data_atual)

    # Data anterior, tem o index menos 1
    data_anterior = lista_data_dia[contador_data - 1]
    # Verifica se data anterior é par ou impar
    data_anterior_par = diversos_fun.verif_par_impar(data_anterior)

    
    # Flag para o loop interno, checagem de porteiro
    flag_checando_porteiro = True
    
    # Loop interno se inicia
    while flag_checando_porteiro:
        
        # Puxa informação de porteiro_atual
        porteiro_atual = lista_porteiros[contador_port]
        
        # Se tabela não estiver vazia, verifica se o porteiro_atual não
        # está já presente no último item adicionado '[-1]'
        if len(tabela_porteiros) != 0:
            if porteiro_atual in tabela_porteiros[-1]:
                # Caso esteja, pula para próximo porteiro '+1'
                contador_port += 1
                # Verifica se contador não excedeu o numeroi
                # de porteiros, caso True, zera novamente contador
                contador_port = diversos_fun.contadores_check(
                        contador_port,len(lista_porteiros))
                continue
                
        # Cria parametros para adicionar porteiros na tabela
        dispo_porteiro_atual = True
        
        # Loop verifica os dias de indisponibilidade do porteiro atual
        for dia_dispos in porteiros[porteiro_atual]:
            # se o dia em que não esta disponivel está na string
            # da data atual

            if dia_dispos in data_atual or dia_dispos == data_atual_par:
                # se True, altera a disponibilidade para False
                dispo_porteiro_atual = False
                
        # Se a disponibilidade do porteiro atual for True
        if dispo_porteiro_atual == True:
            # Adiciona na tabela_porteiros
            tabela_porteiros.append(data_atual + ' : ' + porteiro_atual)
            # Quebra loop interno
            flag_checando_porteiro = False
        # Caso disponibilidade = False, avança para próximo porteiro.
        else:
            contador_port += 1
            contador_port = diversos_fun.contadores_check(
                    contador_port,len(lista_porteiros))
    # ao final, avança para a próxima data com +1 no index
    contador_data += 1

registro_dias_trabalhados = {}

media_dias = diversos_fun.media_trabalho_lista(tabela_porteiros, lista_porteiros)

for ports  in lista_porteiros:

    dias_trabalhados = diversos_fun.dias_trabalhado_porteiro(tabela_porteiros, ports)
    registro_dias_trabalhados[ports] = dias_trabalhados

for i in tabela_porteiros:
    
    print(i)

print("\nQuantidade de dias trabalhados de cada porteiro:")
print(registro_dias_trabalhados)
print("Média de dias trabalhados: ", media_dias)
