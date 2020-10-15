import PySimpleGUI as sg      
import hashlib
import re      

# calculate data checksum by xor all data bytes with 0   
def ChecksumCalculate(input_str, HavePrefix0x):          
    extract_data = re.findall(r'0x[0-9A-F]+', input_str, re.I)
    checksum_val = 0
    for i in extract_data:
        i = i[2:]
        checksum_val = checksum_val ^ int(i)

    print("Check sum value", checksum_val)
    return checksum_val
layout = [ [sg.Txt('Enter values to calculate')],      
           [sg.In(size=(50,1), key='numerator')],
           [sg.Checkbox('Have Prefix 0x',size=(20,1), key = 'HavePrefix0x')],      
           [sg.Txt('Checksum value')],             
           [sg.Txt('', size=(50,1), key='output')  ],      
           [sg.Button('Calculate', bind_return_key=True)]]

window = sg.Window('Math', layout)

while True:      
    event, values = window.Read()

    if event is not None:       
        calc = ChecksumCalculate(values['numerator'], values['HavePrefix0x'])        
        window.Element('output').Update(calc)      
    else:      
        break
  