#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HPSDR MultiRX
# Author: Nathaniel Frissell W2NAF
# Description: Records multiple spectrum chunks to disk
# Generated: Sun Sep 30 00:36:44 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

def struct(data): return type('Struct', (object,), data)()
from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from datetime import datetime
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import hpsdr
import sip
import sys
from gnuradio import qtgui


class hpsdr_multirx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "HPSDR MultiRX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HPSDR MultiRX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.working_dir = working_dir = "/media/icerx/icerx/hf_data/"
        self.timestamp_iso = timestamp_iso = datetime.utcnow().isoformat()+"Z"
        self.rx_samp_rate = rx_samp_rate = 192000
        self.rx_6 = rx_6 = struct({'label': 'WWV_10050', 'frequency': 10.05e6, })
        self.rx_5 = rx_5 = struct({'label': 'HAM_14096', 'frequency': 14.096e6, })
        self.rx_4 = rx_4 = struct({'label': 'CHU_14670', 'frequency': 14.67e6, })
        self.rx_3 = rx_3 = struct({'label': 'HAM_7096', 'frequency': 7.096e6, })
        self.rx_2 = rx_2 = struct({'label': 'CHU_7850', 'frequency': 7.096e6, })
        self.rx_1 = rx_1 = struct({'label': 'HAM_3596', 'frequency': 3.596e6, })
        self.rx_0 = rx_0 = struct({'label': 'CHU_3300', 'frequency': 3.33e6, })
        self.metadata = metadata = {'call':'W2NAF','grid':'<6-digit-grid>','rx':'Red Pitaya','ant':'DXE RF-PRO-1B'}
        self.file_stamp = file_stamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0_5 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_6.frequency, #fc
        	rx_samp_rate, #bw
        	rx_6.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_5.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_5.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_5.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_5.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_5.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_5.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_5.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_5.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_5.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_5.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_5_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_5.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_5_win)
        self.qtgui_waterfall_sink_x_0_4 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_5.frequency, #fc
        	rx_samp_rate, #bw
        	rx_5.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_4.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_4.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_4.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_4.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_4.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_4.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_4.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_4.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_4.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_4.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_4_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_4.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_4_win)
        self.qtgui_waterfall_sink_x_0_3 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_4.frequency, #fc
        	rx_samp_rate, #bw
        	rx_4.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_3.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_3.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_3.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_3.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_3.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_3.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_3.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_3.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_3.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_3_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_3_win)
        self.qtgui_waterfall_sink_x_0_2 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_3.frequency, #fc
        	rx_samp_rate, #bw
        	rx_3.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_2.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_2.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_2.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_2.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_2_win)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_2.frequency, #fc
        	rx_samp_rate, #bw
        	rx_2.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_win)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_1.frequency, #fc
        	rx_samp_rate, #bw
        	rx_1.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_0.frequency, #fc
        	rx_samp_rate, #bw
        	rx_0.label, #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	000000, #fc
        	rx_samp_rate, #bw
        	'Received Spectrum', #name
        	7 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['{!s} MHz'.format(rx_0.frequency*1e-6), '{!s} MHz'.format(rx_1.frequency*1e-6), '{!s} MHz'.format(rx_2.frequency*1e-6), '{!s} MHz'.format(rx_3.frequency*1e-6), '{!s} MHz'.format(rx_4.frequency*1e-6),
                  '{!s} MHz'.format(rx_5.frequency*1e-6), '{!s} MHz'.format(rx_6.frequency*1e-6), '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(7):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.hpsdr_hermesNB_0 = hpsdr.hermesNB(int(rx_0.frequency), int(rx_1.frequency), int(rx_2.frequency), int(rx_3.frequency), int(rx_4.frequency), int(rx_5.frequency), int(rx_6.frequency), 10000000, 10000000, 0, 0, 1, 1, 0, rx_samp_rate, "enp2s0", "0xF0", 0xa0, 0, 0x00, 0x10, 0, 7, "*")
        self.analog_sig_source_x_1 = analog.sig_source_c(48000, analog.GR_COS_WAVE, -1000, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.hpsdr_hermesNB_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 1), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.hpsdr_hermesNB_0, 2), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.hpsdr_hermesNB_0, 3), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.hpsdr_hermesNB_0, 4), (self.qtgui_freq_sink_x_0, 4))
        self.connect((self.hpsdr_hermesNB_0, 5), (self.qtgui_freq_sink_x_0, 5))
        self.connect((self.hpsdr_hermesNB_0, 6), (self.qtgui_freq_sink_x_0, 6))
        self.connect((self.hpsdr_hermesNB_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 1), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 2), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.hpsdr_hermesNB_0, 3), (self.qtgui_waterfall_sink_x_0_2, 0))
        self.connect((self.hpsdr_hermesNB_0, 4), (self.qtgui_waterfall_sink_x_0_3, 0))
        self.connect((self.hpsdr_hermesNB_0, 5), (self.qtgui_waterfall_sink_x_0_4, 0))
        self.connect((self.hpsdr_hermesNB_0, 6), (self.qtgui_waterfall_sink_x_0_5, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_working_dir(self):
        return self.working_dir

    def set_working_dir(self, working_dir):
        self.working_dir = working_dir

    def get_timestamp_iso(self):
        return self.timestamp_iso

    def set_timestamp_iso(self, timestamp_iso):
        self.timestamp_iso = timestamp_iso

    def get_rx_samp_rate(self):
        return self.rx_samp_rate

    def set_rx_samp_rate(self, rx_samp_rate):
        self.rx_samp_rate = rx_samp_rate
        self.qtgui_waterfall_sink_x_0_5.set_frequency_range(rx_6.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0_4.set_frequency_range(rx_5.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0_3.set_frequency_range(rx_4.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0_2.set_frequency_range(rx_3.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(rx_2.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(rx_1.frequency, self.rx_samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(rx_0.frequency, self.rx_samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(000000, self.rx_samp_rate)
        self.hpsdr_hermesNB_0.set_RxSampRate(self.rx_samp_rate)

    def get_rx_6(self):
        return self.rx_6

    def set_rx_6(self, rx_6):
        self.rx_6 = rx_6

    def get_rx_5(self):
        return self.rx_5

    def set_rx_5(self, rx_5):
        self.rx_5 = rx_5

    def get_rx_4(self):
        return self.rx_4

    def set_rx_4(self, rx_4):
        self.rx_4 = rx_4

    def get_rx_3(self):
        return self.rx_3

    def set_rx_3(self, rx_3):
        self.rx_3 = rx_3

    def get_rx_2(self):
        return self.rx_2

    def set_rx_2(self, rx_2):
        self.rx_2 = rx_2

    def get_rx_1(self):
        return self.rx_1

    def set_rx_1(self, rx_1):
        self.rx_1 = rx_1

    def get_rx_0(self):
        return self.rx_0

    def set_rx_0(self, rx_0):
        self.rx_0 = rx_0

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    def get_file_stamp(self):
        return self.file_stamp

    def set_file_stamp(self, file_stamp):
        self.file_stamp = file_stamp


def main(top_block_cls=hpsdr_multirx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
