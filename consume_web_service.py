from zeep import Client

'''
Create a SOAP client object
'''
client = Client('http://www.dneonline.com/calculator.asmx?WDSL')

'''
Call Operations Supported by the Web Service
'''

'''
ADD
'''

Sum = client.service.Add(5, 5)
print('Sum:', Sum)

'''
Multiply
'''

Product = client.service.Multiply(5, 5)
print('Product:', Product)

'''
Divide
'''

Quotient = client.service.Divide(5, 5)
print('Quotient:', Quotient)

'''
Subtract
'''

Difference = client.service.Subtract(5, 5)
print('Difference:', Difference)
