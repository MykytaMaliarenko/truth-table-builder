from .graph import GraphNode, GraphEndpoint
from .operations import Operations

basic_funcs = {
    Operations.Union: "&",
    Operations.Intersection: "-",
    Operations.Equivalence: "==",
    Operations.SchaefferStroke: "|",
    Operations.Implication: "->",
    Operations.PierceArrow: "!&"
}


def build_graph(func: str) -> GraphNode:
    pass
