from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#from ElementTree_pretty import prettify
import xml.etree.ElementTree as ET

'''top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that' '''

#  ss:ExpandedColumnCount="5" ss:ExpandedRowCount="6" x:FullColumns="1" x:FullRows="1" ss:DefaultColumnWidth="54" ss:DefaultRowHeight="15.75">
#    <Column ss:Index="3" ss:AutoFitWidth="0" ss:Width="76.5"/>

# <Column ss:Index="9" ss:AutoFitWidth="0" ss:Width="135.75"/>

row = 10
cell = 10

Table = Element('Table')
for i in range(row):
    Column = SubElement(Table, 'Column', attrib={"ss:Index": str(i + 2), "ss:AutoFitWidth": "0", "ss:Width": "42"})
Row = SubElement(Table, 'Row', attrib={"ss:AutoFitHeight":"0", "ss:Height":"42"})
Cell = SubElement(Row, 'Cell', attrib={"ss:MergeAcross":str(row-1), "ss:StyleID":"m1"})
Data = SubElement(Cell, 'Data', attrib={"ss:Type":"String"})
Data.text = 'ДЕКАБРЯ'
for x in range(row):
    Row = SubElement(Table, 'Row', attrib={"ss:AutoFitHeight":"0", "ss:Height":"42"})
    for y in range(cell):
        if x == 0: Cell = SubElement(Row, 'Cell', attrib={"ss:StyleID":"s2"})
        if x != 0: Cell = SubElement(Row, 'Cell', attrib={"ss:StyleID":"s1"})
        #Cell = SubElement(Row, 'Cell')
        #Cell.text = '2'

        Data = SubElement(Cell, 'Data', attrib={"ss:Type":"Number"})
        #Data = SubElement(Cell, 'Data')
        Data.text = str((x+1)*(y+1))



'''child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that' '''


#print (tostring(top, encoding='utf-8').decode('utf-8'))
print (tostring(Table, encoding='utf-8').decode('utf-8'))
#rint (prettify(top, encoding='utf8').decode('utf8'))

#top2 = ET.ElementTree(top)
#top2.write('22.xml')

#Table1 = ET.ElementTree(Table)
#Table1.write('23.xml')

f = open('text.xml', 'w')
a00 = f'<?xml version="1.0"?><?mso-application progid="Excel.Sheet"?><Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet" xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet" xmlns:html="http://www.w3.org/TR/REC-html40"><Styles><Style ss:ID="Default" ss:Name="Normal"><Font ss:FontName="Calibri" ss:Size="12" ss:Color="#000000"/></Style>'
#a0 = f'<?xml version="1.0"?><?mso-application progid="Excel.Sheet"?><Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet" xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet" xmlns:html="http://www.w3.org/TR/REC-html40"><Styles><Style ss:ID="Default" ss:Name="Normal"><Font ss:FontName="Calibri" ss:Size="12" ss:Color="#000000"/></Style><Style ss:ID="s1"><Borders><Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="0"/><Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="0"/><Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="0"/><Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="0"/></Borders></Style></Styles><Worksheet ss:Name="1">'
a0 = f'<Style ss:ID="s2"><Alignment ss:Horizontal="Center" ss:Vertical="Top"/><Borders><Border ss:Position="Bottom" ss:LineStyle="Continuous"/><Border ss:Position="Left" ss:LineStyle="Continuous"/><Border ss:Position="Right" ss:LineStyle="Continuous"/><Border ss:Position="Top" ss:LineStyle="Continuous"/></Borders></Style><Style ss:ID="s1"><Alignment ss:Horizontal="Left" ss:Vertical="Center"/><Borders><Border ss:Position="Bottom" ss:LineStyle="Continuous"/><Border ss:Position="Left" ss:LineStyle="Continuous"/><Border ss:Position="Right" ss:LineStyle="Continuous"/><Border ss:Position="Top" ss:LineStyle="Continuous"/></Borders></Style><Style ss:ID="m1"><Alignment ss:Horizontal="Center" ss:Vertical="Center"/></Style></Styles>'
a01 = f'<Worksheet ss:Name="1">'
a1 = tostring(Table, encoding='utf-8').decode('utf-8')
a2 = f'</Worksheet></Workbook>'

f.write(a00+a0+a01+a1+a2)
#f.write(a1)

f.close()