from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        with open(file) as csvfile:
            return list(csv.DictReader(csvfile))
