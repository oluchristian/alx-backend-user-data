#!/usr/bin/env python3
"""User Model
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """nakes password with bcrpt
    """
    encoded_pwd = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)
    return hashed_pwd
