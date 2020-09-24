# coding: utf-8

import cupom
import pytest


def verifica_campo_obrigatorio_param(
    mensagem_esperada,
    nome_loja,
    logradouro,
    numero,
    complemento,
    bairro,
    municipio,
    estado,
    cep,
    telefone,
    observacao,
    cnpj,
    inscricao_estadual
):
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja_param(
            nome_loja,
            logradouro,
            numero,
            complemento,
            bairro,
            municipio,
            estado,
            cep,
            telefone,
            observacao,
            cnpj,
            inscricao_estadual
        )
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)


# Todas as variaveis preenchidas

NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"

TEXTO_ESPERADO_LOJA_COMPLETA = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_loja_completa():
    assert (
        cupom.dados_loja_param(
            NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL
        )
        == TEXTO_ESPERADO_LOJA_COMPLETA
    )


def test_nome_vazio():
    verifica_campo_obrigatorio_param(
        "O campo nome da loja é obrigatório",
        "",
        LOGRADOURO,
        NUMERO,
        COMPLEMENTO,
        BAIRRO,
        MUNICIPIO,
        ESTADO,
        CEP,
        TELEFONE,
        OBSERVACAO,
        CNPJ,
        INSCRICAO_ESTADUAL
    )


def test_logradouro_vazio():
    verifica_campo_obrigatorio_param(
        "O campo logradouro do endereço é obrigatório",
        NOME_LOJA,
        "",
        NUMERO,
        COMPLEMENTO,
        BAIRRO,
        MUNICIPIO,
        ESTADO,
        CEP,
        TELEFONE,
        OBSERVACAO,
        CNPJ,
        INSCRICAO_ESTADUAL
    )


TEXTO_ESPERADO_SEM_NUMERO = """Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_numero_zero():
    assert (
        cupom.dados_loja_param(
            NOME_LOJA,
            LOGRADOURO,
            0,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL
        )
        == TEXTO_ESPERADO_SEM_NUMERO
    )


TEXTO_ESPERADO_SEM_COMPLEMENTO = """Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_complemento():
    assert (
        cupom.dados_loja_param(
            NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            None,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL
        )
        == TEXTO_ESPERADO_SEM_COMPLEMENTO
    )


TEXTO_ESPERADO_SEM_BAIRRO = """Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_bairro():
    assert (
        cupom.dados_loja_param(
            NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            None,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL
        )
        == TEXTO_ESPERADO_SEM_BAIRRO
    )


def test_municipio_vazio():
    verifica_campo_obrigatorio_param("O campo município do endereço é obrigatório", NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            "",
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL)


def test_estado_vazio():
    verifica_campo_obrigatorio_param("O campo estado do endereço é obrigatório", NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            "",
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL)


TEXTO_ESPERADO_SEM_CEP = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_cep():
    assert cupom.dados_loja_param(NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            None,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL) == TEXTO_ESPERADO_SEM_CEP


TEXTO_ESPERADO_SEM_TELEFONE = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_telefone():
    assert cupom.dados_loja_param(NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            None,
            OBSERVACAO,
            CNPJ,
            INSCRICAO_ESTADUAL) == TEXTO_ESPERADO_SEM_TELEFONE


TEXTO_ESPERADO_SEM_OBSERVACAO = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_observacao():
    assert cupom.dados_loja_param(NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            None,
            CNPJ,
            INSCRICAO_ESTADUAL) == TEXTO_ESPERADO_SEM_OBSERVACAO


def test_cnpj_vazio():
    verifica_campo_obrigatorio_param("O campo CNPJ da loja é obrigatório", NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            "",
            INSCRICAO_ESTADUAL)


def test_inscricao_estadual_vazia():
    verifica_campo_obrigatorio_param("O campo inscrição estadual da loja é obrigatório", NOME_LOJA,
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            MUNICIPIO,
            ESTADO,
            CEP,
            TELEFONE,
            OBSERVACAO,
            CNPJ,
            "")


def test_exercicio2_customizado():

    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = "Boa vista Flores"
    logradouro = "Rua Jardim Peres"
    numero = 122
    complemento = "EUC F30/31/44"
    bairro = "Centro"
    municipio = "Monteiro"
    estado = "PB"
    cep = "58500000"
    telefone = "(99) 9999-9999"
    observacao = "Loja 122 (PDB)"
    cnpj = "22.300.551/0110-56"
    inscricao_estadual = "432.118.667.777"

    # E atualize o texto esperado abaixo
    assert (
        cupom.dados_loja_param(nome_loja, logradouro, numero, complemento, bairro, municipio, estado, cep, telefone, observacao, cnpj, inscricao_estadual)
        == 
"""Boa vista Flores
Rua Jardim Peres, 122 EUC F30/31/44
Centro - Monteiro - PB
CEP:58500000 Tel (99) 9999-9999
Loja 122 (PDB)
CNPJ: 22.300.551/0110-56
IE: 432.118.667.777"""
)

