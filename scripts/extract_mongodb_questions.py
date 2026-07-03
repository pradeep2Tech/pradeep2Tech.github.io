"""Extract QUESTIONS from generate_mongodb_handbook_refactor.py into shared module."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = (ROOT / "generate_mongodb_handbook_refactor.py").read_text(encoding="utf-8")
start = src.index("QUESTIONS = [")
end = src.index("]\n\nassert len(QUESTIONS)", start) + 1
block = src[start:end]
out = ROOT / "mongodb_questions_data.py"
out.write_text(
    '"""Top 150 MongoDB interview questions — shared data."""\n\n' + block + "\n",
    encoding="utf-8",
)
print(f"Wrote {out}")
