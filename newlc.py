#!/usr/bin/env python3
"""
Create a new LeetCode problem folder with a solution + unit test stub.

Usage:
  python newlc.py "Two Sum" --slug two-sum --id 1 --difficulty Easy --tags array,hash-table
"""
import argparse, pathlib, datetime, re, json

TEMPLATE_SOLUTION = """from typing import List

class Solution:
    def solve(self, *args, **kwargs):
        \"\\""
        Implement your solution here.
        Replace signature to match the problem (e.g., twoSum(self, nums: List[int], target: int) -> List[int]).
        \"\\""
        raise NotImplementedError
"""

TEMPLATE_TEST = """import pytest
from python.solutions.{module_name}.solution import Solution

def test_example():
    s = Solution()
    # TODO: replace with real tests for this problem
    # Example for Two Sum:
    # assert s.twoSum([2,7,11,15], 9) == [0,1]
    with pytest.raises(NotImplementedError):
        s.solve()
"""

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "problem"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help="Problem title as shown on LeetCode")
    ap.add_argument("--slug", default=None, help="LeetCode slug (e.g., two-sum)")
    ap.add_argument("--id", default="", help="Optional LeetCode ID (e.g., 1)")
    ap.add_argument("--difficulty", default="Unknown", help="Easy/Medium/Hard")
    ap.add_argument("--tags", default="", help="Comma-separated tags")
    args = ap.parse_args()

    today = datetime.date.today().isoformat()  # YYYY-MM-DD
    slug = args.slug or slugify(args.title)
    module_name = (today + "-" + slug).replace("-", "_")

    base = pathlib.Path("python", "solutions", f"{today}-{slug}")
    base.mkdir(parents=True, exist_ok=False)

    # metadata
    meta = {
        "id": args.id,
        "title": args.title,
        "slug": slug,
        "difficulty": args.difficulty,
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "created": today
    }
    (base / "meta.json").write_text(json.dumps(meta, indent=2))

    # solution stub
    (base / "solution.py").write_text(TEMPLATE_SOLUTION)

    # test stub
    test_path = pathlib.Path("python", "tests", f"test_{module_name}.py")
    if not test_path.exists():
        test_path.write_text(TEMPLATE_TEST.format(module_name=f"{today}-{slug}".replace("-", "_")))

    print(f"Created {base} and {test_path}")
    print("Next steps:")
    print("  1) Edit solution.py with the real method signature & logic.")
    print("  2) Update/add tests in python/tests/.")
    print("  3) Run: pytest -q ; then commit & push.")

if __name__ == "__main__":
    main()
