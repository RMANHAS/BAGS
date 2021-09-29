import random

upper_char = ["A","S","E","R","Q"]

lower_char = ["a","q","e","for","t"]



num = ["1","2","3","4","5","6","7","8","9","0"]

hello = random.choice(upper_char)+random.choice(lower_char)+random.choice(special_char)+random.choice(num)

print("YOUR PASSWORD IS :-",hello)
