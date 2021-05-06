import numpy as np
from typing import List


def binDigits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def makeAlphas(n: int) -> List[np.array]:
    n_res = int(pow(2, n))
    zero = np.zeros((1, n), dtype=bool)[0]
    res = [zero.copy() for i in range(n_res)]
    for i in range(n_res):
        for idx, bit in enumerate(binDigits(i, n)):
            res[i][idx] = False if bit == '0' else True
    return res


def allSubLists(l: np.array) -> List[np.array]:
    idx_true = list()  # True的赋予任意值
    n = l.shape[0]
    for i in range(n):
        if l[i]:
            idx_true.append(i)
    n_true = len(idx_true)
    if n_true == 0:
        return [l]
    else:
        n_res = int(pow(2, n_true))
        res = [l.copy() for i in range(n_res)]
        for i in range(n_res):
            for idx, bit in enumerate(binDigits(i, n_true)):
                res[i][idx_true[idx]] = False if bit == '0' else True
        return res


def antiSymmetric(adj: np.ndarray) -> bool:
    assert adj.shape[0] == adj.shape[1]  # 必须是方阵
    n = adj.shape[0]
    for row in range(n):
        for col in range(n):
            if adj[row][col] and adj[col][row]:
                return False
    return True


def setDiag(adj: np.ndarray, b: bool):
    assert adj.shape[0] == adj.shape[1]  # 必须是方阵
    adj[np.diag_indices_from(adj)] = b


def setDiagFalse(adj: np.ndarray):
    setDiag(adj, False)
    return adj


def setDiagTrue(adj: np.ndarray):
    setDiag(adj, True)
    return adj


def adj2PairList(adj: np.ndarray):
    assert adj.shape[0] == adj.shape[1]  # 必须是方阵
    res = list()
    n = adj.shape[0]
    for row in range(n):
        for col in range(n):
            if adj[row][col]:
                res.append((row, col))
    return res


def filterPositionsId(line: np.array):
    line_list = set()
    for idx, value in enumerate(line):
        if value:
            line_list.add(idx)
    return line_list


def setFilterPositionsId(line: np.array):
    return set(filterPositionsId(line))


if __name__ == '__main__':
    matrix = np.zeros((4, 4), dtype=bool)
    pairList = adj2PairList(matrix)
    print(pairList)
