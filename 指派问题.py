#指派问题pulp
import pulp
import numpy as np

def assignment_problem(efficiency_matrix):
    row = len(efficiency_matrix)
    col = len(efficiency_matrix[0])

    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

    m = pulp.LpProblem('assignment', sense=pulp.LpMinimize)
    var_x = [[pulp.LpVariable(f'x{i}{j}', cat=pulp.LpBinary) for j in range(col)] for i in range(row)]

    m += pulp.lpDot(efficiency_matrix.flatten(), flatten(var_x))

    for i in range(row):
        m += (pulp.lpDot(var_x[i], [1]*col) == 1)

    for j in range(col):
        m += (pulp.lpDot([var_x[i][j] for i in range(row)], [1]*row) == 1)

    m.solve()

    print(m)
    return {'objective': pulp.value(m.objective), 'var': [[pulp.value(var_x[i][j]) for j in range(col)] for i in range(row)]}


efficiency_matrix = np.array([
    [5010, 4390, 3820, 4870, 5060, 6650, 7090],
    [4240, 5290, 4190, 3020, 4650, 4400, 4970],
    [5610, 5950, 4930, 4270, 4910, 4950, 5320],
    [4500, 3990, 3280, 3580, 3460, 4320, 4460],
    [2950, 2720, 3060, 3490, 3620, 4330, 4530],
    [3060, 4310, 4740, 3900, 5760, 5300, 6020],
    [4680, 4380, 3290, 3620, 3970, 4960, 5220]
])

res = assignment_problem(efficiency_matrix)
print(f'min={res["objective"]}')
print(res['var'])
