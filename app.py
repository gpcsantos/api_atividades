from flask import Flask, request
from flask_restful import  Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS={
#     'glauco':'321',
#     'santos':'321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     # print('validando usuário')
#     # print(USUARIOS.get(login) == senha)
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha


@auth.verify_password
def verificacao(login, senha):
    # print('validando usuário')
    # print(USUARIOS.get(login) == senha)
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            status = 'error'
            msg = 'O nome procurado nao existe no banco'
            response={
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response

    def put(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dados = request.json
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()

            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            status = 'error'
            msg = 'O nome procurado nao existe no banco'
            response={
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }

        return response

    def delete(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            pessoa.delete()
            status = 'success'
            msg = 'Pessoa {} excluida com sucesso'.format(nome)
            response = {
                'status': status,
                'msg': msg
            }
        except AttributeError:
            status = 'error'
            msg = 'O nome procurado nao existe no banco'
            response={
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome': i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        try:
            dados = request.json
            pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'] )
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except Exception:
            status = 'error'
            msg =  'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome, 'status':i.status} for i in atividades]
        return response

    def post(self):
        try:
            dados = request.json
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            atividade = Atividades(nome=dados['nome'], pessoa=pessoa, status=dados['status'])
            atividade.save()
            response = {
                'id': atividade.id,
                'nome': atividade.nome,
                'status': atividade.status,
                'pessoa': atividade.pessoa.nome
            }
        except AttributeError:
            status = 'error'
            msg = 'O nome informado nao existe no banco'
            response = {
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response

class Atividade(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            atividade = Atividades.query.filter_by(pessoa=pessoa).first()
            response = {
                'id': atividade.id,
                'nome': atividade.nome,
                'pessoa': atividade.pessoa.nome
            }
        except AttributeError:
            status = 'error'
            msg = 'O nome {} informado nao existe no banco'.format(nome)
            response = {
                'status': status,
                'msg': msg
            }
        return response

class AtividadeAltera(Resource):
    def put(self, id):
        try:
            atividade = Atividades.query.filter_by(id=id).first()
            dados = request.json
            atividade.status = dados['status']
            atividade.save()
            response = {
                'id':atividade.id,
                'nome':atividade.nome,
                'pessoa':atividade.pessoa.nome,
                'status':atividade.status
            }
        except AttributeError:
            status = 'error'
            msg = 'O id {} nao existe no banco'.format(id)
            response = {
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response
    def get(self, id):
        try:
            atividade = Atividades.query.filter_by(id=id).first()
            response = {
                'status':atividade.status
            }
        except AttributeError:
            status = 'error'
            msg = 'O id {} nao existe no banco'.format(id)
            response = {
                'status': status,
                'msg': msg
            }
        except Exception:
            status = 'error'
            msg = 'Erro desconhecido. Contacte o Administrador do Sistema'
            response = {
                'status': status,
                'msg': msg
            }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividade/')
api.add_resource(Atividade, '/atividade/<string:nome>/')
api.add_resource(AtividadeAltera, '/atividade/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)