#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/Volumes/Untitled/Flask/ex_during")
from ex_during import app as application
