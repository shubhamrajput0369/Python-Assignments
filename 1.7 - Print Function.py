// Author: Shubham Bhagwansing Rajput
// Python

// 1st Method
n = int(input())

for n in range(1,n+1):
    print(n,end='')


// 2nd Method
n = int(input())

print(*range(1,n+1), sep='')
