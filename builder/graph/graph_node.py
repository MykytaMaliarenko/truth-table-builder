from bool_operations import Operations, execute_operation
from builder.graph.bounds import Bounds


class GraphNode(object):
    operation: Operations
    child_a = None
    child_b = None
    denial: bool = False
    # __operation_bounds: Bounds = None

    def __init__(self, operation: Operations, child_a, child_b):
        self.operation = operation
        self.child_a = child_a
        self.child_b = child_b

    def execute(self, data: dict) -> bool:
        child_a_res = None
        child_b_res = None

        if isinstance(self.child_a, str):
            child_a_res = data[self.child_a] if "!" not in self.child_a else not data[self.child_a[1]]
        else:
            child_a_res = self.child_a.execute(data)

        if isinstance(self.child_b, str):
            child_b_res = data[self.child_b] if "!" not in self.child_b else not data[self.child_b[1]]
        else:
            child_b_res = self.child_b.execute(data)

        res = execute_operation(self.operation, child_a_res, child_b_res)
        return not res if self.denial else res

    """@property
    def operation_bounds(self):
        return self.__operation_bounds

    @operation_bounds.setter
    def operation_bounds(self, bounds: Bounds):
        self.__operation_bounds = bounds"""
