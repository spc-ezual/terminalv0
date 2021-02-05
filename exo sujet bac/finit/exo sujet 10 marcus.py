#exo 1
def maxi(tab):
    tabBase=tab.copy()
    tab.sort()
    print(tabBase.index(9))
    return tabBase.index(tab[-1])
print(maxi([7,8,5,3,4,9,8,7]))
#------------------------------------------------------
#exo 2
def positif(T):
    T2 = ...(T)
    T3 = ...
    while T2 != []:
        x = ...
        if ... >= 0:
            T3.append(...)
    T2 = []
    while T3 != ...:
        x = T3.pop()
        ...
    print('T = ',T)
    return T2