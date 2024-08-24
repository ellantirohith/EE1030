import matplotlib.pyplot as plt


A = (1, 2)
B = (4, 3)
C = (6, 6)
D = (3, 5)


points = [A, B, C, D, A]


x_coords, y_coords = zip(*points)


plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='g')


plt.text(*A, ' A(1,2)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(*B, ' B(4,3)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(*C, ' C(6,6)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(*D, ' D(3,5)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Parallelogram ABCD')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')


plt.show()

