from tdd import importe_fruta

def test_calculo_importe():
    importe = 2.95
    cantidad = 0.5
    assert importe_fruta(importe, cantidad) == importe * cantidad
    cantidad = 1
    assert importe_fruta(importe, cantidad) == importe * cantidad