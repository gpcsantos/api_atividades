from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tarefa_new.db',convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__='programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)
    email = Column(String(50), index=True)

    def __repr__(self):
        return '<Dev: {}-{} | idade: {}>'.format(self.id,self.nome,self.idade)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Habilidade(Base):
    __tablename__='habilidade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    def __repr__(self):
        return '<habilidade: {}-{}>'.format(self.id,self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class ProgramadorHabilidade(Base):
    __tablename__ = 'programador_habiliade'
    id = Column(Integer, primary_key=True)
    fk_programador = Column(Integer,ForeignKey('programador.id'))
    programador = relationship('Programador')
    fk_habilidade = Column(Integer,ForeignKey('habilidade.id'))
    habilidade = relationship('Habilidade')

    def __repr__(self):
        return '<id: {} - fk_programador: {} - fk_habilidade: {}>'.format(self.id, self.fk_programador, self.fk_habilidade)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
