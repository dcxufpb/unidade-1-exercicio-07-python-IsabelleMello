# coding: utf-8

def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):
    # Implemente aqui

    if not nome_loja:
        raise Exception ("O campo nome da loja é obrigatório")
    if not logradouro:
        raise Exception ("O campo logradouro do endereço é obrigatório")
    
    _logradouro = logradouro + ", "
    _numero = "s/n" if numero == 0 else str(numero)
    _complemento = " " + complemento if complemento else ""
    _bairro = bairro + " - " if bairro else ""

    if not municipio:
        raise Exception ("O campo município do endereço é obrigatório")
        
    _municipio = municipio + " - "

    if not estado:
        raise Exception ("O campo estado do endereço é obrigatório")
   
    _cep = "CEP:" + cep if cep else ""
    _telefone = "Tel " + telefone if telefone else ""
    _telefone = " " + _telefone if cep and telefone else _telefone
    _observacao = observacao if observacao else ""

    if not cnpj:
        raise Exception ("O campo CNPJ da loja é obrigatório")
    
    _cnpj = "CNPJ: " + cnpj

    if not inscricao_estadual:
        raise Exception ("O campo inscrição estadual da loja é obrigatório")
    
    _inscricao_estadual = "IE: " + inscricao_estadual
    
    return (f"""{nome_loja}
{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{estado}
{_cep}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}""")