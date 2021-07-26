# Python code
#
comp_read = 0
Rotation_Pitch = 0
Compass = 0


def on_forever():
    global Compass
    global Rotation_Pitch
    Compass = input.compass_heading()
    Rotation_Pitch = input.rotation(Rotation.Pitch)
    if Compass > 180:
        Compass = (180 - Compass)
    if Rotation_Pitch > 180:
        Rotation_Pitch = (180 - Rotation_Pitch)
    led.plot_bar_graph(input.compass_heading(), 50)
    pins.servo_write_pin(AnalogPin.P1, Rotation_Pitch)
    pins.servo_write_pin(AnalogPin.P2, Compass)


basic.forever(on_forever)
