from fastapi import APIRouter

from .utility import login

api_router = APIRouter()

######################### BAY Fund Transfer (for Loan Disbursement) ###########################################

pre_route = "fund_transfer"


api_router.include_router(
	login.router,
	tags=["BAY Fund Transfer (for Loan Disbursement)"],
	prefix=f"/{pre_route}",
)

