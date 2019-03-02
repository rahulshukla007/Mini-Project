# OTP Generation

import random

def genOTP():
    OTP = ""
    for i in range(4):
        OTP = OTP + str(random.randint(0,9))
    return OTP

print(genOTP())
