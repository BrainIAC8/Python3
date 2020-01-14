from pdfminer.pdfinterp import PDFResourceManager
from pdfminer. import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen

def lerPDF(arquivoPDF):
    # PDFResourceManager Usado para armazenar recursos compartilhados
    # como fontes e imagens
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
    process_pdf(recursos, dispositivo, arquivoPDF)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

# Abrindo arquivo PDF online
arquivoPDF = urlopen('c:\Arqpy/fgts.pdf')
stringSaida = lerPDF(arquivoPDF)
print(stringSaida)
arquivoPDF.close()