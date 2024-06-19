from conversor_medidas import ConversorMedidas



print("[1]. converter_CM_para_M")

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = ConversorMedidas.converter_CM_para_M(value)



print('Result:', result)