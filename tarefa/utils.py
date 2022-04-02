from models import Programador, Habilidade, ProgramadorHabilidade

#Sessão de INSERTS
#inserir dados na tabela programador
def insere_programador():
    dev = Programador(nome='Glauco Santos ', idade=43, email='gpcsantos@gmail.com')
    dev.save()
    print(dev)

#iserir dados na tabela habilidades
def insere_habilidade():
    habilidade = Habilidade(nome='REST API')
    print(habilidade)
    habilidade.save()

#inserir realcionamento entre programador e habilidades
def insere_relacionamento():
    rel = ProgramadorHabilidade(fk_programador=1, fk_habilidade=3)
    rel.save()
    print(rel)

#Sessão de Consutas
#consulta programadores
def consulta_programador():
    dev = Programador.query.all()
    print(dev)

#Consulta habilidades
def consulta_habilidades():
    habilidade = Habilidade.query.all()
    print(habilidade)

#Consulta Relacionamento entre programador e habilidades
def consulta_relacionamentos():
    rel = ProgramadorHabilidade.query.all()
    for i in rel:
        print(i)

#sessão de DELETE
#DELETE programador
def delete_programado():
    dev = Programador.query.filter_by(id=4).first()
    dev.delete()

if __name__ == '__main__':
    #insere_programador()
    #insere_habilidade()
    #insere_relacionamento()
    consulta_programador()
    consulta_habilidades()
    consulta_relacionamentos()
    delete_programado()
    consulta_programador()