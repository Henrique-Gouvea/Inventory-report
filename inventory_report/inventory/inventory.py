# from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, file, type_report):
        if type_report == "simples":
            return SimpleReport.generate(cls.verify_type_archive(file))

        if type_report == "completo":
            return CompleteReport.generate(cls.verify_type_archive(file))

    def verify_type_archive(file):
        if file.endswith("csv"):
            return CsvImporter.import_data(file)
        elif file.endswith("json"):
            return JsonImporter.import_data(file)
        elif file.endswith("xml"):
            return XmlImporter.import_data(file)
        else:
            return ValueError("Arquivo inválido")
