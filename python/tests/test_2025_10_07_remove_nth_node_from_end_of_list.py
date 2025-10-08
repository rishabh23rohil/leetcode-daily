import importlib.util
import pathlib
import pytest

# --- helpers for linked list <-> list ---

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_ll(vals):
    d = ListNode(0)
    cur = d
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return d.next

def ll_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

# --- your dynamic loader unchanged ---

def load_solution():
    base = pathlib.Path(__file__).parents[2] / "python" / "solutions"
    matches = sorted(base.glob("*-remove-nth-node-from-end-of-list"))
    assert matches, "solution folder not found"
    solution_py = matches[-1] / "solution.py"

    spec = importlib.util.spec_from_file_location("solution_mod", solution_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()

# --- tests ---

@pytest.mark.parametrize(
    "arr,n,expected",
    [
        ([1,2,3,4,5], 2, [1,2,3,5]),  # middle removal
        ([1],          1, []),        # remove head only node
        ([1,2],        1, [1]),       # remove tail
        ([1,2],        2, [2]),       # remove head when n == len
    ],
)
def test_examples(arr, n, expected):
    s = load_solution()
    head_in = list_to_ll(arr)
    head_out = s.removeNthFromEnd(head_in, n)
    assert ll_to_list(head_out) == expected
