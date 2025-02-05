"""Module to handle user feedback and suggestions."""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict

FEEDBACK_FILE = Path("data/feedback.json")


def init_feedback_file():
    """Create feedback file if it doesn't exist."""
    FEEDBACK_FILE.parent.mkdir(exist_ok=True)
    if not FEEDBACK_FILE.exists():
        FEEDBACK_FILE.write_text('{"suggestions": []}', encoding="utf-8")


def save_suggestion(suggestion: str, category: str, details: str) -> None:
    """Save a new suggestion to the feedback file."""
    init_feedback_file()

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["suggestions"].append(
        {
            "date": datetime.now().isoformat(),
            "category": category,
            "suggestion": suggestion,
            "details": details,
            "status": "pending",
        }
    )

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_suggestions() -> List[Dict]:
    """Retrieve all suggestions."""
    init_feedback_file()
    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["suggestions"]
