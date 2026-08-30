# methods and examples for data construct of list
# list for grocery shopping
grocery_list = ["apples", "rice", "milk", "bread","eggs","cooking oil","sugar","salt","butter","cheese"]
print("Grocery List:", grocery_list)
# method append() to add an item to the list
grocery_list.append("chicken")
print("Grocery List after adding chicken:", grocery_list)
# method extend() to add another list to the existing list
additional_items = ["vegetables", "fruits"]
grocery_list.extend(additional_items)
print("Grocery List after adding additional items:", grocery_list)
# method insert() to add an item at a specific index
grocery_list.insert(2, "yogurt")
print("Grocery List after inserting yogurt:", grocery_list)
# method remove() to remove an item from the list
grocery_list.remove("sugar")
print("Grocery List after removing sugar:", grocery_list)
# method index() to find the index of an item in the list
index_of_milk = grocery_list.index("milk")
print("Index of milk in the Grocery List:", index_of_milk)
# method count() to count the occurrences of an item in the list
count_of_apples = grocery_list.count("apples")
print("Count of apples in the Grocery List:", count_of_apples)
# method pop() to remove an item at a specific index
popped_item = grocery_list.pop(3)
print("Popped item:", popped_item)
print("Grocery List after popping an item:", grocery_list)
# method reverse() to reverse the order of the list
grocery_list.reverse()
print("Grocery List after reversing:", grocery_list)
# method sort() to sort the list in ascending order
grocery_list.sort()
print("Grocery List after sorting:", grocery_list)
# method copy() to create a shallow copy of the list
new_grocery_list = grocery_list.copy()
print("New Grocery List", new_grocery_list)
# method max() to find the maximum item in the list
max_item = max(grocery_list)
print("Maximum item in the Grocery List:", max_item)
# method min() to find the minimum item in the list
min_item = min(grocery_list)
print("Minimum item in the Grocery List:", min_item)
# method len() to find the length of the list
length_of_list = len(grocery_list)
print("Length of the Grocery List:", length_of_list)
# method clear() to remove all items from the list
grocery_list.clear()    
print("Grocery List after clearing:", grocery_list)

# methods and examples for data construct of tuple
# tuple for days of the week
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Days of the Week:", days_of_week)
# method count() to count the occurrences of an item in the tuple
count_of_monday = days_of_week.count("Monday")
print("Count of Monday in the Days of the Week:", count_of_monday)
# method index() to find the index of an item in the tuple
index_of_friday = days_of_week.index("Friday")
print("Index of Friday in the Days of the Week:", index_of_friday)
# method add() to add an item to the tuple (tuples are immutable, so we create a new tuple)
new_days_of_week = days_of_week + ("Holiday",)
print("New Days of the Week after adding Holiday:", new_days_of_week)
# method len() to find the length of the tuple
length_of_tuple = len(days_of_week)
print("Length of the Days of the Week:", length_of_tuple)
# method max() to find the maximum item in the tuple
max_day = max(days_of_week)
print("Maximum day in the Days of the Week:", max_day)
# method min() to find the minimum item in the tuple
min_day = min(days_of_week)
print("Minimum day in the Days of the Week:", min_day)


# methods and examples for data construct of set
# set for unique numbers
unique_numbers = {1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}
print("Unique Numbers:", unique_numbers)
# method add() to add an item to the set
unique_numbers.add(11)
print("Unique Numbers after adding 11:", unique_numbers)
# method remove() to remove an item from the set
unique_numbers.remove(5)
print("Unique Numbers after removing 5:", unique_numbers)
# method discard() to remove an item from the set (does not raise an error if the item is not found)
unique_numbers.discard(6)
print("Unique Numbers after discarding 6:", unique_numbers)
# method pop() to remove and return an arbitrary item from the set
popped_number = unique_numbers.pop()
print("Popped number:", popped_number)
# method clear() to remove all items from the set
unique_numbers.clear()
print("Unique Numbers after clearing:", unique_numbers)

# methods and examples for data construct of dictionary
# dictionary for employee details
employee_details = {
    "name": "arthur",
    "lastname": "morgan",
    "age": 36,
    "position": "outlaw",
    "department": "gang"
}
print("Employee Details:", employee_details)
# method keys() to get all the keys in the dictionary
employee_keys = employee_details.keys()
print("Employee Keys:", employee_keys)
# method values() to get all the values in the dictionary
employee_values = employee_details.values()
print("Employee Values:", employee_values)
# method items() to get all the key-value pairs in the dictionary
employee_items = employee_details.items()
print("Employee Items:", employee_items)
# method get() to get the value of a specific key in the dictionary
employee_age = employee_details.get("age")
print("Employee Age:", employee_age)
# method update() to update the value of a specific key in the dictionary
employee_details.update({"age": 37})
print("Employee Details after updating age:", employee_details)
# method pop() to remove a specific key-value pair from the dictionary
removed_item = employee_details.pop("position")
print("Removed Item:", removed_item)
print("Employee Details after removing position:", employee_details)
# method popitem() to remove and return an arbitrary key-value pair from the dictionary
removed_item = employee_details.popitem()
print("Removed Item:", removed_item)
print("Employee Details after removing arbitrary item:", employee_details)
# method len the length of the dictionary
print("Length of Employee Details:", len(employee_details))
# method append() to add an item to the list
employee_details["salary"] = 50000
print("Employee Details after adding salary:", employee_details)
# method copy() to create a shallow copy of the dictionary
new_employee_details = employee_details.copy()
print("New Employee Details", new_employee_details)
# method setdefault() Gets a value; adds key if it doesn't exist
employee_setdefualt = employee_details.setdefault("city" , "black_water")
print("employee setdefault after adding anew value" , employee_setdefualt)
print("now print employee details after adding new key and value" , employee_details)
# method clear() to remove all items from the dictionary
employee_details.clear()
print("Employee Details after clearing:", employee_details)