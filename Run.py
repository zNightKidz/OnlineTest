import requests
import unittest
import json
from HTMLTestRunner
import time

import test_allFacility_get

suite = unittest.TestSuite()

suite.addTest(test_allFacility_get.test_allFacility_get("test_allFacility_get"))

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(suite)

    now = time.strftime("%Y-%m-%d %H_%M_%S")

    runner = HT
