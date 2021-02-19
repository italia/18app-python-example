import zeep
from zeep.exceptions import Fault
import unittest
from merchantclient import Voucher 
class IntegrationTests(unittest.TestCase):
    def test_attivazione(self):
        v = Voucher('123', 'test')
        v.AttivazioneSistema()
    
    def test_verifica(self):
        v = Voucher('123', 'test')
        result = v.Verifica()
        print(result)

if __name__ == '__main__':
    unittest.main()
