"""Craete and configure app for metrichub."""

from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> Any:
    """
    Root is base path for the app.

    Returns
    -------
    Any
        simple dict for testing purpose.
    """
    return {"message": "Hello user!"}
