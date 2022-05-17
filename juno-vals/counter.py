from collections import OrderedDict

addr_dictionary = {}
df = open("/Users/yusuf/proj/coinhall-research/juno-vals/delegator_address_w_top15.csv")

for line in df:
    if line in addr_dictionary:
        addr_dictionary[line] += 1
    else:
        addr_dictionary[line] = 1

sorted_dict = dict(sorted(addr_dictionary.items(), key=lambda item: item[1]))

for k, v in sorted_dict.items():
    if v >= 2:
        print(k.strip('\n'), ':' , v)
