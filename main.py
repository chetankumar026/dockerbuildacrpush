import json, os
import requests

from fastapi import FastAPI

import weaviate
from weaviate.embedded import EmbeddedOptions

from fastapi.middleware.cors import CORSMiddleware
auth_config = weaviate.AuthApiKey(api_key="uo6WeAK9JJzwdowMsxGM8nY4zN3nCAbQB4zI") 
        
app.weaviate_client = weaviate.Client(
    embedded_options=EmbeddedOptions(
        client = weaviate.Client(url="https://testingunb-v65i3yzc.weaviate.network", auth_client_secret=auth_config )
    )
)
    

def init_app():
  print("Initiating weaviate")
  init_weaviate()
  print("Done Initiating weaviate")

  # Allow all origins
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

app = FastAPI()
init_app()

@app.get("/")
def hello_world():
    return {"Hello": "World"}
