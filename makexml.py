import xml.etree.ElementTree as et
root = et.Element('root')
tree = et.ElementTree(element=root)

fruits = et.SubElement(root, 'fruits')

fruit = et.SubElement(fruits, 'fruit')
fruit_id = et.SubElement(fruit, 'name')
fruit_id.text = 'apple'
fruit_id = et.SubElement(fruit, 'price')
fruit_id.text = '100'

fruit = et.SubElement(fruits, 'fruit')
fruit_id = et.SubElement(fruit, 'name')
fruit_id.text = 'orange'
fruit_id = et.SubElement(fruit, 'price')
fruit_id.text = '200'

tree.write('fruits.xml', encoding='utf-8', xml_declaration=True)