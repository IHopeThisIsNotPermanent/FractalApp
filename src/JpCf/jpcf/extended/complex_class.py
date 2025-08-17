import numpy as np
import warnings

def strict_arange(start, stop, step):
    return ((np.arange(0,step).astype(np.float64)/(step-1))) * (stop - start) + start

class cif:
    """Complex Iterated Function class
    """
    #AS PER https://stackoverflow.com/questions/16500656/which-color-gradient-is-used-to-color-mandelbrot-in-wikipedia#25816111
    #I'm not super creative and i think the Wikipeia one looks clean :)
    mapping = [
    (66, 30, 15),(25, 7, 26),(9, 1, 47),
    (4, 4, 73),(0, 7, 100),(12, 44, 138),
    (24, 82, 177),(57, 125, 209),(134, 181, 229),
    (211, 236, 248),(241, 233, 191),(248, 201, 95),
    (255, 170, 0),(204, 128, 0),(153, 87, 0),
    (106, 52, 3)
    ]
    map_arr = [
        np.array([val[0] for val in mapping]),
        np.array([val[1] for val in mapping]),
        np.array([val[2] for val in mapping])
    ]

    def __init__(self, f, width, height, Cutoff, count_factor = 1.0):

        """This class allows you to apply a transformation to a section of the complex plane, 
        every time you apply a batch of transormations it returns a numpy image representation of the
        section.

        Args:
            f (lambda x, x0): A function that does some opation to two numpyarray with datatype 'complex'
            width (int): The width of the image in px
            height (int): The height of the image in px
            Cutoff (float): The value in which if the arg of the number goes above, we note the iteration it occured on.

        """

        self.f = f
        self.width, self.height = width, height
        self.Cutoff = Cutoff
        self.count_factor = count_factor

        self.M = None # The current matrix of values
        self.M0 = None # The previous matrix of values
        self.Count = None # The iteration the points arg became greater than Cutoff
        self.Final = None # The point when the arg first became greater than Cutoff
        
        #NOTE: this is not exactly correct, for the sake of simplfication it is though ;)
        self.Final_1 = None # The previous point when the arg first became greater than Cutoff

        self.i = None


    def start(self, x0,y0,x1,y1):
        """Initializes the internal variables.

        Args:
            x0 (float): The left xlim
            y0 (float): The top ylim
            x1 (float): The right xlim
            y1 (float): The bottom ylim
        """
        self.M = np.array([strict_arange(x0, x1, self.width) for _ in range(self.height)]) + \
                np.transpose(np.array([strict_arange(y0,y1,self.height) for _ in range(self.width)])) * 1j
        self.M0 = np.array(self.M)
        self.Count = np.zeros(self.M.shape)
        self.Final = np.zeros(self.M.shape)
        self.Final1 = np.zeros(self.M.shape)
        self.M1 = np.zeros(self.M.shape)
        self.i = 0

    def val(self, Iterations):
        """Get the image of the state after Iterations.

        Args:
            Iterations (int): The number of iterations you wish to do.

        Returns:
            np.array(shape = (self.Width, self.Height, 3)).astype(int): The image representing the state of the sim.
        """
        with warnings.catch_warnings(): #numpy likes to spam overflow warnings >_<
            for _ in range(Iterations):
                self.i += 1
                self.Count = self.Count + (self.Count == 0) * (np.abs(self.M) > self.Cutoff) * self.i
                self.Final = np.where((self.Final == 0) & (np.abs(self.M) > self.Cutoff), np.abs(self.M), self.Final)
                self.Final1 = np.where((self.Final1 == 0) & (np.abs(self.M) > self.Cutoff), 
                                    ((self.Cutoff-np.abs(self.M1))/(np.abs(self.M) - np.abs(self.M1))), 
                                    self.Final1) #so here Final1 actually stores the "decimal count" its calcuated naively.
                self.M1 = np.array(self.M)
                self.M = self.f(self.M, self.M0)
        
            return (np.dstack([
                cif.map_arr[2][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[1][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[0][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0)
                ]) 
                +
                (
                np.dstack([
                cif.map_arr[2][(((self.Count+1)*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[1][(((self.Count+1)*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[0][(((self.Count+1)*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0)
                ]) -    
                np.dstack([
                cif.map_arr[2][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[1][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0),
                cif.map_arr[0][((self.Count*self.count_factor) % 16).astype(np.int8)] * (self.Count != 0)
                ])
                )
                * np.dstack([
                    self.Final1,
                    self.Final1,
                    self.Final1
                ])
            )
    