class Botao:
    def __init__(self):
        self._economia_energia = False

    def ligar_desligar_economia(self):
        if self._economia_energia:
            self._economia_energia = False
            print("A economia de energia foi desligada.")
        else:
            self._economia_energia = True
            print("A economia de energia foi ligada.")

    def status_economia_energia(self):
        if self._economia_energia:
            print("A economia de energia está ligada.")
        else:
            print("A economia de energia está desligada.")

    def _metodo_privado(self):
        print("Este é um método privado.")

    def protegido(self):
        self._metodo_privado()


class BotaoEconomiaEnergia(Botao):
    def __init__(self):
        super().__init__()

    def ligar_desligar_economia(self):
        super().ligar_desligar_economia()

    def _metodo_privado(self):
        print("Este é um método privado sobrescrito pela classe BotaoEconomiaEnergia.")


class BotaoPersonalizado(Botao):
    def __init__(self, mensagem_ligado, mensagem_desligado):
        super().__init__()
        self.mensagem_ligado = mensagem_ligado
        self.mensagem_desligado = mensagem_desligado

    def ligar_desligar_economia(self):
        if self._economia_energia:
            self._economia_energia = False
            print(self.mensagem_desligado)
        else:
            self._economia_energia = True
            print(self.mensagem_ligado)

    def _metodo_privado(self):
        print("Este é um método privado sobrescrito pela classe BotaoPersonalizado.")


class BotaoEconomiaEnergiaPersonalizado(BotaoPersonalizado):
    def __init__(self):
        super().__init__("Economia de energia ligada.", "Economia de energia desligada.")


# Teste dos botões
botao1 = Botao()
botao1.status_economia_energia()
botao1.protegido()

resposta = input("Deseja ligar a economia de energia? (s/n): ")
if resposta.lower() == "s":
    botao1.ligar_desligar_economia()

botao1.status_economia_energia()

botao2 = BotaoEconomiaEnergia()
botao2.status_economia_energia()
botao2.protegido()

resposta = input("Deseja ligar a economia de energia? (s/n): ")
if resposta.lower() == "s":
    botao2.ligar_desligar_economia()

botao2.status_economia_energia()

botao3 = BotaoEconomiaEnergiaPersonalizado()
botao3.status_economia_energia()
botao3.protegido()

resposta = input("Deseja ligar a economia de energia? (s/n): ")
if resposta.lower() == "s":
    botao3.ligar_desligar_economia()

botao3.status_economia_energia()
