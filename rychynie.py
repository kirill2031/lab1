import manual

def test_stroka():
    if manual.reverse_string("Hello") == "olleH":
        print("Test stroka(Hello) is OK ")
    else:
        print("Test stroka(Hello) is Fail")

def test_stroka():
    if manual.reverse_string("Car") == "raC":
        print("Test stroka(Car) is OK ")
    else:
        print("Test stroka(Car) is Fail")

def test_stroka():
    if manual.reverse_string("Tools") == "slooT":
        print("Test stroka(Tools) is OK ")
    else:
        print("Test stroka(Tools) is Fail")

def test_stroka():
    if manual.reverse_string("World") == "dlroW":
        print("Test stroka(World) is OK ")
    else:
        print("Test stroka(World) is Fail")

def test_stroka():
    if manual.reverse_string("Dogs") == "sgoD":
        print("Test stroka(Dogs) is OK ")
    else:
        print("Test stroka(Dogs) is Fail")



def test_polindrome():
    if manual.is_palindrome("Anna") == "Anna":
        print("Test polindrome(Anna) is OK")
    else:
        print("Test polindrome(Anna) is Fail")

def test_polindrome():
    if manual.is_palindrome("stats") == "stats":
        print("Test polindrome(stats) is OK")
    else:
        print("Test polindrome(stats) is Fail")

def test_polindrome():
    if manual.is_palindrome("refer") == "refer":
        print("Test polindrome(refer) is OK")
    else:
        print("Test polindrome(refer) is Fail")

def test_polindrome():
    if manual.is_palindrome("madam") == "madam":
        print("Test polindrome(madam) is OK")
    else:
        print("Test polindrome(madam) is Fail")

def test_polindrome():
    if manual.is_palindrome("level") == "level":
        print("Test polindrome(level) is OK")
    else:
        print("Test polindrome(level) is Fail")

def test_voweles():
    if manual.extract_vowels("Шла") == 1 :
        print("Test vowels(Шла) is OK")
    else:
        print("Test vowels(Шла) is Fail")

def test_voweles():
    if manual.extract_vowels("Машина") == 3 :
        print("Test vowels(Машина) is OK")
    else:
        print("Test vowels(Машина) is Fail")

def test_voweles():
    if manual.extract_vowels("Собака") == 3 :
        print("Test vowels(Собака) is OK")
    else:
        print("Test vowels(Собака) is Fail")

def test_voweles():
    if manual.extract_vowels("Кошка") == 2 :
        print("Test vowels(Кошка) is OK")
    else:
        print("Test vowels(Кошка) is Fail")

def test_voweles():
    if manual.extract_vowels("Школа") == 2 :
        print("Test vowels(Школа) is OK")
    else:
        print("Test vowels(Школа) is Fail")

def test_duplicates():
    if manual.remove_duplicates("Hello world") == "Helo wrd":
        print("Test duplicate(Hello world) is OK")
    else:
        print("Test duplicate(Hello world) is Fail")

def test_duplicates():
    if manual.remove_duplicates("he knows Inglish") == "he knows gli":
        print("Test duplicate(he knows Inglish) is OK")
    else:
        print("Test duplicate(he knows Inglish) is Fail")

def test_duplicate():
    if manual.remove_duplicates("qweqweqwe") == "qwe":
        print("Test duplicate(qweqweqwe) is OK")
    else:
        print("Test duplicate(qweqweqwe) is Fail")

def test_duplicate():
    if manual.remove_duplicates("asdasdasd") == "asd":
        print("Test duplicate(asdasdasd) is OK")
    else:
        print("Test duplicate(asdasdasd) is Fail")

def test_duplicate():
    if manual.remove_duplicates("zxczxczxc") == "zxc":
        print("Test duplicate(zxczxczxc) is OK")
    else:
        print("Test duplicate(zxczxczxc) is Fail")

test_stroka()
test_polindrome()
test_voweles()
test_duplicate()