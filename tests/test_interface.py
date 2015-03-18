# coding=utf-8
import unittest
from tabelafipe.interface import *


class InterfaceTestCase(unittest.TestCase):

    def test_instance(self):
        instance = Interface(TIPO_CARRO)
        self.assertIsInstance(instance, Interface)
