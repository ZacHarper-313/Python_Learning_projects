#converting to float
integer_number=123
float_number=1.23
new_number=integer_number+float_number
print(new_number)
#display new value and resulting data type
print("value:",new_number)
print("data type:",type(new_number))
num_string='12'
num_integer=13
print("Data type of num_string before type casting:", type(num_string))
#explicit type conversion
num_string=int(num_string)
num_sum=num_integer+num_string
print('sum:',num_sum)
print('data type of num_sum:',type(num_sum))