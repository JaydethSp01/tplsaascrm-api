from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_metrics():
    # Simulating some metrics for demonstration purposes
    metrics = {
        "leads": 50,
        "oportunidades": 20,
        "conversionRate": 40.0  # This would be calculated based on real data
    }
    return metrics
