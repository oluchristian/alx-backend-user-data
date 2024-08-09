#!/usr/bin/env python3
"""Module for basic auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits the Auth class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns base64 part
        """
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
