from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Kafka Chat',
        docs_url='/api/docs',
        description='A simple kafka example',
        debug=True,
    )