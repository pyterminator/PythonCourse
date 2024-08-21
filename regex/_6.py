import re 

text = "LoRem Ipsum is simply dummy 16781679 text of the printing and \
typesetting industry. Şeir Lorem Ipsum has been the industry's standard \
dummy 1567 text ever since the 1500s, When an unknown printer took a galley \
of type and scrambled it to make a type specimen book. It has survived \
not only five centuries, but also the 17890 leap into electronic typesetting, \
    remaining essentially unchanged. It was popularised in the 1960s with the \
        release of Letraset sheets containing 1780 Lorem Ipsum passages, and more recently\
            with desktop sum, publishing software like Aldus PageMaker including versions of \
                Lorem Ip"

def EndsWith(text: str, pattern: str) -> bool:
    return bool(re.search(pattern+"$", text, re.IGNORECASE))


print(
    EndsWith(text, "ip")
)

def StartsWith(text: str, pattern: str) -> bool:
    return bool(re.match(r"(?i)"+pattern, text))
    # return bool(re.match(pattern, text, re.IGNORECASE))

print(
    StartsWith(text, "lore")
)