from importlib import import_module
import datetime

def test_two_sum():
    today = datetime.date.today().isoformat().replace('-', '_')
    mod = import_module(f"python.solutions.{today}_two_sum.solution")
    S = getattr(mod, "Solution")
    s = S()
    assert sorted(s.twoSum([2,7,11,15], 9)) == [0,1]
