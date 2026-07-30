from fastapi import FastAPI
from presentation.routers import router

main = FastAPI(
    title='Car API',
    description='modern Car API',
    version='0.1.0',
)


main.include_router(router)
