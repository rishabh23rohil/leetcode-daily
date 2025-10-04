import importlib.util
import pathlib

def load_solution():
    # locate the latest two-sum solution.py
    base = pathlib.Path(__file__).parents[2] / "python" / "solutions"
    matches = sorted(base.glob("*-two-sum"))
    solution_py = matches[-1] / "solution.py"

    spec = importlib.util.spec_from_file_location("solution", solution_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()

def test_two_sum_example():
    s = load_solution()
    assert sorted(s.twoSum([2,7,11,15], 9)) == [0,1]
