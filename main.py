import duckdb

conexao = duckdb.connect()

consulta = """
select
    categoria,
    count(*) as total_vendas,
    sum(quantidade) as total_itens,
    sum(quantidade * preco) as receita_total,
    avg(preco) as produto_medio
from 'data/vendas.csv'
group by categoria
order by receita_total desc
"""

resultado = conexao.execute(consulta).df()
print(resultado)