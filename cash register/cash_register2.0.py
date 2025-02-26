def change(ammount_paid, ammount_due):
    # Denominations in cents (R1 = 1, R2 = 2, etc. to avoid floating point issues)
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    
    # Calculate the change due in cents (to avoid floating-point issues)
    change_due = round(ammount_paid - ammount_due, 2) * 100
    
    change_dict = {}

    # Loop through each denomination, starting from the largest
    for denomination in denominations:
        # How many of this denomination are needed
        count = change_due // denomination
        
        # If this denomination is needed, add it to the dictionary
        if count > 0:
            # Store the denomination in Rand (R)
            change_dict[f"R{denomination / 100}"] = count
            
            # Reduce the change_due by the amount we've given in this denomination
            change_due -= count * denomination

    # Adding remaining change in smaller denominations
    if change_due > 0:
        change_dict["Remaining change in smaller denominations"] = change_due / 100

    return change_dict

# Example usage:
ammount_1 = 250  # R250
ammount_2 = 183.75  # R183.75

change_dict = change(ammount_1, ammount_2)
print(change_dict)
