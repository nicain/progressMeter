#
#  example.py
#  progressMeter
#
#  Created by nicain on 5/5/10.
#  Copyright (c) 2010 __MyCompanyName__. All rights reserved.
#

import progressMeter as pm
import time
import random

total = 20
p = pm.ProgressMeter(total=total)

while total > 0:
    p.update(1)
    time.sleep(1)
    total -= 1