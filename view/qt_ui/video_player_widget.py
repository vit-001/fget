# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Dropbox/Hobby/PRG/PyWork/FGet/view/ui/video_player_widget.ui'
#
# Created: Wed Mar 25 17:24:44 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        VideoPlayer.setObjectName("VideoPlayer")
        VideoPlayer.resize(988, 587)
        self.verticalLayout = QtWidgets.QVBoxLayout(VideoPlayer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(VideoPlayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(-1, 4, -1, 4)
        self.top_frame_layout.setObjectName("top_frame_layout")
        self.mid_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mid_frame.sizePolicy().hasHeightForWidth())
        self.mid_frame.setSizePolicy(sizePolicy)
        self.mid_frame.setBaseSize(QtCore.QSize(0, 0))
        self.mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.mid_frame_grid_layout = QtWidgets.QGridLayout(self.mid_frame)
        self.mid_frame_grid_layout.setObjectName("mid_frame_grid_layout")
        self.top_frame_layout.addWidget(self.mid_frame)
        self.verticalLayout.addWidget(self.top_frame)
        self.bottom_frame = QtWidgets.QFrame(VideoPlayer)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.bottom_frame_layout = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.bottom_frame_layout.setContentsMargins(-1, 0, -1, 0)
        self.bottom_frame_layout.setObjectName("bottom_frame_layout")
        self.bn_play = QtWidgets.QToolButton(self.bottom_frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk_media_play_ltr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_play.setIcon(icon)
        self.bn_play.setIconSize(QtCore.QSize(30, 30))
        self.bn_play.setCheckable(False)
        self.bn_play.setAutoRaise(True)
        self.bn_play.setObjectName("bn_play")
        self.bottom_frame_layout.addWidget(self.bn_play)
        self.bn_pause = QtWidgets.QToolButton(self.bottom_frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk_media_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_pause.setIcon(icon1)
        self.bn_pause.setIconSize(QtCore.QSize(30, 30))
        self.bn_pause.setAutoRaise(True)
        self.bn_pause.setObjectName("bn_pause")
        self.bottom_frame_layout.addWidget(self.bn_pause)
        self.bn_stop = QtWidgets.QToolButton(self.bottom_frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk-media-stop_1950.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_stop.setIcon(icon2)
        self.bn_stop.setIconSize(QtCore.QSize(30, 32))
        self.bn_stop.setAutoRaise(True)
        self.bn_stop.setObjectName("bn_stop")
        self.bottom_frame_layout.addWidget(self.bn_stop)
        self.playlist_frame = QtWidgets.QFrame(self.bottom_frame)
        self.playlist_frame.setEnabled(True)
        self.playlist_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playlist_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playlist_frame.setObjectName("playlist_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.playlist_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bn_prev = QtWidgets.QToolButton(self.playlist_frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk_media_next_rtl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_prev.setIcon(icon3)
        self.bn_prev.setIconSize(QtCore.QSize(30, 30))
        self.bn_prev.setAutoRaise(True)
        self.bn_prev.setObjectName("bn_prev")
        self.horizontalLayout.addWidget(self.bn_prev)
        self.bn_next = QtWidgets.QToolButton(self.playlist_frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk_media_next_ltr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_next.setIcon(icon4)
        self.bn_next.setIconSize(QtCore.QSize(30, 30))
        self.bn_next.setAutoRaise(True)
        self.bn_next.setObjectName("bn_next")
        self.horizontalLayout.addWidget(self.bn_next)
        self.bottom_frame_layout.addWidget(self.playlist_frame)
        self.bn_add = QtWidgets.QToolButton(self.bottom_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/add_4471.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_add.setIcon(icon5)
        self.bn_add.setIconSize(QtCore.QSize(30, 30))
        self.bn_add.setAutoRaise(True)
        self.bn_add.setObjectName("bn_add")
        self.bottom_frame_layout.addWidget(self.bn_add)
        self.bn_minus = QtWidgets.QToolButton(self.bottom_frame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/gtk-remove_7385.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_minus.setIcon(icon6)
        self.bn_minus.setIconSize(QtCore.QSize(30, 30))
        self.bn_minus.setAutoRaise(True)
        self.bn_minus.setObjectName("bn_minus")
        self.bottom_frame_layout.addWidget(self.bn_minus)
        self.bn_playlist = QtWidgets.QToolButton(self.bottom_frame)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/editcut_2753.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_playlist.setIcon(icon7)
        self.bn_playlist.setIconSize(QtCore.QSize(30, 30))
        self.bn_playlist.setAutoRaise(True)
        self.bn_playlist.setObjectName("bn_playlist")
        self.bottom_frame_layout.addWidget(self.bn_playlist)
        self.bn_uget = QtWidgets.QToolButton(self.bottom_frame)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/uget/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_uget.setIcon(icon8)
        self.bn_uget.setIconSize(QtCore.QSize(30, 30))
        self.bn_uget.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.bn_uget.setAutoRaise(True)
        self.bn_uget.setObjectName("bn_uget")
        self.bottom_frame_layout.addWidget(self.bn_uget)
        self.progress_slider = QtWidgets.QSlider(self.bottom_frame)
        self.progress_slider.setOrientation(QtCore.Qt.Horizontal)
        self.progress_slider.setObjectName("progress_slider")
        self.bottom_frame_layout.addWidget(self.progress_slider)
        self.progress_buffer = QtWidgets.QProgressBar(self.bottom_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_buffer.sizePolicy().hasHeightForWidth())
        self.progress_buffer.setSizePolicy(sizePolicy)
        self.progress_buffer.setProperty("value", 24)
        self.progress_buffer.setTextVisible(False)
        self.progress_buffer.setOrientation(QtCore.Qt.Horizontal)
        self.progress_buffer.setObjectName("progress_buffer")
        self.bottom_frame_layout.addWidget(self.progress_buffer)
        self.lbl_time = QtWidgets.QLabel(self.bottom_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_time.setPalette(palette)
        self.lbl_time.setObjectName("lbl_time")
        self.bottom_frame_layout.addWidget(self.lbl_time)
        self.bn_size = QtWidgets.QToolButton(self.bottom_frame)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/size.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_size.setIcon(icon9)
        self.bn_size.setIconSize(QtCore.QSize(30, 30))
        self.bn_size.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.bn_size.setAutoRaise(True)
        self.bn_size.setObjectName("bn_size")
        self.bottom_frame_layout.addWidget(self.bn_size)
        self.dial_volume = QtWidgets.QDial(self.bottom_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_volume.sizePolicy().hasHeightForWidth())
        self.dial_volume.setSizePolicy(sizePolicy)
        self.dial_volume.setMinimumSize(QtCore.QSize(50, 50))
        self.dial_volume.setBaseSize(QtCore.QSize(0, 0))
        self.dial_volume.setMaximum(100)
        self.dial_volume.setSingleStep(1)
        self.dial_volume.setPageStep(5)
        self.dial_volume.setOrientation(QtCore.Qt.Horizontal)
        self.dial_volume.setWrapping(False)
        self.dial_volume.setNotchesVisible(False)
        self.dial_volume.setObjectName("dial_volume")
        self.bottom_frame_layout.addWidget(self.dial_volume)
        self.bn_mute = QtWidgets.QToolButton(self.bottom_frame)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/mute_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon10.addPixmap(QtGui.QPixmap("../qt_ui/files/icons/simple/mute_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_mute.setIcon(icon10)
        self.bn_mute.setIconSize(QtCore.QSize(30, 30))
        self.bn_mute.setCheckable(True)
        self.bn_mute.setAutoRaise(True)
        self.bn_mute.setObjectName("bn_mute")
        self.bottom_frame_layout.addWidget(self.bn_mute)
        self.verticalLayout.addWidget(self.bottom_frame)

        self.retranslateUi(VideoPlayer)
        QtCore.QMetaObject.connectSlotsByName(VideoPlayer)

    def retranslateUi(self, VideoPlayer):
        _translate = QtCore.QCoreApplication.translate
        VideoPlayer.setWindowTitle(_translate("VideoPlayer", "Form"))
        self.bn_play.setText(_translate("VideoPlayer", "PLAY"))
        self.bn_pause.setText(_translate("VideoPlayer", "PAUSE"))
        self.bn_stop.setText(_translate("VideoPlayer", "Stop"))
        self.bn_prev.setText(_translate("VideoPlayer", "PREV"))
        self.bn_next.setText(_translate("VideoPlayer", "NEXT"))
        self.bn_add.setText(_translate("VideoPlayer", "Add to playlist"))
        self.bn_minus.setText(_translate("VideoPlayer", "Remove"))
        self.bn_playlist.setText(_translate("VideoPlayer", "..."))
        self.bn_uget.setText(_translate("VideoPlayer", "uGet"))
        self.lbl_time.setText(_translate("VideoPlayer", "0:00"))
        self.bn_size.setText(_translate("VideoPlayer", "Size"))
        self.bn_mute.setText(_translate("VideoPlayer", "MUTE"))

