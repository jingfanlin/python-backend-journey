from rules import is_valid_status

STATUS_MAP = {
    "tired": {"msg": "疲惫"},
    "focus": {"msg": "高度专注"},
    "good": {"msg": "状态不错"},
}

class InvalidStatusError(Exception):
    """参数格式不合法（400）"""
    pass

class StatusNotFoundError(Exception):
    """资源不存在（404）"""
    pass

def get_status_info(status: str) -> dict:
    # 1) 参数格式检查 -> 400
    if not is_valid_status(status):
        raise InvalidStatusError(status)

    # 2) 资源是否存在 -> 404
    info = STATUS_MAP.get(status)
    if not info:
        raise StatusNotFoundError(status)

    return info