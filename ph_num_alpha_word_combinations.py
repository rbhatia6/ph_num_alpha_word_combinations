from itertools import product

dict1 = {'2':'ABC', '3':'DEF', '4': 'GHI'}

def permcomb(phnum):

    alph_all = (dict1[dig] for dig in phnum)

    lst = []
    
    for alph in product(*alph_all):
        lst.append(''.join(alph))
    return lst
        

print(permcomb('234'))
assert len(permcomb('234')) == 27
assert permcomb('234') != []
for i in range(1,3):
    if i == 1:
        ph_str = '2'
    elif i == 2:
        ph_str = '23'
    else:
        ph_str = '234'

    assert len(permcomb(ph_str)) == pow(3, i)

assert permcomb('') == ['']
