class SeaError(Exception):
    pass


class CRSMismatchError(SeaError):
    """Ошибка, если СК не совпали"""

    pass


class UndefinedCRSError(SeaError):
    """Ошибка, если СК не задана"""

    pass
