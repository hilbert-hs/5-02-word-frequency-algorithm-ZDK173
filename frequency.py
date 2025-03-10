# 5.02 Word Frequency Algorithm

# replace the sample text with your paragraph.
example_paragraph = "Those were great images in the background for the cruicible connections."

# make all letters lowercase
ex_par_lowered = example_paragraph.lower()

#remove all periods (you'll want to repeat this for any other punctuation in your paragraph)
ex_par_lower_no_punc = ex_par_lowered.replace(".", "").replace(",", "")

# convert the paragraph into a list of individual strings
ex_word_list = ex_par_lower_no_punc.split(" ")

words = ex_word_list
dictionary = {

    }

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

# for word in words:
#     print(f'{word} apears {dictionary[word]} times. ')

wordWanted = input("What word would you like to see? ")
if wordWanted in words:
    print(f'{wordWanted} apears {dictionary[wordWanted]} times.')
else:
    print("That word is not avalible.")
