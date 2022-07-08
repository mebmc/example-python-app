import random
import string
from typing import Optional


class Random(object):
    def __init__(self, seed: Optional[int] = None):
        if seed:
            random.seed(seed)

    def number(self, min: int = 0, max: int = 100) -> int:
        return random.randint(min, max)

    def password(self, length: int = 32, numbers: bool = True, special: bool = True) -> str:
        charset = string.ascii_letters
        charset += string.digits if numbers else ""
        charset += "_+=!@*#" if special else ""

        return "".join(random.choice(charset) for _ in range(length))
