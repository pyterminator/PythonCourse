from datetime import datetime, timezone, timedelta
# import locale
# locale.setlocale(locale.LC_ALL, "az_AZ")
# ----
# # Asia/Baku - UTC+4

# print(
#     datetime.now()
# )

# print(
#     datetime.now(tz=timezone.utc)
# )

# my_birthday = datetime(2000, 4, 9) 

# print(my_birthday + timedelta(days=20, hours=12))

# ---------------------------------------
# indiki_vaxt = datetime.now()

# print(
#     indiki_vaxt + timedelta(minutes=5)
# )

# my_birthday = datetime(2000, 4, 9) 

# print(
#     my_birthday.year,
#     my_birthday.month,
#     # my_birthday.date(),
#     # my_birthday.time(),
#     my_birthday.hour,
#     my_birthday.minute,
#     my_birthday.day
# )

# my_birthday = "2002.03.25"
my_birthday = "2024.08.27"

print(my_birthday)
my_birthday = datetime.strptime(my_birthday, "%Y.%m.%d") + timedelta(days=75, hours=5, minutes=47)
# print(
#     my_birthday + timedelta(days=75)
# )
# my_birthday = my_birthday.strftime("%d %m, %Y | %H:%M:%S")
# my_birthday = my_birthday.strftime("%d %b, %Y | %H:%M:%S")
my_birthday = my_birthday.strftime("%d %B, %Y | %H:%M:%S")
print(
    my_birthday
)


