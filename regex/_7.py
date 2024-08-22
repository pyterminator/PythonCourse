import re 
 
# all() - built-in function
# any() - built-in function

password = "g.Ş12"

def HasLower(password: str) -> bool:
    if isinstance(password, str):
        return bool(re.search(r"[a-zşüğöəçı]", password))
    return False

def HasUpper(password: str) -> bool:
    if isinstance(password, str):
        return bool(re.search(r"[A-ZŞÜĞƏÖÇİ]", password))
    return False

def HasDigit(password: str) -> bool:
    if isinstance(password, str):
        return bool(re.search(r"[0-9]", password))
    return False

def HasPunctuation(password: str) -> bool:
    if isinstance(password, str):
        return bool(re.search(r"\.", password))
    return False


def PasswordChecker(password:str) -> bool:
    if isinstance(password, str):
        return all([ 
            HasLower(password), 
            HasUpper(password), 
            HasDigit(password), 
            HasPunctuation(password),
            len(password) > 8
            ])
    return False


print(
    PasswordChecker(password)
)