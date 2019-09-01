import cv2
import numpy as np
import math
import sys
import matplotlib.pylab as plt

def easy_drawings():
    window_name = "Easy Drawings"
    w = 512
    h = 512

    img_base_w = np.ones((h, w, 3), np.uint8) * 255
    img_base_b = np.zeros((h, w, 3), np.uint8)
    img_base = img_base_w

    #NOTE
    # RGB is coded as Blue, Green and Red

    # Straight Line
    #cv2.line(img_base, (35, 90), (100, 90), (130, 135, 228), 2, 8, 0)

    # Rectangle
    #cv2.rectangle(img_base, (60, 100), (90, 150), (128, 12, 150), 2, 4, 0)

    # Polyline    
    '''
    t_start = 0
    t_end = 1
    Fs = 44100
    fc = 440
    t = np.arange(t_start, t_end, 1/Fs)
    A = 1
    s = A*np.cos(2*np.pi*fc*t)
    s = (s + A) / A # Shift signla in the positive range and normalize it
    
    i_plot_start = 4500
    i_plot_end = 4950
    t_plot = t[i_plot_start : i_plot_end]
    s_plot = s[i_plot_start : i_plot_end]
    plt.plot(t_plot, s_plot)
    plt.xlabel('time [sec]')
    plt.ylabel('Cosine fc={} sampled at Fs={}'.format(fc, Fs))
    plt.axis('tight')
    plt.show()    
    sys.stdout.write('Time ({} samples) {}\n'.format(t.size, t))
    sys.stdout.write('Cosine fc={} sampled at Fs={} ({} samples) {}\n'.format(fc, Fs, s.size, s))    
    '''

    t_start = 0
    t_end = w
    Fs = 1
    fc = 0.04
    t = np.arange(t_start, t_end, 1/Fs)
    A = int(h/2)
    s = A*np.cos(2*np.pi*fc*t)
    s = (s + A) # Shift signla in the positive range
    s = np.rint(s)
    '''
    i_plot_start = 0
    i_plot_end = 512
    t_plot = t[i_plot_start : i_plot_end]
    s_plot = s[i_plot_start : i_plot_end]
    plt.plot(t_plot, s_plot)
    plt.xlabel('time [sec]')
    plt.ylabel('Cosine fc={} sampled at Fs={}'.format(fc, Fs))
    plt.axis('tight')
    plt.show()    
    sys.stdout.write('Time ({} samples) {}\n'.format(t.size, t))
    sys.stdout.write('Cosine fc={} sampled at Fs={} ({} samples) {}\n'.format(fc, Fs, s.size, s))    
    '''
    pts = np.empty([s.size, 2], dtype=np.int32)
    for i in range(0, s.size, 1):
        pts[i, :] = [t[i], s[i]]    
    cv2.polylines(img_base, [pts], False, (208, 128, 80), 2, 4, 0)

    cv2.imshow(window_name, img_base)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)