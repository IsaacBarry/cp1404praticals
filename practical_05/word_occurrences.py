"""
Word Occurrences
"""

texts = input("Text: ")
text = texts.split()
count_dict = {}

for word in text:
    count_dict[word] = count_dict.get(word, 0) + 1
text_list = list(count_dict.keys())
text_list.sort()
for word in text_list:
    print("{} : {}".format(word,count_dict[word]))
