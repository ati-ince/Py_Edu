'''
Write a function that takes a string as input and returns the length of the longest sequence of identical characters
found in the string. For example, longestRun(“abcd”) returns 1, longestRun(“abcccd”) returns 3, longestRun(“a
simple string with aaabbbccccdddd”) returns 4.

Bonus: write unit tests
'''

def LongestRun(sstring):
    #get uniq
    uniq=list(set(sstring))
    longest=0

    for un in uniq:
        lenn = 0
        for ch in sstring:
            if un==ch:
                lenn+=1
        if lenn>longest:
            longest=lenn
    return longest
     

Testdata= [
        "abcd",
        "abcccd",
        "aaabbbccccdddd",
        "aaaxxxrrrfffgggyyykkkkkkdfdettrtrgsdffdnhgmjkjikkkkkkkkkkkkkkfffdddcasee"
          ]

def TestLongestRun(data):
    for i,dt in enumerate(data):
        res=LongestRun(dt)
        print(i, res)


TestLongestRun(Testdata)

# 15 min spend