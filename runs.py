from math import floor

def symmetric(start,end,perm):
    if (end-start)%2 == 0:
        while start < end:
            if perm[start] != perm[end]: return False
            start += 1
            end -= 1
    else:
        while start <= end:
            if perm[start] != perm[end]: return False
            start += 1
            end -= 1
    return True

def from_left(perm):
    val = 0
    start = 0
    profile = []

    while start < len(perm):
        reach = len(perm)-1
        while reach >=0 and not symmetric(start,reach,perm):
            reach -= 1
        profile.append(reach-start+1)
        val += 1
        start = reach+1

    return val, profile
    
def base_to_list(value, length, base):
    num_digits = length
    rep = []
    for _ in range(length):
        rep.append(value % base)
        value = value // base
    return rep

def max_profile(n, base=2):
    lst = []
    freq_dict = {}
    max = 0
    for i in range(base**n): 
        seq = base_to_list(i,n,base)
        if seq[0] == 0:
            val_temp = from_left(seq)
            val = val_temp[0]
            profile = val_temp[1]
            if val == floor((3*n+10)/7):
                print(f'{seq}   {profile}')

# returns the dictionary used to calculate average runs of of length n+1 sequences of a given base 
def avg_runs_from_left(n,base):
    lst = []
    freq_dict = {}
    for i in range(base**n): 
        seq = base_to_list(i,n,base)
        if seq[0] == 0:
            val_temp = from_left(seq)
            val = val_temp[0]
            profile = val_temp[1]
            lst.append(val)
            try:
                freq_dict[val] += 1
            except KeyError:
                freq_dict[val] = 1
    return freq_dict

# returns the dictionary used to calculate average runs of of length n+1 sequences of a given base 
def each_run_from_left(n,base):
    lst = []
    freq_dict = {}
    for i in range(base**n): 
        run = base_to_list(i, n, base)
        run.reverse()
        if run[0] == 0:
            val = from_left(run)[0]
            lst.append(val)
            try:
                freq_dict[val].append(run)
            except KeyError:
                freq_dict[val] = [run]
    return freq_dict

def get_average_from_freq(freq_dict):
    numerator = 0
    denominator = 0
    for key, value in freq_dict.items():
        numerator += key * value
        denominator += value
    return numerator/denominator

def get_max_from_freq(freq_dict):

    max_val = -float('inf')
    for key in freq_dict:
        if key > max_val: max_val = key
    return key
