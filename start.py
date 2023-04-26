import os
os.system("uvicorn SocketAPP:app_asgi --host 0.0.0.0 --port $PORT")
