import pytest

from libpythonpro.tests.test_spam.db import Conexao
from libpythonpro.tests.test_spam.modelos import Usuario


@pytest.fixture
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sesao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome='Charles')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def teste_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='Charles'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()


