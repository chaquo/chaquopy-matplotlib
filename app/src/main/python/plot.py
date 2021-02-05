import io
import matplotlib.pyplot as plt

def plot(x, y):
    xa = [float(word) for word in x.split()]
    ya = [float(word) for word in y.split()]

    fig, ax = plt.subplots()
    ax.plot(xa, ya)

    f = io.BytesIO()
    plt.savefig(f, format="png")
    return f.getvalue()
