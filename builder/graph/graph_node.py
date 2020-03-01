from builder.operations import Operations, execute


class GraphNode(object):
    __operation: Operations
    __child_a = None
    __child_b = None

    def __init__(self, operation: Operations, child_a, child_b):
        self.__operation = operation
        self.__child_a = child_a
        self.__child_b = child_b

    def execute(self, data: dict) -> bool:
        child_a_res = self.__child_a.execute(data)
        child_b_res = self.__child_b.execute(data)
        return execute(self.__operation, child_a_res, child_b_res)

    def set_children(self, a, b):
        self.__child_a = a
        self.__child_b = b
