input.onButtonPressed(Button.A, () => {
    basic.showString("1")
    pins.digitalWritePin(DigitalPin.P2, 1)
})
input.onButtonPressed(Button.B, () => {
    basic.showString("0")
    pins.digitalWritePin(DigitalPin.P2, 0)
})
input.onButtonPressed(Button.AB, () => {
    basic.showLeds(`
        . . # . .
        . # . # .
        # # # # #
        . # . # .
        . . # . .
        `)
    pins.digitalWritePin(DigitalPin.P2, 1)
    control.waitMicros(500)
    pins.digitalWritePin(DigitalPin.P2, 0)
    control.waitMicros(500)
    pins.digitalWritePin(DigitalPin.P2, 1)
    control.waitMicros(500)
    pins.digitalWritePin(DigitalPin.P2, 0)
})
basic.showString("GO!")
