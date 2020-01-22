from time import sleep
import pifacedigitalio


DELAY = 2.0  # seconds


if __name__ == "__main__":
    pifacedigital = pifacedigitalio.PiFaceDigital()
    #  2020-01-20 Turn off SIKAMAT2 LAN switch
    pifacedigital.leds[0].turn_on()
