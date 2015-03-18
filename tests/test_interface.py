# coding=utf-8
import unittest
from tabelafipe.client import *


class ClientTestCase(unittest.TestCase):

    def test_instance(self):
        instance = Client(TIPO_CARRO)
        self.assertIsInstance(instance, Client)
