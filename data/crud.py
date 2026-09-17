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
    usuario = sessao.query(Usuario).filter_by(email = email).first()
    
    if not usuario:
        return {"status":"Erro", "mensagem":"Usuario não encontrado"}
    
    if usuario.senha != senha:
        return {"status":"Erro", "mensagem":"senha incorreta"}
    
    return {"status":"sucesso", "usuario":{
        "id" : usuario.id,
        "nome" : usuario.nome,
        "email": usuario.email,
        "papel" : usuario.papel
    }}

def salva_ideia(usuarios_id, titulo, conteudo):
    try:
        sessao = Sessao()
        nova = Ideia(usuarios_id = usuarios_id, titulo = titulo, conteudo = conteudo)
        sessao.add(nova)
        sessao.commit()
        sessao.refresh(nova)
        return {"status":"sucesso","retorno":nova}
    except Exception as e:
        return {"status":"erro", "retorno":e}


        

