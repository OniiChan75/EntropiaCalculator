#entropy calculator taking text from a text(file)
import sys

#open file and read text(text)
f = open("texts/"+sys.argv[1], "rb")
text = f.read()
f.close()
    
#calculation of letters
letter_count = {}
text_length = len(text)
print(text_length)

#counting cycle
for letter in set(text):
    letter_count[chr(letter)] = text.count(letter)

#calculation of the percentage
for letter, count in letter_count.items():
    letter_count[letter] = {'count': count, 'percentage': count / text_length * 100}

#sort the dictionary
letter_count_sorted = dict(sorted(letter_count.items(), key=lambda x: x[1]['percentage'], reverse=True))

#print the result as output
for letter, info in letter_count_sorted.items():
    print(f"'{letter}': count: {info['count']}, percentage: {info['percentage']:.2f}%")
    