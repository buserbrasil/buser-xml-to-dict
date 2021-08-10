from src.xml_parser import XmlAdapter

import os
CTE_XML = '/'.join([os.path.dirname(__file__), 'mocks/cte.xml'])


class TestParseXML():

    def test_read_xml(self):
        cte = XmlAdapter.from_xmlpath(CTE_XML)
        assert cte['cteProc__CTe__infCte__ide__cUF'].text == '35'
        assert cte['cteProc__CTe__infCte__ide__CFOP'].text =='5353'

    def test_not_found_field_xml(self):
        cte = XmlAdapter.from_xmlpath(CTE_XML)
        assert cte['cteProc__CTe__infCte__ide__cUF'] != None


    def test_get_all_keys(self):
        xml = open(CTE_XML).read()
        cte = XmlAdapter.from_xmlstr(xml)
        assert len(cte.keys()) == 143

    def test_get_all_objects_from_key(self):
        xml = open(CTE_XML).read()
        xml_parsed = XmlAdapter.from_xmlstr(xml)
        for key in xml_parsed.keys():
            assert xml_parsed[key] != None
 
    def test_get_list_of_objects(self):
        xml = open(CTE_XML).read()
        cte = XmlAdapter.from_xmlstr(xml)
        infoQs = cte['cteProc__CTe__infCte__infCTeNorm__infCarga__infQ__qCarga']
        assert len(infoQs) > 0
