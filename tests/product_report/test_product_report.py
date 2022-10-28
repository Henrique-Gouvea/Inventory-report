from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_relatorio_produto():
    fake = ProductFactory()
    product = Product(
        fake.id,
        fake.nome_do_produto,
        fake.nome_da_empresa,
        fake.data_de_fabricacao,
        fake.data_de_validade,
        fake.numero_de_serie,
        fake.instrucoes_de_armazenamento,
    )

    data = (
        f"O produto {fake.nome_do_produto}"
        f" fabricado em {fake.data_de_fabricacao}"
        f" por {fake.nome_da_empresa} com validade"
        f" até {fake.data_de_validade}"
        f" precisa ser armazenado {fake.instrucoes_de_armazenamento}."
    )

    assert product.__repr__() == data
    assert len(product.__repr__()) == len(data)
