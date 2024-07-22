# definition of the points
points = []

for i in range(2):
    x = float(input(f"enter x coordinate for {i + 1}. point: "))
    y = float(input(f"enter y coordinate for {i + 1}. point: "))
    points.append((x, y))


# Function of the Euclidean distance
def euclidean_Distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# Calculation of the Euclidean distance
distance = euclidean_Distance(points[0], points[1])

# print the results
print("Euclidean Distance is: ", distance)
