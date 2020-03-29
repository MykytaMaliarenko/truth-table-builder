from builder.graph import GraphNode
from builder.graph_builder import build_graph


def build_truth_table(bool_func: str, bool_vars: list) -> list:
    graph = build_graph("".join(bool_func.split()))
    bool_vars.reverse()
    res = list()

    for i in range(2 ** len(bool_vars)):
        bool_vars_values = {var_name: bool(i & (2 ** j)) for j, var_name in enumerate(bool_vars)}
        res.append(graph.execute(bool_vars_values))

    return res
