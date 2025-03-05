[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18544517)
# 5.02-Word-Frequency-Algorithm

In this lab we will implement a word frequency algorithm. It will tell you how many of each word you had in an essay.

At the top of the document save a variable with a long paragraph (example below). In order to turn this paragraph into a list of lower case words we will use the `split(" ")`, `replace()`, and `lower()` functions. There is starter code in the `frequency.py` file that will do this for you. Feel free to read more about `split()` in the Python documentation, but it's not critical to this lab.

For each word in the document, count the number of times it occurs. Consider the following phrase: 
```
'Cats are cool. Baby cats are called kittens. Cats make great pets.'
```
The word 'cats' appears 3 times. The word 'are' appears 2 times.

The program will first create a dictionary with the words as keys and the number of times they occur as values. 

You will need to write a loop that iterates over your list of words in order to count the frequency. Use this loop to update the value of each word-key in your dictionary. First, check to see if the word already exists in your dictionary. If it does, update the number; if it does not, add it with a frequency of 1.

Then, add the ability for your user to check the frequency of words they are curious about. If the word was in the paragraph it will print the number of times it occurred.

### Example

```
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? cats
'cats' occurs 3 times

>>> python3 word_frequency_lab.py

What word would you like to know the frequency of? dogs
'dogs' does not occur
```

## split(), replace(), and lower()

This is the code to lower case the letters in the paragraph, remove the periods, and split them into individual words:

```python
example_paragraph = "lorem ipsum....."

# make all letters lowercase
ex_par_lowered = example_paragraph.lower()

#remove all periods (you'll want to repeat this for any other punctuation in your paragraph)
ex_par_lower_no_punc = ex_par_lowered.replace(".", "")

# convert the paragraph into a list of individual strings
ex_word_list = ex_par_no_punc.split(" ")
```


