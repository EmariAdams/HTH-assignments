#task 1 working with strings
food = 'pizza'
print(food[:3])

print(food[-3:])
print(food[2:5])

first_last = food[0] + food[-1]
print(first_last)

food_list = food.split('pizza')
print(food_list)
'pizza'.join()
print(food_list)

number_list = [1, 100, 200, 300, 400]
number_list.append(500)
number_list.insert(2, 250)
print(number_list)
number_list.pop(4)
print(number_list)