# rules.py

STATUS_MAP = {
    "tired": {"msg": "疲惫"},
    "focus": {"msg": "专注"},
}

def is_valid_status(status: str) -> bool:
    # 规则：只允许英文字母（你现在的 232421 / @#% 就会被判 400）
    return status.isalpha()