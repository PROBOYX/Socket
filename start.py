import os
os.system("uvicorn socketAPP:app_asgi --host 0.0.0.0 --port $PORT")
