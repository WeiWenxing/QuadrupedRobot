import numpy as np


class Command:
    """Stores movement command
    """

    def __init__(self):
        self.horizontal_velocity = np.zeros(2, dtype=np.float64)
        self.yaw_rate = 0.0
        self.height = -0.07
        self.pitch = 0.0
        self.roll = 0.0
        self.activation = 0
        
        self.hop_event = False
        self.trot_event = False
        self.activate_event = False
        self.dance_activate_event = False

        self.dance_switch_event = False
        self.gait_switch_event = False
        
        self.shutdown_signal = False
        
        # Fales: dance triggered by controller
        # True: dance triggered by command line
        self.pseudo_dance_event = False
