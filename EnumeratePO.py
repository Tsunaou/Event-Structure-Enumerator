import numpy as np
import time

from typing import List
from lemma1 import cond1, cond2, cond3, concat, cond2v2, cond3v2
from utils import adj2PairList, antiSymmetric, setDiagTrue, setDiagFalse, makeAlphas, save_obj2json, load_json


def get_cond3(A, alpha):
    return cond3(A, alpha)
    # return cond3v2(A, alpha)


def get_cond2(A, alpha):
    return cond2(A, alpha)
    # return cond2v2(A, alpha)


def enumeratePreorders(N) -> List[np.ndarray]:
    if N == 0:
        return [np.ones((0, 0), dtype=bool)]
    if N == 1:
        return [np.ones((1, 1), dtype=bool)]
    alphas = makeAlphas(N - 1)
    preOrders = list()
    As = enumeratePreorders(N - 1)
    for A in As:
        for alpha in alphas:
            if get_cond3(A, alpha):
                betas = cond1(A, alpha)
                for beta in betas:
                    if get_cond2(A, beta):
                        preOrders.append(concat(A, alpha, beta))
    return preOrders


def enumerateStrictPreorders(N) -> List[np.ndarray]:
    preorders = enumeratePreorders(N)
    strictPreorders = list(map(setDiagFalse, preorders))
    return strictPreorders


def enumerateStrictPOs(N) -> List[np.ndarray]:
    strictPreorders = enumerateStrictPreorders(N)
    strictPOs = list(filter(antiSymmetric, strictPreorders))
    return strictPOs


def enumeratePo(N) -> List[np.ndarray]:
    strictPOs = enumerateStrictPOs(N)
    Po = list(map(adj2PairList, map(setDiagTrue, strictPOs)))
    return Po


def enumerateStrictPOsAdj(N) -> List[np.ndarray]:
    strictPOs = enumerateStrictPOs(N)
    Po = list(map(adj2PairList, strictPOs))
    return Po


def test():
    start = time.time()
    pos = list()
    preOrders = list()
    for i in range(7):
        print("Calculating N={}".format(i))
        preOrders.append(enumeratePreorders(i))
        print("Number of preorder[{}] is {}".format(i, preOrders[i].__len__()))
        pos.append(enumeratePo(i))
        print("Number of Po[{}] is {}".format(i, pos[i].__len__()))
    end = time.time()
    print("Time for cond2v2:%.2f seconds" % (end - start))

if __name__ == '__main__':

    n = 8
    filename = "strictPo0-{}.json".format(n)
    strictPos = dict()

    for i in range(n):
        strictPo = enumerateStrictPOsAdj(i)
        strictPos[i] = strictPo

    save_obj2json(strictPos, filename)
    res = load_json(filename)
    print(strictPos == res)
