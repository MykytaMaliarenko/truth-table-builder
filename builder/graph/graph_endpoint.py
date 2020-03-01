from builder.operations import Operations, execute


class GraphEndpoint:
    __operation: Operations
    __endpoint_var_a: str
    __endpoint_var_b: str

    def __init__(self, operation: Operations, endpoint_var_a: str, endpoint_var_b: str):
        self.__operation = operation
        self.__endpoint_var_a = endpoint_var_a
        self.__endpoint_var_b = endpoint_var_b

    def execute(self, data: dict) -> bool:
        a = data[self.__endpoint_var_a]
        b = data[self.__endpoint_var_b]

        if a is None or b is None:
            raise ValueError
        else:
            return execute(self.__operation, a, b)
