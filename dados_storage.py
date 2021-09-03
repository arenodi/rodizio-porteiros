class Porteiro():
    def __init__(self):
        self.nome = ""
        self.indisp_esp = ""
        self.indisp_dia = ""
        self.whip = {}

    def writing(self, nome, indisp_esp, indisp_dia):
        self.whip[nome] = [indisp_esp, indisp_dia]
        with open('dados_porteiros.txt', 'w', encoding='utf-8') as f:
            f.write(str(self.whip))
        print(nome + ' cadastrado com sucesso!\n\n')

    def reading(self):
        with open('dados_porteiros.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            self.whip = eval(s)
        #self.whip = open('deed.txt', 'r').read()
            name = input("> ")
            if name in self.whip:
                print('\n' + name + ':')
                print('\tIndisponivel no dia: ' + self.whip[name][0] + \
                        '\n\tIndisponivel na escala/dia: ' + \
                        self.whip[name][1] + '\n\n')
            elif name == 'todos':
                print('\n\n--------- Atualmente Cadastrados -----------')
                for nome, info in self.whip.items():
                    print(nome, info)
                print('--------------------------------------------\n\n')
            
    def force_read(self):
        with open('dados_porteiros.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            self.whip = eval(s)

    def retorna_dicio(self):
        with open('dados_porteiros.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            self.whip = eval(s)

        return self.whip

    def deleting(self):
        with open('dados_porteiros.txt', 'r+', encoding='utf-8') as f:
            s = f.read()
            self.whip = eval(s)
            name = input('> ')
            if name in self.whip:
                del self.whip[name]
            f.seek(0)
            f.truncate()
            f.write(str(self.whip))
            print('Porteiro deletado com sucesso!\n\n')
