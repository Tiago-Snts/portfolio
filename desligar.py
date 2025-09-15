import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey

os.system('cls')
os.system('shutdown /a')
print("********** caso queira cancelar o desligamento, abra o programa novamente! **********")

db = create_engine("sqlite:///tempo.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Tempo(Base):
        __tablename__="tempos"
        id = Column(Integer, primary_key=True, autoincrement=True)
        minuto = Column(Integer)

        def __init__(self, minuto):
            self.minuto = minuto


Base.metadata.create_all(bind=db)

tempo_existente = session.query(Tempo).first()

desligar = input("Você quer desligar o computador: (sim/não)")
if desligar in ['sim', 'Sim', 's', 'S']:
      if tempo_existente:
            usar_anterior = input(f"você quer usar o tempo anterior de {tempo_existente.minuto} minutos: (sim/não)")
            if usar_anterior in ['sim', 'Sim', 's', 'S']:
                  pergunta = tempo_existente.minuto
            else:
                  pergunta = int(input("digite o novo tempo em minutos: "))
                  session.delete(tempo_existente)
                  session.commit()
                  novo_tempo = Tempo(minuto=pergunta)
                  session.add(novo_tempo)
                  session.commit()
      else:
        pergunta = int(input("Digite o tempo em minutos: "))
        novo_tempo = Tempo(minuto=pergunta)
        session.add(novo_tempo)
        session.commit()
      minutos = pergunta*60
      print(f"Desligando o computador em {pergunta} minutos") 
      os.system(f"shutdown /s /t {minutos}")
else:
     print("cancelado")
     exit