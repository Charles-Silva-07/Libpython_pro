from libpythonpro.spam.modelos import Usuario


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome='Charles')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def teste_listar_usuario(sessao):
    usuarios = [Usuario(nome='Charles'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()


