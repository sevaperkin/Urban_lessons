def get_multiplied_digits(number):
  str_number = str(number)
  if len(str_number) == 0:
    return 1
  first = int(str_number[0])
  if len(str_number) == 1:
    return first if first != 0 else 1
  rest = int(str_number[1:])
  return first * get_multiplied_digits(rest) if first != 0 else get_multiplied_digits(rest)

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)


