# Micro:bit as Steering Wheel

This program, get data by serial connection, and then simulates a Steering Wheel using VGamepad lib.

It is designed to recieve data from micro:bit by serial connection. Micro:bit send accelerometer position in y-axis, this code, recieves that and then emulates a virtual gamepad,
where y-axis recieved is "translated" to the x-axis of the left analogue.



When you turn the steering wheel 90 degrees, it reaches the maximum range of the left analogue, I will soon take care of expanding the range of rotation.
