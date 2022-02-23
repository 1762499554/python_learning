#  归并排序的递归方法
import math

def mergeSort(aa):
    if len(aa)<2:
        return aa
    middle = math.floor(len(aa)/2)
    left, right = aa[0:middle], aa[middle:]
    return sort(mergeSort(left), mergeSort(right))


def sort(bb, cc):
    result = []
    while bb and cc:
        if bb[0] <= cc[0]:
            result.append(bb.pop(0))
        else:
            result.append(cc.pop(0))
    while bb:
        result.append(bb.pop(0))
    while cc:
        result.append(cc.pop(0))

    return result

aa=[4,2,1,5,8,9,7,4]
print(mergeSort(aa))
