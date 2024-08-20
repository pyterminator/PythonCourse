import re 

text = "Lorem Ipsum is simply dummy 16781679 text of the printing and \
typesetting industry. Lorem Ipsum has been the industry's standard \
dummy 1567 text ever since the 1500s, when an unknown printer took a galley \
of type and scrambled it to make a type specimen book. It has survived \
not only five centuries, but also the 17890 leap into electronic typesetting, \
    remaining essentially unchanged. It was popularised in the 1960s with the \
        release of Letraset sheets containing 1780 Lorem Ipsum passages, and more recently\
            with desktop publishing software like Aldus PageMaker including versions of \
                Lorem Ipsum."

my_list = re.findall(r"\d{4,}",text)

print(my_list)