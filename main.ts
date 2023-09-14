input.onButtonPressed(Button.A, function () {
    hraj = true
})
input.onButtonPressed(Button.B, function () {
    hraj = false
})
let hraj = false
hraj = false
music.setTempo(400)
basic.forever(function () {
    if (hraj) {
        music.playTone(pins.analogReadPin(AnalogPin.P1) + 300, music.beat(BeatFraction.Sixteenth))
    }
})
