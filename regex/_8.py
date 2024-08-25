import re

text = """
    It is a 0779009090 long established fact that a reader will be distracted 
    by the readable content of a page when looking at its layout. The point of
    using Lorem Ipsum is that it has 050 900 90 90 a more-or-less normal 
    distribution of letters, as opposed to using 'Content here, content here', 
    making it look like readable English. Many desktop publishing packages and 
    web page editors now use 070-990-9090 Lorem Ipsum as their default 055-222-22-22 
    model text, and a search for 'lorem ipsum' will uncover many web sites still in 
    their infancy. Various versions have evolved over the years, sometimes by accident, 
    sometimes on purpose (injected humour and the like).
"""
 
 
pattern = r"(050|051|055|070|077)(-?|\s?)\d{3}(-?|\s?)\d{2}(-?|\s?)\d{2}"

phone_numbers = re.finditer(pattern, text)
 
for phone in phone_numbers:
    phone = phone.group().replace(" ", "").replace("-", "") 
    print(f"+994{phone[1:3]}-{phone[3:6]}-{phone[6:8]}-{phone[8:]}")