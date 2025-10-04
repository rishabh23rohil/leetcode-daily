# LeetCode Daily Practice

Solve **2–3 problems every day** and push to GitHub.
- Language: Python 3
- Testing: `pytest`
- Structure: one folder per problem with `solution.py` and `test_solution.py`
- Commit convention: `feat(lc): <slug> - <difficulty> [tags]`

## How to use

1. Create a new problem stub (example):
   ```bash
   python newlc.py "Two Sum" --slug two-sum --id 1 --difficulty Easy --tags array,hash-table
   ```

2. Edit `solution.py` and `test_solution.py`.
3. Run tests:
   ```bash
   pip install -r requirements.txt
   pytest -q
   ```
4. Commit & push:
   ```bash
   git add .
   git commit -m "feat(lc): two-sum - Easy [array, hash-table]"
   git push origin main
   ```

## Daily plan
- **Warm‑up (10–15m):** 1 Easy to keep flow.
- **Main (25–35m):** 1 Medium on core patterns (two pointers / sliding window / binary search / stack / heap / graph / DP).
- **Stretch (15–25m):** 1 Medium/Hard if time allows; else revisit a previous one and write better tests.

Track streak in this table (update automatically by committing daily):

| Date | Count | Notes |
|------|-------|-------|
| YYYY‑MM‑DD | 2 | e.g., sliding window & heap |
