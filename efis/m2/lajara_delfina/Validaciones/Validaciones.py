from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

def ValidarSolamenteLetras():
    rx = QRegularExpression("[A-Za-zñÑ]{20}")
    validator = QRegularExpressionValidator(rx)
    return validator
    
def ValidarSolamenteNumeros():
    rx = QRegularExpression("[0-9]{20}")
    validator = QRegularExpressionValidator(rx)
    return validator

def ValidarSolamenteDNI():
    rx = QRegularExpression("[0-9]{9}")
    validator = QRegularExpressionValidator(rx)
    return validator