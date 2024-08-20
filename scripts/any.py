"""
TASK :
    Password validator yazın getsin
    Ən az 1 böyük hərf
    Ən az 1 kiçik hərf
    Ən az 1 rəqəm
    Ən az 1 dənə nöqtə
    Uzunluğu minimum 8 simvoldan ibarət olsun
"""

my_password = "mushvigShukurov"


def HasNumeric(text:str) -> bool:
    if isinstance(text, str):
        my_list = [letter.isnumeric() for letter in text]
        return any(my_list)
    raise Exception("Yalnız str-tipində data göndər!")

print(
    HasNumeric(my_password)
)

