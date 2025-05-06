from fastapi import FastAPI
from app.routes.optimize import router as dynamic_router

app = FastAPI(title="Dynamic Congestion Optimize API")

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "API running. Use '/dynamic_congestion_optimize_service/' to POST input."}

# Montar únicamente el router del servicio de optimización dinámica
app.include_router(
    dynamic_router,
    prefix="",
    tags=["DynamicCongestion"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)