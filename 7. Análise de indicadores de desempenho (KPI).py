import pandas as pd

# Exemplo de dados de produtos e vendas
dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'Preço de Venda': [100, 200, 150, 50, 300],
    'Custo do Produto': [60, 120, 100, 30, 180],
    'Quantidade Vendida': [10, 15, 20, 30, 25]
}

# Criando um DataFrame com os dados
df = pd.DataFrame(dados)

# Calculando a margem de lucro de cada produto
df['Margem de Lucro (%)'] = ((df['Preço de Venda'] - df['Custo do Produto']) / df['Preço de Venda']) * 100

# Ticket médio (Total de Vendas / Número de Vendas)
df['Valor de Venda Total'] = df['Preço de Venda'] * df['Quantidade Vendida']
ticket_medio = df['Valor de Venda Total'].sum() / df['Quantidade Vendida'].sum()

# Produtos com margem de lucro baixa (Definido como margem < 10%)
produtos_com_margem_baixa = df[df['Margem de Lucro (%)'] < 10]

# Top 3 produtos mais lucrativos
df['Lucro Total'] = (df['Preço de Venda'] - df['Custo do Produto']) * df['Quantidade Vendida']
top_3_produtos = df.sort_values(by='Lucro Total', ascending=False).head(3)

# Exibindo os resultados
print("Ticket Médio: R$", round(ticket_medio, 2))
print("\nProdutos com Margem de Lucro Baixa (menor que 10%):")
print(produtos_com_margem_baixa[['Produto', 'Margem de Lucro (%)']])
print("\nTop 3 Produtos Mais Lucrativos:")
print(top_3_produtos[['Produto', 'Lucro Total']])







