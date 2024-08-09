#!/usr/bin/env python3
"""Module for API auth"""
from flask import request
from typing import List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits the Auth class
    """
