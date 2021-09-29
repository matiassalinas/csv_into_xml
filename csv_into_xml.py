from xml.dom import minidom
import os
import csv

# Initialize doc xml
doc = minidom.Document()
xml = doc.createElement('main')
doc.appendChild(xml)

# Read csv
with open('input.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	header = next(csv_reader)
	for row in csv_reader:
		row_data = doc.createElement('row')
		for index, value in enumerate(header):
			tag = doc.createElement(value) # Header value
			text = doc.createTextNode(row[index]) # Row value
			tag.appendChild(text)
			row_data.appendChild(tag) # <tag>text</tag>
		xml.appendChild(row_data)

# Generate output xml
xml_str = doc.toprettyxml(indent ="\t")
path_file = "output.xml"
with open(path_file, "w") as f:
	f.write(xml_str)
