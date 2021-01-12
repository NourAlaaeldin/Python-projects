#Dictionaries contains values and keys

#creating a dictionarie:

monthConversion = {
    #key:value
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(monthConversion)
print("*********************************")
print(monthConversion["Nov"])
print("*********************************")
print(monthConversion.get("Nov"))
print("*********************************")
print(monthConversion.get("Love","Not a valid key"))