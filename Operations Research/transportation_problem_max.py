# 解运输问题最优最大运费
import pulp
import numpy as np
from pprint import pprint

def transportation_problem(costs, x_max, y_max):
    row = len(costs)
    col = len(costs[0])

    prob = pulp.LpProblem('Transportation Problem', sense=pulp.LpMaximize)

    var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger)
            for j in range(col)] for i in range(row)]

    def flatten(x): return [y for l in x for y in flatten(
        l)] if type(x) is list else [x]

    prob += pulp.lpDot(flatten(var), costs.flatten())

    for i in range(row):
        prob += (pulp.lpSum(var[i]) <= x_max[i])

    for j in range(col):
        prob += (pulp.lpSum([var[i][j] for i in range(row)]) <= y_max[j])

    prob.solve()

    return {'objective': pulp.value(prob.objective), 'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}

if __name__ == '__main__':
    costs = np.array([[3, 11, 3, 10],
                       [1, 9, 2, 8],
                       [7, 4, 10, 5]])

    max_chan = [7, 4, 9]
    max_xiao = [3, 6, 5, 6]
    res = transportation_problem(costs, max_chan, max_xiao)

    print(f'max={res["objective"]}')
    print('value:')
    pprint(res['var'])
