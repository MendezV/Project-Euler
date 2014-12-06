import sys

n=int(sys.argv[1])
sum_squares= n*(n+1)*(2*n+1)/6
sum=n*(n+1)/2
square_sum=sum**2

difference= square_sum - sum_squares

print difference