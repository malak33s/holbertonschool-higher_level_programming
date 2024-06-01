#!/usr/bin/python3
"""Serialization and deserialization with XML as alternative format JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary XML file"""
    root_element = ET.Element("data")

    for a, b in dictionary.items():
        child_element = ET.SubElement(root_element, a)
        child_element.text = str(b)

    tree = ET.ElementTree(root_element)

    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserialize data XML file"""
    tree = ET.parse(filename)
    root_element = tree.getroot()

    dictio = {}

    for child in root_element:
        dictio[child.tag] = child.text

    return dictio
