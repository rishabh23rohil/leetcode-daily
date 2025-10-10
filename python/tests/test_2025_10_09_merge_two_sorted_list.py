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

# --- dynamic loader (supports both common slugs) ---

def _find_solution_file():
    base = pathlib.Path(__file__).parents[2] / "python" / "solutions"
    # try plural first (LeetCode slug), then singular
    patterns = ["*-merge-two-sorted-lists", "*-merge-two-sorted-list"]
    for pat in patterns:
        matches = sorted(base.glob(pat))
        if matches:
            return matches[-1] / "solution.py"
    raise AssertionError("solution folder not found (tried plural and singular slugs)")

def load_solution():
    solution_py = _find_solution_file()
    spec = importlib.util.spec_from_file_location("solution_mod", solution_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()

# --- tests ---

@pytest.mark.parametrize(
    "arr1,arr2,expected",
    [
        ([], [], []),                               # both empty
        ([], [0], [0]),                             # one empty
        ([1], [], [1]),                             # other empty
        ([1,3,5], [2,4,6], [1,2,3,4,5,6]),          # interleaving
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),          # duplicates across lists
        ([1,1,1], [1,1], [1,1,1,1,1]),              # many duplicates
        ([-3,-1,2], [-2,0,3], [-3,-2,-1,0,2,3]),    # negatives and positives
        ([1,2,3], [4,5,6], [1,2,3,4,5,6]),          # already separated ranges
        ([4,5,6], [1,2,3], [1,2,3,4,5,6]),          # all from l2 first, then l1
        (list(range(0, 20, 2)), list(range(1, 20, 2)), list(range(20))),  # larger
    ],
)
def test_merge_two_sorted_lists(arr1, arr2, expected):
    s = load_solution()
    l1 = list_to_ll(arr1)
    l2 = list_to_ll(arr2)
    out = s.mergeTwoLists(l1, l2)
    assert ll_to_list(out) == expected

def test_original_lists_nodes_reused():
    """Optional sanity: ensure nodes are reused (not required by problem but common pattern)."""
    s = load_solution()
    l1 = list_to_ll([1,3])
    l2 = list_to_ll([2,4])
    # Keep references to original nodes
    l1_first, l2_first = l1, l2
    merged = s.mergeTwoLists(l1, l2)
    vals = []
    nodes = []
    while merged:
        vals.append(merged.val)
        nodes.append(merged)
        merged = merged.next
    assert vals == [1,2,3,4]
    # At least the first two nodes should be from original lists
    assert nodes[0] is l1_first or nodes[0] is l2_first
    assert nodes[1] is not None
