from bool_operations import Operations, execute_operation
from builder.graph_builder import get_index_of_closing_bracket
from builder.truth_table_builder import build_truth_table


class TestBoolOperations:
    def test_union(self):
        assert execute_operation(Operations.Union, True, True) is True
        assert execute_operation(Operations.Union, True, False) is True
        assert execute_operation(Operations.Union, False, False) is False
        assert execute_operation(Operations.Union, False, True) is True

    def test_intersection(self):
        assert execute_operation(Operations.Intersection, False, True) is False
        assert execute_operation(Operations.Intersection, False, False) is False
        assert execute_operation(Operations.Intersection, True, True) is True
        assert execute_operation(Operations.Intersection, True, False) is False

    def test_implication(self):
        assert execute_operation(Operations.Implication, False, False) is True
        assert execute_operation(Operations.Implication, False, True) is True
        assert execute_operation(Operations.Implication, True, True) is True
        assert execute_operation(Operations.Implication, True, False) is False

    def test_equivalence(self):
        assert execute_operation(Operations.Equivalence, True, False) is False
        assert execute_operation(Operations.Equivalence, False, True) is False
        assert execute_operation(Operations.Equivalence, False, False) is True
        assert execute_operation(Operations.Equivalence, True, True) is True

    def test_modulo(self):
        assert execute_operation(Operations.Modulo2Sum, False, True) is True
        assert execute_operation(Operations.Modulo2Sum, True, True) is False
        assert execute_operation(Operations.Modulo2Sum, True, False) is True
        assert execute_operation(Operations.Modulo2Sum, False, False) is False

    def test_schaeffer_stroke(self):
        assert execute_operation(Operations.SchaefferStroke, True, True) is False
        assert execute_operation(Operations.SchaefferStroke, True, False) is True
        assert execute_operation(Operations.SchaefferStroke, False, True) is True
        assert execute_operation(Operations.SchaefferStroke, False, False) is True

    def test_pirse_arrow(self):
        assert execute_operation(Operations.PierceArrow, False, False) is True
        assert execute_operation(Operations.PierceArrow, True, False) is False
        assert execute_operation(Operations.PierceArrow, False, True) is False
        assert execute_operation(Operations.PierceArrow, True, True) is False


class TestGetIndexOfClosingBracket:
    def test_1(self):
        assert get_index_of_closing_bracket("(x^(y->z))") == 9

    def test_2(self):
        assert get_index_of_closing_bracket("(x^(y->(x&g)))") == 13

    def test_3(self):
        assert get_index_of_closing_bracket("(y->(x&g))") == 9

    def test_4(self):
        assert get_index_of_closing_bracket("(y->(x&g))&(y->(x&g))") == 9

    def test_5(self):
        assert get_index_of_closing_bracket("((x=>(x=>z))|((y==z)-x))|((!z&y)=>x)") == 23


class TestTruthTableBuilder:

    def test1(self):
        assert build_truth_table("!(!(x*y -> z) v (!x == (y ^ z )))", ["x", "y", "z"]) == [False, True, True, True,
                                                                                           True, False, False, False]

    def test2(self):
        assert build_truth_table("((x -> y) -> z) v ((x == y) == z)", ["x", "y", "z"]) == [False, True, True, True,
                                                                                           True, True, False, True]

    def test3(self):
        assert build_truth_table("(x v y v z) == (x + z) * y", ["x", "y", "z"]) == [True, False, False, True,
                                                                                    False, False, True, False]

    def test4(self):
        assert build_truth_table("!(!(x*y -> z) v (!x == (y ^ z)))", ["x", "y", "z"]) == [False, True, True, True,
                                                                                          True, False, False, False]
