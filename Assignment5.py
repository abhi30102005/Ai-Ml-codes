import json
# with open("names.txt", "w") as f:
#     for i in range(5):
#         f.write(input("enter the name")+"\n")

# with open("names.txt", "r") as f:
#     print("\n  Names in the file:")
#     for i in f:
#         print(i.strip())







# with open("log.txt","a") as f:
#     f.write("\n program run successfully")

# with open("log.txt","r") as f:
#     for log in f:
#         print(log.strip())


# list=[5,10,15,20,25]

# ans=[i for i in list if i>15]
# print(ans)


dict={
    "gorakhpur" : 50000,
    "deoria": 5410,
    "lucknow":4578,
}

# print(type(dict))

# with open("cities.json","w") as f:
#     json.dump(dict,f, indent=4)

with open("cities.json","r") as f:
    py_obj=json.load(f)
    print(py_obj)
with open("cities.json","w") as f:
    new_city=input("enter the city")
    new_population=input("enter the new population")
    # Add new city
    dict[new_city] = new_population
    json.dump(py_obj,f, indent=4)