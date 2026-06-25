"""Analyse Data"""
from abc import ABC, abstractmethod


class Analyser(ABC):
    """Abstract base class. All concrete clients inherit from this."""

    @abstractmethod
    def complete(self, prompt: str, **kwargs) -> str:
        """Send a prompt, return the completion text."""
        ...
