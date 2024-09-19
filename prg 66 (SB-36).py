from collections import defaultdict

def count_tuples(A, B, C, D):
    sum_count = defaultdict(int)
    for a in A:
        for b in B:
            sum_count[a + b] += 1
    
    count = 0
    for c in C:
        for d in D:
            target_sum = -(c + d)
            if target_sum in sum_count:
                count += sum_count[target_sum]
    
    return count

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(count_tuples(A, B, C, D))  
