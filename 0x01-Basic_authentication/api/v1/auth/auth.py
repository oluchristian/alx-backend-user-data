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
        if path and not path.endswith('/'):
            path = path + '/'
        if not path or path not in excluded_paths:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> None:
        """_summary_
        """
        key = 'Authorization'
        if request is None or key not in request.headers:
            return None
        return request.headers.get(key)

    def current_user(self, request=None) -> None:
        """_summary_
        """
        return None
