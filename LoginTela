import hashlib

class UsuarioBase:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.criptografar_senha(password)

    def verificar_credenciais(self, password):
        return self.password_hash == self.criptografar_senha(password)

    def alterar_senha(self, new_password):
        self.password_hash = self.criptografar_senha(new_password)
        print("Senha alterada com sucesso.")

    @staticmethod
    def criptografar_senha(password):
        salt = "SALT_RANDOM"  # Adicione um valor de salt seguro aqui (RANDOM)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash

    def exibir_tipo_usuario(self):
        return "Usuário Base"


class UsuarioAdministrador(UsuarioBase):
    def exibir_tipo_usuario(self):
        return "Usuário Administrador"


class SistemaLogin:
    def __init__(self):
        self.usuarios = []

    def criar_login(self):
        username = input("Digite um nome de usuário: ")
        password = input("Digite uma senha: ")
        cnpj = input("Digite sua CNPJ: ")
        empresa = input("Digite sua empresa: ")
        email = input("Digite seu email empresarial: ")

        novo_usuario = UsuarioBase(username, password)
        self.usuarios.append(novo_usuario)
        print("Login criado com sucesso.")

    def criar_login_administrador(self):
        username = input("Digite um nome de usuário: ")
        password = input("Digite uma senha: ")
        cnpj = input("Digite sua CNPJ: ")
        empresa = input("Digite sua empresa: ")
        email = input("Digite seu email empresarial: ")

        novo_usuario = UsuarioAdministrador(username, password)
        self.usuarios.append(novo_usuario)
        print("Login de administrador criado com sucesso.")

    def login(self):
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        for usuario in self.usuarios:
            if usuario.username == username and usuario.verificar_credenciais(password):
                print("Login bem-sucedido.")
                return
        print("Credenciais inválidas.")


# Uso do código

sistema = SistemaLogin()

# Criar um login
sistema.criar_login()

# Criar um login de administrador
sistema.criar_login_administrador()

# Tentativa de login
sistema.login()

# Alterar senha do usuário
usuario_base = sistema.usuarios[0]  # Supondo que haja pelo menos um usuário na lista
usuario_base.alterar_senha("nova_senha")

# Exemplo de polimorfismo
for usuario in sistema.usuarios:
    print(f"Usuário: {usuario.username}, Tipo: {usuario.exibir_tipo_usuario()}")
