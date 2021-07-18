import math
import itertools

possible_alleles= {
    'A': [('A','A'), ('A','O')],
    'B': [('B','B'), ('B','O')],
    'AB': [('A','B')],
    'O': [('O','O')]
}

allele_dict = {}
for k,v in possible_alleles.items():
    for pair in v:
        allele_dict[pair] = k

possible_rh = {
    '+': [('+','-'),('+','+')],
    '-': [('-','-')]
}

rh_dict = {}
for k,v in possible_rh.items():
    for pair in v:
        rh_dict[pair] = k


def translate_allele(allele_tuple):
    if allele_tuple[0] > allele_tuple[1]:
        allele_tuple = (allele_tuple[1], allele_tuple[0])
    return allele_dict[allele_tuple]

def translate_rh(rh_tuple):
    if rh_tuple[0] > rh_tuple[1]:
        rh_tuple = (rh_tuple[1], rh_tuple[0])
    return rh_dict[rh_tuple]



def build_bloodtype_tuple(bloodtype_string):
    if bloodtype_string == "?": return None
    cut_index = math.ceil(len(bloodtype_string)/2)
    return (bloodtype_string[:cut_index], bloodtype_string[cut_index:])

def build_bloodtype_string(bloodtype_tuple):
    return bloodtype_tuple[0]+bloodtype_tuple[1]

def format_solution(bloodtype_tuple_list):
    if len(bloodtype_tuple_list) == 0: return "IMPOSSIBLE"
    formatted = "{"
    for tp in bloodtype_tuple_list:
        formatted += build_bloodtype_string(tp)+', '
    formatted = formatted[:-2] + "}"
    return formatted



def solve(p1=None, p2=None, ch=None):
    if ch is None:
        solution = format_solution(solve_for_child(p1, p2))
        return f"{build_bloodtype_string(p1)} {build_bloodtype_string(p2)} {solution}"
    elif p1 is None:
        solution = format_solution(solve_for_parent(p2, ch))
        return f"{solution} {build_bloodtype_string(p2)} {build_bloodtype_string(ch)}"
    else:  
        solution = format_solution(solve_for_parent(p1, ch))
        return f"{build_bloodtype_string(p1)} {solution} {build_bloodtype_string(ch)}"

def solve_for_child(p1, p2):
    p1_type, p1_rh = p1[0], p1[1]
    p2_type, p2_rh = p2[0], p2[1]

    possible_couples_al= list(itertools.product(possible_alleles[p1_type], possible_alleles[p2_type]))
    alleles_set = set()
    for couple in possible_couples_al:
        alleles_set = alleles_set.union(set(itertools.product(couple[0], couple[1])))
    alleles_set = set(map(translate_allele, alleles_set))

    possible_couples_rh = list(itertools.product(possible_rh[p1_rh], possible_rh[p2_rh]))
    rh_set = set()
    for couple in possible_couples_rh:
        rh_set = rh_set.union(set(itertools.product(couple[0], couple[1])))
    rh_set = (set(map(translate_rh, rh_set)))

    return list(itertools.product(alleles_set, rh_set))


def solve_for_parent(p, ch):
    print(f"solving for parent with child: {ch} and parent: {p}")
    p_type, p_rh = p[0], p[1]
    ch_type, ch_rh = ch[0], ch[1]



if __name__ == '__main__':
    count = 1
    while True:
        line = input()
        if line == "E N D":
            break
        
        tokens =line.split(" ")
        case=map(build_bloodtype_tuple, tokens)
        print(f"Case {count}: {solve(*case)}")
        count += 1