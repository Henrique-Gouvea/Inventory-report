# from helper.filters_simple_report import EarliestManufacturing
from operator import itemgetter
from collections import Counter
from datetime import date


class SimpleReport:
    def EarliestManufacturing(data):
        earliest = min(data, key=itemgetter("data_de_fabricacao"))
        return earliest["data_de_fabricacao"]

    def ClosestExpirationDate(data):
        return min(
            date.fromisoformat(product["data_de_validade"])
            for product in data
            if date.fromisoformat(product["data_de_validade"]) >= date.today()
        ).isoformat()

    def companyMoreProducts(data):
        return Counter(
            [product["nome_da_empresa"] for product in data]
        ).most_common(1)[0][0]

    @staticmethod
    def generate(data):
        earliest_manufacturing_date = SimpleReport.EarliestManufacturing(data)
        closest_expiration_date = SimpleReport.ClosestExpirationDate(data)
        company_more_products = SimpleReport.companyMoreProducts(data)

        return (
            f"Data de fabricação mais antiga: {earliest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_more_products}"
        )
