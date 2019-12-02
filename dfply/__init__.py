from .base import *
from .group import *
from .join import *
from .mask_helpers import *
from .reshape import *
from .select import *
from .select import *
from .set_ops import *
from .string_helpers import *
from .subset import *
from .summarize import *
from .transform import *
from .data import diamonds
from .summary_functions import *
from .window_functions import *
from .vector import *

for verb in dir():
    if 'ize' in verb:
        exec(verb.replace('ize', 'ise') + '=' + verb)
