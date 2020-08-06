# 解运输问题最优最小运费,产销平衡
import pulp
import numpy as np
from pprint import pprint

def transportation_problem(costs, x_max, y_max):
    row = len(costs)
    col = len(costs[0])

    prob = pulp.LpProblem('Transportation Problem', sense=pulp.LpMinimize)   #建模

    var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger)     #定义约束变量
            for j in range(col)] for i in range(row)]

    def flatten(x): return [y for l in x for y in flatten(
        l)] if type(x) is list else [x]

    prob += pulp.lpDot(flatten(var), costs.flatten())   #目标函数

    for i in range(row):
        prob += (pulp.lpSum([var[i][j] for j in range(col)]) == x_max[i])    #约束条件等式，产销平衡

    for j in range(col):
        prob += (pulp.lpSum([var[i][j] for i in range(row)]) == y_max[j])

    prob.solve()
    print(prob)

    return {'objective': pulp.value(prob.objective), 'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}

if __name__ == '__main__':
    costs = np.array([[90, 70, 100],
                       [80, 65, 80]])

    max_chan = [200, 250]
    max_xiao = [100, 150, 200]
    res = transportation_problem(costs, max_chan, max_xiao)

    print(f'min={res["objective"]}')
    print('value:')
    pprint(res['var'])
