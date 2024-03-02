import numpy as np

def calculate(ls):
    calculations = {}
    if len(ls) != 9:
        raise ValueError("List must contain nine numbers.")
    list_as_arr = np.array([ls[:3], ls[3:6], ls[6:]])
    
    calculations['mean'] = [list_as_arr.mean(axis=0), list_as_arr.mean(axis=1), list_as_arr.mean()]
    calculations['variance'] = [list_as_arr.var(axis=0), list_as_arr.var(axis=1), list_as_arr.var()]
    calculations['standard deviation'] = [list_as_arr.std(axis=0), list_as_arr.std(axis=1), list_as_arr.std()]
    calculations['max'] = [list_as_arr.max(axis=0), list_as_arr.max(axis=1), list_as_arr.max()]
    calculations['min'] = [list_as_arr.min(axis=0), list_as_arr.min(axis=1), list_as_arr.min()]
    calculations['sum'] = [list_as_arr.sum(axis=0), list_as_arr.sum(axis=1), list_as_arr.sum()]

    for key in calculations.keys():
        for i in range(len(calculations[key])):
            if type(calculations[key][i]) == np.ndarray:
                calculations[key][i] = list(calculations[key][i])

    return calculations