def change(ammount_paid, ammount_due):
  denominations = ["200","100","50","20","10","5","2","1"]
  change_due = int(round(ammount_paid - ammount_due, 2) *100)
  change_dict = {}

  for i in denominations:
    count = change_due // int(i)
    if count > 0:
      change_dict[f"R{int(i) / 100}"] = count  # Store the count with denomination
      change_due -= count * int(i) # Subtract the value of the denomination from the change_due
  return change_dict
      
ammount_1 = 12250  # R250
ammount_2 = 183.75  # R183.75
change_1 = change(ammount_1, ammount_2)
print(change_1)
      

  # for a,b in zip(ammount_paid, ammount_due):
  #   if ammount_due > ammount_paid:
  #     return ValueError
  #   if ammount_due == ammount_paid:
  #     return "no change"
  #   if ammount_due < ammount_paid: