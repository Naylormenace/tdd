def change(ammount_paid, ammount_due):
    denominations = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5 ]
    change_due = ammount_paid - ammount_due
    change_dict = {}

    for i in denominations:
        count = change_due // i
        if count > 0:
            change_dict[f"R{i:.2f}"] = int(count) # Format the denomination correctly and store the count
            change_due -= count * i # Subtract the value of the denomination from the change_due
    return change_dict

ammount_1 = 250  # R250
ammount_2 = 183.75  # R183.75
change_1 = change(ammount_1, ammount_2)
print(change_1)
