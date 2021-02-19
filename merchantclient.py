import zeep
import logging
import verificavoucherresult
import merchantconfig
import inspect
from requests import Session
from zeep.transports import Transport
from zeep.wsse.signature import Signature
from zeep.exceptions import Fault
import logging.config

class Voucher:
    """ Gestione dei voucher """
    def __init__(self, codiceVoucher, partitaIvaEsercente):
        self.codiceVoucher = codiceVoucher
        self.partitaIvaEsercente = partitaIvaEsercente
        session = Session()
        session.cert = ('certificatodiprova.pem', 'private.key')
        session.verify = False
        transport = Transport(session=session)
        wsdl = merchantconfig.MerchantConfig.wsdl()
        self._client = zeep.Client(wsdl=wsdl, transport=transport)

    """ Ritorna informazioni sul borsellino senza consumare il voucher
        e quindi senza scalare l’importo dal borsellino del beneficiario """
    def Verifica(self):
        try:
            check = self._Check(1)
            return check
        except Exception as e:
            print("Errore Ver")
            print("Code " + e.code)
            print("MEssage " + e.message)
            detail = e.detail
            print("TEXT " + detail.tag)
            print(dir(e.detail))

    def Consuma(self):
        self._Check(2)

    def Impegna(self):
        self._Check(3)

    def Conferma(self):
        return self._Confirm() == "OK"

    """Esegue la chiamata--one time--di attivazione del servizio per l'esercente. """
    def AttivazioneSistema(self):
        try:
            check_type = self._client.get_type('ns0:Check')
            check = check_type(1,
                               "11aa22bb", self.partitaIvaEsercente)
            wsdl = merchantconfig.MerchantConfig.wsdl()
            checkResult = self._client.service.Check(check)
            result = verificavoucherresult.VerificaVoucherResult(checkResult.ambito,
                                                                checkResult.bene,
                                                                checkResult.importo,
                                                                checkResult.partitaIvaEsercente,
                                                                checkResult.nominativoBeneficiario)
                                           
            #result = verificavoucherresult.VerificaVoucherResult(checkResult.ambito,
            #                               checkResult.bene,
            #                               checkResult.importo,
            #                               checkResult.partitaIvaEsercente,
            #                               checkResult.nominativoBeneficiario)
            return result
        except Exception as e:
            logging.error(e)

    def _Check(self, op):
        try:
            check_type = self._client.get_type('ns0:Check')
            check = check_type(op,
                               self.codiceVoucher, self.partitaIvaEsercente)
            checkResult = self._client.service.Check(check)
            result = verificavoucherresult.VerificaVoucherResult(checkResult.ambito,
                                           checkResult.bene,
                                           checkResult.importo,
                                           checkResult.partitaIvaEsercente,
                                           checkResult.nominativoBeneficiario)
            return result
        except Exception as e:
            print("Errore ")
            logging.error(e)
            logging.error(e.message)
            raise

    def _Confirm(self, op):
        try:
            check_type = self.client.get_type('ns0:Confirm')
            check = check_type(op,
                               self.codiceVoucher,
                               self.partitaIvaEsercente)
            checkResult = self.client.VerificaVoucher.Check(check)
            return checkResult
        except Exception as e:
            logging.error(e)

# logging.config.dictConfig({
#     'version': 1,
#     'formatters': {
#         'verbose': {
#             'format': '%(name)s: %(message)s'
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'zeep.transports': {
#             'level': 'DEBUG',
#             'propagate': True,
#             'handlers': ['console'],
#         },
#     }
# })
