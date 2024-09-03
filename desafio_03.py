import json

def processar_faturamento(arquivo_json):
    # Lê os dados de um arquivo JSON
    # O arquivo em si é só um exemplo e não faz leitura alguma
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    valores_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

    if not valores_faturamento:
        return "Não há faturamento para processar."

    menor_faturamento = min(valores_faturamento)
    maior_faturamento = max(valores_faturamento)

    media_mensal = sum(valores_faturamento) / len(valores_faturamento)

    dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

arquivo_json = 'dados.json'

resultados = processar_faturamento(arquivo_json)

if isinstance(resultados, dict):
    print(f"Menor faturamento do mês: R${resultados['menor_faturamento']:.2f}")
    print(f"Maior faturamento do mês: R${resultados['maior_faturamento']:.2f}")
    print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_da_media']}")
else:
    print(resultados)