dict_ = {
    'city': 'Moscow',
    'temperature': '20'
}

print(dict_["city"])
dict_["temperature"] = str(int(dict_["temperature"]) - 5)
print(dict_["temperature"])

print(dict_.get("country", "Russia"))

dict_["date"] = '27.05.2019'
print(dict_)
print(len(dict_))