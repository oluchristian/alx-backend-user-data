#!/usr/bin/env python3
"""Module for basic auth"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, Optional


class BasicAuth(Auth):
    """inherits the Auth class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """returns base64 part
        """
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Base64 decode
        """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64.b64decode(
                base64_authorization_header,
                validate=True
                )
            decoded_value = base64_bytes.decode('utf-8')
            return decoded_value
        except(base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[Optional[str], Optional[str]]:
        """User credentials
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        user, password = decoded_base64_authorization_header.split(":")
        return (user, password)
