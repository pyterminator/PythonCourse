# pip install googletrans==3.1.0a0 

from googletrans import Translator

tt = Translator().translate


text = "Salam Müşviq, Necəsən ?"

result = tt(text=text, dest="ru")

print(result.text)
