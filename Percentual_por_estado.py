import re


def faturamento_mensal(lista):
    convertido_int = [int(re.sub(r'[^\d+\s]', '', numero)) for numero in lista]
    total = 0
    for num in convertido_int:
        total += num
    divisao = [round(numb / total * 100) for numb in convertido_int]
    return divisao


dados = ["SP – R$67.836,43", "RJ – R$36.678,66", "MG – R$29.229,88", "ES – R$27.165,48", "Outros – R$19.849,53"]
siglas_estados = [re.findall("\w+\s+", valor)[0] for valor in dados]
for numeros in range(len(siglas_estados)):
    print(f"O percentual de representação de {siglas_estados[numeros]}foi de {faturamento_mensal(dados)[numeros]}%")



