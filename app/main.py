from fastapi import FastAPI

main = FastAPI(
    title='Car API',
    description='modern Car API',
    version='0.1.0',
)


@main.get('/')
def read_root():
    return {'status': 'ok'}
