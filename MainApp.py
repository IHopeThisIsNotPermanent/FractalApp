# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SimpleFractalLienRH.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import SimpleFractal_Resources_rc

class Ui_SimpleFractal(object):
    def setupUi(self, SimpleFractal):
        if not SimpleFractal.objectName():
            SimpleFractal.setObjectName(u"SimpleFractal")
        SimpleFractal.resize(1638, 947)
        icon = QIcon()
        icon.addFile(u":/Icons/icon.jpeg", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/newPrefix/resources/icon.jpeg", QSize(), QIcon.Selected, QIcon.Off)
        SimpleFractal.setWindowIcon(icon)
        SimpleFractal.setIconSize(QSize(48, 48))
        self.actionSaveAs = QAction(SimpleFractal)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionSave = QAction(SimpleFractal)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(SimpleFractal)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(SimpleFractal)
        self.centralwidget.setObjectName(u"centralwidget")
        SimpleFractal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SimpleFractal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1638, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        SimpleFractal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SimpleFractal)
        self.statusbar.setObjectName(u"statusbar")
        SimpleFractal.setStatusBar(self.statusbar)
        self.PlayerDock = QDockWidget(SimpleFractal)
        self.PlayerDock.setObjectName(u"PlayerDock")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayerDock.sizePolicy().hasHeightForWidth())
        self.PlayerDock.setSizePolicy(sizePolicy)
        self.PlayerDock.setMinimumSize(QSize(1638, 180))
        self.PlayerDock.setMaximumSize(QSize(524287, 180))
        self.PlayerDock.setFeatures(QDockWidget.DockWidgetMovable)
        self.PlayerDock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.horizontalLayout_30 = QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_34 = QFrame(self.dockWidgetContents_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_34)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_31 = QLabel(self.frame_34)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_31)

        self.TextBrowser_ErrorLog = QTextBrowser(self.frame_34)
        self.TextBrowser_ErrorLog.setObjectName(u"TextBrowser_ErrorLog")
        self.TextBrowser_ErrorLog.setMinimumSize(QSize(300, 0))

        self.verticalLayout_10.addWidget(self.TextBrowser_ErrorLog)


        self.horizontalLayout_30.addWidget(self.frame_34)

        self.frame_21 = QFrame(self.dockWidgetContents_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.horizontalLayout_30.addWidget(self.frame_21)

        self.frame_35 = QFrame(self.dockWidgetContents_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_35)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_22 = QFrame(self.frame_35)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.SpinBox_TimeStep = QSpinBox(self.frame_22)
        self.SpinBox_TimeStep.setObjectName(u"SpinBox_TimeStep")
        self.SpinBox_TimeStep.setMinimum(10)
        self.SpinBox_TimeStep.setMaximum(10000)
        self.SpinBox_TimeStep.setSingleStep(10)
        self.SpinBox_TimeStep.setValue(100)

        self.horizontalLayout_18.addWidget(self.SpinBox_TimeStep)

        self.label_22 = QLabel(self.frame_22)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_18.addWidget(self.label_22)

        self.SpinBox_EndTime = QSpinBox(self.frame_22)
        self.SpinBox_EndTime.setObjectName(u"SpinBox_EndTime")
        self.SpinBox_EndTime.setMinimum(1)
        self.SpinBox_EndTime.setMaximum(500)

        self.horizontalLayout_18.addWidget(self.SpinBox_EndTime)

        self.PushButton_PlayPause = QPushButton(self.frame_22)
        self.PushButton_PlayPause.setObjectName(u"PushButton_PlayPause")

        self.horizontalLayout_18.addWidget(self.PushButton_PlayPause)

        self.PushButton_Stop = QPushButton(self.frame_22)
        self.PushButton_Stop.setObjectName(u"PushButton_Stop")

        self.horizontalLayout_18.addWidget(self.PushButton_Stop)


        self.verticalLayout_11.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_35)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_19.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_23)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_19.addWidget(self.label_24)

        self.Slider_Time = QSlider(self.frame_23)
        self.Slider_Time.setObjectName(u"Slider_Time")
        self.Slider_Time.setMaximum(10000)
        self.Slider_Time.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.Slider_Time)


        self.verticalLayout_11.addWidget(self.frame_23)


        self.horizontalLayout_30.addWidget(self.frame_35)

        self.frame_27 = QFrame(self.dockWidgetContents_4)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_28)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_27 = QLabel(self.frame_28)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_27)

        self.PlainTextEdit_Path = QPlainTextEdit(self.frame_28)
        self.PlainTextEdit_Path.setObjectName(u"PlainTextEdit_Path")
        self.PlainTextEdit_Path.setMinimumSize(QSize(200, 0))
        self.PlainTextEdit_Path.setMaximumSize(QSize(16777215, 56))

        self.verticalLayout_8.addWidget(self.PlainTextEdit_Path)


        self.horizontalLayout_27.addWidget(self.frame_28)


        self.horizontalLayout_30.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.dockWidgetContents_4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_29)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_33 = QFrame(self.frame_29)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_32 = QFrame(self.frame_33)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_30 = QLabel(self.frame_32)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_26.addWidget(self.label_30)

        self.ComboBox_ZoomInterp = QComboBox(self.frame_32)
        self.ComboBox_ZoomInterp.addItem("")
        self.ComboBox_ZoomInterp.addItem("")
        self.ComboBox_ZoomInterp.addItem("")
        self.ComboBox_ZoomInterp.setObjectName(u"ComboBox_ZoomInterp")

        self.horizontalLayout_26.addWidget(self.ComboBox_ZoomInterp)


        self.horizontalLayout_29.addWidget(self.frame_32)

        self.frame_30 = QFrame(self.frame_33)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_22.addWidget(self.label_28)

        self.ComboBox_XInterp = QComboBox(self.frame_30)
        self.ComboBox_XInterp.addItem("")
        self.ComboBox_XInterp.addItem("")
        self.ComboBox_XInterp.addItem("")
        self.ComboBox_XInterp.setObjectName(u"ComboBox_XInterp")

        self.horizontalLayout_22.addWidget(self.ComboBox_XInterp)


        self.horizontalLayout_29.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_33)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_29 = QLabel(self.frame_31)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_25.addWidget(self.label_29)

        self.ComboBox_YInterp = QComboBox(self.frame_31)
        self.ComboBox_YInterp.addItem("")
        self.ComboBox_YInterp.addItem("")
        self.ComboBox_YInterp.addItem("")
        self.ComboBox_YInterp.setObjectName(u"ComboBox_YInterp")

        self.horizontalLayout_25.addWidget(self.ComboBox_YInterp)


        self.horizontalLayout_29.addWidget(self.frame_31)


        self.verticalLayout_9.addWidget(self.frame_33)

        self.frame_24 = QFrame(self.frame_29)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_26 = QLabel(self.frame_26)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_21.addWidget(self.label_26)

        self.SpinBox_Height = QSpinBox(self.frame_26)
        self.SpinBox_Height.setObjectName(u"SpinBox_Height")
        self.SpinBox_Height.setMinimum(1)
        self.SpinBox_Height.setMaximum(2048)
        self.SpinBox_Height.setValue(100)

        self.horizontalLayout_21.addWidget(self.SpinBox_Height)


        self.horizontalLayout_28.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.frame_25)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.SpinBox_Width = QSpinBox(self.frame_25)
        self.SpinBox_Width.setObjectName(u"SpinBox_Width")
        self.SpinBox_Width.setMinimum(1)
        self.SpinBox_Width.setMaximum(2048)
        self.SpinBox_Width.setValue(100)

        self.horizontalLayout_20.addWidget(self.SpinBox_Width)


        self.horizontalLayout_28.addWidget(self.frame_25)


        self.verticalLayout_9.addWidget(self.frame_24)


        self.horizontalLayout_30.addWidget(self.frame_29)

        self.PlayerDock.setWidget(self.dockWidgetContents_4)
        SimpleFractal.addDockWidget(Qt.BottomDockWidgetArea, self.PlayerDock)
        self.CodeDock = QDockWidget(SimpleFractal)
        self.CodeDock.setObjectName(u"CodeDock")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.CodeDock.sizePolicy().hasHeightForWidth())
        self.CodeDock.setSizePolicy(sizePolicy2)
        self.CodeDock.setMinimumSize(QSize(358, 700))
        self.CodeDock.setMaximumSize(QSize(524287, 524287))
        self.CodeDock.setMouseTracking(False)
        self.CodeDock.setFeatures(QDockWidget.DockWidgetMovable)
        self.CodeDock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.dockWidgetContents_2)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_36 = QFrame(self.frame)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy3.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy3)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_36)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget = QTabWidget(self.frame_36)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setMinimumSize(QSize(300, 300))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Label_Point_Count = QLabel(self.frame_3)
        self.Label_Point_Count.setObjectName(u"Label_Point_Count")

        self.horizontalLayout.addWidget(self.Label_Point_Count)

        self.Silder_GradientFlow_PointCount = QSlider(self.frame_3)
        self.Silder_GradientFlow_PointCount.setObjectName(u"Silder_GradientFlow_PointCount")
        self.Silder_GradientFlow_PointCount.setMinimum(1)
        self.Silder_GradientFlow_PointCount.setMaximum(1000)
        self.Silder_GradientFlow_PointCount.setValue(100)
        self.Silder_GradientFlow_PointCount.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.Silder_GradientFlow_PointCount)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.Text_Label_AvgLife = QLabel(self.frame_7)
        self.Text_Label_AvgLife.setObjectName(u"Text_Label_AvgLife")

        self.horizontalLayout_5.addWidget(self.Text_Label_AvgLife)

        self.Silder_GradientFlow_AverageLife = QSlider(self.frame_7)
        self.Silder_GradientFlow_AverageLife.setObjectName(u"Silder_GradientFlow_AverageLife")
        self.Silder_GradientFlow_AverageLife.setMinimum(100)
        self.Silder_GradientFlow_AverageLife.setMaximum(30000)
        self.Silder_GradientFlow_AverageLife.setSingleStep(100)
        self.Silder_GradientFlow_AverageLife.setValue(1000)
        self.Silder_GradientFlow_AverageLife.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.Silder_GradientFlow_AverageLife)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.Text_Label_TrailLife = QLabel(self.frame_8)
        self.Text_Label_TrailLife.setObjectName(u"Text_Label_TrailLife")

        self.horizontalLayout_7.addWidget(self.Text_Label_TrailLife)

        self.Silder_GradientFlow_TrailLife = QSlider(self.frame_8)
        self.Silder_GradientFlow_TrailLife.setObjectName(u"Silder_GradientFlow_TrailLife")
        self.Silder_GradientFlow_TrailLife.setMinimum(100)
        self.Silder_GradientFlow_TrailLife.setMaximum(30000)
        self.Silder_GradientFlow_TrailLife.setSingleStep(100)
        self.Silder_GradientFlow_TrailLife.setValue(1000)
        self.Silder_GradientFlow_TrailLife.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.Silder_GradientFlow_TrailLife)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.ComboBox_GradientFlow_ColouringMethod = QComboBox(self.frame_9)
        self.ComboBox_GradientFlow_ColouringMethod.addItem("")
        self.ComboBox_GradientFlow_ColouringMethod.addItem("")
        self.ComboBox_GradientFlow_ColouringMethod.addItem("")
        self.ComboBox_GradientFlow_ColouringMethod.addItem("")
        self.ComboBox_GradientFlow_ColouringMethod.addItem("")
        self.ComboBox_GradientFlow_ColouringMethod.setObjectName(u"ComboBox_GradientFlow_ColouringMethod")
        self.ComboBox_GradientFlow_ColouringMethod.setMaxCount(10)

        self.horizontalLayout_8.addWidget(self.ComboBox_GradientFlow_ColouringMethod)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.ComboBox_GradientFlow_ColouringScheme = QComboBox(self.frame_10)
        self.ComboBox_GradientFlow_ColouringScheme.addItem("")
        self.ComboBox_GradientFlow_ColouringScheme.addItem("")
        self.ComboBox_GradientFlow_ColouringScheme.addItem("")
        self.ComboBox_GradientFlow_ColouringScheme.addItem("")
        self.ComboBox_GradientFlow_ColouringScheme.addItem("")
        self.ComboBox_GradientFlow_ColouringScheme.setObjectName(u"ComboBox_GradientFlow_ColouringScheme")

        self.horizontalLayout_6.addWidget(self.ComboBox_GradientFlow_ColouringScheme)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10)

        self.frame_15 = QFrame(self.tab_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.Label_Point_Count_2 = QLabel(self.frame_15)
        self.Label_Point_Count_2.setObjectName(u"Label_Point_Count_2")

        self.horizontalLayout_13.addWidget(self.Label_Point_Count_2)

        self.Silder_StepFlow_PointCount = QSlider(self.frame_15)
        self.Silder_StepFlow_PointCount.setObjectName(u"Silder_StepFlow_PointCount")
        self.Silder_StepFlow_PointCount.setMinimum(1)
        self.Silder_StepFlow_PointCount.setMaximum(1000)
        self.Silder_StepFlow_PointCount.setValue(100)
        self.Silder_StepFlow_PointCount.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.Silder_StepFlow_PointCount)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.Text_Label_AvgLife_2 = QLabel(self.frame_11)
        self.Text_Label_AvgLife_2.setObjectName(u"Text_Label_AvgLife_2")

        self.horizontalLayout_9.addWidget(self.Text_Label_AvgLife_2)

        self.Silder_StepFlow_AverageLife = QSlider(self.frame_11)
        self.Silder_StepFlow_AverageLife.setObjectName(u"Silder_StepFlow_AverageLife")
        self.Silder_StepFlow_AverageLife.setMinimum(100)
        self.Silder_StepFlow_AverageLife.setMaximum(30000)
        self.Silder_StepFlow_AverageLife.setSingleStep(100)
        self.Silder_StepFlow_AverageLife.setValue(1000)
        self.Silder_StepFlow_AverageLife.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.Silder_StepFlow_AverageLife)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_14 = QFrame(self.tab_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.Text_Label_TrailLife_2 = QLabel(self.frame_14)
        self.Text_Label_TrailLife_2.setObjectName(u"Text_Label_TrailLife_2")

        self.horizontalLayout_12.addWidget(self.Text_Label_TrailLife_2)

        self.Silder_StepFlow_TrailLife = QSlider(self.frame_14)
        self.Silder_StepFlow_TrailLife.setObjectName(u"Silder_StepFlow_TrailLife")
        self.Silder_StepFlow_TrailLife.setMinimum(100)
        self.Silder_StepFlow_TrailLife.setMaximum(30000)
        self.Silder_StepFlow_TrailLife.setSingleStep(100)
        self.Silder_StepFlow_TrailLife.setValue(1000)
        self.Silder_StepFlow_TrailLife.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.Silder_StepFlow_TrailLife)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.tab_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.ComboBox_StepFlow_ColouringMethod = QComboBox(self.frame_13)
        self.ComboBox_StepFlow_ColouringMethod.addItem("")
        self.ComboBox_StepFlow_ColouringMethod.addItem("")
        self.ComboBox_StepFlow_ColouringMethod.addItem("")
        self.ComboBox_StepFlow_ColouringMethod.addItem("")
        self.ComboBox_StepFlow_ColouringMethod.addItem("")
        self.ComboBox_StepFlow_ColouringMethod.setObjectName(u"ComboBox_StepFlow_ColouringMethod")
        self.ComboBox_StepFlow_ColouringMethod.setMaxCount(10)

        self.horizontalLayout_11.addWidget(self.ComboBox_StepFlow_ColouringMethod)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.ComboBox_StepFlow_ColouringScheme = QComboBox(self.frame_12)
        self.ComboBox_StepFlow_ColouringScheme.addItem("")
        self.ComboBox_StepFlow_ColouringScheme.addItem("")
        self.ComboBox_StepFlow_ColouringScheme.addItem("")
        self.ComboBox_StepFlow_ColouringScheme.addItem("")
        self.ComboBox_StepFlow_ColouringScheme.addItem("")
        self.ComboBox_StepFlow_ColouringScheme.setObjectName(u"ComboBox_StepFlow_ColouringScheme")

        self.horizontalLayout_10.addWidget(self.ComboBox_StepFlow_ColouringScheme)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.frame_16 = QFrame(self.tab_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.LineEdit_Iterated_Red = QLineEdit(self.frame_16)
        self.LineEdit_Iterated_Red.setObjectName(u"LineEdit_Iterated_Red")

        self.horizontalLayout_14.addWidget(self.LineEdit_Iterated_Red)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.tab_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.LineEdit_Iterated_Green = QLineEdit(self.frame_17)
        self.LineEdit_Iterated_Green.setObjectName(u"LineEdit_Iterated_Green")

        self.horizontalLayout_15.addWidget(self.LineEdit_Iterated_Green)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.tab_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.LineEdit_Iterated_Blue = QLineEdit(self.frame_18)
        self.LineEdit_Iterated_Blue.setObjectName(u"LineEdit_Iterated_Blue")

        self.horizontalLayout_16.addWidget(self.LineEdit_Iterated_Blue)


        self.verticalLayout_7.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.tab_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.LineEdit_Iterated_CutOff = QLineEdit(self.frame_19)
        self.LineEdit_Iterated_CutOff.setObjectName(u"LineEdit_Iterated_CutOff")

        self.horizontalLayout_17.addWidget(self.LineEdit_Iterated_CutOff)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.tab_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 10, 101, 16))
        self.spinBox = QSpinBox(self.frame_20)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(120, 10, 91, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(100)

        self.verticalLayout_7.addWidget(self.frame_20)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_12.addWidget(self.tabWidget)


        self.verticalLayout_14.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy3.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy3)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_37)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tabWidget_2 = QTabWidget(self.frame_37)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy4.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy4)
        self.tabWidget_2.setMinimumSize(QSize(300, 0))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser_3 = QTextBrowser(self.tab_4)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout.addWidget(self.textBrowser_3)

        self.frame_2 = QFrame(self.tab_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.LineEdit_Complex = QLineEdit(self.frame_2)
        self.LineEdit_Complex.setObjectName(u"LineEdit_Complex")

        self.horizontalLayout_2.addWidget(self.LineEdit_Complex)


        self.verticalLayout.addWidget(self.frame_2)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser_4 = QTextBrowser(self.tab_5)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_3.addWidget(self.textBrowser_4)

        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.LineEdit_MatrixX = QLineEdit(self.frame_4)
        self.LineEdit_MatrixX.setObjectName(u"LineEdit_MatrixX")

        self.horizontalLayout_3.addWidget(self.LineEdit_MatrixX)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.LineEdit_MatrixY = QLineEdit(self.frame_5)
        self.LineEdit_MatrixY.setObjectName(u"LineEdit_MatrixY")

        self.horizontalLayout_4.addWidget(self.LineEdit_MatrixY)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_13.addWidget(self.tabWidget_2)


        self.verticalLayout_14.addWidget(self.frame_37)


        self.verticalLayout_4.addWidget(self.frame)

        self.CodeDock.setWidget(self.dockWidgetContents_2)
        SimpleFractal.addDockWidget(Qt.TopDockWidgetArea, self.CodeDock)
        self.DispayDock = QDockWidget(SimpleFractal)
        self.DispayDock.setObjectName(u"DispayDock")
        sizePolicy2.setHeightForWidth(self.DispayDock.sizePolicy().hasHeightForWidth())
        self.DispayDock.setSizePolicy(sizePolicy2)
        self.DispayDock.setMinimumSize(QSize(700, 700))
        self.DispayDock.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.DispayDock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.horizontalLayout_24 = QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.openGLWidget = QOpenGLWidget(self.dockWidgetContents_3)
        self.openGLWidget.setObjectName(u"openGLWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(100)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy5)
        self.openGLWidget.setMinimumSize(QSize(200, 200))

        self.horizontalLayout_24.addWidget(self.openGLWidget)

        self.DispayDock.setWidget(self.dockWidgetContents_3)
        SimpleFractal.addDockWidget(Qt.TopDockWidgetArea, self.DispayDock)
        self.DispayDock.raise_()

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(SimpleFractal)

        self.tabWidget.setCurrentIndex(2)
        self.ComboBox_GradientFlow_ColouringMethod.setCurrentIndex(0)
        self.ComboBox_StepFlow_ColouringMethod.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SimpleFractal)
    # setupUi

    def retranslateUi(self, SimpleFractal):
        SimpleFractal.setWindowTitle(QCoreApplication.translate("SimpleFractal", u"SimpleFractal", None))
        self.actionSaveAs.setText(QCoreApplication.translate("SimpleFractal", u"SaveAs", None))
        self.actionSave.setText(QCoreApplication.translate("SimpleFractal", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("SimpleFractal", u"Open", None))
        self.menuFile.setTitle(QCoreApplication.translate("SimpleFractal", u"File", None))
        self.label_31.setText(QCoreApplication.translate("SimpleFractal", u"Error Log", None))
        self.TextBrowser_ErrorLog.setHtml(QCoreApplication.translate("SimpleFractal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Errors :)</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("SimpleFractal", u"Time Step (ms) : ", None))
        self.label_22.setText(QCoreApplication.translate("SimpleFractal", u"End Time (s) :", None))
        self.PushButton_PlayPause.setText(QCoreApplication.translate("SimpleFractal", u"Play/Pause", None))
        self.PushButton_Stop.setText(QCoreApplication.translate("SimpleFractal", u"Stop", None))
        self.label_23.setText(QCoreApplication.translate("SimpleFractal", u"t (s) = ", None))
        self.label_24.setText(QCoreApplication.translate("SimpleFractal", u"0.0", None))
        self.label_27.setText(QCoreApplication.translate("SimpleFractal", u"Path (x,y,zoom)", None))
        self.PlainTextEdit_Path.setPlainText(QCoreApplication.translate("SimpleFractal", u"(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)", None))
        self.label_30.setText(QCoreApplication.translate("SimpleFractal", u"zoom interp :", None))
        self.ComboBox_ZoomInterp.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Linear", None))
        self.ComboBox_ZoomInterp.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Cosine", None))
        self.ComboBox_ZoomInterp.setItemText(2, QCoreApplication.translate("SimpleFractal", u"Cubic", None))

        self.label_28.setText(QCoreApplication.translate("SimpleFractal", u"x interp :", None))
        self.ComboBox_XInterp.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Linear", None))
        self.ComboBox_XInterp.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Cosine", None))
        self.ComboBox_XInterp.setItemText(2, QCoreApplication.translate("SimpleFractal", u"Cubic", None))

        self.label_29.setText(QCoreApplication.translate("SimpleFractal", u"y interp :", None))
        self.ComboBox_YInterp.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Linear", None))
        self.ComboBox_YInterp.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Cosine", None))
        self.ComboBox_YInterp.setItemText(2, QCoreApplication.translate("SimpleFractal", u"Cubic", None))

        self.label_26.setText(QCoreApplication.translate("SimpleFractal", u"Height (px, max 2048) :", None))
        self.label_25.setText(QCoreApplication.translate("SimpleFractal", u"Width (px, max 2048) : ", None))
        self.label_3.setText(QCoreApplication.translate("SimpleFractal", u"Point Options", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("SimpleFractal", u"Number of points being rendered", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SimpleFractal", u"Point Count :", None))
        self.Label_Point_Count.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_6.setText(QCoreApplication.translate("SimpleFractal", u"Average Life (s) :", None))
        self.Text_Label_AvgLife.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_8.setText(QCoreApplication.translate("SimpleFractal", u"Trail Life (s) :", None))
        self.Text_Label_TrailLife.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_9.setText(QCoreApplication.translate("SimpleFractal", u"Colouring Method :", None))
        self.ComboBox_GradientFlow_ColouringMethod.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Velocity", None))
        self.ComboBox_GradientFlow_ColouringMethod.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Mono", None))
        self.ComboBox_GradientFlow_ColouringMethod.setItemText(2, QCoreApplication.translate("SimpleFractal", u"LifeTime", None))
        self.ComboBox_GradientFlow_ColouringMethod.setItemText(3, QCoreApplication.translate("SimpleFractal", u"Angle", None))
        self.ComboBox_GradientFlow_ColouringMethod.setItemText(4, QCoreApplication.translate("SimpleFractal", u"RAINBOW", None))

        self.ComboBox_GradientFlow_ColouringMethod.setCurrentText(QCoreApplication.translate("SimpleFractal", u"Velocity", None))
        self.label_7.setText(QCoreApplication.translate("SimpleFractal", u"Colour Scheme :", None))
        self.ComboBox_GradientFlow_ColouringScheme.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Red-Blue", None))
        self.ComboBox_GradientFlow_ColouringScheme.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Hot Rainbow", None))
        self.ComboBox_GradientFlow_ColouringScheme.setItemText(2, QCoreApplication.translate("SimpleFractal", u"Cold Rainbow", None))
        self.ComboBox_GradientFlow_ColouringScheme.setItemText(3, QCoreApplication.translate("SimpleFractal", u"Purple-Silver", None))
        self.ComboBox_GradientFlow_ColouringScheme.setItemText(4, QCoreApplication.translate("SimpleFractal", u"Blue-Gold", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SimpleFractal", u"Gradiant Flow", None))
        self.label_10.setText(QCoreApplication.translate("SimpleFractal", u"Point Options", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("SimpleFractal", u"Number of points being rendered", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("SimpleFractal", u"Point Count :", None))
        self.Label_Point_Count_2.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_11.setText(QCoreApplication.translate("SimpleFractal", u"Average Life (s) :", None))
        self.Text_Label_AvgLife_2.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_14.setText(QCoreApplication.translate("SimpleFractal", u"Trail Life (s) :", None))
        self.Text_Label_TrailLife_2.setText(QCoreApplication.translate("SimpleFractal", u"1", None))
        self.label_13.setText(QCoreApplication.translate("SimpleFractal", u"Colouring Method :", None))
        self.ComboBox_StepFlow_ColouringMethod.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Velocity", None))
        self.ComboBox_StepFlow_ColouringMethod.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Mono", None))
        self.ComboBox_StepFlow_ColouringMethod.setItemText(2, QCoreApplication.translate("SimpleFractal", u"LifeTime", None))
        self.ComboBox_StepFlow_ColouringMethod.setItemText(3, QCoreApplication.translate("SimpleFractal", u"Angle", None))
        self.ComboBox_StepFlow_ColouringMethod.setItemText(4, QCoreApplication.translate("SimpleFractal", u"RAINBOW", None))

        self.ComboBox_StepFlow_ColouringMethod.setCurrentText(QCoreApplication.translate("SimpleFractal", u"Velocity", None))
        self.label_12.setText(QCoreApplication.translate("SimpleFractal", u"Colour Scheme :", None))
        self.ComboBox_StepFlow_ColouringScheme.setItemText(0, QCoreApplication.translate("SimpleFractal", u"Red-Blue", None))
        self.ComboBox_StepFlow_ColouringScheme.setItemText(1, QCoreApplication.translate("SimpleFractal", u"Hot Rainbow", None))
        self.ComboBox_StepFlow_ColouringScheme.setItemText(2, QCoreApplication.translate("SimpleFractal", u"Cold Rainbow", None))
        self.ComboBox_StepFlow_ColouringScheme.setItemText(3, QCoreApplication.translate("SimpleFractal", u"Purple-Silver", None))
        self.ComboBox_StepFlow_ColouringScheme.setItemText(4, QCoreApplication.translate("SimpleFractal", u"Blue-Gold", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SimpleFractal", u"Step Flow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SimpleFractal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Defined Params:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ITC : The <span style=\" text-decoration: underline;\">C</span>ount of the iteration when the point became undefined (norm is larger then cuttoff, div by zero, ect...). 0 if the point never becomes undefined</p>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ITV.x/ITV.y : The previously defined <span style=\" text-decoration: underline;\">V</span>alue before the point became undefined. The final value at the end of iteration if the point never becomes undefined.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ITS : The final <span style=\" text-decoration: underline;\">S</span>tate of the point, 0 if the point became undefined, 1 if it remained defined.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MAX : The largest unsigned float64</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">t : unsigned float64 number of seconds in animation</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Note:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The colour channels are normalized on eachother, i.e, if there is a value above 1, then all channels are divided by the largest value amongst the channels. Netagtive values will be raised to zero, and undefined values will be set to zero.</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("SimpleFractal", u"Red :", None))
        self.LineEdit_Iterated_Red.setText(QCoreApplication.translate("SimpleFractal", u"ITC/100", None))
        self.label_17.setText(QCoreApplication.translate("SimpleFractal", u"Green :", None))
        self.LineEdit_Iterated_Green.setText(QCoreApplication.translate("SimpleFractal", u"100 - ITC/100", None))
        self.label_18.setText(QCoreApplication.translate("SimpleFractal", u"Blue : ", None))
        self.LineEdit_Iterated_Blue.setText(QCoreApplication.translate("SimpleFractal", u"0.5", None))
        self.label_19.setText(QCoreApplication.translate("SimpleFractal", u"Cutoff: |N| >", None))
        self.LineEdit_Iterated_CutOff.setText(QCoreApplication.translate("SimpleFractal", u"MAX", None))
        self.label_20.setText(QCoreApplication.translate("SimpleFractal", u"Max Iterations :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SimpleFractal", u"Iterated", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("SimpleFractal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Defined Params:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N : The current value.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N_n : the nth previous number, where n is an int.</p>\n"
"<p style"
                        "=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N0 : the origonal value at this point.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pi : float64 pi rounded to nearest.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e : float64 e rounded to nearest.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">t - float64 number of seconds in animation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Defined Functions:</span></p>\n"
"<p style=\" ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ : binary addition.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- : binary subtraction.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* : binary multiplication.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/ : binary divide.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">^ : binary power.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sin"
                        "( ... ) : measured in radians </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cos( ... ) : measured in radians</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">round( ... ) : round to nearest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">floor( ... ) : round down</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ceil( ... ) : round up</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n % m : modulo</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SimpleFractal", u"N_{n+1} =", None))
        self.LineEdit_Complex.setText(QCoreApplication.translate("SimpleFractal", u"N^2 + N0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("SimpleFractal", u"Complex", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("SimpleFractal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Defined Params:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N.x: The current x value.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N.y: The current y value.</p>\n"
"<p style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N_n.x : the x of the nth previous number, where n is an int.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N_n.y : the y of the nth previous number, where n is an int.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N0.x : the origonal x value at this point.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">N0.y : the origonal y value at this point.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pi : float64 pi rounded to nearest.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e : float64 e rounded to nearest.</p>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">t - float64 number of seconds in animation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Defined Functions:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ : binary addition.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- : binary subtraction.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* : binary multiplication.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/ : binary divide.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">^ : binary power.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sin( ... ) : measured in radians </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cos( ... ) : measured in radians</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">round( "
                        "... ) : round to nearest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">floor( ... ) : round down</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ceil( ... ) : round up</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n % m : modulo</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SimpleFractal", u"N_{n+1}.x =", None))
        self.LineEdit_MatrixX.setText(QCoreApplication.translate("SimpleFractal", u"N0.x + N.x^2 - N.y^2", None))
        self.label_5.setText(QCoreApplication.translate("SimpleFractal", u"N_{n+1}.y =", None))
        self.LineEdit_MatrixY.setText(QCoreApplication.translate("SimpleFractal", u"N0.y + 2 * N.x * N.y", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("SimpleFractal", u"Transformation Matrix", None))
    # retranslateUi

if __name__ == "__main__":
    Ui_SimpleFractal.exec()