import time
import cv2
from io import BytesIO

import threading
import warnings

from ipycanvas import Canvas
from ipywidgets import Image

class interactable_canvas:

    def __init__(self,width,height,f,MAX_ITER=200,x0=-2,y0=-2,x1=2,y1=2):
        self.c = Canvas(width = width, height = height)
        
        self.width, self.height = width, height
        self.x0,self.y0,self.x1,self.y1 = x0,y0,x1,y1
        #Origin
        self.Ox0,self.Oy0,self.Ox1,self.Oy1 = x0,y0,x1,y1
        self.c.on_mouse_up(self.handle_mouse_up)
        self.c.on_mouse_down(self.handle_mouse_down)
        self.c.on_mouse_wheel(self.handle_mouse_wheel)

        self.prev_pos = 0,0

        self.quick_click = 0.5
        self.prev_click_time = time.time()
        self.down_time = time.time()
        self.quick_clicks = 0

        self.f = f

        self.MAX_ITER = MAX_ITER
        self.draw_switch = 0
        
        #Lock the drawing function
        self.draw_lock = threading.Lock()

        #Lock incrementing the draw switch :)
        self.increment_lock = threading.Lock()

        #Lock appending to the states
        self.states_lock = threading.Lock()

        self.states = []

        t=threading.Thread(target = self.draw)
        t.start()

    def draw(self):

        with self.increment_lock:
            self.draw_switch += 1
            my_draw_switch = self.draw_switch

        with self.draw_lock:
            BATCH = 20
            itr = 0
            self.f.start(self.x0,self.y0,self.x1,self.y1)
            while my_draw_switch == self.draw_switch and itr < self.MAX_ITER:
                itr += BATCH
                nxt_img_np = self.f.val(BATCH)
                nxt_img = Image.from_file(BytesIO(cv2.imencode('.jpg', nxt_img_np)[1].tobytes()))
                self.c.draw_image(nxt_img)
            
    def handle_mouse_down(self, x, y):
        self.prev_pos = x,y
        self.down_time = time.time()

    def handle_mouse_up(self, x, y):
        DELTA = 3
        td = time.time() - self.down_time
        since_last_click_td = time.time() - self.prev_click_time
        if abs(x - self.prev_pos[0]) <= DELTA and \
           abs(y - self.prev_pos[1]) <= DELTA and \
           td <= self.quick_click:
            
            self.quick_clicks += 1
            if self.quick_clicks >= 2 and \
               since_last_click_td <= self.quick_click:
                
                self.quick_clicks = 0
                self.x0,self.y0,self.x1,self.y1 = self.Ox0,self.Oy0,self.Ox1,self.Oy1
                with self.states_lock:
                    self.states = []
                t=threading.Thread(target = self.draw)
                t.start()
        else:
            self.quick_clicks = 0
            xd = self.x1 - self.x0
            yd = self.y1 - self.y0
            Lx = min(x, self.prev_pos[0])
            Rx = max(x, self.prev_pos[0])
            Ly = min(y, self.prev_pos[1])
            Ry = max(y, self.prev_pos[1])
            px0 = self.x0
            py0 = self.y0
            self.x0 = px0 + xd * (Lx/self.width)
            self.y0 = py0 + yd * (Ly/self.height)
            self.x1 = px0 + xd * (Rx/self.width)
            self.y1 = py0 + yd * (Ry/self.height)
            with self.states_lock:
                self.states.append((self.x0,self.y0,self.x1,self.y1))
            t=threading.Thread(target = self.draw)
            t.start()
        self.prev_click_time = time.time()

    def handle_mouse_wheel(self, x, y):
        completed = False
        with self.states_lock:
            if len(self.states) != 0:
                completed = True
                prev = self.states.pop()
                self.x0 = prev[0]
                self.y0 = prev[1]
                self.x1 = prev[2]
                self.y1 = prev[3]
        if completed:
            t=threading.Thread(target = self.draw)
            t.start()
