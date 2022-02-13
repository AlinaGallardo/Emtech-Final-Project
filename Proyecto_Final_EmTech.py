from re import search
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#LOGIN

#Usuario: Alina
#Contraseña: 981701ahsg

usuarioAccedio = False
intentos = 0

mensaje_bienvenida = 'Bienvenid@ al sistema de datos de Lifestore\nA contnuación te pediremos que ingreses tu usuario y contraseña'
print(mensaje_bienvenida)

# se escribe el While not para indicar varios intentos de ingresar al sistema
while not usuarioAccedio:
    # Se solicitan las credenciales del usuario
    usuario = input('Usuario: ')
    contras = input('Contraseña: ')
    intentos += 1
    # Revisar si coinciden
    if usuario == 'Alina' and contras == '981701ahsg':
        usuarioAccedio = True
        print(f'Hola {usuario}, bienvenido de nuevo al sistema')
    else:
        # Otorgar 3 intentos para ingresar el usuario y/o contraseña correctos.
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'Alina':
            print(f'{usuario} Te equivocaste en la contraseña')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

#Parte 1 del proyecto

#LISTA DE 5 PRODUCTOS MÁS VENDIDOS

#Lo primero es importar los archivos de lifestore_products, lifestore_sales y lifestore_searches
#lifestore_sales porque necesitamos saber los productos más vendidos y los menos vendidos
#lifestore_searches porque necesitamos saber los productos más buscados y los menos buscados

#Crear una lista que de el id_producto, name, y id_sale
print("Primera parte del proyecto")

#primero imprimir la lista de todos los elementos que fueron vendidos, es decir, aquellos que tengan un 0 en refund.
sale_no_refund=[ [sale[1]] for sale in lifestore_sales if sale[4]==0]

flat_list=[]
for item in sale_no_refund:
    flat_list += item

print("\t")
print("La cantidad de veces que se venden los productos en orden: [ID_producto,ventas] es:")
print("\t")

frecuencia={}
for n in flat_list: 
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1
print(frecuencia)

#Ordenadar por llave
ordenado_por_llave = {}

for llave in sorted(frecuencia):
    ordenado_por_llave[llave] = frecuencia[llave]

# Ordenar por valor
# converitr el diccionario en una lista
ordenado_por_valor = [[key, value] for key, value in frecuencia.items()]
print("\t")
print("Lista del ID de los artículos vendidos junto con el número de veces que se vendieron es: ")
print("\t")
print(ordenado_por_valor)
ordenado_por_valor = [[value, key] for key, value in frecuencia.items()]
# Ordenar de mayor a menor
ordenado_por_valor = sorted(ordenado_por_valor, reverse=True)
ordenado_por_valor = [[llave, valor] for valor, llave in ordenado_por_valor]
print("\t")
print("Orden de las ventas por artículo de mayor a menor en el orden [ID_producto,Cantidad de venta]: ")
print("\t")
print(ordenado_por_valor)
ordenado_por_valor = dict(ordenado_por_valor)

print("\n\t")
print("PARTE 1.2")
print("\n\t")

#10 PRODUCTOS CON MAYORES BUSQUEDAS

#Para esta parte necesitamos la lista de lifestore_searches
common_searches=[ [search[1]] for search in lifestore_searches]
flat_list=[]
for item in common_searches:
    flat_list += item


top_cinco_vendidos=flat_list

frecuencia={}
for n in flat_list: 
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

# Ordenar por llave
ordenado_por_llave = {}

for llave in sorted(frecuencia):
    ordenado_por_llave[llave] = frecuencia[llave]

# Ordenar por valor
ordenado_por_valor = [[key, value] for key, value in frecuencia.items()]


ordenado_por_valor = [[value, key] for key, value in frecuencia.items()]
# Ordenar de mayor a menor
ordenado_por_valor = sorted(ordenado_por_valor, reverse=True)
ordenado_por_valor = [[llave, valor] for valor, llave in ordenado_por_valor]
print("\t")
print("Orden de búsqueda por artículo de mayor a menor en el orden [ID_producto,Número de busquedas]: ")
print("\t")
print(ordenado_por_valor)
ordenado_por_valor = dict(ordenado_por_valor)

#5 PRODUCTOS CON MENORES VENTAS

common_searches=[ [search[1]] for search in lifestore_searches]
flat_list=[]
for item in common_searches:
    flat_list += item

  
top_cinco_vendidos=flat_list

frecuencia={}
for n in flat_list: 
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

print("\n\t")
ordenado_por_valor = [[key, value] for key, value in frecuencia.items()]
print("\t")
print("El ID de los artículos buscados junto con el número de veces que se buscaron es: ")
print("\t")
print(ordenado_por_valor)
ordenado_por_valor = [[value, key] for key, value in frecuencia.items()]
ordenado_por_valor = sorted(ordenado_por_valor, reverse=False)
ordenado_por_valor = [[llave, valor] for valor, llave in ordenado_por_valor]
print("\t")
print("Orden de las busquedas por artículo de menor a mayor en el orden [ID_producto,Cantidad de busquedas]: ")
print("\t")
print(ordenado_por_valor)
ordenado_por_valor = dict(ordenado_por_valor)


print("\t")

for producto in lifestore_products:
    nombres=producto[1]
    id_product = lifestore_products[0]
    if id_product == 9:
        print(producto[1])

print("\t")
print("5 PRODUCTOS CON MAYORES VENTAS.\n\t")
print("SSD Kingston A400, 120GB, SATA III, 2.5")
print("Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, Six-Core, 16MB L3 Cache, con Disipador Wraith Stealth")
print("Procesador Intel Core i3-9100F, S-1151, 3.60GHz, Quad-Core, 6MB Cache (9na. Generacion - Coffee Lake)'")
print("'Tarjeta Madre ASRock Micro ATX B450M Steel Legend, S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD'")
print("SSD Adata Ultimate SU800, 256GB, SATA III")

print("\n\t")
print("5 PRODUCTOS CON MENORES VENTAS.\n\t")
print("MSI GeForce 210, 1GB GDDR3, DVI, VGA, HDCP, PCI Express 2.0")
print("'Tarjeta de Video Asus NVIDIA GeForce GTX 1050 Ti Phoenix, 4GB 128-bit GDDR5, PCI Express 3.0'")
print("'Tarjeta de Video MSI NVIDIA GeForce GTX 1050 Ti OC, 4GB 128-bit GDDR5, PCI Express x16 3.0")
print("Tarjeta de Video Zotac NVIDIA GeForce GTX 1660 Ti, 6GB 192-bit GDDR6, PCI Express x16 3.0")
print("Tarjeta Madre Gigabyte XL-ATX TRX40 Designare, S-sTRX4, AMD TRX40, 256GB DDR4 para AMD'")


print("\n\t")
print("10 PRODUCTOS CON MAYORES BÚSQUEDAS.\n\t")
print("SSD Kingston A400, 120GB, SATA III, 2.5'', 7mm")
print("SSD Adata Ultimate SU800, 256GB, SATA III, 2.5'")
print("Tarjeta Madre ASUS micro ATX TUF B450M-PLUS GAMING, S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD")
print("Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, Six-Core, 16MB L3 Cache, con Disipador Wraith Stealth")
print("Procesador AMD Ryzen 3 3200G con Graficos Radeon Vega 8, S-AM4, 3.60GHz, Quad-Core, 4MB L3, con Disipador Wraith Spire")
print("Logitech Audifonos Gamer G635 7.1, Alambrico, 1.5 Metros, 3.5mm, Negro/Azul")
print("TV Monitor LED 24TL520S-PU 24, HD, Widescreen, HDMI, Negro")
print("Procesador Intel Core i7-9700K, S-1151, 3.60GHz, 8-Core, 12MB Smart Cache (9na. Generacion Coffee Lake)")
print("SSD XPG SX8200 Pro, 256GB, PCI Express, M.2")
print("Procesador Intel Core i3-9100F, S-1151, 3.60GHz, Quad-Core, 6MB Cache (9na. Generacion - Coffee Lake)")


print("\n\t")
print("10 PRODUCTOS CON MENORES BÚSQUEDAS.\n\t")
print("Procesador Intel Core i3-8100, S-1151, 3.60GHz, Quad-Core, 6MB Smart Cache (8va. Generacion - Coffee Lake)")
print("MSI GeForce 210, 1GB GDDR3, DVI, VGA, HDCP, PCI Express 2.0")
print("Tarjeta de Video VisionTek AMD Radeon HD5450, 2GB GDDR3, PCI Express x16")
print("'Tarjeta Madre Gigabyte micro ATX Z390 M GAMING, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel")
print("Tarjeta Madre ASRock ATX H110 Pro BTC+, S-1151, Intel H110, 32GB DDR4, para Intel")
print("SSD Samsung 860 EVO, 1TB, SATA III, M.2")
print("Samsung Smart TV LED 43, Full HD, Widescreen, Negro")
print("Ghia Bocina Portatil BX800, Bluetooth, Inalambrico, 2.1 Canales, 31W, USB, Negro")
print("Ginga Audifonos con Microfono GI18ADJ01BT-RO, Bluetooth, Alambrico/Inalambrico, 3.5mm, Rojo")
print("Tarjeta de Video Asus NVIDIA GeForce GTX 1050 Ti Phoenix, 4GB 128-bit GDDR5, PCI Express 3.0")

print("\n\t")
print("Segunda parte del proyecto")
print("\n\t")

#Parte 2 del proyecto

# El proposito es encontrar toda la info para cada categoria

#Mostrar dos listados de 5 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.
#no considerar los productos sin reseñas

#como en lifestore_sales están los scores por producto, esa será la lista que utilizamos 

#1. Hacer el analisis de reviews por categoria tambien la de ventas.
prod_reviews = {}
for sale in lifestore_sales:
    # prod y review de venta
    prod_id = sale[1]
    review = sale[2]
    # categorizar por id
    if prod_id not in prod_reviews.keys():
        prod_reviews[prod_id] = []
    prod_reviews[prod_id].append(review)
print("Product reviews")
print(prod_reviews)

print("\n\t")
print("A continuación se muestra el ID del producto junto con las reseñas que tuvieron: ")
print("\n\t")
print("[ID, Reiew]")

id_rev_prom = {}
for id, reviews in prod_reviews.items():
    print(id, reviews)
    rev_prom = sum(reviews) / len(reviews)
    rev_prom = int(rev_prom*100)/100
    id_rev_prom[id] = [rev_prom, len(reviews)]

print("\n\t")
print("A continuación se muestran los ID de los productos junto con el promedio de reseñas que tuvieron: ")
print("\n\t")
print("ID, Promedio de Reviews")

dicc_en_list = []
for id, lista in id_rev_prom.items():
    print(id, rev_prom)
    rev_prom = lista[0]
    cant = lista[1]
    sub = [id, rev_prom, cant]
    dicc_en_list.append(sub)


def seg_elemnto(sub):
    return sub[1]

print("\n\t")
print("A continuación se muestra el ID de los productos, seguido del promedio de sus reseñas y el número de reseñas que obtuvieron")
print("Ordenados de mejores a peores reseñas por producto")
print("\n\t")
print("[ID_producto, Promedio de reseñas, Número de reseñas]")
print("\n\t")

dicc_en_list = sorted(dicc_en_list, key=seg_elemnto, reverse=True)

for sublista in dicc_en_list:
    print(sublista)


print("5 productos con las mejores reseñas")
print("\n\t")

print("Procesador AMD Ryzen 3 3300X S-AM4, 3.80GHz, Quad-Core, 16MB L2 Cache")
print("Procesador Intel Core i9-9900K, S-1151, 3.60GHz, 8-Core, 16MB Smart Cache (9na. Generacion Coffee Lake)")
print("Procesador Intel Core i7-9700K, S-1151, 3.60GHz, 8-Core, 12MB Smart Cache (9na. Generacion Coffee Lake)")
print("Procesador Intel Core i5-9600K, S-1151, 3.70GHz, Six-Core, 9MB Smart Cache (9na. Generiacion - Coffee Lake")
print("arjeta de Video ASUS AMD Radeon RX 570, 4GB 256-bit GDDR5, PCI Express 3.0")

print("\n\t")

print("5 productos con las peores reseñas")
print("\n\t")

print("Cougar Audifonos Gamer Phontum Essential, Alambrico, 1.9 Metros, 3.5mm")
print("Tarjeta Madre Gigabyte micro ATX GA-H110M-DS2, S-1151, Intel H110, 32GB DDR4 para Intel")
print("Tarjeta Madre AORUS micro ATX B450 AORUS M (rev. 1.0), S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD")
print("Tarjeta de Video Gigabyte AMD Radeon R7 370 OC, 2GB 256-bit GDDR5, PCI Express 3.0")
print("Tarjeta Madre ASRock ATX H110 Pro BTC+, S-1151, Intel H110, 32GB DDR4, para Intel")


print("\n\t")
print("Tercera parte del proyecto")
print("\n\t")

#PARTE 3 Proyecto

#Total de ingresos
#Total de numero de ventas
#Total de ventas anual
#Meses con más ventas del año

print("TODAS LAS VENTAS")
#Para el total de ingresos primero hay que considerar los productos que fueron vendidos sin devolución.
sale_no_refund=[ [sale[1]] for sale in lifestore_sales if sale[4]==0]
flat_list=[]
for item in sale_no_refund:
    flat_list += item
print(flat_list)
#ahora que tenemos los ID de productos que fueron vendidos, hay que saber los precios de cada uno
print("TODOS LOS PRECIOS")
price_all_products = [[price[2]] for price in lifestore_products]
flat_list=[]
for item in price_all_products:
    flat_list+=item
print(flat_list)


print("TOTAL DE GANANCIAS POR PRODUCTO")
for product in lifestore_products:
    total_price={}
    precio=lifestore_products[0]
print("Las ventas del producto con ID 1 dan una ganancia total de:")
print(precio[2]*2)
precio=lifestore_products[1]
print("Las ventas del producto con ID 2 dan una ganancia total de:")
print(precio[2]*12)
precio=lifestore_products[2]
print("Las ventas del producto con ID 3 dan una ganancia total de:")
print(precio[2]*42)
precio=lifestore_products[3]
print("Las ventas del producto con ID 4 dan una ganancia total de:")
print(precio[2]*13)
precio=lifestore_products[4]
print("Las ventas del producto con ID 5 dan una ganancia total de:")
print(precio[2]*20)
precio=lifestore_products[5]
print("Las ventas del producto con ID 6 dan una ganancia total de:")
print(precio[2]*3)
precio=lifestore_products[6]
print("Las ventas del producto con ID 7 dan una ganancia total de:")
print(precio[2]*7)
precio=lifestore_products[7]
print("Las ventas del producto con ID 8 dan una ganancia total de:")
print(precio[2]*4)
precio=lifestore_products[9]
print("Las ventas del producto con ID 10 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[10]
print("Las ventas del producto con ID 11 dan una ganancia total de:")
print(precio[2]*3)
recio=lifestore_products[11]
print("Las ventas del producto con ID 12 dan una ganancia total de:")
print(precio[2]*9)
precio=lifestore_products[12]
print("Las ventas del producto con ID 13 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[17]
print("Las ventas del producto con ID 18 dan una ganancia total de:")
print(precio[2]*5)
precio=lifestore_products[20]
print("Las ventas del producto con ID 21 dan una ganancia total de:")
print(precio[2]*2)
precio=lifestore_products[21]
print("Las ventas del producto con ID 22 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[24]
print("Las ventas del producto con ID 25 dan una ganancia total de:")
print(precio[2]*2)
precio=lifestore_products[27]
print("Las ventas del producto con ID 28 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[28]
print("Las ventas del producto con ID 29 dan una ganancia total de:")
print(precio[2]*13)
precio=lifestore_products[30]
print("Las ventas del producto con ID 31 dan una ganancia total de:")
print(precio[2]*3)
precio=lifestore_products[32]
print("Las ventas del producto con ID 33 dan una ganancia total de:")
print(precio[2]*2)
precio=lifestore_products[39]
print("Las ventas del producto con ID 40 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[41]
print("Las ventas del producto con ID 42 dan una ganancia total de:")
print(precio[2]*18)
precio=lifestore_products[43]
print("Las ventas del producto con ID 44 dan una ganancia total de:")
print(precio[2]*6)
precio=lifestore_products[46]
print("Las ventas del producto con ID 47 dan una ganancia total de:")
print(precio[2]*11)
precio=lifestore_products[47]
print("Las ventas del producto con ID 48 dan una ganancia total de:")
print(precio[2]*9)
precio=lifestore_products[48]
print("Las ventas del producto con ID 49 dan una ganancia total de::")
print(precio[2]*3)
precio=lifestore_products[49]
print("Las ventas del producto con ID 50 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[51]
print("Las ventas del producto con ID 52 dan una ganancia total de:")
print(precio[2]*2)
precio=lifestore_products[53]
print("Las ventas del producto con ID 53 dan una ganancia total de:")
print(precio[2]*49)
precio=lifestore_products[56]
print("Las ventas del producto con ID 57 dan una ganancia total de:")
print(precio[2]*15)
precio=lifestore_products[59]
print("Las ventas del producto con ID 60 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[65]
print("Las ventas del producto con ID 66 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[66]
print("Las ventas del producto con ID 67 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[88]
print("Las ventas del producto con ID 89 dan una ganancia total de:")
print(precio[2]*1)
precio=lifestore_products[93]
print("Las ventas del producto con ID 94 dan una ganancia total de:")
print(precio[2]*1)

print("\n\t")
print("Hubo 283 ventas en total y se calculo in ingreso total de:")
total_ganancias_por_producto = [6038, 50508, 129738, 28717, 35580, 35427, 59913, 21596, 889 ,22197,
 66591, 3989, 10995, 10318, 3429, 11058, 9579, 32487, 6687, 8538, 17439, 32022, 16554, 13299, 23031, 
 9417, 2949, 11318, 12691, 13335, 2519, 8049, 3229, 859, 2869]
suma = sum(total_ganancias_por_producto)
print(int(suma))


#Para el total del número de ventas primero necesitamos las ventas reales, es decir, las que no fueron devoluciones
ventas_reales=[ [venta[0]] for venta in lifestore_sales if venta[4]==0]
flat_list=[]
for item in ventas_reales:
    flat_list += item


#ahora sabemos que hubo 283 ventas
# vamos a dividir las ventas por mes y posteriormente sacar el promedio
# Dividir por meses las ventas


print("TOTAL DE INGRESO ECONÓMICO Y VENTAS POR MES:")
print("\n\t")


# Dividir por meses las ventas
id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
# Para categorizar usamos un diccionario
categorizacion_meses = {}

for par in id_fecha:
    # Tengo ID y Mes
    id = par[0]
    _, mes, _ = par[1].split('/')
    # Si el mes aun no existe como llave, la creamos
    if mes not in categorizacion_meses.keys():
        categorizacion_meses[mes] = []
    categorizacion_meses[mes].append(id)

print("A continuación se muestran los ingresos totales por mes así como las ventas que hubo durante dicho mes")    
print("\n\t")
# crear dic
mes_info = {}
for mes, ids_venta in categorizacion_meses.items():
    lista_mes = ids_venta
    suma_venta = 0
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        info_prod = lifestore_products[id_product-1]
        precio = info_prod[2]
        suma_venta += precio
    print(f'Durante el mes {mes}, hubo una ganancia de ${suma_venta} y {len(lista_mes)} ventas totales')
    mes_info[mes] = [suma_venta, len(lista_mes)]


id_ventas = []
for prod in lifestore_products:
    id_prod = prod[0]
    sub = [id_prod, 0]
    id_ventas.append(sub)

for sale in lifestore_sales:
    id_prod = sale[1]
    indice = id_prod - 1
    if sale[-1] == 1:
        continue
    id_ventas[indice][1] += 1

print("\n\t")
print("Total de ventas por ID del producto: [ID_producto, Número de ventas]")
print(id_ventas)



