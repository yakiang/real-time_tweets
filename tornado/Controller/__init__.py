''' Add Model/ into system path so that
I can import modules inside, from within Controller/
'''

import os
import sys


currentPath = os.path.realpath(__file__)
modelPath = os.path.join(os.path.dirname(currentPath), '..')

sys.path.append(modelPath)
