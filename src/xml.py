import xml.etree.ElementTree as ET

class XmlAdapter():
    @classmethod
    def from_xmlstr(cls, xml_str):
        return cls(ET.fromstring(xml_str))

    @classmethod
    def from_xmlpath(cls, xml_path):
        return cls(ET.parse(xml_path).getroot())

    def __init__(self, xml, *args, **kw):
        self.xml = xml
        self.query = None
        self.cache = {}
        self.build()

    def __getitem__(self, key):
        if key.lower() in self.cache:
            return self.cache[key.lower()]

    def build(self):
        root = self.xml
        queue = [("", root)]

        def _strip(key):
            end = key.index('}')
            return key[end+1:].lower()

        while(len(queue) > 0):
            label, cur = queue.pop(0)
            if(cur.text is not None):
                key = label+'__'+_strip(cur.tag)
                if key in self.cache:
                    if type(self.cache[key]) == list:
                        self.cache[key].append(cur)
                    else:
                        self.cache[key] = [cur, self.cache[key]]
                else:
                    self.cache[key] = cur
            for child in cur.getchildren():
                if label != "":
                    key = label+"__"+_strip(cur.tag)
                    queue.append((key, child))
                else:
                    queue.append((_strip(cur.tag), child))

    def keys(self):
        return self.cache.keys()