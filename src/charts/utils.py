"""Chart utils."""


COLORS = {
    "dark_blue": "#092640",
    "blue": "#1F5DAD",
    "coral": "#FF5836",
    "yellow": "#FAB61B",
    "turquoise": "#00B2A2",
}


def process_label(text: str, max_chars: int, break_every: int) -> str:
    """Process a category label by truncating and adding line breaks.

    Args:
        text: Original category text
        max_chars: Maximum characters allowed
        break_every: Add a line break every N words

    Returns:
        Processed label text
    """
    # Truncate if needed
    if len(text) > max_chars:
        text = text[: max_chars - 1] + "…"

    # Split into words
    words = text.split()

    if break_every == 0:
        return text

    lines = []
    for i in range(0, len(words), break_every):
        lines.append(" ".join(words[i : i + break_every]))

    return "<br>".join(lines)

def get_splits(n_labels: int) -> tuple[int, int]:
    """Get the splits for the labels.

    Args:
        n_labels: Number of labels
    """
    if n_labels <= 2:
        max_chars = 60
        break_every = 3
    elif n_labels <= 3:
        max_chars = 40
        break_every = 2
    elif n_labels <= 4:
        max_chars = 30
        break_every = 2
    else:
        max_chars = 30
        break_every = 1

    return max_chars, break_every
