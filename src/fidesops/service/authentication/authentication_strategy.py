from abc import ABC, abstractmethod

from requests import PreparedRequest

from fidesops.models.connectionconfig import ConnectionConfig


class AuthenticationStrategy(ABC):
    """Abstract base class for SaaS authentication strategies"""

    @abstractmethod
    def add_authentication(
        self, request: PreparedRequest, connection_config: ConnectionConfig
    ) -> PreparedRequest:
        """Add authentication to the request"""
