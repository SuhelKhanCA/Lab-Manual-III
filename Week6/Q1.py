# create 3rd tuple from two tuple

tup1 = tuple(map(int, input("Enter the elments of first tuple: ").split()))
tup2 = tuple(map(int, input("Enter the elments of second tuple: ").split())
)
tup3 = tup1 + tup2

print(tup3)