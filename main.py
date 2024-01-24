from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import meter_routes, logs_routes, configs_routes
from models import meter_model, logs_model, configs_model, registry_model
from configs.database import engine


meter_model.Base.metadata.create_all(bind=engine)
logs_model.Base.metadata.create_all(bind=engine)
configs_model.Base.metadata.create_all(bind=engine)
registry_model.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}", "Detail": f"{err}"})


@app.get("/")
async def index():
    return {"message": "welcome to the root of the micro_service, developed by black, Copyright @ 2023"}


app.include_router(meter_routes.router, prefix='/api/meter')
app.include_router(logs_routes.router, prefix='/api/logger')
app.include_router(configs_routes.router, prefix='/api/configs')
