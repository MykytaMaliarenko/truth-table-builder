from builder.operations import Operations, execute


class TestBoolOperations:
    def test_union(self):
        assert execute(Operations.Union, True, True) is True
        assert execute(Operations.Union, True, False) is True
        assert execute(Operations.Union, False, False) is False
        assert execute(Operations.Union, False, True) is True

    def test_intersection(self):
        assert execute(Operations.Intersection, False, True) is False
        assert execute(Operations.Intersection, False, False) is False
        assert execute(Operations.Intersection, True, True) is True
        assert execute(Operations.Intersection, True, False) is False

    def test_implication(self):
        assert execute(Operations.Implication, False, False) is True
        assert execute(Operations.Implication, False, True) is True
        assert execute(Operations.Implication, True, True) is True
        assert execute(Operations.Implication, True, False) is False

    def test_equivalence(self):
        assert execute(Operations.Equivalence, True, False) is False
        assert execute(Operations.Equivalence, False, True) is False
        assert execute(Operations.Equivalence, False, False) is True
        assert execute(Operations.Equivalence, True, True) is True

    def test_modulo(self):
        assert execute(Operations.Modulo2Sum, False, True) is True
        assert execute(Operations.Modulo2Sum, True, True) is False
        assert execute(Operations.Modulo2Sum, True, False) is True
        assert execute(Operations.Modulo2Sum, False, False) is False

    def test_schaeffer_stroke(self):
        assert execute(Operations.SchaefferStroke, True, True) is False
        assert execute(Operations.SchaefferStroke, True, False) is True
        assert execute(Operations.SchaefferStroke, False, True) is True
        assert execute(Operations.SchaefferStroke, False, False) is True

    def test_pirse_arrow(self):
        assert execute(Operations.PierceArrow, False, False) is True
        assert execute(Operations.PierceArrow, True, False) is False
        assert execute(Operations.PierceArrow, False, True) is False
        assert execute(Operations.PierceArrow, True, True) is False
