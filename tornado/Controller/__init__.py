import os
import sys


currentPath = os.path.realpath(__file__)
modelPath = os.path.join(os.path.dirname(currentPath), '..')

sys.path.append(modelPath)
