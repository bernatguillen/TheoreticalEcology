import numpy as np
import matplotlib.pyplot as plt

def newp(p, WA, W):
    return p*WA/W


def WA(WAA, WAa, Waa, p):
    return p*WAA + (1-p)*WAa


def W(WAA, WAa, Waa, p):
    return p**2*WAA + 2*p*(1-p)*WAa + (1-p)**2*Waa


def myplot(WAA, WAa, Waa):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p = np.linspace(0, 1, 100)
    pprime = newp(p, WA(WAA, WAa, Waa, p), W(WAA, WAa, Waa, p))
    line, = ax.plot(p, pprime, lw=2)
    line1, = ax.plot(p, p, "r--")
    ax.set_title("$W_{AA}=$" + str(WAA) + ", $W_{Aa}=$" + str(WAa) +
                 ", $W_{aa}=$" + str(Waa))
    ax.set_xlabel("$p$")
    ax.set_ylabel("$p'$")
    fig.savefig("WAA" + str(WAA) + "WAa" + str(WAa) +
                "Waa" + str(Waa) + ".png")


def plotW(WAA, WAa, Waa):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p = np.linspace(0, 1, 100)
    Wbar = W(WAA, WAa, Waa, p)
    line, = ax.plot(p, Wbar, lw=2)
    ax.set_title("$W_{AA}=$" + str(WAA) + ", $W_{Aa}=$" + str(WAa) +
                 ", $W_{aa}=$" + str(Waa))
    ax.set_xlabel("$p$")
    ax.set_ylabel("$\\bar{W}$")
    fig.savefig("Wbar" + "WAA" + str(WAA) + "WAa" + str(WAa) +
                "Waa" + str(Waa) + ".png")
