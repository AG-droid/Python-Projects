# k h d m d c m

print('WELCOME TO THE UNIT CONVERTER')
print('')
print('')

y = input("What do you want to measure ? :")

a = input('What do you want to convert from (Full forms only)  -->')
b = input('What do you want to convert to -->')
c = float(input('pls enter the value that you want to convert -->'))
def weight():
    if a == "kilogram" or a == "Kg" or a == "Kilogram" or a == "kg" :
        if b == 'hectogram'or b == 'Hectogram':
            print(c * 10 , 'hectogram')
        elif b == "dekagram" or b == "Dekagram":
            print(c * 100 , 'dekagram')
        elif b == 'gram' or b =='Gram':
            print(c * 1000 , 'gram')
        elif b == "decigram" or b == 'Decigram':
            print(c * 10000, 'decigram')
        elif b == 'centigram' or b == 'Centigram':
            print(c * 100000 , 'centigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 1000000, 'miligram')

    elif a == "hectagram" or a == "Hg" or a == "Hectagram" or a == "hg" :
        if b == 'Kilogram'or b == 'kilogram':
            print(c / 10 , 'Kilogram')
        elif b == "dekagram" or b == "Dekagram":
            print(c * 10 , 'dekagram')
        elif b == 'gram' or b =='Gram':
            print(c * 100 , 'gram')
        elif b == "decigram" or b == 'Decigram':
            print(c * 1000, 'decigram')
        elif b == 'centigram' or b == 'Centigram':
            print(c * 10000 , 'centigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 100000, 'miligram')

    elif a == "dekagram" or a == "Dag" or a == "Dekagram" or a == "dag" :
        if b == 'Kilogram'or b == 'kilogram':
            print(c / 100 , 'Kilogram')
        elif b == "hectagram" or b == "Hectagram":
            print(c / 10 , 'Hectagram')
        elif b == 'gram' or b =='Gram':
            print(c * 10 , 'gram')
        elif b == "decigram" or b == 'Decigram':
            print(c * 100, 'decigram')
        elif b == 'centigram' or b == 'Centigram':
            print(c * 1000 , 'centigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 10000, 'miligram')

    elif a == "gram" or a == "g" or a == "Gram" or a == "G":
        if b == 'Kilogram' or b == 'kilogram':
            print(c / 1000, 'Kilogram')
        elif b == "hectagram" or b == "Hectagram":
            print(c / 100, 'Hectagram')
        elif b == 'dekagram' or b == 'Dekaram':
            print(c / 10, 'gram')
        elif b == "decigram" or b == 'Decigram':
            print(c * 10, 'decigram')
        elif b == 'centigram' or b == 'Centigram':
            print(c * 100, 'centigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 1000, 'miligram')

    elif a == "decigram" or a == "dg" or a == "Decigram" or a == "Dg":
        if b == 'Kilogram' or b == 'kilogram':
            print(c / 10000, 'Kilogram')
        elif b == "hectagram" or b == "Hectagram":
            print(c / 1000, 'Hectagram')
        elif b == 'dekagram' or b == 'Dekaram':
            print(c / 100, 'gram')
        elif b == "gram" or b == 'Gram':
            print(c / 10, 'decigram')
        elif b == 'centigram' or b == 'Centigram':
            print(c * 10, 'centigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 100, 'miligram')

    elif a == "centigram" or a == "cg" or a == "Centigram" or a == "Cg":
        if b == 'Kilogram' or b == 'kilogram':
           print(c / 100000, 'Kilogram')
        elif b == "hectagram" or b == "Hectagram":
            print(c / 10000, 'Hectagram')
        elif b == 'dekagram' or b == 'Dekaram':
            print(c / 1000, 'gram')
        elif b == "gram" or b == 'Gram':
            print(c / 100, 'gram')
        elif b == 'decigram' or b == 'Decigram':
            print(c / 10, 'Decigram')
        elif b == 'Mililgram' or b == 'miligram':
            print(c * 10, 'miligram')

    elif a == "miliigram" or a == "mg" or a == "miligram" or a == "Mg":
        if b == 'Kilogram' or b == 'kilogram':
           print(c / 1000000, 'Kilogram')
        elif b == "hectagram" or b == "Hectagram":
            print(c / 100000, 'Hectagram')
        elif b == 'dekagram' or b == 'Dekaram':
            print(c / 10000, 'gram')
        elif b == "gram" or b == 'Gram':
            print(c / 1000, 'gram')
        elif b == 'centigram' or b == 'Centigram':
            print(c / 10, 'centigram')
        elif b == 'decigram' or b == 'Decigram':
            print(c/100, 'decigram')


def length():
    if a == "kilometer" or a == "Km" or a == "Kilometer" or a == "km" :
        if b == 'hectometer'or b == 'Hectometer':
            print(c * 10 , 'hectometer')
        elif b == "dekameter" or b == "Dekameter":
            print(c * 100 , 'dekameter')
        elif b == 'meter' or b =='Meter':
            print(c * 1000 , 'meter')
        elif b == "decimeter" or b == 'Decimeter':
            print(c * 10000, 'decimeter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c * 100000 , 'centimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 1000000, 'milimeter')

    elif a == "hectameter" or a == "Hm" or a == "Hectameter" or a == "hm" :
        if b == 'Kilometer'or b == 'kilometer':
            print(c / 10 , 'Kilometer')
        elif b == "dekameter" or b == "Dekameter":
            print(c * 10 , 'dekameter')
        elif b == 'meter' or b =='Meter':
            print(c * 100 , 'meter')
        elif b == "decimeter" or b == 'Decimeter':
            print(c * 1000, 'decimeter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c * 10000 , 'centimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 100000, 'milimeter')

    elif a == "dekameter" or a == "Dam" or a == "Dekameter" or a == "dam" :
        if b == 'Kilometer'or b == 'kilometer':
            print(c / 100 , 'Kilometer')
        elif b == "hectameter" or b == "Hectameter":
            print(c / 10 , 'Hectameter')
        elif b == 'meter' or b =='Meter':
            print(c * 10 , 'meter')
        elif b == "decimeter" or b == 'Decimeter':
            print(c * 100, 'decimeter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c * 1000 , 'centimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 10000, 'milimeter')

    elif a == "meter" or a == "m" or a == "Meter" or a == "M":
        if b == 'Kilometer' or b == 'kilometer':
            print(c / 1000, 'Kilometer')
        elif b == "hectameter" or b == "Hectameter":
            print(c / 100, 'Hectameter')
        elif b == 'dekameter' or b == 'Dekaram':
            print(c / 10, 'meter')
        elif b == "decimeter" or b == 'Decimeter':
            print(c * 10, 'decimeter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c * 100, 'centimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 1000, 'milimeter')

    elif a == "decimeter" or a == "dm" or a == "Decimeter" or a == "Dm":
        if b == 'Kilometer' or b == 'kilometer':
            print(c / 10000, 'Kilometer')
        elif b == "hectameter" or b == "Hectameter":
            print(c / 1000, 'Hectameter')
        elif b == 'dekameter' or b == 'Dekarameter':
            print(c / 100, 'meter')
        elif b == "meter" or b == 'Meter':
            print(c / 10, 'decimeter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c * 10, 'centimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 100, 'milimeter')

    elif a == "centimeter" or a == "cm" or a == "Centimeter" or a == "Cm":
        if b == 'Kilometer' or b == 'kilometer':
           print(c / 100000, 'Kilometer')
        elif b == "hectameter" or b == "Hectameter":
            print(c / 10000, 'Hectameter')
        elif b == 'dekameter' or b == 'Dekaram':
            print(c / 1000, 'meter')
        elif b == "meter" or b == 'Gram':
            print(c / 100, 'meter')
        elif b == 'decimeter' or b == 'Decimeter':
            print(c / 10, 'Decimeter')
        elif b == 'Mililmeter' or b == 'milimeter':
            print(c * 10, 'milimeter')

    elif a == "miliimeter" or a == "mm" or a == "milimeter" or a == "Mm":
        if b == 'Kilometer' or b == 'kilometer':
           print(c / 1000000, 'Kilometer')
        elif b == "hectameter" or b == "Hectameter":
            print(c / 100000, 'Hectameter')
        elif b == 'dekameter' or b == 'Dekaram':
            print(c / 10000, 'meter')
        elif b == "meter" or b == 'Meter':
            print(c / 1000, 'meter')
        elif b == 'centimeter' or b == 'Centimeter':
            print(c / 10, 'centimeter')
        elif b == 'decimeter' or b == 'Decimeter':
            print(c/100, 'decimeter')


def Capacity():
    if a == "kilolitre" or a == "Kl" or a == "Kilolitre" or a == "kl" :
        if b == 'hectolitre'or b == 'Hectolitre':
            print(c * 10 , 'hectolitre')
        elif b == "dekalitre" or b == "Dekalitre":
            print(c * 100 , 'dekalitre')
        elif b == 'litre' or b =='Litre':
            print(c * 1000 , 'litre')
        elif b == "decilitre" or b == 'Decilitre':
            print(c * 10000, 'decilitre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c * 100000 , 'centilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 1000000, 'mililitre')

    elif a == "hectalitre" or a == "Hl" or a == "Hectalitre" or a == "hl" :
        if b == 'Kilolitre'or b == 'kilolitre':
            print(c / 10 , 'Kilolitre')
        elif b == "dekalitre" or b == "Dekalitre":
            print(c * 10 , 'dekalitre')
        elif b == 'litre' or b =='Litre':
            print(c * 100 , 'litre')
        elif b == "decilitre" or b == 'Decilitre':
            print(c * 1000, 'decilitre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c * 10000 , 'centilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 100000, 'mililitre')

    elif a == "dekalitre" or a == "Dal" or a == "Dekalitre" or a == "dal" :
        if b == 'Kilolitre'or b == 'kilolitre':
            print(c / 100 , 'Kilolitre')
        elif b == "hectalitre" or b == "Hectalitre":
            print(c / 10 , 'Hectalitre')
        elif b == 'litre' or b =='Litre':
            print(c * 10 , 'litre')
        elif b == "decilitre" or b == 'Decilitre':
            print(c * 100, 'decilitre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c * 1000 , 'centilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 10000, 'mililitre')

    elif a == "litre" or a == "g" or a == "Litre" or a == "G":
        if b == 'Kilolitre' or b == 'kilolitre':
            print(c / 1000, 'Kilolitre')
        elif b == "hectalitre" or b == "Hectalitre":
            print(c / 100, 'Hectalitre')
        elif b == 'dekalitre' or b == 'Dekaram':
            print(c / 10, 'litre')
        elif b == "decilitre" or b == 'Decilitre':
            print(c * 10, 'decilitre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c * 100, 'centilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 1000, 'mililitre')

    elif a == "decilitre" or a == "dl" or a == "Decilitre" or a == "Dl":
        if b == 'Kilolitre' or b == 'kilolitre':
            print(c / 10000, 'Kilolitre')
        elif b == "hectalitre" or b == "Hectalitre":
            print(c / 1000, 'Hectalitre')
        elif b == 'dekalitre' or b == 'Dekaram':
            print(c / 100, 'litre')
        elif b == "litre" or b == 'Litre':
            print(c / 10, 'decilitre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c * 10, 'centilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 100, 'mililitre')

    elif a == "centilitre" or a == "cl" or a == "Centilitre" or a == "Cl":
        if b == 'Kilolitre' or b == 'kilolitre':
           print(c / 100000, 'Kilolitre')
        elif b == "hectalitre" or b == "Hectalitre":
            print(c / 10000, 'Hectalitre')
        elif b == 'dekalitre' or b == 'Dekaram':
            print(c / 1000, 'litre')
        elif b == "litre" or b == 'Litre':
            print(c / 100, 'litre')
        elif b == 'decilitre' or b == 'Decilitre':
            print(c / 10, 'Decilitre')
        elif b == 'Milillitre' or b == 'mililitre':
            print(c * 10, 'mililitre')

    elif a == "miliilitre" or a == "ml" or a == "mililitre" or a == "Ml":
        if b == 'Kilolitre' or b == 'kilolitre':
           print(c / 1000000, 'Kilolitre')
        elif b == "hectalitre" or b == "Hectalitre":
            print(c / 100000, 'Hectalitre')
        elif b == 'dekalitre' or b == 'Dekaram':
            print(c / 10000, 'litre')
        elif b == "litre" or b == 'Litre':
            print(c / 1000, 'litre')
        elif b == 'centilitre' or b == 'Centilitre':
            print(c / 10, 'centilitre')
        elif b == 'decilitre' or b == 'Decilitre':
            print(c/100, 'decilitre')







if y == "weight" or "Weight" :
    weight()
if y == 'length' or y == 'Length' or y == 'Height' or y == 'height':
    length()
if y == 'capacity' or y == 'Capacity':
    Capacity()
if y == "":
    print('ERROR : pls assign a value')