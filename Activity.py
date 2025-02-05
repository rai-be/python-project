class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}") 
        print(f"Cargo: {self.cargo}") 
        print(f"Salário: {self.salario}") 


funcionario1 = Funcionario("Sandra", "Desenvolvedora Backend", 5000.00)
funcionario2 = Funcionario("margarida", "Desenvolvedora", 5000.00)

funcionario1.exibir_informacoes()
funcionario2.exibir_informacoes()


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} foi adicionado à empresa {self.nome}.")

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"{nome} foi removido da empresa {self.nome}.")
                return
        print(f"Funcionario {nome} não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print(f"Não tem funcionarios na empresa {self.nome}.")
        else:
            print(f"Lista de funcionarios da empresa {self.nome}:")
            for funcionario in self.funcionarios:
                funcionario.exibir_informacoes()


empresa = Empresa("A volta dos que não foram")

empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)

empresa.listar_funcionarios()

empresa.remover_funcionario("margarida")

empresa.listar_funcionarios()


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")


livro1 = Livro("senhor dos aneis", "J. R. R. Tolkien", 1937)
livro2 = Livro("O sol é para todos", "Harper Lee", 1960)

livro1.exibir_informacoes()
livro2.exibir_informacoes()
