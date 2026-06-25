"""Trainer class"""
from abc import ABC, abstractmethod

class Trainer(ABC):
    """Abstract base class. All concrete trainers inherit from this."""

    @abstractmethod
    def train(self, data: str, **kwargs) -> None:
        """Train the model on the given data."""
        pass
