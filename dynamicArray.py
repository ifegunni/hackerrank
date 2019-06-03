Create a list,seqList , of  empty sequences, where each sequence is indexed from  to . The elements within each of the  sequences also use -indexing.
Create an integer, , and initialize it to .
The  types of queries that can be performed on your list of sequences () are described below:
Query: 1 x y
Find the sequence, , at index  in .
Append integer  to sequence .
Query: 2 x y
Find the sequence, , at index  in .
Find the value of element  in  (where  is the size of ) and assign it to .
Print the new value of  on a new line
Task 
Given , , and  queries, execute each query.

Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.

Input Format

The first line contains two space-separated integers,  (the number of sequences) and  (the number of queries), respectively. 
Each of the  subsequent lines contains a query in the format defined above.

Constraints

It is guaranteed that query type  will never query an empty sequence or index.
Output Format

For each type  query, print the updated value of  on a new line.

Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3
Explanation

Initial Values: 
 
 
 = [ ] 
 = [ ]

Query 0: Append  to sequence . 
 
 = [5] 
 = [ ]

Query 1: Append  to sequence . 
 = [5] 
 = [7]

Query 2: Append  to sequence . 
 
 = [5, 3] 
 = [7]

Query 3: Assign the value at index  of sequence  to , print . 
 
 = [5, 3] 
 = [7]

7
Query 4: Assign the value at index  of sequence  to , print . 
 
 = [5, 3] 
 = [7]

3




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastAnswer  = 0
    seqList = []
    res = []

    for i in range(n):
        seqList.append([])

    for q in queries:
        index = (q[1]^lastAnswer)%n

        if q[0] == 1:
            seqList[index].append(q[2])

        else:
            position = q[2] % len(seqList[index])
            lastAnswer = seqList[index][position]
            res.append(lastAnswer)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
