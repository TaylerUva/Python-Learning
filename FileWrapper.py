import time
import os
creator = "Tayler Uva"

dash = "============================="


def __printKey(msg, fileName):
    print("\n%s" % dash,
          msg, "- %s" % os.path.basename(fileName),
          "- Created by %s" % creator,
          "%s\n" % dash)


def hello(fileName):
    __printKey("START", fileName)


def goodbye(fileName):
    __printKey("END", fileName)
