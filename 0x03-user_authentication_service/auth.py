#!/usr/bin/env python3
"""User Model
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """nakes password with bcrpt
    """
