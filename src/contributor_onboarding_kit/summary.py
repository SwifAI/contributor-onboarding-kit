def format_summary(name: str, notes: list[str]) -> str:
    note_text = ", ".join(notes) if notes else "no notes"
    return f"Contributor {name}: {note_text}"
