def compare_codes(guess, secret):
    # possible_colors = ['r',y,b1,g,p,o]
    correct = 0
    correctish = 0
    for a,b in zip(guess, secret):
        if a == b:
            correct += 1
    for a,b in zip(guess, secret):
        if a != b and a in secret and guess.count(a) >= secret.count(a):
            correctish += 1
    return correct, correctish

print(compare_codes("1122","2111"))
   
   
   
   
  #  #input-validation 
    # for a,b in zip(guess, secret):
    #   if not guess.isinstance(guess, str) or not secret.isinstance(secret, str):
    #     return ValueError
    #   if not guess.isalpha() or not secret.isalpha():
    #     return ValueError
    #   if guess.len() != 4 or secret.len() != 4:
    #     return ValueError