import numpy as np
from math import pow

from EnumeratePO import enumeratePreorders
from utils import makeAlphas


def isReflexive(a: np.ndarray) -> bool:
    return (a[np.diag_indices_from(a)] == True).all()


def isTransitive(a: np.ndarray) -> bool:
    n = a.shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][j] and a[j][k]:
                    if not a[i][k]:
                        return False
    return True


def getPreOrders(n):
    res = list()
    alphas = makeAlphas(n * n)
    samples = [alpha.reshape(n, n) for alpha in alphas]
    for sample in samples:
        if isReflexive(sample) and isTransitive(sample):
            res.append(sample)
    return res


if __name__ == '__main__':
    n = 4
    std = getPreOrders(n)
    out = enumeratePreorders(n)
    std_line = [x.reshape(1, n*n)[0].tolist().__str__() for x in std]
    out_line = [x.reshape(1, n*n)[0].tolist().__str__() for x in out]
    std_set = set(std_line)
    out_set = set(out_line)
