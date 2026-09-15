from .models import Usuario, Ideia
from data.data_base import Sessao


def criar_usuario(nome, email, senha, papel ):
    try:
        sessao = Sessao()
        novo_usuario = Usuario(nome = nome, email = email, senha = senha, papel = papel)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return {"Status":"Sucesso", "mensagem":f"Usuario {nome} adicionado com sucesso"}
    except Exception as e:
        return {"status":"Erro","mensagem": f"Erro ao criar usuario {e}"}

def fazer_login(email, senha):
    sessao = Sessao()
    Usuario = sessao.query(Usuario).filter_by(email = email).first()
    
    if not Usuario:
        return {"status":"Erro", "mensagem":"Usuario não encontrado"}
    
    if Usuario.senha != senha:
        return {"status":"Erro", "mensagem":"senha incorreta"}
    
    return {"status":"sucesso", "mensagem":"Acesso permitido"}
        

