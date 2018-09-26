import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_points = 0
    bob_points = 0
    a_triplet=[a0,a1,a2]
    b_triplet=[b0,b1,b2]
    for a_val, b_val in zip(a_triplet, b_triplet):
        if a_val < b_val:
            bob_points += 1
        elif a_val > b_val:
            alice_points += 1

        
    print (alice_points,bob_points)
	
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
