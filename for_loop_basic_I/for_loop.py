# 1. Basic - Print all integers from 0 to 150.
for i in range(0, 151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1000, 5):
    print(i)

""" 3. Counting, Dojo Way - print integer 1 to 100.
If divisible by, print "Coding" instead.
If divisible by 10, print "Coding Dojo"."""
for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

""" 4. That Sucker's Huge - Add odd integers from 0 to 500,000
and print the final sum."""
odd_sum = 0
for x in range(1, 500001, 2):
    odd_sum = odd_sum + x
print(odd_sum)

"""5. Countdown by Fours - Print positive numbers starting at 2018
counting down by fours."""
for x in range(2018, 0, -4):
    print(x)

""" 6. Flexible Counter - set three variables lowNum, highNum, mult.
Starting at lowNum and going thru highNum, print only the integers
that are a multiple of mult. For example, if lowNum=2, highNum=9
and mult=3, the loop should print 3, 6, 9 (onsuccessive lines)"""
lowNum = 2
highNum = 9
mult = 3
for count in range(lowNum, highNum + 1):
    if count % mult == 0:
        print(count)
