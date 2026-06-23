import pandas as pd
from conexao import conectar

conexao = conectar()
# Lê os dados direto do MySQL para um DataFrame do Pandas
df = pd.read_sql("SELECT * FROM vendas", conexao)

print("\n--- DADOS CADASTRADOS NO BANCO DE DADOS ---")
print(df)
print("-------------------------------------------\n")

conexao.close()
