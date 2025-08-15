from channels.generic.websocket import AsyncJsonWebsocketConsumer

class SyncConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_json({"type":"hello","msg":"ws up"})

    async def receive_json(self, content, **kwargs):
        await self.send_json({"type":"echo","content":content})
