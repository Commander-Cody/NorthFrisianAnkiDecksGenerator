def var(name: str) -> str:
    """Return an Anki variable name formatted to be included in card html"""
    return '{{' + name + '}}'