import math
import itertools
import re

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
    if len(bloodtype_tuple_list) == 1: return build_bloodtype_string(bloodtype_tuple_list[0])
    formatted = "{"
    for tp in bloodtype_tuple_list:
        formatted += build_bloodtype_string(tp)+', '
    formatted = formatted[:-2] + "}"
    return formatted



def solve(p1=None, p2=None, ch=None):
    if ch is None:
        solution = format_solution(solve_for_child(p1, p2))
        return "{} {} {}".format(build_bloodtype_string(p1), build_bloodtype_string(p2), solution)
    elif p1 is None:
        solution = format_solution(solve_for_parent(p2, ch))
        return "{} {} {}".format(solution, build_bloodtype_string(p2), build_bloodtype_string(ch))
    elif p2 is None:  
        solution = format_solution(solve_for_parent(p1, ch))
        return "{} {} {}".format(build_bloodtype_string(p1), solution, build_bloodtype_string(ch))
    else:
        return "{} {} {}".format(build_bloodtype_string(p1),build_bloodtype_string(p2),build_bloodtype_string(ch))

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
    p_type, p_rh = p[0], p[1]
    ch_type, ch_rh = ch[0], ch[1]

    possible_parent_alleles = set()
    p_alleles = possible_alleles[p_type]
    all_parents = list(allele_dict.keys())
    possible_couples_al = set(itertools.product(p_alleles, all_parents))
    
    for couple in possible_couples_al:
        if ch_type in set(map(translate_allele, set(itertools.product(couple[0], couple[1])))):
            possible_parent_alleles.add(translate_allele(couple[1]))

    possible_parent_rh = set()
    p_rh_alleles = possible_rh[p_rh]
    all_parents_rh = list(rh_dict.keys())
    possible_couples_rh = set(itertools.product(p_rh_alleles, all_parents_rh))
    
    for couple in possible_couples_rh:
        if ch_rh in set(map(translate_rh, set(itertools.product(couple[0], couple[1])))):
            possible_parent_rh.add(translate_rh(couple[1]))

    return list(itertools.product(possible_parent_alleles, possible_parent_rh))

count = 1
while True:
    line = input()
    if line == "": continue

    tokens = re.findall('([^\s]+)', line)
    if " ".join(tokens) == "E N D": break
    
    case=map(build_bloodtype_tuple, tokens)
    print("Case {}: {}".format(count, solve(*case)))
    count += 1