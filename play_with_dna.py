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
    # to do     

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
                            
                
            
        