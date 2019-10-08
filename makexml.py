import xml.etree.ElementTree as et
root = et.Element('math')
tree = et.ElementTree(element=root)

function = et.SubElement(root, 'mi')

fruit = et.SubElement(function, 'fruit')
fruit_id = et.SubElement(function, 'name')
fruit_id.text = 'apple'
fruit_id = et.SubElement(function, 'price')
fruit_id.text = '100'

fruit = et.SubElement(function, 'fruit')
fruit_id = et.SubElement(function, 'name')
fruit_id.text = 'orange'
fruit_id = et.SubElement(function, 'price')
fruit_id.text = '200'

tree.write('fruits.xml', encoding='utf-8', xml_declaration=True)