from pydantic import BaseModel, Field
from typing import Dict

class DynamicCongestionOptimizeInput(BaseModel):
    weight_PublicTransport: float
    weight_Congestion: float
    weight_OperationalCost: float
    weight_Emissions: float
    
class KPIResults(BaseModel):
    baseline: Dict[str, float]
    optimized: Dict[str, float]
    difference: Dict[str, float]

class DynamicCongestionOptimizeOutput(BaseModel):
    KPIs: KPIResults
