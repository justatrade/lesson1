my_list = [3, 5, 7, 9, 10.5]
print(my_list)

my_list.append("Python")
print(len(my_list))

print(f'{my_list[0]} {my_list[-1]}')
print(f'{my_list[1:4]}')
my_list.remove('Python')


my_dict = {
    "city": "Moscow",
    "temperature": "20"
}
print(my_dict["city"])
my_dict["temperature"] = int(my_dict["temperature"]) - 5
print(my_dict)

print(my_dict.get("country", "Russia"))
my_dict["date"] = "27.05.2019"

print(len(my_dict))