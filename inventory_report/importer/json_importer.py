from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        try:
            if not file.endswith(".json"):
                raise ValueError("Arquivo inválido")
            with open(file) as jsonfile:
                return json.load(jsonfile)
        except IOError:
            raise ValueError("Problema ao abrir arquivo")
