from collections import defaultdict
import datetime as dt

#
# Quick and dirty quoalise data interface, to be improved / documented
#


class Record:
    def __init__(self, name, time, value, unit):

        self.name = name
        self.time = time
        self.value = value
        self.unit = unit

    @staticmethod
    def from_senml_xml(xml):
        records = []
        base_name = None
        base_time = None
        base_unit = None
        base_value = None

        for elem in xml.findall(".//{urn:ietf:params:xml:ns:senml}senml"):
            if "bn" in elem.attrib:
                base_name = elem.attrib["bn"]
            if "bt" in elem.attrib:
                base_time = int(elem.attrib["bt"])
            if "bu" in elem.attrib:
                base_unit = elem.attrib["bu"]
            if "bv" in elem.attrib:
                base_value = float(elem.attrib["bv"])

            name = elem.attrib.get("n", None)
            if base_name is not None:
                name = base_name + name if name is not None else base_name

            time = elem.attrib.get("t", None)
            if time is not None:
                time = int(time)
            if base_time is not None:
                time = base_time + time if time is not None else base_time
            if time is not None:
                time = dt.datetime.utcfromtimestamp(time)

            unit = elem.attrib.get("u", None)
            if base_unit is not None:
                unit = base_unit + unit if unit is not None else base_unit

            value = elem.attrib.get("v", None)
            if value is not None:
                value = float(value)
            if base_value is not None:
                value = base_value + value if value is not None else base_value

            record = Record(name, time, value, unit)
            records.append(record)
        return records


class Data:
    def __init__(self, quoalise_xml):

        self.xml = quoalise_xml

        meta = quoalise_xml.find(".//{urn:quoalise:0}data/{urn:quoalise:0}meta")
        self.meta = Data.xml_to_dict(meta)["meta"]

        records = quoalise_xml.find(
            ".//{urn:quoalise:0}data/{urn:ietf:params:xml:ns:senml}sensml"
        )
        self.records = Record.from_senml_xml(records)

    @classmethod
    def xml_to_dict(cls, t):
        # From K3---rnc on
        # https://stackoverflow.com/questions/7684333/converting-xml-to-dictionary-using-elementtree
        _, _, t.tag = t.tag.rpartition("}")  # strip ns
        d = {t.tag: {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(cls.xml_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update((k, v) for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    d[t.tag]["#text"] = text
            else:
                d[t.tag] = text
        return d
