import logging 
import pyvisa
logger = logging.getLogger(__name__)


class DSA815: 
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self._spectrum = rm.open_resource() # Open the first available resource and fix this

    
    def set_start_freq(self, start_freq): 
        """Set the start frequency of the spectrum analyzer"""
        self._spectrum.write(":SENS:FREQ:STAR %e HZ")
        logger.info(f"Set start frequency to {start_freq} Hz")
    
    def get_start_freq(self): 
        """Get the start frequency of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:FREQuency:STARt?")