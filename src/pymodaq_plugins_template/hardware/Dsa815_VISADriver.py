import logging 
import pyvisa
logger = logging.getLogger(__name__)


class DSA815: 
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self._spectrum = rm.open_resource() # Open the first available resource and fix this

    
    def set_start_freq(self, start_freq): 
        self._spectrum.write(":SENS:FREQ:STAR %e HZ")
        logger.info(f"Set start frequency to {start_freq} Hz")