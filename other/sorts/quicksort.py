def quick_sort(list):
    if len(list)<=1:
        return list
    l, g = [], []
    pivot = list[0]
    for record in list[1:]:
        if record < pivot:
            l.append(record)
        else:
            g.append(record)
    return quick_sort(l) + [pivot] + quick_sort(g)
