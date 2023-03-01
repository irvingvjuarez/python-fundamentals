from collections.abc import Sequence
from typing import Dict, Tuple

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    # Some code broadcasting the message
    pass