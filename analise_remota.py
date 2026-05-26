# Importando a biblioteca pandas
import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv("faturamento_ti.csv")

# Criando a nova coluna com a fórmula:
# Faturamento = 50 * Horas + 200

dados["Total_Cobrado_R$"] = 50 * dados["Horas_Suporte"] + 200

# Calculando a média do faturamento
media_faturamento = dados["Total_Cobrado_R$"].mean()

# Mostrando a média no terminal
print("Média de faturamento: R$", media_faturamento)

# Exportando o relatório final
dados.to_csv("relatorio_ti_final.csv", index=False)

print("Relatório final criado com sucesso!")