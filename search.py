import matplotlib.pyplot as plt
import numpy as np

def draw_p(a, d, e):
    x = np.linspace(-10, 10, 400)
    y = a * (x + d)**2 + e 

    plt.plot(x, y, label=f'y = {a}(x + {d})² + {e}', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('parabola')
    plt.axhline(0, color='black',linewidth=0.2)
    plt.axvline(0, color='black',linewidth=0.2)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.2)
    plt.legend()
    plt.show()

print("Formula: a(x+d)²+e")
a = float(input('enter (a): '))
d = float(input('enter (d): '))
e = float(input('enter (e): '))
draw_p(a, d, e)
