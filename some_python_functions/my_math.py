# если не можешь скачать numpy , соболезнования, держи вот енто


def faktorial(num):
    if num == 1:
        return num
    return num * faktorial(num-1)


def C(n, k):
    """
    Сочетание из n по k
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    if n == k:
        return 1
    return int(faktorial(n) / (faktorial(k) * faktorial(n-k)))
