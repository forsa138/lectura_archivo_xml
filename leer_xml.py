
"""
    Lectura y obtencion de datos de archivo xml.
    Archivo XML de muestra entregado por el Servicio de Impuestos Internos
"""

from xml.dom import minidom

doc = minidom.parse('factura.xml')
#print(doc.nodeName)
#print(doc.firstChild.tagName)


# datos proveedor
n_emisor = doc.getElementsByTagName("RznSoc")[0].firstChild.nodeValue
r_emisor = doc.getElementsByTagName("RUTEmisor")[0].firstChild.nodeValue
giroEmisor = doc.getElementsByTagName("GiroEmis")[0].firstChild.nodeValue

print('')
print('------ Datos del Proveedor ------')
print('Razon Social:    '+ n_emisor)
print('RUT:             '+ r_emisor)
print('Giro:            '+ giroEmisor)

print('')
print('------ Datos de Facturacion ------')

# fecha emision documento
fchEmision = doc.getElementsByTagName("FchEmis")[0].firstChild.nodeValue
print('Fecha Emision:   '+ fchEmision)


# detalle de la factura
documento = doc.getElementsByTagName("Documento")
for detalle in documento:
    getDetalle = detalle.getElementsByTagName("Detalle")
    for item in getDetalle:
        getItem = item.getElementsByTagName("NmbItem")[0].firstChild.nodeValue
        getCantidad = item.getElementsByTagName("QtyItem")[0].firstChild.nodeValue
        getPrecioUnit = item.getElementsByTagName("PrcItem")[0].firstChild.nodeValue
        getPrecioTotal = item.getElementsByTagName("MontoItem")[0].firstChild.nodeValue

        print('Nombre Item: '+getItem, '| Cantidad: '+getCantidad, '| P.Unitario: '+getPrecioUnit, '| P.Total: '+getPrecioTotal)

# Montos factura
montoNeto = doc.getElementsByTagName("MntNeto")[0].firstChild.nodeValue
montoIva = doc.getElementsByTagName("IVA")[0].firstChild.nodeValue
montoTotal = doc.getElementsByTagName("MntTotal")[0].firstChild.nodeValue

print('')
print('Monto Neto:      $'+montoNeto)
print('Monto Neto:      $'+montoIva)
print('Monto Neto:      $'+montoTotal)


#print(r_emisor)