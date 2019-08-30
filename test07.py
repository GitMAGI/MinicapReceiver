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
    Fs = 44100
    fc = 440
    t = np.arange(0, 1, 1/Fs)
    A = 1
    s = A*np.cos(2*np.pi*fc*t)
    s = (s + A) / A # Shift signla in the positive range and normalize it
    '''
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
    i_start = 4500
    i_end = 4950
    s_for_poly = np.round(s[i_start : i_end] * h/2)
    t_for_poly =  np.linspace(0, i_end - i_start, num=i_end - i_start)    

    '''
    plt.plot(t_for_poly, s_for_poly)
    plt.xlabel('time [sec]')
    plt.ylabel('Cosine fc={} sampled at Fs={}'.format(fc, Fs))
    plt.axis('tight')
    plt.show()

    sys.stdout.write('Resampled Time ({} samples) {}\n'.format(s_for_poly.size, s_for_poly))
    sys.stdout.write('Resampled Cosine fc={} sampled at Fs={} ({} samples) {}\n'.format(fc, Fs, s_for_poly.size, s_for_poly))    
    '''

    #cv2.polylines(img_base, [pts], False, (208, 128, 80), 2, 4, 0)

    #cv2.imshow(window_name, img_base)
    #cv2.waitKey(0)
    #cv2.destroyWindow(window_name)