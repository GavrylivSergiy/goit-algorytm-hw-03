import matplotlib.pyplot as plt
import numpy as np

def koch_curve(order, length):
    def recurse(order):
        if order == 0:
            return "F"
        else:
            curve = recurse(order - 1)
            return curve.replace("F", "F+F--F+F")

    curve = recurse(order)
    angle = 0
    current_pos = np.array([0, 0])
    points = [current_pos]

    for move in curve:
        if move == "F":
            new_pos = current_pos + length * np.array([np.cos(angle), np.sin(angle)])
            points.append(new_pos)
            current_pos = new_pos
        elif move == "+":
            angle += np.pi / 3
        elif move == "-":
            angle -= np.pi / 3

    return np.array(points)

def koch_snowflake(order, size):
    length = size / (3 ** order)

    # Initial triangle points
    angle = 2 * np.pi / 3
    p1 = np.array([0, 0])
    p2 = np.array([size, 0])
    p3 = np.array([size * np.cos(angle), size * np.sin(angle)])

    # Generate each side of the snowflake
    side1 = koch_curve(order, length) + p1
    side2 = koch_curve(order, length) @ np.array([[np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)], 
                                                  [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]]) + p2
    side3 = koch_curve(order, length) @ np.array([[np.cos(4 * np.pi / 3), -np.sin(4 * np.pi / 3)], 
                                                  [np.sin(4 * np.pi / 3), np.cos(4 * np.pi / 3)]]) + p3

    # Correct side connections
    side2 += side1[-1] - side2[0]
    side3 += side2[-1] - side3[0]

    return np.vstack([side1[:-1], side2[:-1], side3])

def main():
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = float(input("Введіть розмір фракталу: "))

    # Build the Koch snowflake
    snowflake = koch_snowflake(order, size)

    # Plot the snowflake
    plt.figure(figsize=(8, 8))
    plt.plot(snowflake[:, 0], snowflake[:, 1], 'k-')
    plt.fill(snowflake[:, 0], snowflake[:, 1], 'white')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
