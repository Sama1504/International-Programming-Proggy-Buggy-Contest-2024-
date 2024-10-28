number = 1
while True:
    text_representation = str(number)
    letter_count = len(text_representation)
    
    if letter_count >= 100:
        print(number)
        break
    
    number += 1