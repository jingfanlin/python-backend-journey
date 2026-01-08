import re

def is_valid_status(status: str) -> bool:
    # 只允许：英文字母（你现在用的就是 tired / ghost / focus)
    return bool(re.fullmatch(r"[a-zA-Z]+", status))