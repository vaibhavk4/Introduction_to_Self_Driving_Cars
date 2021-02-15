#!/usr/bin/env python
# coding: utf-8

# # Calculating Probabilities
# 
# In this lesson, you learned a lot about **Bayes' rule** and got more practice calculating the probability that an event will happen while working through examples. In the following quizzes, you'll be asked to write some simple functions that can help you calculate prior, joint, and total probabilities, given limited information. These will be useful calculations to understand and implement in code.
# 
# Once you write your code, it's good practice to test your code and work through any small errors that may occur, so I encourage you to run your code with some test probability values to see if your code is working the way you expect. The last cell in this notebook will also provide feedback on your output! 
# 
# The following code quizzes assume that you are familiar with the notation:
# 
# The probability of an event A happening:
# $$P(A)$$
# 
# The probability of another event or test B happening, given the occurrence of event A:
# $$P(B|A)$$
# 
# The probability of another event or test B happening, given that event A has *not* occurred:
# $$P(B|\neg A)$$ 

# ### TODO: Complete the `complement` function
# 
# Complete the function so that it returns the complement of P(A), which is the probability that the event did not happen.

# In[23]:


# The complement function takes in the probability of an event, P(A).
def complement(p_A):
    
    
    complement = 1 - (p_A)
    
    return complement

    
## Change this test value and test out your code!
p_test = 0.7

# Running your code with the p_test value
complement_test = complement(p_test)
print('Your function returned that the complement of '+str(p_test) +' is: '+str(complement_test))


# ### Testing Cell
# 
# Run this cell and it will compare the output of your function with the correct, expected output.
# 
# **Assertions**
# 
# This cell is using something called `assertions` in Python, which are statements that check the validity of code. In this case, the assertion checks that the output of your function: `comp`, is equal to the expected output: `correct_comp` and then prints out feedback!
# 
# **Your code should pass both tests and work for any value of p_A.**

# In[24]:



import solution

test_value = 0.4265

# This line calls the function and stores the output
comp = complement(test_value)
correct_comp = solution.complement(test_value)

# Assertion, comparison test
try:
    assert(abs(comp - correct_comp) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the complement is: ' +str(comp) 
           + ', which does not match the correct value: ' +str(correct_comp))


# Test 2
comp2 = complement(solution.test_value)
correct_comp2 = solution.complement(solution.test_value)

# Assertion, comparison test
try:
    assert(abs(comp2 - correct_comp2) < 0.0001)
    print('That\'s right!')
except:
    print ('For test 2, your code returned that the complement is: ' +str(comp2) 
           + ', which does not match the correct value.')


# ### Calculating Joint Probabilities
# 
# ### TODO: Comple `joint`

# In[27]:


## joint function
def joint(p_A, p_B):
    
    
    ## calculates the joint probability of 
    ## any variables p_A, p_B, WHEN THOSE PROBABILITIES
    ## ARE INDEPENDENT (this code wouldn't work 
    ## for probabilities that depend on each other).
    joint = p_A*p_B
    
    return joint

    
## Defined test probabilities and wrote print statements to test 
## the output of your function!
p_a_test = 0.2
p_b_test = 0.4
j = joint(p_a_test, p_b_test)

print('Your function returned that the joint probability is: '+str(j))


# ### Testing Cell
# 
# Run this cell and it will compare the output of your function with the correct, expected output.
# 
# **Your code should pass both tests and work for any value of p_A and p_B.**

# In[28]:


# Test values
test_A = 0.15
test_B = 0.42

# This line calls  function and stores the output
j = joint(test_A, test_B)
correct_j = solution.joint(test_A, test_B)

# Assertion, comparison test
try:
    assert(abs(j - correct_j) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the joint probability is: ' +str(j) 
           + ', which does not match the correct value.')

