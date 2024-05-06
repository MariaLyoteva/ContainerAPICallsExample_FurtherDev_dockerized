from fastapi import FastAPI, Request
#from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def hello(request: Request):
    # Get the request origin from the forwarded headers
    request_origin = request.headers.get("X-Forwarded-For") or request.client.host
    print(f"Request origin: {request_origin}")
    return {"message": "Hello from the backend!"}
