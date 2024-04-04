class Maquina:
    def __init__(self, nome, ligada=False):
        self.nome = nome
        self.ligada = ligada

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


class Luz:
    def __init__(self, nome, ligada=False):
        self.nome = nome
        self.ligada = ligada

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


class Comodo:
    def __init__(self, nome):
        self.nome = nome
        self.maquinas = []
        self.luzes = []

    def adicionar_maquina(self, maquina):
        self.maquinas.append(maquina)

    def adicionar_luz(self, luz):
        self.luzes.append(luz)

    def contar_maquinas_ligadas(self):
        maquinas_ligadas = sum(maquina.esta_ligada() for maquina in self.maquinas)
        return maquinas_ligadas

    def contar_luzes_ligadas(self):
        luzes_ligadas = sum(luz.esta_ligada() for luz in self.luzes)
        return luzes_ligadas

    def obter_status(self):
        maquinas_ligadas = self.contar_maquinas_ligadas()
        luzes_ligadas = self.contar_luzes_ligadas()
        return f"No {self.nome} há {maquinas_ligadas} máquina(s) ligada(s) e {luzes_ligadas} luz(es) ligada(s)."


# Exemplo de uso:
sala = Comodo("Sala")

# Adicionar máquinas e luzes
sala.adicionar_maquina(Maquina("Máquina de café"))
sala.adicionar_maquina(Maquina("Ar condicionado"))
sala.adicionar_luz(Luz("Luz principal"))
sala.adicionar_luz(Luz("Luz de leitura"))

# Ligar algumas máquinas e luzes
sala.maquinas[0].ligar()
sala.maquinas[1].ligar()
sala.luzes[0].ligar()

# Obter o status do cômodo
status = sala.obter_status()
print(status)
