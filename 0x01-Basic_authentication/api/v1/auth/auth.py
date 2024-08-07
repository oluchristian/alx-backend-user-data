#!/usr/bin/env python3
"""Module for API auth"""
from flask import request
from typing import List


class Auth:
    """Manages API auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_
        """
        return False

    def authorization_header(self, request=None) -> str:
        """_summary_
        """
        return request


    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return request
