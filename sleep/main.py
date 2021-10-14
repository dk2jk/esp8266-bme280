from machine import reset_cause
x=reset_cause()
if x==6:
    y="hardware"
elif x==5:
    y="deepsleep_reset"
elif x==0:
    y="poweron"
elif x==4:
    y="soft"
elif x==1:
    y= "watchdog"
print("\nreset from '{}'".format(y))

#from deep_sleep import *