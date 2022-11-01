from inventory_report.reports.colored_report import ColoredReport
from tests.factories.product_factory import ProductFactory
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    fake = ProductFactory()
    fake2 = ProductFactory()

    product_list = [
        {
            "id": fake.id,
            "nome_do_produto": fake.nome_do_produto,
            "nome_da_empresa": fake.nome_da_empresa,
            "data_de_fabricacao": fake.data_de_fabricacao,
            "data_de_validade": fake.data_de_validade,
            "numero_de_serie": fake.numero_de_serie,
            "instrucoes_de_armazenamento": fake.instrucoes_de_armazenamento,
        },
        {
            "id": fake2.id,
            "nome_do_produto": fake2.nome_do_produto,
            "nome_da_empresa": fake2.nome_da_empresa,
            "data_de_fabricacao": fake2.data_de_fabricacao,
            "data_de_validade": fake2.data_de_validade,
            "numero_de_serie": fake2.numero_de_serie,
            "instrucoes_de_armazenamento": fake2.instrucoes_de_armazenamento,
        },
    ]

    result_simples = ColoredReport(SimpleReport)
    report_simple = result_simples.generate([product_list[0]])

    correct = (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m"
        + str(fake.data_de_fabricacao)
        + "\033[0m"
        + "\n\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m"
        + str(fake.data_de_validade)
        + "\033[0m"
        + "\n\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31m"
        + str(fake.nome_da_empresa)
        + "\033[0m"
    )

    incorrect = (
        "\031[32mData de fabricação mais antiga:\031[0m "
        + "\031[36m"
        + str(fake.data_de_fabricacao)
        + "\031[0m"
        + "\n\031[32mData de validade mais próxima:\031[0m "
        + "\031[36m"
        + str(fake.data_de_validade)
        + "\031[0m"
        + "\n\031[32mEmpresa com mais produtos:\031[0m "
        + "\031[31m"
        + str(fake.nome_da_empresa)
        + "\031[0m"
    )

    assert correct == report_simple
    assert (incorrect == report_simple) is not True
