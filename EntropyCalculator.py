#entropy calculator taking text from a text(file)
import sys

#open file and read text(text)
with open("texts/"+sys.argv[1], "r") as file:
    text = file.read()
    
#calculation of letters
letter_count = {}
character_count = {}
text_length = len(text)

#counting cycle
for letter in text:
    if letter.isalpha():
        if letter in letter_count:
            letter_count[letter]['count'] += 1
        else:
            letter_count[letter] = {'count':1, 'percentage':0}
    else:
        if letter in letter_count:
            character_count[letter]['count'] += 1
        else:
            character_count[letter] = {'count': 1, 'percentage': 0}
            
#I combine the two dictionaries
count_complete = {**letter_count, **character_count}

#calculation of the percentage
for lettera, info in count_complete.items():
    info['percentage'] = (info['count'] / text_length) * 100

#sort the dictionary
count_complete_sorted = dict(sorted(count_complete.items(), key=lambda x: x[1]['percentage'], reverse=True))

#print the result as output
for letter, info in count_complete_sorted.items():
    print(f"'{letter}': count: {info['count']}, percentage: {info['percentage']:.2f}%")