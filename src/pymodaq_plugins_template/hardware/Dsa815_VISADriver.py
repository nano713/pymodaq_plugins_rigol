import logging 
import pyvisa
logger = logging.getLogger(__name__)


class DSA815: 
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self._spectrum = rm.open_resource() # Open the first available resource and fix this

    
    def set_start_freq(self, start_freq): 
        """Set the start frequency of the spectrum analyzer"""
        if start_freq > 0 and start_freq < 7.5e9:
            self._spectrum.write(f":SENS:FREQ:STAR {start_freq} HZ")
            logger.info(f"Set start frequency to {start_freq} Hz")
    
    def get_start_freq(self): 
        """Get the start frequency of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:FREQuency:STARt?")
    
    def set_center_freq(self, center_freq): 
        """Set the center frequency of the spectrum analyzer"""
        if center_freq > 0 and center_freq < 7.5e9:
            self._spectrum.write(f":SENSe:FREQuency:CENTer {center_freq} HZ")
            logger.info(f"Set center frequency to {center_freq} Hz")
    
    def get_center_freq(self): 
        """Get the center frequency of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:FREQuency:CENTer?")