from .xml import XmlAdapter

import os
CTE_XML = '/'.join([os.path.dirname(__file__), 'mocks/cte.xml'])


class TestParseXML():

    def test_read_xml(self):
        cte = XmlAdapter.from_xmlpath(CTE_XML)
        self.assertEqual(cte['cteProc__CTe__infCte__ide__cUF'].text, '35')
        self.assertEqual(cte['cteProc__CTe__infCte__ide__CFOP'].text, '5353')

    def test_not_found_field_xml(self):
        cte = XmlAdapter.from_xmlpath(CTE_XML)
        self.assertIsNone(cte['cteProc__CTe__infCte__ide__cUF1'])

    def test_read_empty_xml(self):
        with self.assertRaises(ET.ParseError):
            cte = XmlAdapter.from_xmlstr('')

    def test_get_all_keys(self):
        xml = open(CTE_XML).read()
        cte = XmlAdapter.from_xmlstr(xml)
        self.assertEqual(len(cte.keys()), 143)

    def test_get_all_objects_from_key(self):
        xml = open(CTE_XML).read()
        xml_parsed = XmlAdapter.from_xmlstr(xml)
        for key in xml_parsed.keys():
            self.assertIsNotNone(xml_parsed[key])

    def test_get_list_of_objects(self):
        xml = open(CTE_XML).read()
        cte = XmlAdapter.from_xmlstr(xml)
        infoQs = cte['cteProc__CTe__infCte__infCTeNorm__infCarga__infQ__qCarga']
        self.assertGreater(len(infoQs), 0)
