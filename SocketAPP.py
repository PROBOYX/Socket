from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = FastAPI()
app_asgi = socketio.ASGIApp(sio, app)

@app.on_event("startup")
async def startup_event():
    print("Server started")

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def play(sid, data):
    print(f"Play received from {sid} - data {data}")
    await sio.emit('play', data, skip_sid=sid)
    
@sio.event
async def playAll(sid, data):
    print(f"PlayAll received from {sid} - data {data}")
    await sio.emit('playAll', data)


@sio.event
async def pause(sid, data):
    print(f"Pause received from {sid} - data {data}")
    await sio.emit('pause', data, skip_sid=sid)

@sio.event
async def seek(sid, data):
    print(f"Seek received from {sid} - data {data}")
    await sio.emit('seek', data, skip_sid=sid)

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app_asgi, host='0.0.0.0', port=8000)
