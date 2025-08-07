if __name__ == "__main__":
    import uvicorn
    from metrichub import app

    uvicorn.run(app, host="0.0.0.0", port=9000)
