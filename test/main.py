x = [1,2,3,4,5]
y = [1,2,3,4,5]
# write down every possibnle combination of x and y

# Path: main.py
x = [1,2,3,4,5]
y = [1,2,3,4,5]
# write down every possibnle combination of x and y
points = []
for i in x:
    for j in y:
        points.append((i,j))
print(points)

