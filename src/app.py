from litestar import Litestar

from config import alchemy
from controller import UserController

app = Litestar(
    route_handlers=[UserController],
    plugins=[alchemy],
)
