from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        with open(file) as xmlfile:
            return xmltodict.parse(xmlfile.read())["dataset"]["record"]
