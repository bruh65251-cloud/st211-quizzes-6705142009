def reverse_string(s: str) -> str:
    """Reverse a string"""
    """synatx: sequenced[start:stop:step]"""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = "".join(s.lower().spilt())
    return cleaned == cleaned[::-1]