from typing import List

from fastapi import WebSocket


class ConnectionManager:
    """
    Managing connection between client and server.

    Attributes
    ----------
    action_manager: ActionManager
        Just to get certificated users because why not

    active_connections: List[WebSocket]
        Current alive connections that is connected to WebSocket

    Methods
    -------
    __init__()
        Initalize the manager
        Set `active_connections`
    connect(websocket: WebSocket)
        Called when client connects to WebSocket
        Assign connection to `active_connections`
    disconnect(websocket: WebSocket)
        Called when client disconnects
        Remove connection from `active_connections`
    send_to_client(message: str, websocket: WebSocket)
        Sends message to the specified client
    broadcast(message: str)
        Sends message to all active connection
    """

    def __init__(self, action_manager) -> None:
        """
        Initalize the manager

        Set `active_connections`
        """
        self.action_manager = action_manager
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        """
        Called when client connects to WebSocket

        Assign connection to `active_connections`
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        """
        Called when client disconnects

        Remove connection from `active_connections`
        """
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_to_client(message: str, websocket: WebSocket) -> None:
        """Sends message to the specified client"""
        await websocket.send_text(message)

    async def broadcast(self, message: str) -> None:
        """Sends message to all logined connection"""
        for connection in self.action_manager.certed.name_ws.values():
            await connection.send_text(message)
