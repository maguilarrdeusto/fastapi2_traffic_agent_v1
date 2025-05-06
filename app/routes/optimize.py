from fastapi import APIRouter, HTTPException
from app.schemas import (
    DynamicCongestionOptimizeInput,
    DynamicCongestionOptimizeOutput
)
from app.services.optimization import dynamic_congestion_optimize_service

router = APIRouter()

@router.post(
    "/dynamic_congestion_optimize_service/",
    response_model=DynamicCongestionOptimizeOutput
)
async def dynamic_congestion_optimize(input_data: DynamicCongestionOptimizeInput):
    try:
        weights = {
            "weight_PublicTransport": input_data.weight_PublicTransport,
            "weight_Congestion": input_data.weight_Congestion,
            "weight_OperationalCost": input_data.weight_OperationalCost,
            "weight_Emissions": input_data.weight_Emissions,
        }
        kpis = await dynamic_congestion_optimize_service(weights)
        return {"KPIs": kpis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))