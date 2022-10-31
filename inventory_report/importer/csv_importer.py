from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        try:
            if not file.endswith(".csv"):
                raise ValueError("Arquivo inválido")
            with open(file) as csvfile:
                return list(csv.DictReader(csvfile))
        except IOError:
            raise ValueError("Problema ao abrir arquivo")
