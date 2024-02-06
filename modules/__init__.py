from .afk import AFK 
from .tor import TOR 
from .general import General
from .redirect import Redirect 
MODULES = [General(), Redirect(),AFK(),TOR()]
