def alarm_clock(day, vacation):
  if day == 0 or day == 6:
    if vacation:
      return "off"
    else:
      return "10:00"
  else:
    if vacation:
      return "10:00"
    else:
      return "7:00"

def string_bits(str):
  new_str = ""
  for x in range(0, len(str), 2):
    new_str += str[x]
  return new_str

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count +=1
  return count
