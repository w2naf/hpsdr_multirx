#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HPSDR MultiRX
# Author: John Ackermann N8UR
# Description: Records multiple spectrum chunks to disk
# Generated: Thu Sep  6 08:53:10 2018
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

    def __init__(self, rx_0=3675000, rx_1=7175000, rx_2=10100000, rx_3=14175000):
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
        # Parameters
        ##################################################
        self.rx_0 = rx_0
        self.rx_1 = rx_1
        self.rx_2 = rx_2
        self.rx_3 = rx_3

        ##################################################
        # Variables
        ##################################################
        self.working_dir = working_dir = "hf_data/"
        self.timestamp_iso = timestamp_iso = datetime.utcnow().isoformat()+"Z"
        self.rx_samp_rate = rx_samp_rate = 192000
        self.metadata = metadata = {'call':'<call>','grid':'<6-digit-grid>','rx':'<radio>','ant':'<antenna>'}
        self.file_stamp = file_stamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	000000, #fc
        	rx_samp_rate, #bw
        	'QT GUI Plot', #name
        	4 #number of inputs
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

        labels = ['RX0', 'RX1', 'RX2', 'Rx3', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.hpsdr_hermesNB_0 = hpsdr.hermesNB(rx_0, rx_1, rx_2, rx_3, 10000000, 10000000, 10000000, 10000000, 10000000, 0, 0, 1, 1, 0, rx_samp_rate, "enp0s3", "0xF0", 0, 0, 0x20, 0x10, 0, 4, "*")
        self.analog_sig_source_x_1 = analog.sig_source_c(48000, analog.GR_COS_WAVE, -1000, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.hpsdr_hermesNB_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.hpsdr_hermesNB_0, 1), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.hpsdr_hermesNB_0, 2), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.hpsdr_hermesNB_0, 3), (self.qtgui_freq_sink_x_0, 3))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rx_0(self):
        return self.rx_0

    def set_rx_0(self, rx_0):
        self.rx_0 = rx_0
        self.hpsdr_hermesNB_0.set_Receive0Frequency(self.rx_0)

    def get_rx_1(self):
        return self.rx_1

    def set_rx_1(self, rx_1):
        self.rx_1 = rx_1
        self.hpsdr_hermesNB_0.set_Receive1Frequency(self.rx_1)

    def get_rx_2(self):
        return self.rx_2

    def set_rx_2(self, rx_2):
        self.rx_2 = rx_2
        self.hpsdr_hermesNB_0.set_Receive2Frequency(self.rx_2)

    def get_rx_3(self):
        return self.rx_3

    def set_rx_3(self, rx_3):
        self.rx_3 = rx_3
        self.hpsdr_hermesNB_0.set_Receive3Frequency(self.rx_3)

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
        self.qtgui_freq_sink_x_0.set_frequency_range(000000, self.rx_samp_rate)
        self.hpsdr_hermesNB_0.set_RxSampRate(self.rx_samp_rate)

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    def get_file_stamp(self):
        return self.file_stamp

    def set_file_stamp(self, file_stamp):
        self.file_stamp = file_stamp


def argument_parser():
    description = 'Records multiple spectrum chunks to disk'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-a", "--rx-0", dest="rx_0", type="intx", default=3675000,
        help="Set rx0 [default=%default]")
    parser.add_option(
        "-b", "--rx-1", dest="rx_1", type="intx", default=7175000,
        help="Set rx1 [default=%default]")
    parser.add_option(
        "-c", "--rx-2", dest="rx_2", type="intx", default=10100000,
        help="Set rx2 [default=%default]")
    parser.add_option(
        "-d", "--rx-3", dest="rx_3", type="intx", default=14175000,
        help="Set rx3 [default=%default]")
    return parser


def main(top_block_cls=hpsdr_multirx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(rx_0=options.rx_0, rx_1=options.rx_1, rx_2=options.rx_2, rx_3=options.rx_3)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
