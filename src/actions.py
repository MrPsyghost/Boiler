from typing import Callable

actions: dict[str, Callable] = {}


def register(name: str):
    def decorator(func: Callable):
        global actions
        actions[name] = func
        return func

    return decorator