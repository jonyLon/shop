import json
database = 'database.json'
def fillDatabase(data):
  with open(database,'w') as file:
    file.write(json.dumps(data))

data = [
    {
        "name": "Sony WH-1000XM4 Headphones",
        "product_type": "headphones",
        "brand": "Sony",
        "price": 3500
    },
    {
        "name": "iPhone 13 Pro Smartphone",
        "product_type": "smartphone",
        "brand": "Apple",
        "price": 12000
    },
    {
        "name": "Samsung QLED Q80A TV",
        "product_type": "television",
        "brand": "Samsung",
        "price": 8000
    },
    {
        "name": "JBL Charge 4 Portable Speaker",
        "product_type": "speaker",
        "brand": "JBL",
        "price": 1500
    },
    {
        "name": "Lenovo ThinkPad X1 Carbon Laptop",
        "product_type": "laptop",
        "brand": "Lenovo",
        "price": 20000
    },
    {
        "name": "Logitech MX Master 3 Wireless Mouse",
        "product_type": "mouse",
        "brand": "Logitech",
        "price": 1200
    },
    {
        "name": "AirPods Pro Headphones",
        "product_type": "headphones",
        "brand": "Apple",
        "price": 2500
    },
    {
        "name": "Panasonic DP-UB820 4K Blu-ray Player",
        "product_type": "player",
        "brand": "Panasonic",
        "price": 3000
    },
    {
        "name": "Sennheiser Momentum 3 Wireless Headphones",
        "product_type": "headphones",
        "brand": "Sennheiser",
        "price": 2800
    },
    {
        "name": "LG NanoCell NANO90 LED TV",
        "product_type": "television",
        "brand": "LG",
        "price": 7000
    }
]
# fillDatabase(data)

def showProducts(databaseFile):
  with open(databaseFile) as file:
    content = json.loads(file.read())
  print("\033[1m№\t\t\tName\t\t\t  Product Type\t Brand\t\tPrice\033[0m")
  count = 1
  for i in content:
    spaces = 5 - len(str(count))
    spaces1 = 45 - len(i['name'])
    spaces2 = 15 - len(i['product_type'])
    spaces3 = 15 - len(i['brand'])
    spaces4 = 10 - len(str(i['price']))
    print("{}".format(count)+" "*spaces,end="")
    print("{}".format(i['name'])+" "*spaces1,end="")
    print("{}".format(i['product_type'])+" "*spaces2,end="")
    print("{}".format(i['brand'])+" "*spaces3,end="")
    print("{}".format(i['price'])+" "*spaces4,end="")
    print()
    count += 1
# showProducts(database)

def addProduct(name,product_type,brand,price):
  with open(database) as file:
    content = json.loads(file.read())
  content.append({
    "name":name,
    "product_type": product_type,
    "brand": brand,
    "price": price})
  print(content)
  with open(database,'w') as file:
    file.write(json.dumps(content))
  showProducts(database)
# addProduct("Bose QuietComfort 35 II Headphones","headphones","Bose",2800.0)

def delProduct(number):
  index = number - 1
  with open(database) as file:
    content = json.loads(file.read())
  content.pop(index)
  print(content)
  with open(database,'w') as file:
    file.write(json.dumps(content))
  showProducts(database)
# delProduct(11)

def editProduct(number):
  index = number - 1
  with open(database) as file:
    content = json.loads(file.read())
  product = content[index]
  print("Name:", product["name"])
  print("Product Type:", product["product_type"])
  print("Brand:", product["brand"])
  print("Price:", product["price"])
  print("="*30)
  while True:
    editOption = int(input("1 - Name\n2 - Product Type\n3 - Brand\n4 - Price\n0 - Exit\nChoose edit option: "))
    match editOption:
      case 0:
        break
      case 1:
        name = input("Enter new name: ")
        content[index]['name'] = name
        print(content[index])
      case 2:
        productType = input("Enter new product type: ")
        content[index]['product_type'] = productType
        print(content[index])
      case 3:
        brand = input("Enter new brand: ")
        content[index]['brand'] = brand
        print(content[index])
      case 4:
        price = float(input("Enter new price: "))
        content[index]['price'] = price
        print(content[index])
      case _:
        print("Invalid input. Try again.")
  with open(database,'w') as file:
    file.write(json.dumps(content))
  showProducts(database)
# editProduct(10)
def sortProductsBy(criteria):
  with open(database) as file:
    content = json.loads(file.read())
  content.sort(key=lambda item:item[f"{criteria}"])
  with open(database,'w') as file:
    file.write(json.dumps(content))
  showProducts(database)
# sortProductsBy('name')

dataset = 'filtred.json'
def searchProducts(by,title):
  with open(database) as file:
    content = json.loads(file.read())
  def filterBy(x):
    if x[by] == title:
      return True
    else:
      return False
  filtredData = list(filter(filterBy,content))
  with open(dataset,'w') as file:
    file.write(json.dumps(filtredData))
### REFACTOR ###

# searchProducts('product_type', 'headphones')

def productsSample(prodType,min,max):
  sampleData = 'sample.json'
  sample = []
  searchProducts('product_type', prodType)
  with open(dataset) as file:
    content = json.loads(file.read())
  for i in content:
    if float(i['price']) <= max and float(i['price']) >= min:
      sample.append(i)
  with open(sampleData,'w') as file:
    file.write(json.dumps(sample))
  showProducts(sampleData)
# productsSample('headphones',2000,3000)

def averagePrice(prodType):
  searchProducts('product_type', prodType)
  with open(dataset) as file:
    content = json.loads(file.read())
  counter = 0
  allSum = 0
  for i in content:
    counter += 1
    allSum += i['price']
  average = allSum / counter
  print(f'{prodType.capitalize()} average price equals {round(average,2)}')
# averagePrice('headphones')
def prodCorrection(prodType,priceChange):
  newData = []
  with open(database) as file:
    content = json.loads(file.read())
  for i in content:
    if i['product_type'] == prodType:
      i['price'] *= priceChange
    newData.append(i)
  with open(database,'w') as file:
    file.write(json.dumps(newData))
  showProducts(database)
# prodCorrection('television',1.05)

def prodCorrectionDel(key,value):
  newData = []
  with open(database) as file:
    content = json.loads(file.read())
  for i in content:
    newData.append(i)
    if i[key] == value:
      newData.pop()
  with open(database,'w') as file:
    file.write(json.dumps(newData))
  showProducts(database)
# prodCorrectionDel('brand','LG')
def prodTypeList():
  typeList = []
  with open(database) as file:
    content = json.loads(file.read())
  for i in content:
      typeList.append(i['product_type'])
  return list(set(typeList))
typeList = prodTypeList()

while True:
  try:
    print('*'*50)
    option = int(input('1 - Fill database\n2 - Browse database\n3 - Add product to the database\n4 - Delete product from the database\n5 - Edit record about a product\n6 - Put records in order\n7 - Search records\n8 - Form a sample\n9 - Calculate average price\n10 - Change price for products of same type\n11 - Delete products with specific value\n0 - Exit\nChoose option: '))
    match option:
      case 0:
        break
      case 1:
        fillDatabase(data)
        print('Done')
      case 2:
        showProducts(database)
      case 3:
        name = input('Enter name of a product: ')
        product_type = input('Enter product type: ')
        brand = input('Enter brand of a product: ')
        price = float(input('Enter price of a product: '))
        addProduct(name,product_type,brand,price)
      case 4:
        numberOfProd = int(input('Enter ordinal number of the prodact that you want to delete: '))
        delProduct(numberOfProd)
      case 5:
        numberOfProd = int(input('Enter ordinal number of the prodact that you want to edit: '))
        editProduct(numberOfProd)
      case 6:
        key = input("Enter sorting crateria(name,brand,price,product_type): ")
        if key == "name" or key == "brand" or key == "price" or key == "product_type":
          sortProductsBy(key)
        else:
          raise ValueError
      case 7:
        key = input("Enter searching crateria(name,brand,price,product_type): ")
        value = input("Enter searching value: ")
        if key == "name" or key == "brand" or key == "price" or key == "product_type":
          searchProducts(key, value)
          showProducts(dataset)
        else:
          raise ValueError
      case 8:
        print(typeList)
        typeIndex = int(input("Enter product type index: "))
        minPrice = float(input("Enter min price: "))
        maxPrice = float(input("Enter max price: "))
        productsSample(typeList[typeIndex],minPrice,maxPrice)
      case 9:
        print(typeList)
        typeIndex = int(input("Enter product type index: "))
        averagePrice(typeList[typeIndex])
      case 10:
        print(typeList)
        typeIndex = int(input("Enter product type index: "))
        percent = int(input('Enter a percent change of a price for example (5% or -5%): '))
        actualChange = 1 + percent/100
        prodCorrection(typeList[typeIndex],actualChange)
      case 11:
        key = input("Enter deleting crateria(name,brand,price,product_type): ")
        value = input("Enter deleting value: ")
        if key == "name" or key == "brand" or key == "price" or key == "product_type":
          prodCorrectionDel(key, value)
        else:
          raise ValueError
      case _:
        print('Invalid input. Try again.')
  except ValueError:
    print('Please enter correct value')