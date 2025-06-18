import random
import time

def quick(arr):
    if len(arr)<=1:
        return arr
    piv=arr[len(arr)//2]
    high=[x for x in arr if x >piv ]
    low=[x for x in arr if x <piv]
    mid = [x for x in arr if x ==piv]
    return quick(low)+mid+quick(high)

def calc_time(arr):
    start=time.time()
    quick(arr)
    size=len(arr)
    avg_time=time.time()-start
    start=time.time()
    quick(sorted(arr))

    best_time=time.time()-start
    quick(sorted(arr,reverse=True)) 
    
    worst_time=time.time()-start

    return len(arr),best_time,avg_time,worst_time

user_inp=[random.randint(1,1000) for _ in range(38)]

print(f"38\t\tBest_Case\t\tAvg_Case\tWorst_Case")
for n in user_inp:
    arr=[random.randint(1,1000) for _ in range(n)]
    n,best_time,avg_time,worst_time=calc_time(arr)
    print(f"\n{n}\t\t{best_time:6f}\t\t{avg_time:6f}\t{worst_time:6f}")

