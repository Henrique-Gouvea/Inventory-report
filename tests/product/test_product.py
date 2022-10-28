from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():
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

    assert product.id == fake.id
    assert product.nome_do_produto == fake.nome_do_produto
    assert product.nome_da_empresa == fake.nome_da_empresa
    assert product.data_de_fabricacao == fake.data_de_fabricacao
    assert product.data_de_validade == fake.data_de_validade
    assert product.numero_de_serie == fake.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento == fake.instrucoes_de_armazenamento
    )
