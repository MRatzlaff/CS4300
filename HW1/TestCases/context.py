import sys, os
# thank you to the person on discord who explained a context file!!
# put the parent directory on the environment's path
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, here)