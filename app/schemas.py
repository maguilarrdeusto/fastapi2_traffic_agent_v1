from pydantic import BaseModel, Field
from typing import Dict

class DynamicCongestionOptimizeInput(BaseModel):
    data: Dict[str, float]
    
class KPIResults(BaseModel):
    baseline: Dict[str, float]
    optimized: Dict[str, float]
    difference: Dict[str, float]

class DynamicCongestionOptimizeOutput(BaseModel):
    KPIs: KPIResults
