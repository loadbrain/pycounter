import os

from lxml import etree

from pycounter import report


def _elements_equal(e1, e2):
    if e1.tag != e2.tag:
        return False
    if e1.text != e2.text:
        return False
    if e1.tail != e2.tail:
        return False
    if e1.attrib != e2.attrib:
        return False
    if len(e1) != len(e2):
        return False
    return all(_elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


def assert_equiv_xml(expect, xml):
    obj1 = etree.fromstring(expect)
    obj2 = etree.fromstring(xml)

    assert _elements_equal(obj1, obj2)


def test_xml():
    with open(os.path.join(os.path.dirname(__file__),
              'data', 'JR1.xml'), 'rb') as expected_file:
        expected_data = expected_file.read()
    rep = report.parse(os.path.join(os.path.dirname(__file__),
                       'data', 'C4JR1.csv'))
    assert_equiv_xml(expected_data, rep.as_xml())
