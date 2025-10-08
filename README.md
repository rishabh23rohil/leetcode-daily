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

Track streak in this table (update automatically by committing daily):

| Date | Count | Notes |
|------|-------|-------|
| 2025‑10‑05 | 5 | blind 75 |
