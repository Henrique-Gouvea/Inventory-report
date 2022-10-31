from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        with open(file) as jsonfile:
            return json.load(jsonfile)
