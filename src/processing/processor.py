"""Processor class"""
from abc import ABC, abstractmethod


class Processor(ABC):
    """Abstract base class. All concrete processors inherit from this."""

    @abstractmethod
    def train(self, data: str, **kwargs) -> None:
        """Train the model on the given data."""
        pass
