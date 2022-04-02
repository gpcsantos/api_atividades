from models import Pessoas, Usuarios

# insere dados na tabela pessoa
def insere_pessoa():
    pessoa = Pessoas(nome='Glauco P C Santos', idade=43)
    print(pessoa)
    pessoa.save()

def inclui_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

# consulta dados na tabela pessoa
def consulta_usuarios():
    usuarios = Usuarios.query.all()
    for usuario in usuarios:
        print(usuario)

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # for i in pessoa:
    #     print(i.nome)
    pessoa = Pessoas.query.filter_by(nome='Glauco').first()
    print(pessoa.idade)

# altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Glauco').first()
    pessoa.idade = 99
    pessoa.save()

# exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Glauco Santos').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoa()
    # inclui_usuario('gpcsantos', '1234')
    # inclui_usuario('santos','12345')
    # consulta_usuarios()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()

