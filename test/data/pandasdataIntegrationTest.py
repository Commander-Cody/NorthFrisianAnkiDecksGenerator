import unittest

from AnkiDeckGenerator.data.pandasdata import GoogleSpreadSheet


class TestGoogleSheetUrl(unittest.TestCase):
    def testRetrieveDataFromGoogleSheets(self):
        sheet = GoogleSpreadSheet('1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs')
        data = sheet.get_data_from('FriesischerSprachkurs1Laks1')
        self.assertGreater(data.size, 1000)


if __name__ == '__main__':
    unittest.main()
