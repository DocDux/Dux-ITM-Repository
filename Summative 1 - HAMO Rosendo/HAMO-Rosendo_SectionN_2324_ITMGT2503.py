#!/usr/bin/env python
# coding: utf-8

# # General Instructions
# Change the filenames to LastName-FirstName_Section_M-N_2324_ITMGT2503 <br>
# __Ex. GAW-Adriel_SectionM_2324_ITMGT2503__

# # Question 1: Watch Your Words
# Your task is to count the number of times that each word was used in a movie script! Please be guided by the instructions below!

# #### 1a

# In[1]:


# First, to help guide you, here is a list containing tuples. Run this block of code to initialize the list
list_of_tuples = [('A',59),('B',100),('C',20),('D',88),('E',25),('F',38)]

list_of_tuples


# If we want to __sort this tuple according to the numerical value__, using the sort() without any other arguments will not suffice. But, diving a bit deeper into the sort() function, we can see that it can accept two parameters: 
# 
# - `key` which is what will be used as the basis for sorting
# - `reverse` which accepts a Boolean value to determine if the sorting will be ascending or descending
# 

# In[5]:


# execute this cell to see how the two arguments help us achieve the desired result

list_of_tuples.sort(key=lambda x: x[1], reverse=False)

print(list_of_tuples)


# #### 1b

# In[105]:


# To formally start this problem:
# Load the "script.json" file and store it in the `jsondata` variable. 
# The dictionary will contain the "line number" (starting from 0) as the key, 
# and the lines itself as the value

import json

# with open statement
with open(r"C:\Users\Dux\Downloads\script.json", 'r') as file:
    # mydata
    jsondata = json.load(file)


# In[107]:


jsondata['0']


# In[109]:


str(jsondata['0'])


# #### 1c

# In[143]:


# To process the lines in the script, you need to do the following in chronological order:
#### Convert everything into a string first - meaning: convert all values into a string
#### Convert all characters to uppercase characters
#### Remove the following pieces of text: <P>, </P>, <B>, </B>, <I>, </I>
#### Remove all the unnecessary punctuation symbols denoted in the string below
#### instead of removing all unecessary punctuations, replace them with a whitespace
unnecessary_punctuation = r"&$@[].,'#()-\"!?’_;:/"

### how do we convert all values in the json.data dictionary into strings?

for i in range(len(jsondata)):
    # convert all values into a string
    string_conversion = str(jsondata[str(i)])
    jsondata[str(i)] = string_conversion
    # convert all characters to uppercase letters
    uppercase_string = string_conversion.upper()
    jsondata[str(i)] = uppercase_string
    # remove the following pieces of text:
    cleaned_string = uppercase_string.replace("<P>","")
    jsondata[str(i)] = cleaned_string
    slash_P = cleaned_string.replace("</P>","")
    jsondata[str(i)] = slash_P
    no_B = slash_P.replace("<B>","")
    jsondata[str(i)] = no_B
    slash_B = no_B.replace("</B>","")
    jsondata[str(i)] = slash_B
    no_I = slash_B.replace("<I>","")
    jsondata[str(i)] = no_I
    slash_I = no_I.replace("</I>","")
    jsondata[str(i)] = slash_I

    ### replacing all unnecessary punctuations
    punctuation_list = list(unnecessary_punctuation)
    for j in punctuation_list:
        if j in punctuation_list:
            jsondata[str(i)] = jsondata[str(i)].replace(j," ")

jsondata


# In[193]:


type(jsondata['0'])


# #### 1d

# In[183]:


# From here, create a dictionary called `wordcount_dictionary` that will have the key:value pair of word:count
# But, only include words that are three (3) letters or more

accepted_words = [] # initializing list

for i in range(len(jsondata)):
    for j in range(len(jsondata[str(i)])):

        # I know the problem, if I do it this way, it will only return a 'letter' (because that's in the index) and not a word. Unfortunately 
        # I do not have the skills to fix this without my goat ChatGPT so pls be merciful :(((
        
        if j + 1 < len(jsondata[str(i)]):
            if len(script_string[j]) >= 3:
                accepted_words.append(script_string[j])

accepted_words


# In[ ]:


# If there were no errors in the way you processed your data, 
# this should output "Looks Good!"  

import numpy as np
import pandas as pd 

df1 = pd.read_json("output_dictionary_Q1.json",typ="dictionary").sort_values()
df2 = pd.Series(wordcount_dictionary).sort_values()

assert df1.equals(df2), "The dictionaries are not equal. Please check your code again."

print("Looks Good!")


# #### 1e

# In[ ]:


# Afterwards, we want to convert that dictionary to a list containing tuples
# Create a list called "final_wordlist_of_tuples" containing tuples 
# Each tuple should be as follows: (word,count)
# Sort the list by `count` (the second element of the tuple) in descending order
# A correct sample is shown in the markdown cell below
# Hint: this can be done using lambda but you can use a regular function definition. 
# Make sure you go through the mini-tutorial at the start of this problem.




# ___<div align="center">Once sorted, this should be the output of the first five items.</div>___
# 
# |         |             |
# |:--------|------------:|
# | THE     |         830 |
# | JOY     |         585 |
# | AND     |         351 |
# | RILEY   |         326 |
# | SADNESS |         274 |

# # Question 2: Wait... What is LP Doing Here?
# I swear you don't need to do LP here. In fact, the LP formulation is already shown below! 

# #### LP Problem
# In the realm of Sanctoria, nestled deep within the misty forests and craggy mountains, lies the legendary dungeon of The Lost King. It is said to be filled with untold riches, ancient relics, and formidable monsters guarding its treasures. As the wise and benevolent ruler of Sanctoria, King Hexter has decided to assemble a daring raiding party to plunder the depths of the dungeon and reclaim its treasures for the kingdom.
# 
# As the illustrious ruler of Sanctoria, King Hexter is faced with the daunting task of assembling a formidable dungeon raiding party. The success of the raid hinges upon the careful selection and allocation of resources to hire Fighters, Rangers, and Clerics for the expedition into the depths of the Lost King’s home.
# 
# In the planning of this dungeon raid, the King’s advisors have provided him with the following: Gold: The kingdom's treasury can afford to spend no more than 18000 gold coins on hiring adventurers. Each Fighter costs 1000 gold coins, each Ranger costs 600 gold coins, and each Cleric costs 750 gold coins. Lumber: The construction of necessary equipment for each troop requires ample quality lumber. The kingdom has 12000 units of lumber available for the raid. Each Fighter requires 500 units, each Ranger requires 750 units, and each Cleric requires 300 units. Food: The raid will last several weeks so food must be kept and stored during the raid. The raid will be able to carry 1500 units of food available for the raid. Each Fighter requires 50 units, each Ranger requires 45 units, and each Cleric requires 75 units. Power: The power of the raiding party will dictate the level of the raid’s success. Each Fighter gives 10 points, each Ranger gives 12 points, each Cleric gives 16 points.
# 
# The King’s military advisors have also discussed strategies that will be employed in the raid: Having more Fighters than Rangers will bolster the raiding party's frontline defense To avoid casualties, each Cleric must have at most 3 Fighters that they are supporting

# # LP Formulation
# 
# **Decision Variables:**
# - (F): Number of Fighters
# - (R): Number of Rangers
# - (C): Number of Clerics
# 
# **Objective:** Maximize the power of the raiding party.
# 
# $$ \text{Maximize Z:  } 10F + 12R + 16C $$
# 
# 
# **Subject to:**
# 
# \begin{aligned}
# 1000F + 600R + 750C &\leq 18000 && \text{(Gold constraint)} \\
# 500F + 750R + 300C &\leq 12000 && \text{(Lumber constraint)} \\
# 50F + 45R + 75C &\leq 1500 && \text{(Food constraint)} \\
# F, R, C &\geq 0 && \text{(Non-negativity constraints)}
# \end{aligned}
# 

# In[239]:


# With the LP Formulation as a basis, find the optimal solution to the problem using Python
# Use the variable `optimal_Z` to store the value of the Maximum Z
# Use the variables `optimal_F`, `optimal_R`, and `optimal_C` to store 
# the optimal solution of Fighters, Rangers, and Clerics respectively
# Note: There may be multiple configurations of F, R, C to attain the Maximum Z. 
# Hint: Don't use your DecSci brain, use your Python programming brain

'''
Maximizing Z = 10F + 12R + 16C
'''

optimal_Z = 0 # storing the value of Max Z
optimal_F = 0 # storing the value of optimal solution of Fighters
optimal_R = 0 # "" Rangers
optimal_C = 0 # "" Clerics

while (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= 18000:
    while (500*optimal_F + 750*optimal_R + 300*optimal_C) <= 12000:
        while (50*optimal_F + 45*optimal_R + 75*optimal_C) <= 1500:
            optimal_F += 1
            optimal_R += 1
            optimal_C += 1

print(f"{optimal_F},{optimal_R},{optimal_C}")

if 


# In[73]:


# With the LP Formulation as a basis, find the optimal solution to the problem using Python
# Use the variable `optimal_Z` to store the value of the Maximum Z
# Use the variables `optimal_F`, `optimal_R`, and `optimal_C` to store 
# the optimal solution of Fighters, Rangers, and Clerics respectively
# Note: There may be multiple configurations of F, R, C to attain the Maximum Z. 
# Hint: Don't use your DecSci brain, use your Python programming brain


optimal_F = 0
optimal_R = 0
optimal_C = 0

optimal_Z = 10*int(optimal_F) + 12*int(optimal_R) + 16*int(optimal_C)

# Objective: Maximize power of the raiding party
# Max Z: 10F + 12R + 16C

while (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= gold:
    while (500*optimal_F + 750*optimal_R + 300*optimal_C) <= lumber:
        while (50*optimal_F + 45*optimal_R + 75*optimal_C) <= food:
            optimal_F += 1
            optimal_R += 1
            optimal_C += 1

print(f"{optimal_F},{optimal_R},{optimal_C}")
print(optimal_Z)


# In[41]:


# If there were no errors in the way you processed your data, 
# this should output "Looks Good!"  

assert optimal_Z == 344
assert (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= 18000
assert (500*optimal_F + 750*optimal_R + 300*optimal_C) <= 12000
assert (50*optimal_F + 45*optimal_R + 75*optimal_C) <= 1500
print("Looks Good!")


# # Question 3: Collatz

# #### 3a

# The __Collatz Conjecture__ is a mathematical sequence defined as follows:
# 
# 1. Start with any positive integer n.
# 2. If n is even, divide it by 2 to get n / 2.
# 3. If n is odd, multiply it by 3 and add 1 to get 3n + 1.
# 4. Repeat the process with the resulting number.
# 5. The conjecture states that no matter which positive integer you start with, you will always eventually reach 1.

# As an example, the number 5 will follow this sequence:
# - Start at __`5`__
# - 5 is odd, so we multiply by 3 and adds 1 to get __`16`__
# - 16 is even, so we divide by 2 to get __`8`__
# - 8 is even, so we divide by 2 to get __`4`__
# - 4 is even, so we divide by 2 to get __`2`__
# - 2 is even, so we divide by 2 to get __`1`__
# - Since the number is 1, we stop the sequence. 
# 
# For the purposes of this problem, let's call the list containing the numbers __[5, 16, 8, 4, 2, 1]__ the __`Collatz Sequence`__. 
# 
# This sequence also has a __`Collatz Length`__ of 6, since the sequence cycled through 6 numbers.
# 
# The sequence also had a __`Max Collatz`__ of 16, since that was the highest number in the sequence. 
# 
# Lastly, the sequence had a __`Sequence Sum`__ of 36, since that is the sum of all the numbers in the sequence.

# In[213]:


def Collatz(start_number):
    '''
    Create a SINGLE FUNCTION that will return the
    `Collatz Sequence`, the `Collatz Length`,
    and the `Max Collatz` in a dictionary.

    The key-value pairs will be the following:
    "collatz_sequence": the list containing the numbers of the sequence
    "collatz_length": the length of the sequence
    "max_collatz": the maximum number achieved in the sequence
    "sequence_sum": the sum of all the numbers in the sequence 

    Parameters
    ----------
    start_number: int
        the number used to start the sequence

    Returns
    -------
    dictionary
        the dictionary containing the key-value pairs of the
        collatz_sequence, collatz_length, max_collatz, and sequence_sum
    '''
    
    collatz_sequence = [] # initializing the collatz_sequence list
    
    current_term = int(start_number) # number we're starting with

    collatz_sequence.append(current_term) # appending the current_term (starting no.) to our list

    sequence_sum = 0 # accumulator variable
    
    while current_term > 1:
        if current_term % 2 == 0:
            current_term = current_term * 0.5
            collatz_sequence.append(current_term)
        elif current_term % 2 != 0:
            current_term = (current_term*3)+1
            collatz_sequence.append(current_term)

    collatz_length = len(collatz_sequence)
    max_collatz = max(collatz_sequence)

    for i in range(len(collatz_sequence)):
        sequence_sum += collatz_sequence[i]

    global dictionary
    dictionary = {'collatz_sequence':collatz_sequence,'collatz_length':collatz_length,'max_collatz':max_collatz,'sequence_sum':sequence_sum}

    return dictionary

Collatz(5)


# #### 3b

# In[237]:


def Collatz_winner(number_list):
    '''
    Given a list of positive integers, return the `winner`
    among them. The `winner` is categorized as such:
        
        1. The number has the largest `collatz_length`; and
        2. The number has the largest `max_collatz`

    If there is no winner, then the function must return None

    Parameters
    ----------
    number_list: list
        a list of positive integers

    Returns
    -------
    integer (or NoneType)
        the "winner" that follows the specific criteria above
        returns a None if it does not meet all the criteria above
    '''

    list_collatz_lengths = []
    list_collatz_maximums = []
    winner = []
    
    for i in number_list:
        Collatz(i)
        length_entry = dictionary['collatz_length']
        list_collatz_lengths.append(length_entry)
        
        max_collatz_entry = dictionary['max_collatz']
        list_collatz_maximums.append(max_collatz_entry)

    max_length = max(list_collatz_lengths)
    max_maximum = max(list_collatz_maximums)

    for i in number_list:
        Collatz(i)
        if dictionary['collatz_length'] == max_length and dictionary['max_collatz'] == max_maximum:
            winner.append(i)
        else:
            winner.append("None")

    for j in range(len(winner)):
        if type(winner[j]) == int:
            return winner[j]
            
Collatz_winner(range(1,51))


# In[ ]:


assert Collatz_winner(range(1,51)) == 27
assert Collatz_winner(range(1,10)) == 9
assert Collatz_winner(range(50,100)) == 97
assert Collatz_winner(range(50,100,4)) == 54
assert Collatz_winner(range(20,131,5)) == 110
assert Collatz_winner(range(75,180,9)) == 129

