"""Redis answer engine for top-150 interview questions."""

from __future__ import annotations

import re
from typing import Dict

from redis_questions_data import QUESTIONS
from redis_top150_unique_answers import UNIQUE_ANSWERS

SECTIONS = ("short", "detailed", "internal", "production", "mistakes", "followup")


def slug_anchor(question: str) -> str:
    base = question.lower().strip()
    base = re.sub(r"[^\w\s-]", "", base)
    base = re.sub(r"[\s_]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    return base[:80].rstrip("-")


def format_answer_block(question: str, sections: dict) -> str:
    return (
        f"## {question}\n\n"
        f"### Short Answer\n{sections['short']}\n\n"
        f"### Detailed Explanation\n{sections['detailed']}\n\n"
        f"### Internal Working\n{sections['internal']}\n\n"
        f"### Production Notes\n{sections['production']}\n\n"
        f"### Common Mistakes\n{sections['mistakes']}\n\n"
        f"### Follow-up Questions\n{sections['followup']}\n\n"
        "---\n"
    )


ANSWERS: Dict[int, Dict[str, str]] = dict(UNIQUE_ANSWERS)

if len(ANSWERS) != 150:
    raise RuntimeError(f"Expected 150 answers, found {len(ANSWERS)}")


def craft_answer(num: int, question: str, topic: str, doc: str) -> dict:
    if num in ANSWERS:
        return ANSWERS[num]
    raise KeyError(f"Missing answer for question {num}")


__all__ = ["ANSWERS", "QUESTIONS", "craft_answer", "format_answer_block", "slug_anchor"]
