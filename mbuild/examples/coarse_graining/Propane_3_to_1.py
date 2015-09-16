from examples.alkane.alkane import Alkane
import mbuild as mb

from mbuild.proxy import create_proxy


class Propane(mb.Compound):
    def __init__(self):
        super(Propane, self).__init__()

        alkane = Alkane(n=3, cap_front=True, cap_end=True)

        self.add(alkane, 'C3')

if __name__ == '__main__':

    p = Propane()

    tier = [Propane]

    proxy = create_proxy(p, leaf_classes=tier)

    print("Leaves of the proxy:")
    for leaf in proxy.particles:
        print(" {}".format(leaf))



