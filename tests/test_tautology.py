import tautology


def test_eval_tautology_1():
    res = tautology.eval_tautology("A1N1")[0]
    assert res
    res = tautology.eval_tautology("A1N0")[0]
    assert res
    res = tautology.eval_tautology("A0N0")[0]
    assert res


def test_eval_tautology_2():
    res = tautology.eval_tautology("A0N1")[0]
    assert not res


def test_solve_1_swapped():
    res = tautology.solve("ArNr")
    assert res


def test_solve_1():
    res = tautology.solve("ApNp")
    assert res


def test_solve_2():
    res = tautology.solve("ApNq")
    assert not res


def test_solve_2_swapped():
    res = tautology.solve("AsNt")
    assert not res
