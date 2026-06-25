"""Evaluation metrics"""
from abc import ABC, abstractmethod

class Evaluator(ABC):
    """Abstract base class. All concrete evaluators inherit from this."""

    @abstractmethod
    def evaluate(self, predictions: list[str], references: list[str], **kwargs) -> dict:
        """Evaluate predictions against references and return metrics."""
        pass
