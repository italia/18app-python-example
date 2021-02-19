class VerificaVoucherResult:
    def __init__(self, ambito, bene, importo, partitaIvaEsercente, nominativoBeneficiario):       
        self._ambito = ambito
        self._bene = bene
        self._importo = importo
        self._partitaIvaEsercente = partitaIvaEsercente
        self._nominativoBeneficiario = nominativoBeneficiario
    #def __init__(self, ambito, bene, importo, partitaIvaEsercente, nominativoBeneficiario):
    #    self._ambito = ambito
    #    self._bene = bene
    #    self._importo = importo
    #    self._partitaIvaEsercente = partitaIvaEsercente
    #    self._nominativoBeneficiario = nominativoBeneficiario

    @property
    def ambito(self):
        return self._ambito

    @ambito.setter
    def ambito(self, value):
        self._ambito = value

    @property
    def bene(self):
        return self._bene

    @bene.setter
    def bene(self, value):
        self._bene = value
    
    @property
    def importo(self):
        return self._importo

    @importo.setter
    def importo(self, value):
        self._importo = value
    
    @property
    def partitaIvaEsercente(self):
        return self._partitaIvaEsercente

    @partitaIvaEsercente.setter
    def partitaIvaEsercente(self, value):
        self._partitaIvaEsercente = value

    @property
    def nominativoBeneficiario(self):
        return self._nominativoBeneficiario

    @nominativoBeneficiario.setter
    def nominativoBeneficiario(self, value):
        self._nominativoBeneficiario = value

  
    
    # def __init__(self, bene, importo, nominativoBeneficiario, partitaIvaEsercente):
    #     self._bene = bene
    #     self._importo = importo
    #     self._nominativoBeneficiario
    #     self._partitaIvaEsercente = partitaIvaEsercente
