import pandas as pd
from conexao import conectar

# Ler Arquivo CSV
df = pd.read_csv("vendas.csv")

# Conectar ao banco de dados
conexao = conectar()
cursor = conexao.cursor()

# Inserir dados
for _, linha in df.iterrows():
    cursor.execute(
        """
        INSERT INTO vendas (id, cliente, produto, valor)
        VALUES (%s, %s, %s, %s)
        """,
        (
            int(linha["id"]),
            linha["cliente"],
            linha["produto"],
            float(linha["valor"])
        )
    )

# Salvar alteracao
conexao.commit()

print("Dados importados com sucesso!")

cursor.close()
conexao.close()
