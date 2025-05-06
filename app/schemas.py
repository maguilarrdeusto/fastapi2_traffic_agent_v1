from pydantic import BaseModel, Field, validator
from typing import Dict

class DynamicCongestionOptimizeInput(BaseModel):
    weight_PublicTransport: float = Field(..., gt=0, lt=1,
        description="Peso para Transporte Público (0 < weight_PublicTransport < 1)")
    weight_Congestion: float = Field(..., gt=0, lt=1,
        description="Peso para Congestión (0 < weight_Congestion < 1)")
    weight_OperationalCost: float = Field(..., gt=0, lt=1,
        description="Peso para Costo Operativo (0 < weight_OperationalCost < 1)")
    weight_Emissions: float = Field(..., gt=0, lt=1,
        description="Peso para Emisiones (0 < weight_Emissions < 1)")

    @validator(
        "weight_PublicTransport", "weight_Congestion",
        "weight_OperationalCost", "weight_Emissions"
    )
    def weights_non_zero(cls, v):
        if v <= 0:
            raise ValueError("El peso debe ser mayor que 0")
        return v

class KPIResults(BaseModel):
    baseline: Dict[str, float]
    optimized: Dict[str, float]
    difference: Dict[str, float]

class DynamicCongestionOptimizeOutput(BaseModel):
    KPIs: KPIResults