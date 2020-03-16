from builder.graph import GraphNode
from bool_operations import basic_funcs, bool_operations
from builder.exceptions import NoClosingBracket
from collections import namedtuple

ClosestOperation = namedtuple("ClosestOperation", ["operation_type", "operation_len", "index"])


def build_graph(root_bool_func: str) -> GraphNode:
    bool_func = root_bool_func

    sub_nodes = dict()
    while "(" in bool_func:
        opening_bracket = bool_func.index("(")
        closing_bracket = opening_bracket + get_index_of_closing_bracket(bool_func[opening_bracket:])

        node = build_graph(bool_func[opening_bracket + 1:closing_bracket])
        sub_nodes[opening_bracket] = node

        bool_func = bool_func[:opening_bracket] + '.' + bool_func[closing_bracket + 1:]

    num_of_funcs = number_of_basic_funcs(bool_func)
    if num_of_funcs > 1:
        res = None

        while len(bool_func) > 0:
            t, operation = parse_closest_operation(bool_func, sub_nodes)
            if res is None:
                res = t
            else:
                if t.child_a is None:
                    t.child_a = res

                if t.child_b is None:
                    t.child_b = res

                res = t

            if len(sub_nodes) > 0:
                delta = operation.index + operation.operation_len + (3 if t.child_a.denial or (isinstance(t.child_a, str)
                                                                                               and "!" in t.child_a)
                                                                     else 2)
                sub_nodes = {index - delta if index > operation.index else index: val for index, val in sub_nodes.items()}

            bool_func = bool_func[:operation.index - 1 if operation.index > 0 else 0] + \
                        bool_func[operation.index + operation.operation_len + 2:]

        return res
    elif num_of_funcs == 1:
        return parse_closest_operation(bool_func, sub_nodes)[0]
    elif bool_func == "!." and len(sub_nodes) == 1:
        node = list(sub_nodes.values())[0]
        node.denial = True
        return node


def parse_closest_operation(bool_func: str, sub_nodes: dict) -> (GraphNode, ClosestOperation):
    operation = get_closest_operation(bool_func)

    a = None
    if operation.index - 1 > -1:
        a = bool_func[operation.index - 1]
        if a == '.':
            a = sub_nodes[operation.index - 1]

        if operation.index - 2 > -1 and bool_func[operation.index - 2] == '!':
            if isinstance(a, str):
                a = "!" + a
            else:
                a.denial = True

    b = None
    if operation.index + operation.operation_len + 1 < len(bool_func):
        if bool_func[operation.index + operation.operation_len + 1] == "!":
            operation = ClosestOperation(operation.operation_type, operation.operation_len + 1, operation.index)
            b = "!" + bool_func[operation.index + operation.operation_len + 1]
            if b == '!.':
                b = sub_nodes[operation.index + operation.operation_len + 1]
                b.denial = True
        else:
            b = bool_func[operation.index + operation.operation_len + 1]
            if b == '.':
                b = sub_nodes[operation.index + operation.operation_len + 1]

    return GraphNode(operation.operation_type, a, b), operation


def get_index_of_closing_bracket(bool_func: str) -> int:
    if ")" in bool_func:
        bool_func = bool_func[1:]
        sub_bool_func = bool_func[:bool_func.index(")")]
        while "(" in sub_bool_func:
            # removing one inner opening bracket and closing bracket
            bool_func = bool_func[:sub_bool_func.index("(")] + '.' + \
                        bool_func[sub_bool_func.index("(") + 1: bool_func.index(")")] + \
                        '.' + bool_func[bool_func.index(")") + 1:]
            # updating
            sub_bool_func = bool_func[:bool_func.index(')')]
        return bool_func.index(")") + 1
    else:
        raise NoClosingBracket(bool_func, 0)


def number_of_basic_funcs(bool_func: str) -> int:
    return sum(list(map(lambda v: bool_func.count(v), list(basic_funcs.values()) + list(bool_operations.values()))))


def get_closest_operation(bool_func: str) -> ClosestOperation:
    for operation_type, operation in bool_operations.items():
        if operation in bool_func:
            return ClosestOperation(operation_type, len(operation) - 1, bool_func.index(operation))

    closest_operation = None
    for operation_type, operation in basic_funcs.items():
        if operation in bool_func and (
                closest_operation is None or closest_operation.index > bool_func.index(operation)):
            closest_operation = ClosestOperation(operation_type, len(operation) - 1, bool_func.index(operation))

    return closest_operation


if __name__ == "__main__":
    m = build_graph("".join("!(!(x*y -> z) v (!x == (y ^ z )))".split()))
    print("res")
