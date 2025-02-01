import logging 
import pyvisa
logger = logging.getLogger(__name__)


class DSA815: 
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self._spectrum = rm.open_resource() # Open the first available resource and fix this
        
    def connect(self, address): 
        """Connect to the spectrum analyzer"""
        self._spectrum.open_resource(address)
        logger.info(f"Connected to {address}")
    
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
    
    def set_stop_freq(self, stop_freq): 
        """Set the stop frequency of the spectrum analyzer"""
        if stop_freq > 0 and stop_freq < 7.5e9:
            self._spectrum.write(f":SENSe:FREQuency:STOP {stop_freq} HZ")
            logger.info(f"Set stop frequency to {stop_freq} Hz")
    
    def get_stop_freq(self): 
        """Get the stop frequency of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:FREQuency:STOP?")
    
    def set_freq_points(self, freq_points): 
        """Set the number of frequency points of the spectrum analyzer"""
        if freq_points > 100 and freq_points < 3002:
            self._spectrum.write(f":SENSe:SWEep:POINts {freq_points}")
            logger.info(f"Set frequency points to {freq_points}")
    
    def get_freq_points(self): 
        """Get the number of frequency points of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:SWEep:POINts?")
    
    def set_sweep_time(self, sweep_time): 
        """Set the sweep time of the spectrum analyzer"""
        if sweep_time > 2e-5 and sweep_time < 7500:
            self._spectrum.write(f":SENSe:SWEep:TIME {sweep_time}")
            logger.info(f"Set sweep time to {sweep_time}")
    
    def get_sweep_time(self): 
        """Get the sweep time of the spectrum analyzer"""
        return self._spectrum.query(":SENSe:SWEep:TIME?")   
    
    def set_continuous_sweep(self, continuous_sweep): 
        """Set the continuous sweep of the spectrum analyzer"""
        if continuous_sweep == True:
            self._spectrum.write(":INITiate:CONTinuous ON")
            logger.info("Set continuous sweep to ON")
        else:
            self._spectrum.write(":INITiate:CONTinuous OFF")
            logger.info("Set continuous sweep to OFF")
    
    def get_continuous_sweep(self): 
        """Get the continuous sweep of the spectrum analyzer"""
        return self._spectrum.query(":INITiate:CONTinuous?")