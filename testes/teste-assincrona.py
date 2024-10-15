# Testando programação assincrona

import asyncio

async def funcao_um():
    print('Função Um: Iniciando')
    await asyncio.sleep(3)
    print('Função Um: Terminando')

async def funcao_dois():
    print('Função Dois: Iniciando')
    await asyncio.sleep(2)
    print('Função Dois: Terminando')

async def principal():
    # Executar ambas as funções assíncronas ao mesmo tempo
    await asyncio.gather(funcao_um(), funcao_dois())

# Executar a função principal que coordena as outras
asyncio.run(principal())