#Question 1
names=["Tarteel","Asmaa","Ahmae"]
names.insert(0,"Nada")
print(names)
names.pop()
print(names)
names.append("Noor")
print(names)
del names[2]
print(names)

#Question 2
friends=["Adel","Ahmed"]
employees=["Samah","Amjad"]
school=["Ali","Basma"]

tot_list=friends+employees+school
print(tot_list)
def tot_list(friends,employees,school):
    tot_list=friends+employees+school
    return tot_list

print(tot_list)

#Question 3
def concatenate_dictionaries(*dicts):
    new_dict = {}
    for dictionary in dicts:
        new_dict.update(dictionary)
    return new_dict

# Create the dictionaries
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}


concatenated_dict = concatenate_dictionaries(dict1, dict2, dict3)

print(concatenated_dict)

#Question 4
def s_square_dict():
    square_dict={}
    for num in range (1,16):
        square_dict[num]=num**2
    return square_dict

ans_dict=s_square_dict()
print(ans_dict)

#Question 5
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 400}

def c_dictionaries(d1, d2):
    c_dict = {}

    for key in d1:
        if key in d2:
            c_dict[key] = d1[key] + d2[key]
        else:
            c_dict[key] = d1[key]

    for key in d2:
        if key not in c_dict:
            c_dict[key] = d2[key]

    return c_dict

ans_dict = c_dictionaries(d1, d2)
print(ans_dict)

#Question 6
def lists_to_dictionary(keys, values):
    result_dict = dict(zip(keys, values))
    return result_dict

list1 = ['Ten', 'Twenty', 'Thirty']
list2 = [10, 20, 30]
result_dict = lists_to_dictionary(list1, list2)
print(result_dict)

#Qusetion 7
sampleDict = {
    "Class": {
        "Student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["Class"]["Student"]["marks"]["history"])

#Qusetion 8
def print_values_less_than_10(dictionary):
    values_less_than_10 = [value for key, value in dictionary.items() if key < 10]
    print(' -> '.join(values_less_than_10))

my_dict = {1: "Alaa", 5: "Hadeel", 7: "Hanin", 13: "Malak"}
print_values_less_than_10(my_dict)