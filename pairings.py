def find_pairs(num_string):
  # split with " "
  # convert to int
  # sort
  # append number to each number after it

  nums = num_string.split(" ")
  # print(nums)

  nums_list = list(map(int, nums))
  nums_list.sort()
  
  


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")

  # nums = num_string.split(" ")
  # # print(nums)

  # nums_int = []
  # for num in nums:
  #   nums_int.append(int(num))

  # nums_int.sort()
  # output = set()
  # for i in range(len(nums_int)):
  #   for j in range(i+1,len(nums_int)):
  #     output.add((nums_int[i], nums_int[j]))   
  # print(output)
  # return output