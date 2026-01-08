# logic.py
from rules import STATUS_MAP, is_valid_status

class InvalidStatusError(Exception):
    pass

class StatusNotFoundError(Exception):
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