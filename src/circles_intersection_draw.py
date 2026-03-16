import matplotlib.pyplot as plt

def draw_data(circle1, circle2):
    x1, y1, r1 = circle1.values()
    x2, y2, r2 = circle2.values()

    fig, ax = plt.subplots()

    circle_a = plt.Circle((x1, y1), r1, fill=False, color="blue")  # vytvoření kružnice
    circle_b = plt.Circle((x2, y2), r2, fill=False, color="blue")  # vytvoření kružnice
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)

    ax.set_aspect("equal")
    ax.autoscale(enable=True, axis='both', tight=None)
    plt.show()