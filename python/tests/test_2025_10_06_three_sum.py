import importlib.util
import pathlib

def load_solution():
    base = pathlib.Path(__file__).parents[2] / "python" / "solutions"
    # find the latest folder for this slug
    matches = sorted(base.glob("*-three-sum"))
    assert matches, "solution folder not found"
    solution_py = matches[-1] / "solution.py"

    spec = importlib.util.spec_from_file_location("solution_mod", solution_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()

def test_examples():
    s = load_solution()
    assert s.threeSum([-1,0,1,2,-1,-4])==[[-1,-1,2],[-1,0,1]]

