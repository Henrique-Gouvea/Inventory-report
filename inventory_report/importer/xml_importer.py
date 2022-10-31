from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        try:
            if not file.endswith(".xml"):
                raise ValueError("Arquivo inválido")
            with open(file) as xmlfile:
                return xmltodict.parse(xmlfile.read())["dataset"]["record"]
        except IOError:
            raise ValueError("Problema ao abrir arquivo")
