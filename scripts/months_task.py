from datetime import datetime
my_date = "10.01.2024"

my_datetime_object = datetime.strptime(my_date, "%d.%m.%Y")

months = {
    1:["Yanvar","Qış"],
    2:["Fevral","Qış"],
    3:["Mart","Yaz"],
    4:["Aprel","Yaz"],
    5:["May","Yaz"],
    6:["İyun","Yay"],
    7:["İyul","Yay"],
    8:["Avqust","Yay"],
    9:["Sentyabr","Payız"],
    10:["Oktyabr","Payız"],
    11:["Noyabr","Payız"],
    12:["Dekabr","Qış"],
}
 
print(months[my_datetime_object.month])