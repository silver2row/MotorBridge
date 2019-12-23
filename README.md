# MotorBridge
MotorBridge.py now needs smbus2 for i2c use for the Beagleboard.org boards...

    https://github.com/kplindegaard/smbus2

This library can be installed with: 

    pip3 install smbus2. 

# smbus2.py has been added
Now...we can alter line 302 in the smbus2.py file to fit our needs.

First, go to .local/lib/python3.5/site-packages/smbus2/smbus2.py

    filepath = "/dev/i2c-2".format(bus)

That is how the line 302 should look now outside of the regular pip3 install.

# Additional Source
If you have a BBB, BBG, BBGW, BBBW, or another variation of board from 
beagleboard.org, you can, with their debian images, add a 12v DC battery, a
couple of hook-up wires(4), and a screwdriver, add functionality to your
Motor Bridge Cape with the pip3 install and a DC motor.

...

Look at the source for uMoveI.py for an update to the source. It is simplistic
and approachable. If it keeps running, just run the source and Control-C before
the software starts to cancel the motor from moving.

    uMoveI.py will initiate your motor with time, make several turns, and 
    then turn in the opposite direction and then stop for about 10 seconds 
    before stopping the program. Enjoy!

Seth
