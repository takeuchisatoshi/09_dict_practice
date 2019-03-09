fruits_dict = {"りんご": "Apple",
               "ぶどう": "Grape",
               "みかん": "Orange"
               }

# print(fruits_dict["ぶどう"])

# print(fruits.keys())


for jp_name in fruits_dict.keys():
    print(jp_name)

for en_name in fruits_dict.values():
    print(en_name)

for jp_name, en_name in fruits_dict.items():
    print(f"{jp_name}は英語で{en_name}")
