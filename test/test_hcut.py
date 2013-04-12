#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import hcut
from tempfile import mkstemp

class HcutTest(unittest.TestCase):

    def setUp(self):
        self.fd, self.name = mkstemp()
        self.f = os.fdopen(self.fd, 'w')
        try:
            self.f.write("USER_ID\tNAME\tAGE\n")
            self.f.write("1\tTakahashi\t10\n")
            self.f.write("2\tSatoh\t20\n")
            self.f.write("3\tAbe\t30\n")
        finally:
            self.f.close()

    def tearDown(self):
        os.remove(self.name)

    def testReader(self):
        f = open(self.name)
        try:
            reader = hcut.reader(f, ["USER_ID", "NAME"], False, "\t", "utf-8")
            records = list(reader)
            self.assertEqual([['1', 'Takahashi'], ['2', 'Satoh'], ['3', 'Abe']], records)
        finally:
            f.close()

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(HcutTest)



