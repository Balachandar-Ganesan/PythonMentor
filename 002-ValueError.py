unTypedValues =[1,2,3,'abc',5]
for unTypedValue in unTypedValues:
    try:
      intConvertedValue = int(unTypedValue)
      print(intConvertedValue)
    except ValueError as ex:
      print(ex)
      continue