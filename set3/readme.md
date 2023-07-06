Lab-book wk 3

Exercise 1 was tedious, and I realized that I often overcomplicate everything. I started out by using if statements inside the while loop to manually run break until stubborn asker became super complicated and I asked a friend for help. Using only while made the code much cleaner and easier to follow, which helped with solving the problems.

My code would also commonly fail because of mis-matched formatting, sometimes the numbers were integers and other times they were strings and when I tried to relate these to one another the code would break.

Exercise 3 wasn't working for a while, I took a break and came back to it and then it was fine? I think I was overcomplicating it again but just calling the functions i had previously made worked well and still looked clean. Im not sure why I needed text in inside not_number_rejector and it didn't matter what was in there as long as it had text.

Exercise 4 was pretty difficult. I ended up looking around online for how to do make a binary search algorithm and in doing so I have learnt how the code works. The search is simple and just guesses the middle number, replacing one of the bounds with the middle number if it was incorrect. It repeats this until it finds the number.

Note:
I am on a mac, and running the tests from terminal didn't work here. I would use the same command as always: python3 ../course/set3/tests.py but this would just return the error:

Traceback (most recent call last):
  File "/Users/Nico/1161/me/../course/set3/tests.py", line 16, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

^^ I have now installed figured out that matplotlib was something i needed to install and have installed it as well as installing func_timeout and am now able to run tests.

The tests are saying that stubborn_asker, not_number_rejector, and test_super_asker are all not working which i don't know why since they all pass the when i run it. It might just be a syntax error in the way i have written them and what the tests are looking for.