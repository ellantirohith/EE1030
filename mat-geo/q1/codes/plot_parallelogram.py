import matplotlib.pyplot as plt

# Load the data from the file
data = []
with open('parallelogram.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data.append((x, y))


x_coords, y_coords = zip(*data)


x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]


plt.figure()
plt.plot(x_coords, y_coords, 'bo-', label='Parallelogram')
plt.fill(x_coords, y_coords, alpha=0.3)
plt.title('Parallelogram Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()

