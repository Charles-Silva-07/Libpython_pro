import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviardor = Enviador()
    assert enviardor is not None


@pytest.mark.parametrize('destinatario', ['charlleshp@hotmail.com', 'edvaniavieira2021@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'charllesrocklp@gmail.com',
        'Curso python pro',
        'prairie turma'
    )
    assert destinatario in resultado


@pytest.mark.parametrize('remetente', ['charlleshphotmail.com', 'edvaniavieira2021gmail.com', ''])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente, 'charllesrocklp@gmail.com', 'Curso python pro', 'prairie turma')
