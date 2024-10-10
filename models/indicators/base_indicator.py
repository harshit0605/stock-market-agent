from typing import Dict, List

class BaseIndicator:
    def calculate(self, prices: List[float]) -> Dict[str, float]:
        raise NotImplementedError("Subclasses should implement this method")
