"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

lower_case_list = range(97,122)

seq = [str(chr(X)+chr(Y)+chr(Z)) for X in lower_case_list for Y in lower_case_list for Z in lower_case_list ] 

print seq