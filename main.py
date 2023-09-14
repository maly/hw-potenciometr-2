frequency = 0
ledStatus = False
sirenStatus = False

def on_pin_pressed_p0():
    global ledStatus, sirenStatus
    ledStatus = not ledStatus
    sirenStatus = not sirenStatus
    if ledStatus:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_forever():
    global frequency
    if sirenStatus:
        # Získání hodnoty z potenciometru a mapování na frekvenci sirény
        frequency = pins.map(abs(pins.analog_read_pin(AnalogPin.P1)), 0, 1023, 100, 2000)
        # Hraní sirény s proměnnou frekvencí
        pins.analog_set_pitch_pin(AnalogPin.P2)
        pins.analog_pitch(frequency, 100)
        basic.pause(100)
        pins.analog_pitch(0, 100)
    basic.pause(100)
basic.forever(on_forever)
