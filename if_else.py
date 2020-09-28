list_of_computers = []
list_of_computers = ["comp1", "comp2", "comp3"]
list_of_computers
list_of_used_computers = []
list_of_used_computers = ["comp136", "comp187"]
list_of_used_computers
all_computers = list_of_computers + list_of_used_computers
all_computers
if "comp136" in list_of_used_computers:
  print("Computer is in use")
else:
  print("Computer is not in use")
