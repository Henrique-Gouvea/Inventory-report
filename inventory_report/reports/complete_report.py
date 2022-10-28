# from helper.filters_simple_report import EarliestManufacturing
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def stock_by_company(data):
        companiesQuantityProducts = Counter(
            product["nome_da_empresa"] for product in data
        )
        print("/////////////////////////////////////////////////")
        print(companiesQuantityProducts)
        return companiesQuantityProducts

    def get_print_quantity(data):
        industry_quantity = ''
        for company, count in data.items():
            industry_quantity += f"- {company}: {count}\n"
        return industry_quantity

    @classmethod
    def generate(cls, data):
        return (
            super().generate(data)
            + "\nProdutos estocados por empresa:\n"
            + CompleteReport.get_print_quantity(
                CompleteReport.stock_by_company(data)
            )
        )
