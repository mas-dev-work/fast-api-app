from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
<<<<<<< HEAD
=======
    print('this is line one')
    print('this is line two')
>>>>>>> 1bd2086 (final clean commit)
    print('adding log')
    return {"message": "Hello, FastAPI! updated responnse... adding something"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
