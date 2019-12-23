# MotorBridge
MotorBridge.py now needs smbus2 for i2c use for the Beagleboard.org boards...

    https://github.com/kplindegaard/smbus2

This library can be installed with: 

    pip3 install smbus2. 

# smbus2.py has been added
Now...we can alter line 302 in the smbus2.py file to fit our needs.

    filepath = "/dev/i2c-2".format(bus)

That is how the line 302 should look now outside of the regular pip3 install.

Oh...use this command to get the smbus2 library on your BBG (BeagleBone Green).

    pip3 install smbus2


