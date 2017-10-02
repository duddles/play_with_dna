#!/usr/bin/python
'''
8/4/14
play with dna

'''
verbose = True
import sys
  
def print_matrix(matrix):
    for i in matrix:
        i = map(str, i)
        s = '\t'.join(i)
        print s     

def alignment(s1, s2, print_option = 0):
    '''
    builds 2d list of lists 
    sees if can do global alignment within m changes
    s1 is going vertically down the rows, s2 horizontal across columns
    returns the score in the bottom right
    '''
    a = []
    s1 = '_' + s1
    s2 = '_' + s2
    n = len(s1) # the size of the 2d array will include initialization row/col
    a.append(range(0,-n,-1))
    for i in xrange(1,n):
        a.append([-i] + [0] * (n-1))
    # append an underscore so that i can access the strings the same as the array

    
    for row in xrange(1,n):
        for col in xrange(1,n):
            if s1[row] == s2[col]:
                a[row][col] = max(a[row-1][col]-1, a[row-1][col-1], a[row][col-1]-1)
            else:
                a[row][col] = max(a[row-1][col]-1, a[row-1][col-1]-1, a[row][col-1]-1)
    if print_option != 0:
        print_matrix(a)
    return -a[-1][-1]     

def count_mismatches(s1, s2):
    '''
    returns # of mismatched positions
    '''
    return len([i for i,j in zip(s1,s2) if i != j])

with open(sys.argv[1]) as FH:
    for line in FH:
        matches_seen = {}
        nonmatches_seen = set()
        line = line.rstrip()
        s, m, string = line.split()
        m = int(m)
        
        a = []
        for _ in xrange(m + 1):
            a.append([])
        
        for pos in xrange(len(string)-len(s)+1):
            substring = string[pos:pos+len(s)]
            
            if substring in matches_seen:
                a[matches_seen[substring]].append(substring)
            elif substring not in nonmatches_seen:
                if substring == s:
                    a[0].append(substring)
                else:
                    #n_mismatches = count_mismatches(s, substring)
                    #if n_mismatches <= m:
                    #    a[n_mismatches].append(substring)   
                    #else:
                    score = alignment(substring, s)
                    if score <= m:
                        a[score].append(substring)
                        matches_seen[substring] = score
                    else:
                        nonmatches_seen.add(substring)
               
            # try insertion/deletion pairs
        all_seq = []
        for i in a:
            if i:
                i.sort()
                all_seq = all_seq + i
        if all_seq:
            print ' '.join(all_seq)
        else:
            print 'No match'
                            
                
            
        
