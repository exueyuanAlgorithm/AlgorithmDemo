

def genhao(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) / 2
        value = mid ** 2
        nex_value = (mid + 0.001) ** 2
        # print(mid)
        if value <= n < nex_value:
            return mid
        elif value > n:
            high = mid - 0.001
            # print(high)
        else:
            low = mid + 0.001

ans = genhao(2)
print(ans)
