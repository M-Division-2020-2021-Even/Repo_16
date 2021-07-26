# Python code
#
comp_read = 0
Rotation_Pitch = 0
Compass = 0
Rotation_Roll = 0


def on_forever():
    global Compass
    global Rotation_Pitch
    global Rotation_Roll
    Compass = input.compass_heading()
    Rotation_Pitch = input.rotation(Rotation.Pitch)
    Rotation_Roll = input.rotation(Rotation.Roll)
    if Compass > 180:
        Compass = (180 - Compass)
    if Rotation_Pitch > 180:
        Rotation_Pitch = (180 - Rotation_Pitch)
    if Rotation_Roll > 180:
        Rotation_Roll = (180 - Rotation_Roll)
    led.plot_bar_graph(input.compass_heading(), 50)
    pins.servo_write_pin(AnalogPin.P0, Rotation_Roll)
    pins.servo_write_pin(AnalogPin.P1, Rotation_Pitch)
    pins.servo_write_pin(AnalogPin.P2, Compass)


basic.forever(on_forever)
