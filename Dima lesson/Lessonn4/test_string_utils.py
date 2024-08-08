import pytest
from string_utils import StringUtils

utils = StringUtils()

# capitalize #
def test_capitilize():
    # positive
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello rostov") == "Hello rostov"
    assert utils.capitilize("123") == "123"

    # negative
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("123test") == "123test"
# trim #

def test_trim():
    # positive
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  hello rostov  ") == "hello rostov  "
    assert utils.trim (  " SKY  ") == "SKY  "

    # negative
    assert utils.trim ("") == ""

@pytest.mark.xfail()
def test_negatif_trim():
    assert utils.trim("123") == False
  
@pytest.mark.xfail()
def test_negatif_trim_numbers():
     assert utils.trim(123) == "123"
# to_list #

@pytest.mark.parametrize('string, delimeter, result', [

    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
   # ("abc" , "@", ["a", "b", "c"]),
    # negative
    ("  ", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4 5"]),
]) 

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
        assert res == result

# contains #

@pytest.mark.parametrize('string, symbol, result' , [
    ("банан", "н", True),
    (" гвоздь", "д", True),
    ("мир ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
    ("Ростов", "р", False),
    ("привет", "з", False),
    ("кот", "k", False),
    ("", "з", False),
    ("12345", "h", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

# delete symbol #

@pytest.mark.parametrize('string, symbol, result' , [
    ("корень", "к", "орень"),
    ("Женя", "н", "Жея"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Красная площадь", " ", "Краснаяплощадь"),

    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("зелень", " ", "зелень"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

# starts with #

@pytest.mark.parametrize('string, symbol, result' , [
    ("светофор", "с", True),
    ("", "", True),
    ("Москва", "М", True),
    ("Мира-Зина", "М", True),
    ("Film ", "F", True),
    ("123", "1", True),
    
    ("Ваня", "в", False),
    ("мир", "М", False),
    ("", "@", False),
    ("плащь", "ж", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# end_with #

@pytest.mark.parametrize('string, symbol, result' , [
    ("Мария", "я", True),
    ("ТОРТИК", "К", True),
    ("", "", True),
    ("собака ", "", True),
    ("67", "7", True),
    ("ONE-TWo", "o", True),
    ("Петр1", "1", True),
    ("БаобаБ", "Б", True),

    ("природа", "л", False),
    ("дверь", "Д", False),
    ("", "*", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

# is_empty #

@pytest.mark.parametrize('string, result' , [
    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    (" не пусто с пробелом", False),
    ("345", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# list_to_string #

@pytest.mark.parametrize('lst, joiner, result' , [
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5], None, "1,2,3,4,5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["в", "у", "з"], "", "вуз"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")

])

def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res =  utils.list_to_string(lst, joiner)
        assert res == result






