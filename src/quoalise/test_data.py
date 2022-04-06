import unittest
import datetime as dt
from slixmpp.xmlstream import tostring, ET

from quoalise.data import Data, Record, Sensml, Metadata


class TestSenml(unittest.TestCase):

    DATA_ENERGY = [
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=1227032000,
            unit="Wh",
        ),
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index/distributor/hce",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=847000,
            unit="Wh",
        ),
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index/distributor/hch",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=527659000,
            unit="Wh",
        ),
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index/distributor/hpe",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=178857000,
            unit="Wh",
        ),
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index/distributor/hph",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=158636000,
            unit="Wh",
        ),
        Record(
            name="urn:dev:prm:30001642617347_consumption/energy/index/distributor/p",
            time=dt.datetime.fromisoformat("2022-03-17T23:40:08+00:00"),
            value=361033000,
            unit="Wh",
        ),
    ]

    def test_build_senml(self) -> None:

        sensml = Sensml()
        sensml.extend(self.DATA_ENERGY)
        # print(tostring(sensml.xml_element))
        records_before_compression = list(sensml.records())
        self.assertEqual(len(self.DATA_ENERGY), len(records_before_compression))
        sensml.compress()
        # print(tostring(sensml.xml_element))
        records_compressed = list(sensml.records())

        self.assertEqual(len(records_before_compression), len(records_compressed))

        for original, compressed in zip(records_before_compression, records_compressed):
            self.assertEqual(original.time, compressed.time)
            self.assertEqual(original.value, compressed.value)
            self.assertEqual(original.unit, compressed.unit)
            self.assertEqual(original.name, compressed.name)

    def test_metadata(self) -> None:
        as_dict = {
            "device": {
                "identifier": {
                    "authority": "enedis",
                    "type": "prm",
                    "value": "14419392069520",
                },
                "type": "electricity-meter",
            },
            "measurement": {
                "name": "active-power",
                "direction": "consumption",
                "quantity": "power",
                "type": "electrical",
                "unit": "W",
                "aggregation": "mean",
                "sampling-interval": "PT30M",
            },
        }
        metadata = Metadata(as_dict)
        as_xml = metadata.to_xml()
        back_to_dict = Metadata.from_xml(as_xml).as_dict
        self.assertEqual(as_dict, back_to_dict)

    def test_quoalise(self) -> None:

        quoalise = ET.Element("{urn:quoalise:0}quoalise")

        data = Data(metadata=None, records=self.DATA_ENERGY)
        quoalise.append(data.to_xml())

        print(tostring(quoalise))

    def test_senml_utc_timestamp(self) -> None:

        time = dt.datetime.strptime(
            "2021-02-01 00:00:00+0100",
            "%Y-%m-%d %H:%M:%S%z",
        )
        # GMT Sunday, 31 January 2021 23:00:00
        expected_timestamp = 1612134000.0

        self.assertEqual(expected_timestamp, Sensml.timestamp(time))

    def test_senml_rejects_naive_datetime(self) -> None:

        time = dt.datetime.strptime(
            "2021-02-01 00:00:00",
            "%Y-%m-%d %H:%M:%S",
        )

        with self.assertRaises(AssertionError):
            Sensml.timestamp(time)


if __name__ == "__main__":

    unittest.main()
