"""Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений."""



import string

a="ASFASJFHSAJIFHAIHFIUASDEFUASHAIUFDASIUASDHFIUFUASUFIASUFASUFAUSFAHSFASJFASIUFAUSFIAUSFJJJJMBPUZ"
def rle(arg):
    try:
        res=[]
        alf=string.ascii_uppercase
        for val in alf:
            if val in list(arg):
                intermediate_result = str(val)
                if arg.count(val) > 1:
                    intermediate_result+= str(arg.count(val))
                res.append(intermediate_result)
        print(res)
    except:
        print("Неверные данные")

rle(a)
