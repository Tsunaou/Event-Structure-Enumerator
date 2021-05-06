import numpy as np
from typing import List
from utils import allSubLists, filterPositionsId, setFilterPositionsId, makeAlphas


def cond1(A: np.ndarray, alpha: np.array) -> List[np.array]:
    """
    生成满足条件的 betas
    :param A: 矩阵 n*n
    :param alpha: 行向量 1*n
    :return: 是否可以返回一个符合条件的beta，若存在则返回所有beta的list
    """
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == alpha.shape[0]
    n = A.shape[0]
    zero = np.zeros((1, n), dtype=bool)[0]
    one = np.ones((1, n), dtype=bool)[0]
    if alpha.__eq__(zero).all():
        return allSubLists(one)
    else:
        id_rows = list()
        for idx, value in enumerate(alpha):
            if value:
                id_rows.append(idx)
        tmp = np.ones((1, n), dtype=bool)[0]
        for i in id_rows:
            tmp = tmp.__and__(A[i])

        return allSubLists(tmp)


def cond2(A: np.ndarray, beta: np.array) -> bool:
    """
    :param A: 矩阵 n*n
    :param beta: 行向量 1*n
    :return:
    """
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == beta.shape[0]
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            if not (A[i][j] and beta[i]):
                continue
            if not beta[j]:
                return False
    return True


def cond2v2(A: np.ndarray, beta: np.array) -> bool:
    """
    :param A: 矩阵 n*n
    :param beta: 行向量 1*n
    :return:
    """
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == beta.shape[0]
    row_set = setFilterPositionsId(beta)
    rows = [A[i] for i in row_set]
    sub_row_set = set()
    for row in rows:
        sub_row_set = sub_row_set.union(setFilterPositionsId(row))
    return sub_row_set <= row_set


def cond3(A: np.ndarray, alpha: np.array) -> bool:
    """
    :param A: 矩阵 n*n
    :param alpha: 行向量 n*1
    :return:
    """
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == alpha.shape[0]
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            if not (A[i][j] and alpha[j]):
                continue
            if not alpha[i]:
                return False
    return True

def cond3v2(A: np.ndarray, alpha: np.array) -> bool:
    """
    :param A: 矩阵 n*n
    :param alpha: 行向量 n*1
    :return:
    """
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == alpha.shape[0]
    col_set = setFilterPositionsId(alpha)
    AT = A.T
    cols = [AT[i] for i in col_set]
    sub_col_set = set()
    for col in cols:
        sub_col_set = sub_col_set.union(setFilterPositionsId(col))
    return sub_col_set <= col_set

def concat(A: np.ndarray, alpha: np.array, beta: np.array):
    """
    [A a^T
     b  1 ]
    :param A: n*n
    :param alpha: 1*n
    :param beta: 1*n
    :return:
    """
    n = A.shape[0]
    assert A.shape[0] == A.shape[1]
    assert alpha.shape[0] == n
    assert beta.shape[0] == n
    res = np.ones((n + 1, n + 1), dtype=A.dtype)
    res[:n, :n] = A
    res[:n, n] = alpha.T
    res[n, :n] = beta
    return res


if __name__ == '__main__':
    A = np.ones((1, 1), dtype=bool)
    alphas = makeAlphas(1)
    result = list()
    for alpha in alphas:
        betas = cond1(A, alpha)
        for beta in betas:
            assert cond2(A, beta) == cond2v2(A, beta)
            if cond2(A, beta) and cond3(A, alpha):
                result.append(concat(A, alpha, beta))
