# 同じ階層にあるXML書類を読み込む
import xml.etree.ElementTree as ET

tree = ET.parse("category_master_kakenhi.xml")
root = tree.getroot()

print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

from lxml import etree

tree2 = etree.parse("category_master_kakenhi.xml"  )
root2 = tree2.getroot()

print(root2.tag, root2.attrib)