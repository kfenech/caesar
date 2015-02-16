import visa 
import logging as log

class Device(resource, log):
    """
    """
    
    self.resource= None
    self.rm = None
    self.instrument = None
    self.err_log = None 
    
    def __init__(self, resource):
        self.err_log = log 
        self.resource = resource
        self.rm = visa.ResourceManager()
        self.connect()

    def connect(self):
        try:
            self.instrument = self.rm.open_resource(self.resource)
        except:
            print('Failed to connect to device {}'.format(self.resource))

    def disconnect(self):
        try:
            self.instrument = self.rm.close_resource(self.resource)
        except:
            print('Failed to safely disconnect from device'\
                    '{}'.format(self.resource))

    def write(self):
        pass

    def read(self):
        pass


class IO_Device(Device):
    """
    """
    self.num_analog_input = 0
    self.num_analog_output = 0
    self.num_digital_input = 0
    self.num_digital_output = 0
    self.instrument = None

    def __init__(self):
       pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def update(self):
        pass


