# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinConfig2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
import icons_rc

class Ui_MainWidget(object):

    #Function used for Animated Slide Menu
    def moveLeftMenu(self):
        width = self.left_side_menu.width()
        if width == 0:
            #expand menu
            newWidth = 150
        else:
            #minimize menu
            newWidth = 0
        self.animation = QPropertyAnimation(self.left_side_menu,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
        
    def ShowArchivePage(self):
        self.stackedWidget.setCurrentWidget(self.ArchivePage)
        self.Pin0_5Btn.hide()
        self.Pin6_11Btn.hide()
        self.Pin12_17Btn.hide()
        self.Pin18_23Btn.hide()
        self.Pin24_28Btn.hide()
        self.Pin30_32Btn.hide()
        
    def ShowAboutPage(self):
        self.stackedWidget.setCurrentWidget(self.AboutPage)
        self.Pin0_5Btn.hide()
        self.Pin6_11Btn.hide()
        self.Pin12_17Btn.hide()
        self.Pin18_23Btn.hide()
        self.Pin24_28Btn.hide()
        self.Pin30_32Btn.hide()
            
    def ShowPortPage1(self):
        self.stackedWidget.setCurrentWidget(self.PortPage1) 
        self.Pin0_5Btn.show()
        self.Pin6_11Btn.show()
        self.Pin12_17Btn.show()
        self.Pin18_23Btn.show()
        self.Pin24_28Btn.show()
        self.Pin30_32Btn.show()        

    def ShowPortPage2(self):
        self.stackedWidget.setCurrentWidget(self.PortPage2)    

    def ShowPortPage3(self):
        self.stackedWidget.setCurrentWidget(self.PortPage3)    

    def ShowPortPage4(self):
        self.stackedWidget.setCurrentWidget(self.PortPage4) 

    def ShowPortPage5(self):
        self.stackedWidget.setCurrentWidget(self.PortPage5)

    def ShowPortPage6(self):
        self.stackedWidget.setCurrentWidget(self.PortPage6)            
        
    def DisableOutGroupBox(self):
        if self.InBtn1.isChecked() == True:
            self.OutGroupBox1.setEnabled(False)
        else:
            self.OutGroupBox1.setEnabled(True)
            
        if self.InBtn1_2.isChecked() == True:
           self.OutGroupBox1_2.setEnabled(False)
        else:
           self.OutGroupBox1_2.setEnabled(True)

        if self.InBtn1_3.isChecked() == True:
           self.OutGroupBox1_3.setEnabled(False)
        else:
           self.OutGroupBox1_3.setEnabled(True)

        if self.InBtn1_4.isChecked() == True:
           self.OutGroupBox1_4.setEnabled(False)
        else:
           self.OutGroupBox1_4.setEnabled(True)

        if self.InBtn1_5.isChecked() == True:
           self.OutGroupBox1_5.setEnabled(False)
        else:
           self.OutGroupBox1_5.setEnabled(True)

        if self.InBtn1_6.isChecked() == True:
           self.OutGroupBox1_6.setEnabled(False)
        else:
           self.OutGroupBox1_6.setEnabled(True)
           
        if self.InBtn1_7.isChecked() == True:
           self.OutGroupBox1_7.setEnabled(False)
        else:
           self.OutGroupBox1_7.setEnabled(True)

        if self.InBtn1_8.isChecked() == True:
           self.OutGroupBox1_8.setEnabled(False)
        else:
           self.OutGroupBox1_8.setEnabled(True)

        if self.InBtn1_9.isChecked() == True:
           self.OutGroupBox1_9.setEnabled(False)
        else:
           self.OutGroupBox1_9.setEnabled(True)

        if self.InBtn1_10.isChecked() == True:
           self.OutGroupBox1_10.setEnabled(False)
        else:
           self.OutGroupBox1_10.setEnabled(True)

        if self.InBtn1_11.isChecked() == True:
           self.OutGroupBox1_11.setEnabled(False)
        else:
           self.OutGroupBox1_11.setEnabled(True)

        if self.InBtn1_12.isChecked() == True:
           self.OutGroupBox1_12.setEnabled(False)
        else:
           self.OutGroupBox1_12.setEnabled(True)

        if self.InBtn1_13.isChecked() == True:
           self.OutGroupBox1_13.setEnabled(False)
        else:
           self.OutGroupBox1_13.setEnabled(True)

        if self.InBtn1_14.isChecked() == True:
           self.OutGroupBox1_14.setEnabled(False)
        else:
           self.OutGroupBox1_14.setEnabled(True)

        if self.InBtn1_15.isChecked() == True:
           self.OutGroupBox1_15.setEnabled(False)
        else:
           self.OutGroupBox1_15.setEnabled(True)

        if self.InBtn1_16.isChecked() == True:
           self.OutGroupBox1_16.setEnabled(False)
        else:
           self.OutGroupBox1_16.setEnabled(True)

        if self.InBtn1_17.isChecked() == True:
           self.OutGroupBox1_17.setEnabled(False)
        else:
           self.OutGroupBox1_17.setEnabled(True)

        if self.InBtn1_18.isChecked() == True:
           self.OutGroupBox1_18.setEnabled(False)
        else:
           self.OutGroupBox1_18.setEnabled(True)

        if self.InBtn1_19.isChecked() == True:
           self.OutGroupBox1_19.setEnabled(False)
        else:
           self.OutGroupBox1_19.setEnabled(True)

        if self.InBtn1_20.isChecked() == True:
           self.OutGroupBox1_20.setEnabled(False)
        else:
           self.OutGroupBox1_20.setEnabled(True)

        if self.InBtn1_21.isChecked() == True:
           self.OutGroupBox1_21.setEnabled(False)
        else:
           self.OutGroupBox1_21.setEnabled(True)

        if self.InBtn1_22.isChecked() == True:
           self.OutGroupBox1_22.setEnabled(False)
        else:
           self.OutGroupBox1_22.setEnabled(True)

        if self.InBtn1_23.isChecked() == True:
           self.OutGroupBox1_23.setEnabled(False)
        else:
           self.OutGroupBox1_23.setEnabled(True)

        if self.InBtn1_24.isChecked() == True:
           self.OutGroupBox1_24.setEnabled(False)
        else:
           self.OutGroupBox1_24.setEnabled(True)

        if self.InBtn1_25.isChecked() == True:
           self.OutGroupBox1_25.setEnabled(False)
        else:
           self.OutGroupBox1_25.setEnabled(True)

        if self.InBtn1_26.isChecked() == True:
           self.OutGroupBox1_26.setEnabled(False)
        else:
           self.OutGroupBox1_26.setEnabled(True)

        if self.InBtn1_27.isChecked() == True:
           self.OutGroupBox1_27.setEnabled(False)
        else:
           self.OutGroupBox1_27.setEnabled(True)

        if self.InBtn1_28.isChecked() == True:
           self.OutGroupBox1_28.setEnabled(False)
        else:
           self.OutGroupBox1_28.setEnabled(True)

        if self.InBtn1_29.isChecked() == True:
           self.OutGroupBox1_29.setEnabled(False)
        else:
           self.OutGroupBox1_29.setEnabled(True)

        if self.InBtn1_30.isChecked() == True:
           self.OutGroupBox1_30.setEnabled(False)
        else:
           self.OutGroupBox1_30.setEnabled(True)

        if self.InBtn1_31.isChecked() == True:
           self.OutGroupBox1_31.setEnabled(False)
        else:
           self.OutGroupBox1_31.setEnabled(True)

        if self.InBtn1_32.isChecked() == True:
           self.OutGroupBox1_32.setEnabled(False)
        else:
           self.OutGroupBox1_32.setEnabled(True)

    def DisableInGroupBox(self):
        if self.OutBtn1.isChecked() == True:
            self.InGroupBox1.setEnabled(False)
        else:
            self.InGroupBox1.setEnabled(True)
            
        if self.OutBtn1_2.isChecked() == True:
           self.InGroupBox1_2.setEnabled(False)
        else:
           self.InGroupBox1_2.setEnabled(True)

        if self.OutBtn1_3.isChecked() == True:
           self.InGroupBox1_3.setEnabled(False)
        else:
           self.InGroupBox1_3.setEnabled(True)

        if self.OutBtn1_4.isChecked() == True:
           self.InGroupBox1_4.setEnabled(False)
        else:
           self.InGroupBox1_4.setEnabled(True)

        if self.OutBtn1_5.isChecked() == True:
           self.InGroupBox1_5.setEnabled(False)
        else:
           self.InGroupBox1_5.setEnabled(True)

        if self.OutBtn1_6.isChecked() == True:
           self.InGroupBox1_6.setEnabled(False)
        else:
           self.InGroupBox1_6.setEnabled(True)
           
        if self.OutBtn1_7.isChecked() == True:
           self.InGroupBox1_7.setEnabled(False)
        else:
           self.InGroupBox1_7.setEnabled(True)

        if self.OutBtn1_8.isChecked() == True:
           self.InGroupBox1_8.setEnabled(False)
        else:
           self.InGroupBox1_8.setEnabled(True)

        if self.OutBtn1_9.isChecked() == True:
           self.InGroupBox1_9.setEnabled(False)
        else:
           self.InGroupBox1_9.setEnabled(True)

        if self.OutBtn1_10.isChecked() == True:
           self.InGroupBox1_10.setEnabled(False)
        else:
           self.InGroupBox1_10.setEnabled(True)

        if self.OutBtn1_11.isChecked() == True:
           self.InGroupBox1_11.setEnabled(False)
        else:
           self.InGroupBox1_11.setEnabled(True)

        if self.OutBtn1_12.isChecked() == True:
           self.InGroupBox1_12.setEnabled(False)
        else:
           self.InGroupBox1_12.setEnabled(True)

        if self.OutBtn1_13.isChecked() == True:
           self.InGroupBox1_13.setEnabled(False)
        else:
           self.InGroupBox1_13.setEnabled(True)

        if self.OutBtn1_14.isChecked() == True:
           self.InGroupBox1_14.setEnabled(False)
        else:
           self.InGroupBox1_14.setEnabled(True)

        if self.OutBtn1_15.isChecked() == True:
           self.InGroupBox1_15.setEnabled(False)
        else:
           self.InGroupBox1_15.setEnabled(True)

        if self.OutBtn1_16.isChecked() == True:
           self.InGroupBox1_16.setEnabled(False)
        else:
           self.InGroupBox1_16.setEnabled(True)

        if self.OutBtn1_17.isChecked() == True:
           self.InGroupBox1_17.setEnabled(False)
        else:
           self.InGroupBox1_17.setEnabled(True)

        if self.OutBtn1_18.isChecked() == True:
           self.InGroupBox1_18.setEnabled(False)
        else:
           self.InGroupBox1_18.setEnabled(True)

        if self.OutBtn1_19.isChecked() == True:
           self.InGroupBox1_19.setEnabled(False)
        else:
           self.InGroupBox1_19.setEnabled(True)

        if self.OutBtn1_20.isChecked() == True:
           self.InGroupBox1_20.setEnabled(False)
        else:
           self.InGroupBox1_20.setEnabled(True)

        if self.OutBtn1_21.isChecked() == True:
           self.InGroupBox1_21.setEnabled(False)
        else:
           self.InGroupBox1_21.setEnabled(True)

        if self.OutBtn1_22.isChecked() == True:
           self.InGroupBox1_22.setEnabled(False)
        else:
           self.InGroupBox1_22.setEnabled(True)

        if self.OutBtn1_23.isChecked() == True:
           self.InGroupBox1_23.setEnabled(False)
        else:
           self.InGroupBox1_23.setEnabled(True)

        if self.OutBtn1_24.isChecked() == True:
           self.InGroupBox1_24.setEnabled(False)
        else:
           self.InGroupBox1_24.setEnabled(True)

        if self.OutBtn1_25.isChecked() == True:
           self.InGroupBox1_25.setEnabled(False)
        else:
           self.InGroupBox1_25.setEnabled(True)

        if self.OutBtn1_26.isChecked() == True:
           self.InGroupBox1_26.setEnabled(False)
        else:
           self.InGroupBox1_26.setEnabled(True)

        if self.OutBtn1_27.isChecked() == True:
           self.InGroupBox1_27.setEnabled(False)
        else:
           self.InGroupBox1_27.setEnabled(True)

        if self.OutBtn1_28.isChecked() == True:
           self.InGroupBox1_28.setEnabled(False)
        else:
           self.InGroupBox1_28.setEnabled(True)

        if self.OutBtn1_29.isChecked() == True:
           self.InGroupBox1_29.setEnabled(False)
        else:
           self.InGroupBox1_29.setEnabled(True)

        if self.OutBtn1_30.isChecked() == True:
           self.InGroupBox1_30.setEnabled(False)
        else:
           self.InGroupBox1_30.setEnabled(True)

        if self.OutBtn1_31.isChecked() == True:
           self.InGroupBox1_31.setEnabled(False)
        else:
           self.InGroupBox1_31.setEnabled(True)

        if self.OutBtn1_32.isChecked() == True:
           self.InGroupBox1_32.setEnabled(False)
        else:
           self.InGroupBox1_32.setEnabled(True)
            
    def EnableLineEdit(self):
        if self.defultNameCheckBox1.isChecked() == True:
            self.lineEdit1.setEnabled(False)
        else:
            self.lineEdit1.setEnabled(True)
            
        if self.defultNameCheckBox1_2.isChecked() == True:
           self.lineEdit1_2.setEnabled(False)
        else:
           self.lineEdit1_2.setEnabled(True)

        if self.defultNameCheckBox1_3.isChecked() == True:
           self.lineEdit1_3.setEnabled(False)
        else:
           self.lineEdit1_3.setEnabled(True)

        if self.defultNameCheckBox1_4.isChecked() == True:
           self.lineEdit1_4.setEnabled(False)
        else:
           self.lineEdit1_4.setEnabled(True)

        if self.defultNameCheckBox1_5.isChecked() == True:
           self.lineEdit1_5.setEnabled(False)
        else:
           self.lineEdit1_5.setEnabled(True)

        if self.defultNameCheckBox1_6.isChecked() == True:
           self.lineEdit1_6.setEnabled(False)
        else:
           self.lineEdit1_6.setEnabled(True)
           
        if self.defultNameCheckBox1_7.isChecked() == True:
           self.lineEdit1_7.setEnabled(False)
        else:
           self.lineEdit1_7.setEnabled(True)

        if self.defultNameCheckBox1_8.isChecked() == True:
           self.lineEdit1_8.setEnabled(False)
        else:
           self.lineEdit1_8.setEnabled(True)

        if self.defultNameCheckBox1_9.isChecked() == True:
           self.lineEdit1_9.setEnabled(False)
        else:
           self.lineEdit1_9.setEnabled(True)

        if self.defultNameCheckBox1_10.isChecked() == True:
           self.lineEdit1_10.setEnabled(False)
        else:
           self.lineEdit1_10.setEnabled(True)

        if self.defultNameCheckBox1_11.isChecked() == True:
           self.lineEdit1_11.setEnabled(False)
        else:
           self.lineEdit1_11.setEnabled(True)

        if self.defultNameCheckBox1_12.isChecked() == True:
           self.lineEdit1_12.setEnabled(False)
        else:
           self.lineEdit1_12.setEnabled(True)

        if self.defultNameCheckBox1_13.isChecked() == True:
           self.lineEdit1_13.setEnabled(False)
        else:
           self.lineEdit1_13.setEnabled(True)

        if self.defultNameCheckBox1_14.isChecked() == True:
           self.lineEdit1_14.setEnabled(False)
        else:
           self.lineEdit1_14.setEnabled(True)

        if self.defultNameCheckBox1_15.isChecked() == True:
           self.lineEdit1_15.setEnabled(False)
        else:
           self.lineEdit1_15.setEnabled(True)

        if self.defultNameCheckBox1_16.isChecked() == True:
           self.lineEdit1_16.setEnabled(False)
        else:
           self.lineEdit1_16.setEnabled(True)

        if self.defultNameCheckBox1_17.isChecked() == True:
           self.lineEdit1_17.setEnabled(False)
        else:
           self.lineEdit1_17.setEnabled(True)

        if self.defultNameCheckBox1_18.isChecked() == True:
           self.lineEdit1_18.setEnabled(False)
        else:
           self.lineEdit1_18.setEnabled(True)

        if self.defultNameCheckBox1_19.isChecked() == True:
           self.lineEdit1_19.setEnabled(False)
        else:
           self.lineEdit1_19.setEnabled(True)

        if self.defultNameCheckBox1_20.isChecked() == True:
           self.lineEdit1_20.setEnabled(False)
        else:
           self.lineEdit1_20.setEnabled(True)

        if self.defultNameCheckBox1_21.isChecked() == True:
           self.lineEdit1_21.setEnabled(False)
        else:
           self.lineEdit1_21.setEnabled(True)

        if self.defultNameCheckBox1_22.isChecked() == True:
           self.lineEdit1_22.setEnabled(False)
        else:
           self.lineEdit1_22.setEnabled(True)

        if self.defultNameCheckBox1_23.isChecked() == True:
           self.lineEdit1_23.setEnabled(False)
        else:
           self.lineEdit1_23.setEnabled(True)

        if self.defultNameCheckBox1_24.isChecked() == True:
           self.lineEdit1_24.setEnabled(False)
        else:
           self.lineEdit1_24.setEnabled(True)

        if self.defultNameCheckBox1_25.isChecked() == True:
           self.lineEdit1_25.setEnabled(False)
        else:
           self.lineEdit1_25.setEnabled(True)

        if self.defultNameCheckBox1_26.isChecked() == True:
           self.lineEdit1_26.setEnabled(False)
        else:
           self.lineEdit1_26.setEnabled(True)

        if self.defultNameCheckBox1_27.isChecked() == True:
           self.lineEdit1_27.setEnabled(False)
        else:
           self.lineEdit1_27.setEnabled(True)

        if self.defultNameCheckBox1_28.isChecked() == True:
           self.lineEdit1_28.setEnabled(False)
        else:
           self.lineEdit1_28.setEnabled(True)

        if self.defultNameCheckBox1_29.isChecked() == True:
           self.lineEdit1_29.setEnabled(False)
        else:
           self.lineEdit1_29.setEnabled(True)

        if self.defultNameCheckBox1_30.isChecked() == True:
           self.lineEdit1_30.setEnabled(False)
        else:
           self.lineEdit1_30.setEnabled(True)

        if self.defultNameCheckBox1_31.isChecked() == True:
           self.lineEdit1_31.setEnabled(False)
        else:
           self.lineEdit1_31.setEnabled(True)

        if self.defultNameCheckBox1_32.isChecked() == True:
           self.lineEdit1_32.setEnabled(False)
        else:
           self.lineEdit1_32.setEnabled(True)
        
    def GenerateFile(self):
        if self.OutBtn1.isChecked() == True:
            if self.OutHighBtn1.isChecked() == True:
                Pin1Config = 'PORT_PIN_OUT_HIGH'
            else:
                Pin1Config = 'PORT_PIN_OUT_LOW'
        else:
            if self.HighImpBtn1.isChecked() == True:
                Pin1Config = 'PORT_PIN_IN_FLOATING'  
            else:
                Pin1Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_2.isChecked() == True:
           if self.OutHighBtn1_2.isChecked() == True:
               Pin2Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin2Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_2.isChecked() == True:
               Pin2Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin2Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_3.isChecked() == True:
           if self.OutHighBtn1_3.isChecked() == True:
               Pin3Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin3Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_3.isChecked() == True:
               Pin3Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin3Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_4.isChecked() == True:
           if self.OutHighBtn1_4.isChecked() == True:
               Pin4Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin4Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_4.isChecked() == True:
               Pin4Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin4Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_5.isChecked() == True:
           if self.OutHighBtn1_5.isChecked() == True:
               Pin5Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin5Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_5.isChecked() == True:
               Pin5Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin5Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_6.isChecked() == True:
           if self.OutHighBtn1_6.isChecked() == True:
               Pin6Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin6Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_6.isChecked() == True:
               Pin6Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin6Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_7.isChecked() == True:
           if self.OutHighBtn1_7.isChecked() == True:
               Pin7Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin7Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_7.isChecked() == True:
               Pin7Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin7Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_8.isChecked() == True:
           if self.OutHighBtn1_8.isChecked() == True:
               Pin8Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin8Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_8.isChecked() == True:
               Pin8Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin8Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_9.isChecked() == True:
           if self.OutHighBtn1_9.isChecked() == True:
               Pin9Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin9Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_9.isChecked() == True:
               Pin9Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin9Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_10.isChecked() == True:
           if self.OutHighBtn1_10.isChecked() == True:
               Pin10Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin10Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_10.isChecked() == True:
               Pin10Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin10Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_11.isChecked() == True:
           if self.OutHighBtn1_11.isChecked() == True:
               Pin11Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin11Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_11.isChecked() == True:
               Pin11Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin11Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_12.isChecked() == True:
           if self.OutHighBtn1_12.isChecked() == True:
               Pin12Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin12Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_12.isChecked() == True:
               Pin12Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin12Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_13.isChecked() == True:
           if self.OutHighBtn1_13.isChecked() == True:
               Pin13Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin13Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_13.isChecked() == True:
               Pin13Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin13Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_14.isChecked() == True:
           if self.OutHighBtn1_14.isChecked() == True:
               Pin14Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin14Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_14.isChecked() == True:
               Pin14Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin14Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_15.isChecked() == True:
           if self.OutHighBtn1_15.isChecked() == True:
               Pin15Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin15Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_15.isChecked() == True:
               Pin15Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin15Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_16.isChecked() == True:
           if self.OutHighBtn1_16.isChecked() == True:
               Pin16Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin16Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_16.isChecked() == True:
               Pin16Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin16Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_17.isChecked() == True:
           if self.OutHighBtn1_17.isChecked() == True:
               Pin17Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin17Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_17.isChecked() == True:
               Pin17Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin17Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_18.isChecked() == True:
           if self.OutHighBtn1_18.isChecked() == True:
               Pin18Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin18Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_18.isChecked() == True:
               Pin18Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin18Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_19.isChecked() == True:
           if self.OutHighBtn1_19.isChecked() == True:
               Pin19Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin19Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_19.isChecked() == True:
               Pin19Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin19Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_20.isChecked() == True:
           if self.OutHighBtn1_20.isChecked() == True:
               Pin20Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin20Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_20.isChecked() == True:
               Pin20Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin20Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_21.isChecked() == True:
           if self.OutHighBtn1_21.isChecked() == True:
               Pin21Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin21Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_21.isChecked() == True:
               Pin21Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin21Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_22.isChecked() == True:
           if self.OutHighBtn1_22.isChecked() == True:
               Pin22Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin22Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_22.isChecked() == True:
               Pin22Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin22Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_23.isChecked() == True:
           if self.OutHighBtn1_23.isChecked() == True:
               Pin23Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin23Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_23.isChecked() == True:
               Pin23Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin23Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_24.isChecked() == True:
           if self.OutHighBtn1_24.isChecked() == True:
               Pin24Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin24Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_24.isChecked() == True:
               Pin24Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin24Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_25.isChecked() == True:
           if self.OutHighBtn1_25.isChecked() == True:
               Pin25Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin25Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_25.isChecked() == True:
               Pin25Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin25Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_26.isChecked() == True:
           if self.OutHighBtn1_26.isChecked() == True:
               Pin26Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin26Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_26.isChecked() == True:
               Pin26Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin26Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_27.isChecked() == True:
           if self.OutHighBtn1_27.isChecked() == True:
               Pin27Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin27Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_27.isChecked() == True:
               Pin27Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin27Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_28.isChecked() == True:
           if self.OutHighBtn1_28.isChecked() == True:
               Pin28Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin28Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_28.isChecked() == True:
               Pin28Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin28Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_29.isChecked() == True:
           if self.OutHighBtn1_29.isChecked() == True:
               Pin29Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin29Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_29.isChecked() == True:
               Pin29Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin29Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_30.isChecked() == True:
           if self.OutHighBtn1_30.isChecked() == True:
               Pin30Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin30Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_30.isChecked() == True:
               Pin30Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin30Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_31.isChecked() == True:
           if self.OutHighBtn1_31.isChecked() == True:
               Pin31Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin31Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_31.isChecked() == True:
               Pin31Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin31Config = 'PORT_PIN_IN_PULLUP'
        if self.OutBtn1_32.isChecked() == True:
           if self.OutHighBtn1_32.isChecked() == True:
               Pin32Config = 'PORT_PIN_OUT_HIGH'
           else:
               Pin32Config = 'PORT_PIN_OUT_LOW'
        else:
           if self.HighImpBtn1_32.isChecked() == True:
               Pin32Config = 'PORT_PIN_IN_FLOATING'
           else:
               Pin32Config = 'PORT_PIN_IN_PULLUP'

        filePath = self.Path.text();
        print(filePath+'Port_cfg.h')
        with open(filePath+'Port_cfg.h','w') as file:
            file.writelines(["#define   PIN0             "+Pin1Config+"\n",
                             "#define   PIN1             "+Pin2Config+"\n",
                             "#define   PIN2             "+Pin3Config+"\n",
                             "#define   PIN3             "+Pin4Config+"\n",
                             "#define   PIN4             "+Pin5Config+"\n",
                             "#define   PIN5             "+Pin6Config+"\n",
                             "#define   PIN6             "+Pin7Config+"\n",
                             "#define   PIN7             "+Pin8Config+"\n",
                             "#define   PIN8             "+Pin9Config+"\n",
                             "#define   PIN9             "+Pin10Config+"\n",
                             "#define   PIN10            "+Pin11Config+"\n",
                             "#define   PIN11            "+Pin12Config+"\n",
                             "#define   PIN12            "+Pin13Config+"\n",
                             "#define   PIN13            "+Pin14Config+"\n",
                             "#define   PIN14            "+Pin15Config+"\n",
                             "#define   PIN15            "+Pin16Config+"\n",
                             "#define   PIN16            "+Pin17Config+"\n",
                             "#define   PIN17            "+Pin18Config+"\n",
                             "#define   PIN18            "+Pin19Config+"\n",
                             "#define   PIN19            "+Pin20Config+"\n",
                             "#define   PIN20            "+Pin21Config+"\n",
                             "#define   PIN21            "+Pin22Config+"\n",
                             "#define   PIN22            "+Pin23Config+"\n",
                             "#define   PIN23            "+Pin24Config+"\n",
                             "#define   PIN24            "+Pin25Config+"\n",
                             "#define   PIN25            "+Pin26Config+"\n",
                             "#define   PIN26            "+Pin27Config+"\n",
                             "#define   PIN27            "+Pin28Config+"\n",
                             "#define   PIN28            "+Pin29Config+"\n",
                             "#define   PIN29            "+Pin30Config+"\n",
                             "#define   PIN30            "+Pin31Config+"\n",
                             "#define   PIN31            "+Pin32Config+"\n"])
                             
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1200, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMaximumSize(QSize(16777215, 16777215))
        self.main_header = QFrame(MainWidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setEnabled(True)
        self.main_header.setGeometry(QRect(0, 0, 1200, 50))
        sizePolicy.setHeightForWidth(self.main_header.sizePolicy().hasHeightForWidth())
        self.main_header.setSizePolicy(sizePolicy)
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setMaximumSize(QSize(16777215, 50))
        self.title_bar_container.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.title_bar_container.setFrameShape(QFrame.NoFrame)
        self.title_bar_container.setFrameShadow(QFrame.Plain)
        self.title_bar_container.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.title_bar_container)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-bottom-color: Bold 1px  rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(50, 50))
        self.menuBtn.setMaximumSize(QSize(60, 50))
        self.menuBtn.setFocusPolicy(Qt.NoFocus)
        self.menuBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/list (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(32, 32))
        self.menuBtn.setAutoDefault(False)
        self.menuBtn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.menuBtn)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"background-color: #000;\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout_5.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.title_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        sizePolicy.setHeightForWidth(self.top_right_btns.sizePolicy().hasHeightForWidth())
        self.top_right_btns.setSizePolicy(sizePolicy)
        self.top_right_btns.setMaximumSize(QSize(100, 50))
        self.top_right_btns.setStyleSheet(u"QFrame{\n"
"	background-color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.top_right_btns.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minBtn = QPushButton(self.top_right_btns)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setMinimumSize(QSize(0, 50))
        self.minBtn.setCursor(QCursor(Qt.OpenHandCursor))
        self.minBtn.setFocusPolicy(Qt.NoFocus)
        self.minBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/icons8-minimize-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon1)
        self.minBtn.setIconSize(QSize(24, 24))
        self.minBtn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minBtn)

        self.closeBtn = QPushButton(self.top_right_btns)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(0, 50))
        self.closeBtn.setCursor(QCursor(Qt.OpenHandCursor))
        self.closeBtn.setFocusPolicy(Qt.NoFocus)
        self.closeBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/close (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(24, 24))
        self.closeBtn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.top_right_btns)

        self.main_footer = QFrame(MainWidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setGeometry(QRect(0, 570, 1200, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"background-color: #000;")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.main_body = QFrame(MainWidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setGeometry(QRect(0, 50, 1200, 520))
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"border-top-color: Bold 1px rgb(0, 0, 0);")
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(0, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"	background-color: #000;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topLeftMenuButtons = QFrame(self.left_side_menu)
        self.topLeftMenuButtons.setObjectName(u"topLeftMenuButtons")
        self.topLeftMenuButtons.setFrameShape(QFrame.StyledPanel)
        self.topLeftMenuButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topLeftMenuButtons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.HomeBtn = QPushButton(self.topLeftMenuButtons)
        self.HomeBtn.setObjectName(u"HomeBtn")
        font = QFont()
        font.setFamily(u"Gill Sans Ultra Bold Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.HomeBtn.setFont(font)
        self.HomeBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Eng. Aya Adel/Downloads/icons8-home-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon3)
        self.HomeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.HomeBtn)

        self.ArchBtn = QPushButton(self.topLeftMenuButtons)
        self.ArchBtn.setObjectName(u"ArchBtn")
        font1 = QFont()
        font1.setFamily(u"Gill Sans Ultra Bold Condensed")
        font1.setPointSize(14)
        self.ArchBtn.setFont(font1)
        self.ArchBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Eng. Aya Adel/Downloads/icons8-archive-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ArchBtn.setIcon(icon4)
        self.ArchBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.ArchBtn)


        self.verticalLayout_2.addWidget(self.topLeftMenuButtons, 0, Qt.AlignTop)

        self.minBtn_2 = QPushButton(self.left_side_menu)
        self.minBtn_2.setObjectName(u"minBtn_2")
        self.minBtn_2.setMinimumSize(QSize(0, 50))
        self.minBtn_2.setCursor(QCursor(Qt.ArrowCursor))
        self.minBtn_2.setFocusPolicy(Qt.NoFocus)
        self.minBtn_2.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/75-759623_clip-art-alien-symbol-alien-logo-png-transparent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn_2.setIcon(icon5)
        self.minBtn_2.setIconSize(QSize(150, 150))
        self.minBtn_2.setAutoDefault(False)
        self.minBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.minBtn_2)

        self.pushButton_4 = QPushButton(self.left_side_menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font2 = QFont()
        font2.setFamily(u"Gill Sans Ultra Bold Condensed")
        font2.setPointSize(18)
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.frame_2 = QFrame(self.main_body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 0, 951, 521))
        self.stackedWidget.setStyleSheet(u"QPushButton{\n"
"	padding: 10px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.EntryPage = QWidget()
        self.EntryPage.setObjectName(u"EntryPage")
        self.label = QLabel(self.EntryPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 10, 400, 500))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/75-759623_clip-art-alien-symbol-alien-logo-png-transparent.png"))
        self.label.setScaledContents(True)
        self.stackedWidget.addWidget(self.EntryPage)
        self.PortPage1 = QWidget()
        self.PortPage1.setObjectName(u"PortPage1")
        self.label_6 = QLabel(self.PortPage1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 261, 61))
        font3 = QFont()
        font3.setFamily(u"Broadway")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setWordWrap(True)
        self.pinGroupBox1 = QGroupBox(self.PortPage1)
        self.pinGroupBox1.setObjectName(u"pinGroupBox1")
        self.pinGroupBox1.setGeometry(QRect(20, 90, 291, 181))
        font4 = QFont()
        font4.setFamily(u"Gill Sans Ultra Bold")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.pinGroupBox1.setFont(font4)
        self.pinGroupBox1.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1 = QRadioButton(self.pinGroupBox1)
        self.OutBtn1.setObjectName(u"OutBtn1")
        self.OutBtn1.setGeometry(QRect(10, 20, 82, 17))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.OutBtn1.setFont(font5)
        self.OutBtn1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1 = QRadioButton(self.pinGroupBox1)
        self.InBtn1.setObjectName(u"InBtn1")
        self.InBtn1.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1 = QGroupBox(self.pinGroupBox1)
        self.OutGroupBox1.setObjectName(u"OutGroupBox1")
        self.OutGroupBox1.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1 = QRadioButton(self.OutGroupBox1)
        self.OutHighBtn1.setObjectName(u"OutHighBtn1")
        self.OutHighBtn1.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1 = QRadioButton(self.OutGroupBox1)
        self.OutLowBtn1.setObjectName(u"OutLowBtn1")
        self.OutLowBtn1.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1 = QGroupBox(self.pinGroupBox1)
        self.InGroupBox1.setObjectName(u"InGroupBox1")
        self.InGroupBox1.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1 = QRadioButton(self.InGroupBox1)
        self.HighImpBtn1.setObjectName(u"HighImpBtn1")
        self.HighImpBtn1.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1 = QRadioButton(self.InGroupBox1)
        self.PullUpBtn1.setObjectName(u"PullUpBtn1")
        self.PullUpBtn1.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1 = QLabel(self.pinGroupBox1)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(10, 80, 81, 20))
        self.label1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1 = QLineEdit(self.pinGroupBox1)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1 = QCheckBox(self.pinGroupBox1)
        self.defultNameCheckBox1.setObjectName(u"defultNameCheckBox1")
        self.defultNameCheckBox1.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_2 = QGroupBox(self.PortPage1)
        self.pinGroupBox1_2.setObjectName(u"pinGroupBox1_2")
        self.pinGroupBox1_2.setGeometry(QRect(320, 90, 291, 181))
        self.pinGroupBox1_2.setFont(font4)
        self.pinGroupBox1_2.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_2 = QRadioButton(self.pinGroupBox1_2)
        self.OutBtn1_2.setObjectName(u"OutBtn1_2")
        self.OutBtn1_2.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_2.setFont(font5)
        self.OutBtn1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_2 = QRadioButton(self.pinGroupBox1_2)
        self.InBtn1_2.setObjectName(u"InBtn1_2")
        self.InBtn1_2.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_2 = QGroupBox(self.pinGroupBox1_2)
        self.OutGroupBox1_2.setObjectName(u"OutGroupBox1_2")
        self.OutGroupBox1_2.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_2.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_2 = QRadioButton(self.OutGroupBox1_2)
        self.OutHighBtn1_2.setObjectName(u"OutHighBtn1_2")
        self.OutHighBtn1_2.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_2 = QRadioButton(self.OutGroupBox1_2)
        self.OutLowBtn1_2.setObjectName(u"OutLowBtn1_2")
        self.OutLowBtn1_2.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_2.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_2 = QGroupBox(self.pinGroupBox1_2)
        self.InGroupBox1_2.setObjectName(u"InGroupBox1_2")
        self.InGroupBox1_2.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_2.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_2 = QRadioButton(self.InGroupBox1_2)
        self.HighImpBtn1_2.setObjectName(u"HighImpBtn1_2")
        self.HighImpBtn1_2.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_2 = QRadioButton(self.InGroupBox1_2)
        self.PullUpBtn1_2.setObjectName(u"PullUpBtn1_2")
        self.PullUpBtn1_2.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_2 = QLabel(self.pinGroupBox1_2)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setGeometry(QRect(10, 80, 81, 20))
        self.label1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_2 = QLineEdit(self.pinGroupBox1_2)
        self.lineEdit1_2.setObjectName(u"lineEdit1_2")
        self.lineEdit1_2.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_2.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_2 = QCheckBox(self.pinGroupBox1_2)
        self.defultNameCheckBox1_2.setObjectName(u"defultNameCheckBox1_2")
        self.defultNameCheckBox1_2.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_2.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_3 = QGroupBox(self.PortPage1)
        self.pinGroupBox1_3.setObjectName(u"pinGroupBox1_3")
        self.pinGroupBox1_3.setGeometry(QRect(620, 90, 291, 181))
        self.pinGroupBox1_3.setFont(font4)
        self.pinGroupBox1_3.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_3 = QRadioButton(self.pinGroupBox1_3)
        self.OutBtn1_3.setObjectName(u"OutBtn1_3")
        self.OutBtn1_3.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_3.setFont(font5)
        self.OutBtn1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_3 = QRadioButton(self.pinGroupBox1_3)
        self.InBtn1_3.setObjectName(u"InBtn1_3")
        self.InBtn1_3.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_3 = QGroupBox(self.pinGroupBox1_3)
        self.OutGroupBox1_3.setObjectName(u"OutGroupBox1_3")
        self.OutGroupBox1_3.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_3.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_3 = QRadioButton(self.OutGroupBox1_3)
        self.OutHighBtn1_3.setObjectName(u"OutHighBtn1_3")
        self.OutHighBtn1_3.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_3 = QRadioButton(self.OutGroupBox1_3)
        self.OutLowBtn1_3.setObjectName(u"OutLowBtn1_3")
        self.OutLowBtn1_3.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_3.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_3 = QGroupBox(self.pinGroupBox1_3)
        self.InGroupBox1_3.setObjectName(u"InGroupBox1_3")
        self.InGroupBox1_3.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_3.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_3 = QRadioButton(self.InGroupBox1_3)
        self.HighImpBtn1_3.setObjectName(u"HighImpBtn1_3")
        self.HighImpBtn1_3.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_3 = QRadioButton(self.InGroupBox1_3)
        self.PullUpBtn1_3.setObjectName(u"PullUpBtn1_3")
        self.PullUpBtn1_3.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_3 = QLabel(self.pinGroupBox1_3)
        self.label1_3.setObjectName(u"label1_3")
        self.label1_3.setGeometry(QRect(10, 80, 81, 20))
        self.label1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_3 = QLineEdit(self.pinGroupBox1_3)
        self.lineEdit1_3.setObjectName(u"lineEdit1_3")
        self.lineEdit1_3.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_3.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_3 = QCheckBox(self.pinGroupBox1_3)
        self.defultNameCheckBox1_3.setObjectName(u"defultNameCheckBox1_3")
        self.defultNameCheckBox1_3.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_3.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_4 = QGroupBox(self.PortPage1)
        self.pinGroupBox1_4.setObjectName(u"pinGroupBox1_4")
        self.pinGroupBox1_4.setGeometry(QRect(20, 280, 291, 181))
        self.pinGroupBox1_4.setFont(font4)
        self.pinGroupBox1_4.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_4 = QRadioButton(self.pinGroupBox1_4)
        self.OutBtn1_4.setObjectName(u"OutBtn1_4")
        self.OutBtn1_4.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_4.setFont(font5)
        self.OutBtn1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_4 = QRadioButton(self.pinGroupBox1_4)
        self.InBtn1_4.setObjectName(u"InBtn1_4")
        self.InBtn1_4.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_4 = QGroupBox(self.pinGroupBox1_4)
        self.OutGroupBox1_4.setObjectName(u"OutGroupBox1_4")
        self.OutGroupBox1_4.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_4.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_4 = QRadioButton(self.OutGroupBox1_4)
        self.OutHighBtn1_4.setObjectName(u"OutHighBtn1_4")
        self.OutHighBtn1_4.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_4 = QRadioButton(self.OutGroupBox1_4)
        self.OutLowBtn1_4.setObjectName(u"OutLowBtn1_4")
        self.OutLowBtn1_4.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_4.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_4 = QGroupBox(self.pinGroupBox1_4)
        self.InGroupBox1_4.setObjectName(u"InGroupBox1_4")
        self.InGroupBox1_4.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_4.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_4 = QRadioButton(self.InGroupBox1_4)
        self.HighImpBtn1_4.setObjectName(u"HighImpBtn1_4")
        self.HighImpBtn1_4.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_4 = QRadioButton(self.InGroupBox1_4)
        self.PullUpBtn1_4.setObjectName(u"PullUpBtn1_4")
        self.PullUpBtn1_4.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_4 = QLabel(self.pinGroupBox1_4)
        self.label1_4.setObjectName(u"label1_4")
        self.label1_4.setGeometry(QRect(10, 80, 81, 20))
        self.label1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_4 = QLineEdit(self.pinGroupBox1_4)
        self.lineEdit1_4.setObjectName(u"lineEdit1_4")
        self.lineEdit1_4.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_4.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_4 = QCheckBox(self.pinGroupBox1_4)
        self.defultNameCheckBox1_4.setObjectName(u"defultNameCheckBox1_4")
        self.defultNameCheckBox1_4.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_4.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_5 = QGroupBox(self.PortPage1)
        self.pinGroupBox1_5.setObjectName(u"pinGroupBox1_5")
        self.pinGroupBox1_5.setGeometry(QRect(320, 280, 291, 181))
        self.pinGroupBox1_5.setFont(font4)
        self.pinGroupBox1_5.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_5 = QRadioButton(self.pinGroupBox1_5)
        self.OutBtn1_5.setObjectName(u"OutBtn1_5")
        self.OutBtn1_5.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_5.setFont(font5)
        self.OutBtn1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_5 = QRadioButton(self.pinGroupBox1_5)
        self.InBtn1_5.setObjectName(u"InBtn1_5")
        self.InBtn1_5.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_5 = QGroupBox(self.pinGroupBox1_5)
        self.OutGroupBox1_5.setObjectName(u"OutGroupBox1_5")
        self.OutGroupBox1_5.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_5.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_5 = QRadioButton(self.OutGroupBox1_5)
        self.OutHighBtn1_5.setObjectName(u"OutHighBtn1_5")
        self.OutHighBtn1_5.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_5 = QRadioButton(self.OutGroupBox1_5)
        self.OutLowBtn1_5.setObjectName(u"OutLowBtn1_5")
        self.OutLowBtn1_5.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_5.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_5 = QGroupBox(self.pinGroupBox1_5)
        self.InGroupBox1_5.setObjectName(u"InGroupBox1_5")
        self.InGroupBox1_5.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_5.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_5 = QRadioButton(self.InGroupBox1_5)
        self.HighImpBtn1_5.setObjectName(u"HighImpBtn1_5")
        self.HighImpBtn1_5.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_5 = QRadioButton(self.InGroupBox1_5)
        self.PullUpBtn1_5.setObjectName(u"PullUpBtn1_5")
        self.PullUpBtn1_5.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_5 = QLabel(self.pinGroupBox1_5)
        self.label1_5.setObjectName(u"label1_5")
        self.label1_5.setGeometry(QRect(10, 80, 81, 20))
        self.label1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_5 = QLineEdit(self.pinGroupBox1_5)
        self.lineEdit1_5.setObjectName(u"lineEdit1_5")
        self.lineEdit1_5.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_5.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_5 = QCheckBox(self.pinGroupBox1_5)
        self.defultNameCheckBox1_5.setObjectName(u"defultNameCheckBox1_5")
        self.defultNameCheckBox1_5.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_5.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_6 = QGroupBox(self.PortPage1)
        self.pinGroupBox1_6.setObjectName(u"pinGroupBox1_6")
        self.pinGroupBox1_6.setGeometry(QRect(620, 280, 291, 181))
        self.pinGroupBox1_6.setFont(font4)
        self.pinGroupBox1_6.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_6 = QRadioButton(self.pinGroupBox1_6)
        self.OutBtn1_6.setObjectName(u"OutBtn1_6")
        self.OutBtn1_6.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_6.setFont(font5)
        self.OutBtn1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_6 = QRadioButton(self.pinGroupBox1_6)
        self.InBtn1_6.setObjectName(u"InBtn1_6")
        self.InBtn1_6.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_6 = QGroupBox(self.pinGroupBox1_6)
        self.OutGroupBox1_6.setObjectName(u"OutGroupBox1_6")
        self.OutGroupBox1_6.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_6.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_6 = QRadioButton(self.OutGroupBox1_6)
        self.OutHighBtn1_6.setObjectName(u"OutHighBtn1_6")
        self.OutHighBtn1_6.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_6 = QRadioButton(self.OutGroupBox1_6)
        self.OutLowBtn1_6.setObjectName(u"OutLowBtn1_6")
        self.OutLowBtn1_6.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_6.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_6 = QGroupBox(self.pinGroupBox1_6)
        self.InGroupBox1_6.setObjectName(u"InGroupBox1_6")
        self.InGroupBox1_6.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_6.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_6 = QRadioButton(self.InGroupBox1_6)
        self.HighImpBtn1_6.setObjectName(u"HighImpBtn1_6")
        self.HighImpBtn1_6.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_6 = QRadioButton(self.InGroupBox1_6)
        self.PullUpBtn1_6.setObjectName(u"PullUpBtn1_6")
        self.PullUpBtn1_6.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_6 = QLabel(self.pinGroupBox1_6)
        self.label1_6.setObjectName(u"label1_6")
        self.label1_6.setGeometry(QRect(10, 80, 81, 20))
        self.label1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_6 = QLineEdit(self.pinGroupBox1_6)
        self.lineEdit1_6.setObjectName(u"lineEdit1_6")
        self.lineEdit1_6.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_6.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_6 = QCheckBox(self.pinGroupBox1_6)
        self.defultNameCheckBox1_6.setObjectName(u"defultNameCheckBox1_6")
        self.defultNameCheckBox1_6.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_6.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.PortPage1)
        self.PortPage2 = QWidget()
        self.PortPage2.setObjectName(u"PortPage2")
        self.label_21 = QLabel(self.PortPage2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 20, 261, 61))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21.setWordWrap(True)
        self.pinGroupBox1_7 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_7.setObjectName(u"pinGroupBox1_7")
        self.pinGroupBox1_7.setGeometry(QRect(20, 90, 291, 181))
        self.pinGroupBox1_7.setFont(font4)
        self.pinGroupBox1_7.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_7 = QRadioButton(self.pinGroupBox1_7)
        self.OutBtn1_7.setObjectName(u"OutBtn1_7")
        self.OutBtn1_7.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_7.setFont(font5)
        self.OutBtn1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_7 = QRadioButton(self.pinGroupBox1_7)
        self.InBtn1_7.setObjectName(u"InBtn1_7")
        self.InBtn1_7.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_7 = QGroupBox(self.pinGroupBox1_7)
        self.OutGroupBox1_7.setObjectName(u"OutGroupBox1_7")
        self.OutGroupBox1_7.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_7.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_7 = QRadioButton(self.OutGroupBox1_7)
        self.OutHighBtn1_7.setObjectName(u"OutHighBtn1_7")
        self.OutHighBtn1_7.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_7 = QRadioButton(self.OutGroupBox1_7)
        self.OutLowBtn1_7.setObjectName(u"OutLowBtn1_7")
        self.OutLowBtn1_7.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_7.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_7 = QGroupBox(self.pinGroupBox1_7)
        self.InGroupBox1_7.setObjectName(u"InGroupBox1_7")
        self.InGroupBox1_7.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_7.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_7 = QRadioButton(self.InGroupBox1_7)
        self.HighImpBtn1_7.setObjectName(u"HighImpBtn1_7")
        self.HighImpBtn1_7.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_7 = QRadioButton(self.InGroupBox1_7)
        self.PullUpBtn1_7.setObjectName(u"PullUpBtn1_7")
        self.PullUpBtn1_7.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_7 = QLabel(self.pinGroupBox1_7)
        self.label1_7.setObjectName(u"label1_7")
        self.label1_7.setGeometry(QRect(10, 80, 81, 20))
        self.label1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_7 = QLineEdit(self.pinGroupBox1_7)
        self.lineEdit1_7.setObjectName(u"lineEdit1_7")
        self.lineEdit1_7.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_7.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_7 = QCheckBox(self.pinGroupBox1_7)
        self.defultNameCheckBox1_7.setObjectName(u"defultNameCheckBox1_7")
        self.defultNameCheckBox1_7.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_7.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_8 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_8.setObjectName(u"pinGroupBox1_8")
        self.pinGroupBox1_8.setGeometry(QRect(320, 90, 291, 181))
        self.pinGroupBox1_8.setFont(font4)
        self.pinGroupBox1_8.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_8 = QRadioButton(self.pinGroupBox1_8)
        self.OutBtn1_8.setObjectName(u"OutBtn1_8")
        self.OutBtn1_8.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_8.setFont(font5)
        self.OutBtn1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_8 = QRadioButton(self.pinGroupBox1_8)
        self.InBtn1_8.setObjectName(u"InBtn1_8")
        self.InBtn1_8.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_8 = QGroupBox(self.pinGroupBox1_8)
        self.OutGroupBox1_8.setObjectName(u"OutGroupBox1_8")
        self.OutGroupBox1_8.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_8.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_8 = QRadioButton(self.OutGroupBox1_8)
        self.OutHighBtn1_8.setObjectName(u"OutHighBtn1_8")
        self.OutHighBtn1_8.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_8 = QRadioButton(self.OutGroupBox1_8)
        self.OutLowBtn1_8.setObjectName(u"OutLowBtn1_8")
        self.OutLowBtn1_8.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_8.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_8 = QGroupBox(self.pinGroupBox1_8)
        self.InGroupBox1_8.setObjectName(u"InGroupBox1_8")
        self.InGroupBox1_8.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_8.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_8 = QRadioButton(self.InGroupBox1_8)
        self.HighImpBtn1_8.setObjectName(u"HighImpBtn1_8")
        self.HighImpBtn1_8.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_8 = QRadioButton(self.InGroupBox1_8)
        self.PullUpBtn1_8.setObjectName(u"PullUpBtn1_8")
        self.PullUpBtn1_8.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_8 = QLabel(self.pinGroupBox1_8)
        self.label1_8.setObjectName(u"label1_8")
        self.label1_8.setGeometry(QRect(10, 80, 81, 20))
        self.label1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_8 = QLineEdit(self.pinGroupBox1_8)
        self.lineEdit1_8.setObjectName(u"lineEdit1_8")
        self.lineEdit1_8.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_8.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_8 = QCheckBox(self.pinGroupBox1_8)
        self.defultNameCheckBox1_8.setObjectName(u"defultNameCheckBox1_8")
        self.defultNameCheckBox1_8.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_8.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_9 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_9.setObjectName(u"pinGroupBox1_9")
        self.pinGroupBox1_9.setGeometry(QRect(620, 90, 291, 181))
        self.pinGroupBox1_9.setFont(font4)
        self.pinGroupBox1_9.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_9 = QRadioButton(self.pinGroupBox1_9)
        self.OutBtn1_9.setObjectName(u"OutBtn1_9")
        self.OutBtn1_9.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_9.setFont(font5)
        self.OutBtn1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_9 = QRadioButton(self.pinGroupBox1_9)
        self.InBtn1_9.setObjectName(u"InBtn1_9")
        self.InBtn1_9.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_9 = QGroupBox(self.pinGroupBox1_9)
        self.OutGroupBox1_9.setObjectName(u"OutGroupBox1_9")
        self.OutGroupBox1_9.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_9.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_9 = QRadioButton(self.OutGroupBox1_9)
        self.OutHighBtn1_9.setObjectName(u"OutHighBtn1_9")
        self.OutHighBtn1_9.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_9 = QRadioButton(self.OutGroupBox1_9)
        self.OutLowBtn1_9.setObjectName(u"OutLowBtn1_9")
        self.OutLowBtn1_9.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_9.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_9 = QGroupBox(self.pinGroupBox1_9)
        self.InGroupBox1_9.setObjectName(u"InGroupBox1_9")
        self.InGroupBox1_9.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_9.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_9 = QRadioButton(self.InGroupBox1_9)
        self.HighImpBtn1_9.setObjectName(u"HighImpBtn1_9")
        self.HighImpBtn1_9.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_9 = QRadioButton(self.InGroupBox1_9)
        self.PullUpBtn1_9.setObjectName(u"PullUpBtn1_9")
        self.PullUpBtn1_9.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_9 = QLabel(self.pinGroupBox1_9)
        self.label1_9.setObjectName(u"label1_9")
        self.label1_9.setGeometry(QRect(10, 80, 81, 20))
        self.label1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_9 = QLineEdit(self.pinGroupBox1_9)
        self.lineEdit1_9.setObjectName(u"lineEdit1_9")
        self.lineEdit1_9.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_9.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_9 = QCheckBox(self.pinGroupBox1_9)
        self.defultNameCheckBox1_9.setObjectName(u"defultNameCheckBox1_9")
        self.defultNameCheckBox1_9.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_9.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_10 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_10.setObjectName(u"pinGroupBox1_10")
        self.pinGroupBox1_10.setGeometry(QRect(20, 280, 291, 181))
        self.pinGroupBox1_10.setFont(font4)
        self.pinGroupBox1_10.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_10 = QRadioButton(self.pinGroupBox1_10)
        self.OutBtn1_10.setObjectName(u"OutBtn1_10")
        self.OutBtn1_10.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_10.setFont(font5)
        self.OutBtn1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_10 = QRadioButton(self.pinGroupBox1_10)
        self.InBtn1_10.setObjectName(u"InBtn1_10")
        self.InBtn1_10.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_10 = QGroupBox(self.pinGroupBox1_10)
        self.OutGroupBox1_10.setObjectName(u"OutGroupBox1_10")
        self.OutGroupBox1_10.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_10.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_10 = QRadioButton(self.OutGroupBox1_10)
        self.OutHighBtn1_10.setObjectName(u"OutHighBtn1_10")
        self.OutHighBtn1_10.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_10 = QRadioButton(self.OutGroupBox1_10)
        self.OutLowBtn1_10.setObjectName(u"OutLowBtn1_10")
        self.OutLowBtn1_10.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_10.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_10 = QGroupBox(self.pinGroupBox1_10)
        self.InGroupBox1_10.setObjectName(u"InGroupBox1_10")
        self.InGroupBox1_10.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_10.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_10 = QRadioButton(self.InGroupBox1_10)
        self.HighImpBtn1_10.setObjectName(u"HighImpBtn1_10")
        self.HighImpBtn1_10.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_10 = QRadioButton(self.InGroupBox1_10)
        self.PullUpBtn1_10.setObjectName(u"PullUpBtn1_10")
        self.PullUpBtn1_10.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_10 = QLabel(self.pinGroupBox1_10)
        self.label1_10.setObjectName(u"label1_10")
        self.label1_10.setGeometry(QRect(10, 80, 81, 20))
        self.label1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_10 = QLineEdit(self.pinGroupBox1_10)
        self.lineEdit1_10.setObjectName(u"lineEdit1_10")
        self.lineEdit1_10.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_10.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_10 = QCheckBox(self.pinGroupBox1_10)
        self.defultNameCheckBox1_10.setObjectName(u"defultNameCheckBox1_10")
        self.defultNameCheckBox1_10.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_10.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_11 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_11.setObjectName(u"pinGroupBox1_11")
        self.pinGroupBox1_11.setGeometry(QRect(320, 280, 291, 181))
        self.pinGroupBox1_11.setFont(font4)
        self.pinGroupBox1_11.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_11 = QRadioButton(self.pinGroupBox1_11)
        self.OutBtn1_11.setObjectName(u"OutBtn1_11")
        self.OutBtn1_11.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_11.setFont(font5)
        self.OutBtn1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_11 = QRadioButton(self.pinGroupBox1_11)
        self.InBtn1_11.setObjectName(u"InBtn1_11")
        self.InBtn1_11.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_11 = QGroupBox(self.pinGroupBox1_11)
        self.OutGroupBox1_11.setObjectName(u"OutGroupBox1_11")
        self.OutGroupBox1_11.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_11.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_11 = QRadioButton(self.OutGroupBox1_11)
        self.OutHighBtn1_11.setObjectName(u"OutHighBtn1_11")
        self.OutHighBtn1_11.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_11 = QRadioButton(self.OutGroupBox1_11)
        self.OutLowBtn1_11.setObjectName(u"OutLowBtn1_11")
        self.OutLowBtn1_11.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_11.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_11 = QGroupBox(self.pinGroupBox1_11)
        self.InGroupBox1_11.setObjectName(u"InGroupBox1_11")
        self.InGroupBox1_11.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_11.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_11 = QRadioButton(self.InGroupBox1_11)
        self.HighImpBtn1_11.setObjectName(u"HighImpBtn1_11")
        self.HighImpBtn1_11.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_11 = QRadioButton(self.InGroupBox1_11)
        self.PullUpBtn1_11.setObjectName(u"PullUpBtn1_11")
        self.PullUpBtn1_11.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_11 = QLabel(self.pinGroupBox1_11)
        self.label1_11.setObjectName(u"label1_11")
        self.label1_11.setGeometry(QRect(10, 80, 81, 20))
        self.label1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_11 = QLineEdit(self.pinGroupBox1_11)
        self.lineEdit1_11.setObjectName(u"lineEdit1_11")
        self.lineEdit1_11.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_11.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_11 = QCheckBox(self.pinGroupBox1_11)
        self.defultNameCheckBox1_11.setObjectName(u"defultNameCheckBox1_11")
        self.defultNameCheckBox1_11.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_11.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_12 = QGroupBox(self.PortPage2)
        self.pinGroupBox1_12.setObjectName(u"pinGroupBox1_12")
        self.pinGroupBox1_12.setGeometry(QRect(620, 280, 291, 181))
        self.pinGroupBox1_12.setFont(font4)
        self.pinGroupBox1_12.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_12 = QRadioButton(self.pinGroupBox1_12)
        self.OutBtn1_12.setObjectName(u"OutBtn1_12")
        self.OutBtn1_12.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_12.setFont(font5)
        self.OutBtn1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_12 = QRadioButton(self.pinGroupBox1_12)
        self.InBtn1_12.setObjectName(u"InBtn1_12")
        self.InBtn1_12.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_12 = QGroupBox(self.pinGroupBox1_12)
        self.OutGroupBox1_12.setObjectName(u"OutGroupBox1_12")
        self.OutGroupBox1_12.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_12.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_12 = QRadioButton(self.OutGroupBox1_12)
        self.OutHighBtn1_12.setObjectName(u"OutHighBtn1_12")
        self.OutHighBtn1_12.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_12 = QRadioButton(self.OutGroupBox1_12)
        self.OutLowBtn1_12.setObjectName(u"OutLowBtn1_12")
        self.OutLowBtn1_12.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_12.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_12 = QGroupBox(self.pinGroupBox1_12)
        self.InGroupBox1_12.setObjectName(u"InGroupBox1_12")
        self.InGroupBox1_12.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_12.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_12 = QRadioButton(self.InGroupBox1_12)
        self.HighImpBtn1_12.setObjectName(u"HighImpBtn1_12")
        self.HighImpBtn1_12.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_12 = QRadioButton(self.InGroupBox1_12)
        self.PullUpBtn1_12.setObjectName(u"PullUpBtn1_12")
        self.PullUpBtn1_12.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_12 = QLabel(self.pinGroupBox1_12)
        self.label1_12.setObjectName(u"label1_12")
        self.label1_12.setGeometry(QRect(10, 80, 81, 20))
        self.label1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_12 = QLineEdit(self.pinGroupBox1_12)
        self.lineEdit1_12.setObjectName(u"lineEdit1_12")
        self.lineEdit1_12.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_12.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_12 = QCheckBox(self.pinGroupBox1_12)
        self.defultNameCheckBox1_12.setObjectName(u"defultNameCheckBox1_12")
        self.defultNameCheckBox1_12.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_12.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.PortPage2)
        self.PortPage3 = QWidget()
        self.PortPage3.setObjectName(u"PortPage3")
        self.pinGroupBox1_13 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_13.setObjectName(u"pinGroupBox1_13")
        self.pinGroupBox1_13.setGeometry(QRect(20, 90, 291, 181))
        self.pinGroupBox1_13.setFont(font4)
        self.pinGroupBox1_13.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_13 = QRadioButton(self.pinGroupBox1_13)
        self.OutBtn1_13.setObjectName(u"OutBtn1_13")
        self.OutBtn1_13.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_13.setFont(font5)
        self.OutBtn1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_13 = QRadioButton(self.pinGroupBox1_13)
        self.InBtn1_13.setObjectName(u"InBtn1_13")
        self.InBtn1_13.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_13 = QGroupBox(self.pinGroupBox1_13)
        self.OutGroupBox1_13.setObjectName(u"OutGroupBox1_13")
        self.OutGroupBox1_13.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_13.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_13 = QRadioButton(self.OutGroupBox1_13)
        self.OutHighBtn1_13.setObjectName(u"OutHighBtn1_13")
        self.OutHighBtn1_13.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_13 = QRadioButton(self.OutGroupBox1_13)
        self.OutLowBtn1_13.setObjectName(u"OutLowBtn1_13")
        self.OutLowBtn1_13.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_13.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_13 = QGroupBox(self.pinGroupBox1_13)
        self.InGroupBox1_13.setObjectName(u"InGroupBox1_13")
        self.InGroupBox1_13.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_13.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_13 = QRadioButton(self.InGroupBox1_13)
        self.HighImpBtn1_13.setObjectName(u"HighImpBtn1_13")
        self.HighImpBtn1_13.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_13 = QRadioButton(self.InGroupBox1_13)
        self.PullUpBtn1_13.setObjectName(u"PullUpBtn1_13")
        self.PullUpBtn1_13.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_13 = QLabel(self.pinGroupBox1_13)
        self.label1_13.setObjectName(u"label1_13")
        self.label1_13.setGeometry(QRect(10, 80, 81, 20))
        self.label1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_13 = QLineEdit(self.pinGroupBox1_13)
        self.lineEdit1_13.setObjectName(u"lineEdit1_13")
        self.lineEdit1_13.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_13.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_13 = QCheckBox(self.pinGroupBox1_13)
        self.defultNameCheckBox1_13.setObjectName(u"defultNameCheckBox1_13")
        self.defultNameCheckBox1_13.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_13.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_14 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_14.setObjectName(u"pinGroupBox1_14")
        self.pinGroupBox1_14.setGeometry(QRect(320, 90, 291, 181))
        self.pinGroupBox1_14.setFont(font4)
        self.pinGroupBox1_14.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_14 = QRadioButton(self.pinGroupBox1_14)
        self.OutBtn1_14.setObjectName(u"OutBtn1_14")
        self.OutBtn1_14.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_14.setFont(font5)
        self.OutBtn1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_14 = QRadioButton(self.pinGroupBox1_14)
        self.InBtn1_14.setObjectName(u"InBtn1_14")
        self.InBtn1_14.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_14 = QGroupBox(self.pinGroupBox1_14)
        self.OutGroupBox1_14.setObjectName(u"OutGroupBox1_14")
        self.OutGroupBox1_14.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_14.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_14 = QRadioButton(self.OutGroupBox1_14)
        self.OutHighBtn1_14.setObjectName(u"OutHighBtn1_14")
        self.OutHighBtn1_14.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_14 = QRadioButton(self.OutGroupBox1_14)
        self.OutLowBtn1_14.setObjectName(u"OutLowBtn1_14")
        self.OutLowBtn1_14.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_14.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_14 = QGroupBox(self.pinGroupBox1_14)
        self.InGroupBox1_14.setObjectName(u"InGroupBox1_14")
        self.InGroupBox1_14.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_14.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_14 = QRadioButton(self.InGroupBox1_14)
        self.HighImpBtn1_14.setObjectName(u"HighImpBtn1_14")
        self.HighImpBtn1_14.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_14 = QRadioButton(self.InGroupBox1_14)
        self.PullUpBtn1_14.setObjectName(u"PullUpBtn1_14")
        self.PullUpBtn1_14.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_14 = QLabel(self.pinGroupBox1_14)
        self.label1_14.setObjectName(u"label1_14")
        self.label1_14.setGeometry(QRect(10, 80, 81, 20))
        self.label1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_14 = QLineEdit(self.pinGroupBox1_14)
        self.lineEdit1_14.setObjectName(u"lineEdit1_14")
        self.lineEdit1_14.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_14.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_14 = QCheckBox(self.pinGroupBox1_14)
        self.defultNameCheckBox1_14.setObjectName(u"defultNameCheckBox1_14")
        self.defultNameCheckBox1_14.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_14.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_15 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_15.setObjectName(u"pinGroupBox1_15")
        self.pinGroupBox1_15.setGeometry(QRect(620, 90, 291, 181))
        self.pinGroupBox1_15.setFont(font4)
        self.pinGroupBox1_15.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_15 = QRadioButton(self.pinGroupBox1_15)
        self.OutBtn1_15.setObjectName(u"OutBtn1_15")
        self.OutBtn1_15.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_15.setFont(font5)
        self.OutBtn1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_15 = QRadioButton(self.pinGroupBox1_15)
        self.InBtn1_15.setObjectName(u"InBtn1_15")
        self.InBtn1_15.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_15 = QGroupBox(self.pinGroupBox1_15)
        self.OutGroupBox1_15.setObjectName(u"OutGroupBox1_15")
        self.OutGroupBox1_15.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_15.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_15 = QRadioButton(self.OutGroupBox1_15)
        self.OutHighBtn1_15.setObjectName(u"OutHighBtn1_15")
        self.OutHighBtn1_15.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_15 = QRadioButton(self.OutGroupBox1_15)
        self.OutLowBtn1_15.setObjectName(u"OutLowBtn1_15")
        self.OutLowBtn1_15.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_15.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_15 = QGroupBox(self.pinGroupBox1_15)
        self.InGroupBox1_15.setObjectName(u"InGroupBox1_15")
        self.InGroupBox1_15.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_15.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_15 = QRadioButton(self.InGroupBox1_15)
        self.HighImpBtn1_15.setObjectName(u"HighImpBtn1_15")
        self.HighImpBtn1_15.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_15 = QRadioButton(self.InGroupBox1_15)
        self.PullUpBtn1_15.setObjectName(u"PullUpBtn1_15")
        self.PullUpBtn1_15.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_15 = QLabel(self.pinGroupBox1_15)
        self.label1_15.setObjectName(u"label1_15")
        self.label1_15.setGeometry(QRect(10, 80, 81, 20))
        self.label1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_15 = QLineEdit(self.pinGroupBox1_15)
        self.lineEdit1_15.setObjectName(u"lineEdit1_15")
        self.lineEdit1_15.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_15.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_15 = QCheckBox(self.pinGroupBox1_15)
        self.defultNameCheckBox1_15.setObjectName(u"defultNameCheckBox1_15")
        self.defultNameCheckBox1_15.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_15.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_16 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_16.setObjectName(u"pinGroupBox1_16")
        self.pinGroupBox1_16.setGeometry(QRect(20, 280, 291, 181))
        self.pinGroupBox1_16.setFont(font4)
        self.pinGroupBox1_16.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_16 = QRadioButton(self.pinGroupBox1_16)
        self.OutBtn1_16.setObjectName(u"OutBtn1_16")
        self.OutBtn1_16.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_16.setFont(font5)
        self.OutBtn1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_16 = QRadioButton(self.pinGroupBox1_16)
        self.InBtn1_16.setObjectName(u"InBtn1_16")
        self.InBtn1_16.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_16 = QGroupBox(self.pinGroupBox1_16)
        self.OutGroupBox1_16.setObjectName(u"OutGroupBox1_16")
        self.OutGroupBox1_16.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_16.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_16 = QRadioButton(self.OutGroupBox1_16)
        self.OutHighBtn1_16.setObjectName(u"OutHighBtn1_16")
        self.OutHighBtn1_16.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_16 = QRadioButton(self.OutGroupBox1_16)
        self.OutLowBtn1_16.setObjectName(u"OutLowBtn1_16")
        self.OutLowBtn1_16.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_16.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_16 = QGroupBox(self.pinGroupBox1_16)
        self.InGroupBox1_16.setObjectName(u"InGroupBox1_16")
        self.InGroupBox1_16.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_16.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_16 = QRadioButton(self.InGroupBox1_16)
        self.HighImpBtn1_16.setObjectName(u"HighImpBtn1_16")
        self.HighImpBtn1_16.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_16 = QRadioButton(self.InGroupBox1_16)
        self.PullUpBtn1_16.setObjectName(u"PullUpBtn1_16")
        self.PullUpBtn1_16.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_16 = QLabel(self.pinGroupBox1_16)
        self.label1_16.setObjectName(u"label1_16")
        self.label1_16.setGeometry(QRect(10, 80, 81, 20))
        self.label1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_16 = QLineEdit(self.pinGroupBox1_16)
        self.lineEdit1_16.setObjectName(u"lineEdit1_16")
        self.lineEdit1_16.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_16.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_16 = QCheckBox(self.pinGroupBox1_16)
        self.defultNameCheckBox1_16.setObjectName(u"defultNameCheckBox1_16")
        self.defultNameCheckBox1_16.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_16.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_17 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_17.setObjectName(u"pinGroupBox1_17")
        self.pinGroupBox1_17.setGeometry(QRect(320, 280, 291, 181))
        self.pinGroupBox1_17.setFont(font4)
        self.pinGroupBox1_17.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_17 = QRadioButton(self.pinGroupBox1_17)
        self.OutBtn1_17.setObjectName(u"OutBtn1_17")
        self.OutBtn1_17.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_17.setFont(font5)
        self.OutBtn1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_17 = QRadioButton(self.pinGroupBox1_17)
        self.InBtn1_17.setObjectName(u"InBtn1_17")
        self.InBtn1_17.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_17 = QGroupBox(self.pinGroupBox1_17)
        self.OutGroupBox1_17.setObjectName(u"OutGroupBox1_17")
        self.OutGroupBox1_17.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_17.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_17 = QRadioButton(self.OutGroupBox1_17)
        self.OutHighBtn1_17.setObjectName(u"OutHighBtn1_17")
        self.OutHighBtn1_17.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_17 = QRadioButton(self.OutGroupBox1_17)
        self.OutLowBtn1_17.setObjectName(u"OutLowBtn1_17")
        self.OutLowBtn1_17.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_17.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_17 = QGroupBox(self.pinGroupBox1_17)
        self.InGroupBox1_17.setObjectName(u"InGroupBox1_17")
        self.InGroupBox1_17.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_17.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_17 = QRadioButton(self.InGroupBox1_17)
        self.HighImpBtn1_17.setObjectName(u"HighImpBtn1_17")
        self.HighImpBtn1_17.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_17 = QRadioButton(self.InGroupBox1_17)
        self.PullUpBtn1_17.setObjectName(u"PullUpBtn1_17")
        self.PullUpBtn1_17.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_17 = QLabel(self.pinGroupBox1_17)
        self.label1_17.setObjectName(u"label1_17")
        self.label1_17.setGeometry(QRect(10, 80, 81, 20))
        self.label1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_17 = QLineEdit(self.pinGroupBox1_17)
        self.lineEdit1_17.setObjectName(u"lineEdit1_17")
        self.lineEdit1_17.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_17.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_17 = QCheckBox(self.pinGroupBox1_17)
        self.defultNameCheckBox1_17.setObjectName(u"defultNameCheckBox1_17")
        self.defultNameCheckBox1_17.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_17.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_18 = QGroupBox(self.PortPage3)
        self.pinGroupBox1_18.setObjectName(u"pinGroupBox1_18")
        self.pinGroupBox1_18.setGeometry(QRect(620, 280, 291, 181))
        self.pinGroupBox1_18.setFont(font4)
        self.pinGroupBox1_18.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_18 = QRadioButton(self.pinGroupBox1_18)
        self.OutBtn1_18.setObjectName(u"OutBtn1_18")
        self.OutBtn1_18.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_18.setFont(font5)
        self.OutBtn1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_18 = QRadioButton(self.pinGroupBox1_18)
        self.InBtn1_18.setObjectName(u"InBtn1_18")
        self.InBtn1_18.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_18 = QGroupBox(self.pinGroupBox1_18)
        self.OutGroupBox1_18.setObjectName(u"OutGroupBox1_18")
        self.OutGroupBox1_18.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_18.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_18 = QRadioButton(self.OutGroupBox1_18)
        self.OutHighBtn1_18.setObjectName(u"OutHighBtn1_18")
        self.OutHighBtn1_18.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_18 = QRadioButton(self.OutGroupBox1_18)
        self.OutLowBtn1_18.setObjectName(u"OutLowBtn1_18")
        self.OutLowBtn1_18.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_18.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_18 = QGroupBox(self.pinGroupBox1_18)
        self.InGroupBox1_18.setObjectName(u"InGroupBox1_18")
        self.InGroupBox1_18.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_18.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_18 = QRadioButton(self.InGroupBox1_18)
        self.HighImpBtn1_18.setObjectName(u"HighImpBtn1_18")
        self.HighImpBtn1_18.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_18 = QRadioButton(self.InGroupBox1_18)
        self.PullUpBtn1_18.setObjectName(u"PullUpBtn1_18")
        self.PullUpBtn1_18.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_18 = QLabel(self.pinGroupBox1_18)
        self.label1_18.setObjectName(u"label1_18")
        self.label1_18.setGeometry(QRect(10, 80, 81, 20))
        self.label1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_18 = QLineEdit(self.pinGroupBox1_18)
        self.lineEdit1_18.setObjectName(u"lineEdit1_18")
        self.lineEdit1_18.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_18.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_18 = QCheckBox(self.pinGroupBox1_18)
        self.defultNameCheckBox1_18.setObjectName(u"defultNameCheckBox1_18")
        self.defultNameCheckBox1_18.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_18.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_22 = QLabel(self.PortPage3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 20, 261, 61))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setWordWrap(True)
        self.stackedWidget.addWidget(self.PortPage3)
        self.PortPage4 = QWidget()
        self.PortPage4.setObjectName(u"PortPage4")
        self.pinGroupBox1_19 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_19.setObjectName(u"pinGroupBox1_19")
        self.pinGroupBox1_19.setGeometry(QRect(20, 90, 291, 181))
        self.pinGroupBox1_19.setFont(font4)
        self.pinGroupBox1_19.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_19 = QRadioButton(self.pinGroupBox1_19)
        self.OutBtn1_19.setObjectName(u"OutBtn1_19")
        self.OutBtn1_19.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_19.setFont(font5)
        self.OutBtn1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_19 = QRadioButton(self.pinGroupBox1_19)
        self.InBtn1_19.setObjectName(u"InBtn1_19")
        self.InBtn1_19.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_19 = QGroupBox(self.pinGroupBox1_19)
        self.OutGroupBox1_19.setObjectName(u"OutGroupBox1_19")
        self.OutGroupBox1_19.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_19.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_19 = QRadioButton(self.OutGroupBox1_19)
        self.OutHighBtn1_19.setObjectName(u"OutHighBtn1_19")
        self.OutHighBtn1_19.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_19 = QRadioButton(self.OutGroupBox1_19)
        self.OutLowBtn1_19.setObjectName(u"OutLowBtn1_19")
        self.OutLowBtn1_19.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_19.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_19 = QGroupBox(self.pinGroupBox1_19)
        self.InGroupBox1_19.setObjectName(u"InGroupBox1_19")
        self.InGroupBox1_19.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_19.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_19 = QRadioButton(self.InGroupBox1_19)
        self.HighImpBtn1_19.setObjectName(u"HighImpBtn1_19")
        self.HighImpBtn1_19.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_19 = QRadioButton(self.InGroupBox1_19)
        self.PullUpBtn1_19.setObjectName(u"PullUpBtn1_19")
        self.PullUpBtn1_19.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_19 = QLabel(self.pinGroupBox1_19)
        self.label1_19.setObjectName(u"label1_19")
        self.label1_19.setGeometry(QRect(10, 80, 81, 20))
        self.label1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_19 = QLineEdit(self.pinGroupBox1_19)
        self.lineEdit1_19.setObjectName(u"lineEdit1_19")
        self.lineEdit1_19.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_19.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_19 = QCheckBox(self.pinGroupBox1_19)
        self.defultNameCheckBox1_19.setObjectName(u"defultNameCheckBox1_19")
        self.defultNameCheckBox1_19.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_19.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_20 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_20.setObjectName(u"pinGroupBox1_20")
        self.pinGroupBox1_20.setGeometry(QRect(320, 90, 291, 181))
        self.pinGroupBox1_20.setFont(font4)
        self.pinGroupBox1_20.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_20 = QRadioButton(self.pinGroupBox1_20)
        self.OutBtn1_20.setObjectName(u"OutBtn1_20")
        self.OutBtn1_20.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_20.setFont(font5)
        self.OutBtn1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_20 = QRadioButton(self.pinGroupBox1_20)
        self.InBtn1_20.setObjectName(u"InBtn1_20")
        self.InBtn1_20.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_20 = QGroupBox(self.pinGroupBox1_20)
        self.OutGroupBox1_20.setObjectName(u"OutGroupBox1_20")
        self.OutGroupBox1_20.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_20.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_20 = QRadioButton(self.OutGroupBox1_20)
        self.OutHighBtn1_20.setObjectName(u"OutHighBtn1_20")
        self.OutHighBtn1_20.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_20 = QRadioButton(self.OutGroupBox1_20)
        self.OutLowBtn1_20.setObjectName(u"OutLowBtn1_20")
        self.OutLowBtn1_20.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_20.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_20 = QGroupBox(self.pinGroupBox1_20)
        self.InGroupBox1_20.setObjectName(u"InGroupBox1_20")
        self.InGroupBox1_20.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_20.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_20 = QRadioButton(self.InGroupBox1_20)
        self.HighImpBtn1_20.setObjectName(u"HighImpBtn1_20")
        self.HighImpBtn1_20.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_20 = QRadioButton(self.InGroupBox1_20)
        self.PullUpBtn1_20.setObjectName(u"PullUpBtn1_20")
        self.PullUpBtn1_20.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_20 = QLabel(self.pinGroupBox1_20)
        self.label1_20.setObjectName(u"label1_20")
        self.label1_20.setGeometry(QRect(10, 80, 81, 20))
        self.label1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_20 = QLineEdit(self.pinGroupBox1_20)
        self.lineEdit1_20.setObjectName(u"lineEdit1_20")
        self.lineEdit1_20.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_20.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_20 = QCheckBox(self.pinGroupBox1_20)
        self.defultNameCheckBox1_20.setObjectName(u"defultNameCheckBox1_20")
        self.defultNameCheckBox1_20.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_20.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_21 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_21.setObjectName(u"pinGroupBox1_21")
        self.pinGroupBox1_21.setGeometry(QRect(620, 90, 291, 181))
        self.pinGroupBox1_21.setFont(font4)
        self.pinGroupBox1_21.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_21 = QRadioButton(self.pinGroupBox1_21)
        self.OutBtn1_21.setObjectName(u"OutBtn1_21")
        self.OutBtn1_21.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_21.setFont(font5)
        self.OutBtn1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_21 = QRadioButton(self.pinGroupBox1_21)
        self.InBtn1_21.setObjectName(u"InBtn1_21")
        self.InBtn1_21.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_21 = QGroupBox(self.pinGroupBox1_21)
        self.OutGroupBox1_21.setObjectName(u"OutGroupBox1_21")
        self.OutGroupBox1_21.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_21.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_21 = QRadioButton(self.OutGroupBox1_21)
        self.OutHighBtn1_21.setObjectName(u"OutHighBtn1_21")
        self.OutHighBtn1_21.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_21 = QRadioButton(self.OutGroupBox1_21)
        self.OutLowBtn1_21.setObjectName(u"OutLowBtn1_21")
        self.OutLowBtn1_21.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_21.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_21 = QGroupBox(self.pinGroupBox1_21)
        self.InGroupBox1_21.setObjectName(u"InGroupBox1_21")
        self.InGroupBox1_21.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_21.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_21 = QRadioButton(self.InGroupBox1_21)
        self.HighImpBtn1_21.setObjectName(u"HighImpBtn1_21")
        self.HighImpBtn1_21.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_21 = QRadioButton(self.InGroupBox1_21)
        self.PullUpBtn1_21.setObjectName(u"PullUpBtn1_21")
        self.PullUpBtn1_21.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_21 = QLabel(self.pinGroupBox1_21)
        self.label1_21.setObjectName(u"label1_21")
        self.label1_21.setGeometry(QRect(10, 80, 81, 20))
        self.label1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_21 = QLineEdit(self.pinGroupBox1_21)
        self.lineEdit1_21.setObjectName(u"lineEdit1_21")
        self.lineEdit1_21.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_21.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_21 = QCheckBox(self.pinGroupBox1_21)
        self.defultNameCheckBox1_21.setObjectName(u"defultNameCheckBox1_21")
        self.defultNameCheckBox1_21.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_21.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_22 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_22.setObjectName(u"pinGroupBox1_22")
        self.pinGroupBox1_22.setGeometry(QRect(20, 280, 291, 181))
        self.pinGroupBox1_22.setFont(font4)
        self.pinGroupBox1_22.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_22 = QRadioButton(self.pinGroupBox1_22)
        self.OutBtn1_22.setObjectName(u"OutBtn1_22")
        self.OutBtn1_22.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_22.setFont(font5)
        self.OutBtn1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_22 = QRadioButton(self.pinGroupBox1_22)
        self.InBtn1_22.setObjectName(u"InBtn1_22")
        self.InBtn1_22.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_22 = QGroupBox(self.pinGroupBox1_22)
        self.OutGroupBox1_22.setObjectName(u"OutGroupBox1_22")
        self.OutGroupBox1_22.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_22.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_22 = QRadioButton(self.OutGroupBox1_22)
        self.OutHighBtn1_22.setObjectName(u"OutHighBtn1_22")
        self.OutHighBtn1_22.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_22 = QRadioButton(self.OutGroupBox1_22)
        self.OutLowBtn1_22.setObjectName(u"OutLowBtn1_22")
        self.OutLowBtn1_22.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_22.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_22 = QGroupBox(self.pinGroupBox1_22)
        self.InGroupBox1_22.setObjectName(u"InGroupBox1_22")
        self.InGroupBox1_22.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_22.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_22 = QRadioButton(self.InGroupBox1_22)
        self.HighImpBtn1_22.setObjectName(u"HighImpBtn1_22")
        self.HighImpBtn1_22.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_22 = QRadioButton(self.InGroupBox1_22)
        self.PullUpBtn1_22.setObjectName(u"PullUpBtn1_22")
        self.PullUpBtn1_22.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_22 = QLabel(self.pinGroupBox1_22)
        self.label1_22.setObjectName(u"label1_22")
        self.label1_22.setGeometry(QRect(10, 80, 81, 20))
        self.label1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_22 = QLineEdit(self.pinGroupBox1_22)
        self.lineEdit1_22.setObjectName(u"lineEdit1_22")
        self.lineEdit1_22.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_22.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_22 = QCheckBox(self.pinGroupBox1_22)
        self.defultNameCheckBox1_22.setObjectName(u"defultNameCheckBox1_22")
        self.defultNameCheckBox1_22.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_22.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_23 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_23.setObjectName(u"pinGroupBox1_23")
        self.pinGroupBox1_23.setGeometry(QRect(320, 280, 291, 181))
        self.pinGroupBox1_23.setFont(font4)
        self.pinGroupBox1_23.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_23 = QRadioButton(self.pinGroupBox1_23)
        self.OutBtn1_23.setObjectName(u"OutBtn1_23")
        self.OutBtn1_23.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_23.setFont(font5)
        self.OutBtn1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_23 = QRadioButton(self.pinGroupBox1_23)
        self.InBtn1_23.setObjectName(u"InBtn1_23")
        self.InBtn1_23.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_23 = QGroupBox(self.pinGroupBox1_23)
        self.OutGroupBox1_23.setObjectName(u"OutGroupBox1_23")
        self.OutGroupBox1_23.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_23.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_23 = QRadioButton(self.OutGroupBox1_23)
        self.OutHighBtn1_23.setObjectName(u"OutHighBtn1_23")
        self.OutHighBtn1_23.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_23 = QRadioButton(self.OutGroupBox1_23)
        self.OutLowBtn1_23.setObjectName(u"OutLowBtn1_23")
        self.OutLowBtn1_23.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_23.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_23 = QGroupBox(self.pinGroupBox1_23)
        self.InGroupBox1_23.setObjectName(u"InGroupBox1_23")
        self.InGroupBox1_23.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_23.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_23 = QRadioButton(self.InGroupBox1_23)
        self.HighImpBtn1_23.setObjectName(u"HighImpBtn1_23")
        self.HighImpBtn1_23.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_23 = QRadioButton(self.InGroupBox1_23)
        self.PullUpBtn1_23.setObjectName(u"PullUpBtn1_23")
        self.PullUpBtn1_23.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_23 = QLabel(self.pinGroupBox1_23)
        self.label1_23.setObjectName(u"label1_23")
        self.label1_23.setGeometry(QRect(10, 80, 81, 20))
        self.label1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_23 = QLineEdit(self.pinGroupBox1_23)
        self.lineEdit1_23.setObjectName(u"lineEdit1_23")
        self.lineEdit1_23.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_23.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_23 = QCheckBox(self.pinGroupBox1_23)
        self.defultNameCheckBox1_23.setObjectName(u"defultNameCheckBox1_23")
        self.defultNameCheckBox1_23.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_23.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_24 = QGroupBox(self.PortPage4)
        self.pinGroupBox1_24.setObjectName(u"pinGroupBox1_24")
        self.pinGroupBox1_24.setGeometry(QRect(620, 280, 291, 181))
        self.pinGroupBox1_24.setFont(font4)
        self.pinGroupBox1_24.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_24 = QRadioButton(self.pinGroupBox1_24)
        self.OutBtn1_24.setObjectName(u"OutBtn1_24")
        self.OutBtn1_24.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_24.setFont(font5)
        self.OutBtn1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_24 = QRadioButton(self.pinGroupBox1_24)
        self.InBtn1_24.setObjectName(u"InBtn1_24")
        self.InBtn1_24.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_24 = QGroupBox(self.pinGroupBox1_24)
        self.OutGroupBox1_24.setObjectName(u"OutGroupBox1_24")
        self.OutGroupBox1_24.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_24.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_24 = QRadioButton(self.OutGroupBox1_24)
        self.OutHighBtn1_24.setObjectName(u"OutHighBtn1_24")
        self.OutHighBtn1_24.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_24 = QRadioButton(self.OutGroupBox1_24)
        self.OutLowBtn1_24.setObjectName(u"OutLowBtn1_24")
        self.OutLowBtn1_24.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_24.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_24 = QGroupBox(self.pinGroupBox1_24)
        self.InGroupBox1_24.setObjectName(u"InGroupBox1_24")
        self.InGroupBox1_24.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_24.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_24 = QRadioButton(self.InGroupBox1_24)
        self.HighImpBtn1_24.setObjectName(u"HighImpBtn1_24")
        self.HighImpBtn1_24.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_24 = QRadioButton(self.InGroupBox1_24)
        self.PullUpBtn1_24.setObjectName(u"PullUpBtn1_24")
        self.PullUpBtn1_24.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_24 = QLabel(self.pinGroupBox1_24)
        self.label1_24.setObjectName(u"label1_24")
        self.label1_24.setGeometry(QRect(10, 80, 81, 20))
        self.label1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_24 = QLineEdit(self.pinGroupBox1_24)
        self.lineEdit1_24.setObjectName(u"lineEdit1_24")
        self.lineEdit1_24.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_24.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_24 = QCheckBox(self.pinGroupBox1_24)
        self.defultNameCheckBox1_24.setObjectName(u"defultNameCheckBox1_24")
        self.defultNameCheckBox1_24.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_24.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_23 = QLabel(self.PortPage4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 20, 261, 61))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23.setWordWrap(True)
        self.stackedWidget.addWidget(self.PortPage4)
        self.PortPage5 = QWidget()
        self.PortPage5.setObjectName(u"PortPage5")
        self.pinGroupBox1_25 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_25.setObjectName(u"pinGroupBox1_25")
        self.pinGroupBox1_25.setGeometry(QRect(20, 90, 291, 181))
        self.pinGroupBox1_25.setFont(font4)
        self.pinGroupBox1_25.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_25 = QRadioButton(self.pinGroupBox1_25)
        self.OutBtn1_25.setObjectName(u"OutBtn1_25")
        self.OutBtn1_25.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_25.setFont(font5)
        self.OutBtn1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_25 = QRadioButton(self.pinGroupBox1_25)
        self.InBtn1_25.setObjectName(u"InBtn1_25")
        self.InBtn1_25.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_25 = QGroupBox(self.pinGroupBox1_25)
        self.OutGroupBox1_25.setObjectName(u"OutGroupBox1_25")
        self.OutGroupBox1_25.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_25.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_25 = QRadioButton(self.OutGroupBox1_25)
        self.OutHighBtn1_25.setObjectName(u"OutHighBtn1_25")
        self.OutHighBtn1_25.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_25 = QRadioButton(self.OutGroupBox1_25)
        self.OutLowBtn1_25.setObjectName(u"OutLowBtn1_25")
        self.OutLowBtn1_25.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_25.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_25 = QGroupBox(self.pinGroupBox1_25)
        self.InGroupBox1_25.setObjectName(u"InGroupBox1_25")
        self.InGroupBox1_25.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_25.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_25 = QRadioButton(self.InGroupBox1_25)
        self.HighImpBtn1_25.setObjectName(u"HighImpBtn1_25")
        self.HighImpBtn1_25.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_25 = QRadioButton(self.InGroupBox1_25)
        self.PullUpBtn1_25.setObjectName(u"PullUpBtn1_25")
        self.PullUpBtn1_25.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_25 = QLabel(self.pinGroupBox1_25)
        self.label1_25.setObjectName(u"label1_25")
        self.label1_25.setGeometry(QRect(10, 80, 81, 20))
        self.label1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_25 = QLineEdit(self.pinGroupBox1_25)
        self.lineEdit1_25.setObjectName(u"lineEdit1_25")
        self.lineEdit1_25.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_25.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_25 = QCheckBox(self.pinGroupBox1_25)
        self.defultNameCheckBox1_25.setObjectName(u"defultNameCheckBox1_25")
        self.defultNameCheckBox1_25.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_25.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_26 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_26.setObjectName(u"pinGroupBox1_26")
        self.pinGroupBox1_26.setGeometry(QRect(320, 90, 291, 181))
        self.pinGroupBox1_26.setFont(font4)
        self.pinGroupBox1_26.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_26 = QRadioButton(self.pinGroupBox1_26)
        self.OutBtn1_26.setObjectName(u"OutBtn1_26")
        self.OutBtn1_26.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_26.setFont(font5)
        self.OutBtn1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_26 = QRadioButton(self.pinGroupBox1_26)
        self.InBtn1_26.setObjectName(u"InBtn1_26")
        self.InBtn1_26.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_26 = QGroupBox(self.pinGroupBox1_26)
        self.OutGroupBox1_26.setObjectName(u"OutGroupBox1_26")
        self.OutGroupBox1_26.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_26.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_26 = QRadioButton(self.OutGroupBox1_26)
        self.OutHighBtn1_26.setObjectName(u"OutHighBtn1_26")
        self.OutHighBtn1_26.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_26 = QRadioButton(self.OutGroupBox1_26)
        self.OutLowBtn1_26.setObjectName(u"OutLowBtn1_26")
        self.OutLowBtn1_26.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_26.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_26 = QGroupBox(self.pinGroupBox1_26)
        self.InGroupBox1_26.setObjectName(u"InGroupBox1_26")
        self.InGroupBox1_26.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_26.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_26 = QRadioButton(self.InGroupBox1_26)
        self.HighImpBtn1_26.setObjectName(u"HighImpBtn1_26")
        self.HighImpBtn1_26.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_26 = QRadioButton(self.InGroupBox1_26)
        self.PullUpBtn1_26.setObjectName(u"PullUpBtn1_26")
        self.PullUpBtn1_26.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_26 = QLabel(self.pinGroupBox1_26)
        self.label1_26.setObjectName(u"label1_26")
        self.label1_26.setGeometry(QRect(10, 80, 81, 20))
        self.label1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_26 = QLineEdit(self.pinGroupBox1_26)
        self.lineEdit1_26.setObjectName(u"lineEdit1_26")
        self.lineEdit1_26.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_26.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_26 = QCheckBox(self.pinGroupBox1_26)
        self.defultNameCheckBox1_26.setObjectName(u"defultNameCheckBox1_26")
        self.defultNameCheckBox1_26.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_26.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_27 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_27.setObjectName(u"pinGroupBox1_27")
        self.pinGroupBox1_27.setGeometry(QRect(620, 90, 291, 181))
        self.pinGroupBox1_27.setFont(font4)
        self.pinGroupBox1_27.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_27 = QRadioButton(self.pinGroupBox1_27)
        self.OutBtn1_27.setObjectName(u"OutBtn1_27")
        self.OutBtn1_27.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_27.setFont(font5)
        self.OutBtn1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_27 = QRadioButton(self.pinGroupBox1_27)
        self.InBtn1_27.setObjectName(u"InBtn1_27")
        self.InBtn1_27.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_27 = QGroupBox(self.pinGroupBox1_27)
        self.OutGroupBox1_27.setObjectName(u"OutGroupBox1_27")
        self.OutGroupBox1_27.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_27.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_27 = QRadioButton(self.OutGroupBox1_27)
        self.OutHighBtn1_27.setObjectName(u"OutHighBtn1_27")
        self.OutHighBtn1_27.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_27 = QRadioButton(self.OutGroupBox1_27)
        self.OutLowBtn1_27.setObjectName(u"OutLowBtn1_27")
        self.OutLowBtn1_27.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_27.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_27 = QGroupBox(self.pinGroupBox1_27)
        self.InGroupBox1_27.setObjectName(u"InGroupBox1_27")
        self.InGroupBox1_27.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_27.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_27 = QRadioButton(self.InGroupBox1_27)
        self.HighImpBtn1_27.setObjectName(u"HighImpBtn1_27")
        self.HighImpBtn1_27.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_27 = QRadioButton(self.InGroupBox1_27)
        self.PullUpBtn1_27.setObjectName(u"PullUpBtn1_27")
        self.PullUpBtn1_27.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_27 = QLabel(self.pinGroupBox1_27)
        self.label1_27.setObjectName(u"label1_27")
        self.label1_27.setGeometry(QRect(10, 80, 81, 20))
        self.label1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_27 = QLineEdit(self.pinGroupBox1_27)
        self.lineEdit1_27.setObjectName(u"lineEdit1_27")
        self.lineEdit1_27.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_27.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_27 = QCheckBox(self.pinGroupBox1_27)
        self.defultNameCheckBox1_27.setObjectName(u"defultNameCheckBox1_27")
        self.defultNameCheckBox1_27.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_27.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_28 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_28.setObjectName(u"pinGroupBox1_28")
        self.pinGroupBox1_28.setGeometry(QRect(20, 280, 291, 181))
        self.pinGroupBox1_28.setFont(font4)
        self.pinGroupBox1_28.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_28 = QRadioButton(self.pinGroupBox1_28)
        self.OutBtn1_28.setObjectName(u"OutBtn1_28")
        self.OutBtn1_28.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_28.setFont(font5)
        self.OutBtn1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_28 = QRadioButton(self.pinGroupBox1_28)
        self.InBtn1_28.setObjectName(u"InBtn1_28")
        self.InBtn1_28.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_28 = QGroupBox(self.pinGroupBox1_28)
        self.OutGroupBox1_28.setObjectName(u"OutGroupBox1_28")
        self.OutGroupBox1_28.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_28.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_28 = QRadioButton(self.OutGroupBox1_28)
        self.OutHighBtn1_28.setObjectName(u"OutHighBtn1_28")
        self.OutHighBtn1_28.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_28 = QRadioButton(self.OutGroupBox1_28)
        self.OutLowBtn1_28.setObjectName(u"OutLowBtn1_28")
        self.OutLowBtn1_28.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_28.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_28 = QGroupBox(self.pinGroupBox1_28)
        self.InGroupBox1_28.setObjectName(u"InGroupBox1_28")
        self.InGroupBox1_28.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_28.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_28 = QRadioButton(self.InGroupBox1_28)
        self.HighImpBtn1_28.setObjectName(u"HighImpBtn1_28")
        self.HighImpBtn1_28.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_28 = QRadioButton(self.InGroupBox1_28)
        self.PullUpBtn1_28.setObjectName(u"PullUpBtn1_28")
        self.PullUpBtn1_28.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_28 = QLabel(self.pinGroupBox1_28)
        self.label1_28.setObjectName(u"label1_28")
        self.label1_28.setGeometry(QRect(10, 80, 81, 20))
        self.label1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_28 = QLineEdit(self.pinGroupBox1_28)
        self.lineEdit1_28.setObjectName(u"lineEdit1_28")
        self.lineEdit1_28.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_28.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_28 = QCheckBox(self.pinGroupBox1_28)
        self.defultNameCheckBox1_28.setObjectName(u"defultNameCheckBox1_28")
        self.defultNameCheckBox1_28.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_28.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_29 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_29.setObjectName(u"pinGroupBox1_29")
        self.pinGroupBox1_29.setGeometry(QRect(320, 280, 291, 181))
        self.pinGroupBox1_29.setFont(font4)
        self.pinGroupBox1_29.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_29 = QRadioButton(self.pinGroupBox1_29)
        self.OutBtn1_29.setObjectName(u"OutBtn1_29")
        self.OutBtn1_29.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_29.setFont(font5)
        self.OutBtn1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_29 = QRadioButton(self.pinGroupBox1_29)
        self.InBtn1_29.setObjectName(u"InBtn1_29")
        self.InBtn1_29.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_29 = QGroupBox(self.pinGroupBox1_29)
        self.OutGroupBox1_29.setObjectName(u"OutGroupBox1_29")
        self.OutGroupBox1_29.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_29.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_29 = QRadioButton(self.OutGroupBox1_29)
        self.OutHighBtn1_29.setObjectName(u"OutHighBtn1_29")
        self.OutHighBtn1_29.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_29 = QRadioButton(self.OutGroupBox1_29)
        self.OutLowBtn1_29.setObjectName(u"OutLowBtn1_29")
        self.OutLowBtn1_29.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_29.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_29 = QGroupBox(self.pinGroupBox1_29)
        self.InGroupBox1_29.setObjectName(u"InGroupBox1_29")
        self.InGroupBox1_29.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_29.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_29 = QRadioButton(self.InGroupBox1_29)
        self.HighImpBtn1_29.setObjectName(u"HighImpBtn1_29")
        self.HighImpBtn1_29.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_29 = QRadioButton(self.InGroupBox1_29)
        self.PullUpBtn1_29.setObjectName(u"PullUpBtn1_29")
        self.PullUpBtn1_29.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_29 = QLabel(self.pinGroupBox1_29)
        self.label1_29.setObjectName(u"label1_29")
        self.label1_29.setGeometry(QRect(10, 80, 81, 20))
        self.label1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_29 = QLineEdit(self.pinGroupBox1_29)
        self.lineEdit1_29.setObjectName(u"lineEdit1_29")
        self.lineEdit1_29.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_29.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_29 = QCheckBox(self.pinGroupBox1_29)
        self.defultNameCheckBox1_29.setObjectName(u"defultNameCheckBox1_29")
        self.defultNameCheckBox1_29.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_29.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_30 = QGroupBox(self.PortPage5)
        self.pinGroupBox1_30.setObjectName(u"pinGroupBox1_30")
        self.pinGroupBox1_30.setGeometry(QRect(620, 280, 291, 181))
        self.pinGroupBox1_30.setFont(font4)
        self.pinGroupBox1_30.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_30 = QRadioButton(self.pinGroupBox1_30)
        self.OutBtn1_30.setObjectName(u"OutBtn1_30")
        self.OutBtn1_30.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_30.setFont(font5)
        self.OutBtn1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_30 = QRadioButton(self.pinGroupBox1_30)
        self.InBtn1_30.setObjectName(u"InBtn1_30")
        self.InBtn1_30.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_30 = QGroupBox(self.pinGroupBox1_30)
        self.OutGroupBox1_30.setObjectName(u"OutGroupBox1_30")
        self.OutGroupBox1_30.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_30.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_30 = QRadioButton(self.OutGroupBox1_30)
        self.OutHighBtn1_30.setObjectName(u"OutHighBtn1_30")
        self.OutHighBtn1_30.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_30 = QRadioButton(self.OutGroupBox1_30)
        self.OutLowBtn1_30.setObjectName(u"OutLowBtn1_30")
        self.OutLowBtn1_30.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_30.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_30 = QGroupBox(self.pinGroupBox1_30)
        self.InGroupBox1_30.setObjectName(u"InGroupBox1_30")
        self.InGroupBox1_30.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_30.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_30 = QRadioButton(self.InGroupBox1_30)
        self.HighImpBtn1_30.setObjectName(u"HighImpBtn1_30")
        self.HighImpBtn1_30.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_30 = QRadioButton(self.InGroupBox1_30)
        self.PullUpBtn1_30.setObjectName(u"PullUpBtn1_30")
        self.PullUpBtn1_30.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_30 = QLabel(self.pinGroupBox1_30)
        self.label1_30.setObjectName(u"label1_30")
        self.label1_30.setGeometry(QRect(10, 80, 81, 20))
        self.label1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_30 = QLineEdit(self.pinGroupBox1_30)
        self.lineEdit1_30.setObjectName(u"lineEdit1_30")
        self.lineEdit1_30.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_30.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_30 = QCheckBox(self.pinGroupBox1_30)
        self.defultNameCheckBox1_30.setObjectName(u"defultNameCheckBox1_30")
        self.defultNameCheckBox1_30.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_30.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_24 = QLabel(self.PortPage5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 20, 261, 61))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setWordWrap(True)
        self.stackedWidget.addWidget(self.PortPage5)
        self.PortPage6 = QWidget()
        self.PortPage6.setObjectName(u"PortPage6")
        self.pinGroupBox1_31 = QGroupBox(self.PortPage6)
        self.pinGroupBox1_31.setObjectName(u"pinGroupBox1_31")
        self.pinGroupBox1_31.setGeometry(QRect(170, 140, 291, 181))
        self.pinGroupBox1_31.setFont(font4)
        self.pinGroupBox1_31.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_31 = QRadioButton(self.pinGroupBox1_31)
        self.OutBtn1_31.setObjectName(u"OutBtn1_31")
        self.OutBtn1_31.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_31.setFont(font5)
        self.OutBtn1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_31 = QRadioButton(self.pinGroupBox1_31)
        self.InBtn1_31.setObjectName(u"InBtn1_31")
        self.InBtn1_31.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_31 = QGroupBox(self.pinGroupBox1_31)
        self.OutGroupBox1_31.setObjectName(u"OutGroupBox1_31")
        self.OutGroupBox1_31.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_31.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_31 = QRadioButton(self.OutGroupBox1_31)
        self.OutHighBtn1_31.setObjectName(u"OutHighBtn1_31")
        self.OutHighBtn1_31.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_31 = QRadioButton(self.OutGroupBox1_31)
        self.OutLowBtn1_31.setObjectName(u"OutLowBtn1_31")
        self.OutLowBtn1_31.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_31.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_31 = QGroupBox(self.pinGroupBox1_31)
        self.InGroupBox1_31.setObjectName(u"InGroupBox1_31")
        self.InGroupBox1_31.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_31.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_31 = QRadioButton(self.InGroupBox1_31)
        self.HighImpBtn1_31.setObjectName(u"HighImpBtn1_31")
        self.HighImpBtn1_31.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_31 = QRadioButton(self.InGroupBox1_31)
        self.PullUpBtn1_31.setObjectName(u"PullUpBtn1_31")
        self.PullUpBtn1_31.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_31 = QLabel(self.pinGroupBox1_31)
        self.label1_31.setObjectName(u"label1_31")
        self.label1_31.setGeometry(QRect(10, 80, 81, 20))
        self.label1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_31 = QLineEdit(self.pinGroupBox1_31)
        self.lineEdit1_31.setObjectName(u"lineEdit1_31")
        self.lineEdit1_31.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_31.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_31 = QCheckBox(self.pinGroupBox1_31)
        self.defultNameCheckBox1_31.setObjectName(u"defultNameCheckBox1_31")
        self.defultNameCheckBox1_31.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_31.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pinGroupBox1_32 = QGroupBox(self.PortPage6)
        self.pinGroupBox1_32.setObjectName(u"pinGroupBox1_32")
        self.pinGroupBox1_32.setGeometry(QRect(470, 140, 291, 181))
        self.pinGroupBox1_32.setFont(font4)
        self.pinGroupBox1_32.setStyleSheet(u"    background-color: rgb(154, 125, 195);\n"
"    border: 2px solid #fff;\n"
"	border-radius:10px;\n"
"font: 10pt \"Gill Sans Ultra Bold\";\n"
"\n"
"\n"
"\n"
"	\n"
"")
        self.OutBtn1_32 = QRadioButton(self.pinGroupBox1_32)
        self.OutBtn1_32.setObjectName(u"OutBtn1_32")
        self.OutBtn1_32.setGeometry(QRect(10, 20, 82, 17))
        self.OutBtn1_32.setFont(font5)
        self.OutBtn1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.InBtn1_32 = QRadioButton(self.pinGroupBox1_32)
        self.InBtn1_32.setObjectName(u"InBtn1_32")
        self.InBtn1_32.setGeometry(QRect(10, 50, 82, 17))
        self.InBtn1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutGroupBox1_32 = QGroupBox(self.pinGroupBox1_32)
        self.OutGroupBox1_32.setObjectName(u"OutGroupBox1_32")
        self.OutGroupBox1_32.setGeometry(QRect(120, 20, 161, 71))
        self.OutGroupBox1_32.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.OutHighBtn1_32 = QRadioButton(self.OutGroupBox1_32)
        self.OutHighBtn1_32.setObjectName(u"OutHighBtn1_32")
        self.OutHighBtn1_32.setGeometry(QRect(10, 20, 82, 17))
        self.OutHighBtn1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.OutLowBtn1_32 = QRadioButton(self.OutGroupBox1_32)
        self.OutLowBtn1_32.setObjectName(u"OutLowBtn1_32")
        self.OutLowBtn1_32.setGeometry(QRect(10, 40, 82, 17))
        self.OutLowBtn1_32.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: none;")
        self.InGroupBox1_32 = QGroupBox(self.pinGroupBox1_32)
        self.InGroupBox1_32.setObjectName(u"InGroupBox1_32")
        self.InGroupBox1_32.setGeometry(QRect(120, 100, 161, 71))
        self.InGroupBox1_32.setStyleSheet(u"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"")
        self.HighImpBtn1_32 = QRadioButton(self.InGroupBox1_32)
        self.HighImpBtn1_32.setObjectName(u"HighImpBtn1_32")
        self.HighImpBtn1_32.setGeometry(QRect(10, 20, 141, 17))
        self.HighImpBtn1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.PullUpBtn1_32 = QRadioButton(self.InGroupBox1_32)
        self.PullUpBtn1_32.setObjectName(u"PullUpBtn1_32")
        self.PullUpBtn1_32.setGeometry(QRect(10, 40, 141, 17))
        self.PullUpBtn1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label1_32 = QLabel(self.pinGroupBox1_32)
        self.label1_32.setObjectName(u"label1_32")
        self.label1_32.setGeometry(QRect(10, 80, 81, 20))
        self.label1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit1_32 = QLineEdit(self.pinGroupBox1_32)
        self.lineEdit1_32.setObjectName(u"lineEdit1_32")
        self.lineEdit1_32.setGeometry(QRect(10, 100, 101, 20))
        self.lineEdit1_32.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.defultNameCheckBox1_32 = QCheckBox(self.pinGroupBox1_32)
        self.defultNameCheckBox1_32.setObjectName(u"defultNameCheckBox1_32")
        self.defultNameCheckBox1_32.setGeometry(QRect(10, 130, 91, 17))
        self.defultNameCheckBox1_32.setStyleSheet(u"border-color: none;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.GenerateBtn = QPushButton(self.PortPage6)
        self.GenerateBtn.setObjectName(u"GenerateBtn")
        self.GenerateBtn.setGeometry(QRect(640, 360, 111, 31))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.GenerateBtn.setFont(font6)
        self.Path = QLineEdit(self.PortPage6)
        self.Path.setObjectName(u"Path")
        self.Path.setGeometry(QRect(190, 360, 441, 31))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.Path.setFont(font7)
        self.Path.setStyleSheet(u"border-color: rgb(209, 209, 209);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_25 = QLabel(self.PortPage6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 20, 261, 61))
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setWordWrap(True)
        self.stackedWidget.addWidget(self.PortPage6)
        self.ArchivePage = QWidget()
        self.ArchivePage.setObjectName(u"ArchivePage")
        self.stackedWidget.addWidget(self.ArchivePage)
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.ITILogo = QLabel(self.AboutPage)
        self.ITILogo.setObjectName(u"ITILogo")
        self.ITILogo.setGeometry(QRect(360, 10, 261, 341))
        self.ITILogo.setPixmap(QPixmap(u":/newPrefix/C:/Users/Eng. Aya Adel/Downloads/iti-logo.png"))
        self.ITILogo.setScaledContents(True)
        self.AboutUsText = QLabel(self.AboutPage)
        self.AboutUsText.setObjectName(u"AboutUsText")
        self.AboutUsText.setGeometry(QRect(250, 370, 481, 41))
        self.AboutUsText.setStyleSheet(u"color : rgb(255, 255, 255);\n"
"font: 18pt \"Modern No. 20\";")
        self.AboutUsText.setAlignment(Qt.AlignCenter)
        self.AboutUsText_2 = QLabel(self.AboutPage)
        self.AboutUsText_2.setObjectName(u"AboutUsText_2")
        self.AboutUsText_2.setGeometry(QRect(250, 420, 481, 41))
        self.AboutUsText_2.setStyleSheet(u"color : rgb(255, 255, 255);\n"
"font: 18pt \"Modern No. 20\";")
        self.AboutUsText_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.AboutPage)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.main_body)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	padding: 10px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Pin6_11Btn = QPushButton(self.frame_3)
        self.Pin6_11Btn.setObjectName(u"Pin6_11Btn")
        self.Pin6_11Btn.setGeometry(QRect(0, 130, 101, 31))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.Pin6_11Btn.setFont(font8)
        self.Pin6_11Btn.hide()        
        self.Pin12_17Btn = QPushButton(self.frame_3)
        self.Pin12_17Btn.setObjectName(u"Pin12_17Btn")
        self.Pin12_17Btn.setGeometry(QRect(0, 170, 101, 31))
        self.Pin12_17Btn.setFont(font8)
        self.Pin12_17Btn.hide()        
        self.Pin0_5Btn = QPushButton(self.frame_3)
        self.Pin0_5Btn.setObjectName(u"Pin0_5Btn")
        self.Pin0_5Btn.setGeometry(QRect(0, 90, 101, 31))
        self.Pin0_5Btn.setFont(font8)
        self.Pin0_5Btn.hide()
        self.Pin18_23Btn = QPushButton(self.frame_3)
        self.Pin18_23Btn.setObjectName(u"Pin18_23Btn")
        self.Pin18_23Btn.setGeometry(QRect(0, 210, 101, 31))
        self.Pin18_23Btn.setFont(font8)
        self.Pin18_23Btn.hide()
        self.Pin24_28Btn = QPushButton(self.frame_3)
        self.Pin24_28Btn.setObjectName(u"Pin24_28Btn")
        self.Pin24_28Btn.setGeometry(QRect(0, 250, 101, 31))
        self.Pin24_28Btn.setFont(font8)
        self.Pin24_28Btn.hide()
        self.Pin30_32Btn = QPushButton(self.frame_3)
        self.Pin30_32Btn.setObjectName(u"Pin30_32Btn")
        self.Pin30_32Btn.setGeometry(QRect(0, 290, 101, 31))
        self.Pin30_32Btn.setFont(font8)
        self.Pin30_32Btn.hide()

        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(MainWidget)
        self.minBtn.clicked.connect(MainWidget.showMinimized)
        self.closeBtn.clicked.connect(MainWidget.close)
        self.menuBtn.clicked.connect(self.moveLeftMenu)
        self.HomeBtn.clicked.connect(self.ShowPortPage1)
        self.ArchBtn.clicked.connect(self.ShowArchivePage)
        self.pushButton_4.clicked.connect(self.ShowAboutPage)
        self.Pin0_5Btn.clicked.connect(self.ShowPortPage1)
        self.Pin6_11Btn.clicked.connect(self.ShowPortPage2)
        self.Pin12_17Btn.clicked.connect(self.ShowPortPage3)
        self.Pin18_23Btn.clicked.connect(self.ShowPortPage4)
        self.Pin24_28Btn.clicked.connect(self.ShowPortPage5)
        self.Pin30_32Btn.clicked.connect(self.ShowPortPage6)
        self.GenerateBtn.clicked.connect(self.GenerateFile)
       
        
        # GroupBox Actions Handling
        self.InBtn1.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1.stateChanged.connect(self.EnableLineEdit)
        
        self.InBtn1_2.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_2.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_2.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_3.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_3.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_3.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_4.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_4.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_4.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_5.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_5.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_5.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_6.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_6.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_6.stateChanged.connect(self.EnableLineEdit)
        
        self.InBtn1_7.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_7.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_7.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_8.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_8.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_8.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_9.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_9.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_9.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_10.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_10.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_10.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_11.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_11.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_11.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_12.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_12.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_12.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_13.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_13.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_13.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_14.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_14.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_14.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_15.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_15.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_15.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_16.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_16.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_16.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_17.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_17.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_17.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_18.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_18.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_18.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_19.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_19.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_19.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_20.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_20.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_20.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_21.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_21.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_21.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_22.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_22.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_22.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_23.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_23.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_23.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_24.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_24.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_24.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_25.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_25.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_25.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_26.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_26.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_26.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_27.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_27.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_27.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_28.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_28.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_28.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_29.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_29.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_29.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_30.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_30.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_30.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_31.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_31.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_31.stateChanged.connect(self.EnableLineEdit)

        self.InBtn1_32.toggled.connect(self.DisableOutGroupBox)
        self.OutBtn1_32.toggled.connect(self.DisableInGroupBox)
        self.defultNameCheckBox1_32.stateChanged.connect(self.EnableLineEdit)
        self.menuBtn.setDefault(False)
        self.minBtn_2.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.menuBtn.setText("")
        self.minBtn.setText("")
        self.closeBtn.setText("")
        self.HomeBtn.setText(QCoreApplication.translate("MainWidget", u"   Home", None))
        self.ArchBtn.setText(QCoreApplication.translate("MainWidget", u" Archive", None))
        self.minBtn_2.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWidget", u"About Us", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWidget", u"Pin 0 - Pin 5", None))
        self.pinGroupBox1.setTitle(QCoreApplication.translate("MainWidget", u"PIN 0", None))
        self.OutBtn1.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1.setText("")
        self.defultNameCheckBox1.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_2.setTitle(QCoreApplication.translate("MainWidget", u"PIN 1", None))
        self.OutBtn1_2.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_2.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_2.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_2.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_2.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_2.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_2.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_2.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_2.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_2.setText("")
        self.defultNameCheckBox1_2.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_3.setTitle(QCoreApplication.translate("MainWidget", u"PIN 2", None))
        self.OutBtn1_3.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_3.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_3.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_3.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_3.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_3.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_3.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_3.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_3.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_3.setText("")
        self.defultNameCheckBox1_3.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_4.setTitle(QCoreApplication.translate("MainWidget", u"PIN 3", None))
        self.OutBtn1_4.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_4.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_4.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_4.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_4.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_4.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_4.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_4.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_4.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_4.setText("")
        self.defultNameCheckBox1_4.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_5.setTitle(QCoreApplication.translate("MainWidget", u"PIN 4", None))
        self.OutBtn1_5.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_5.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_5.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_5.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_5.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_5.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_5.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_5.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_5.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_5.setText("")
        self.defultNameCheckBox1_5.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_6.setTitle(QCoreApplication.translate("MainWidget", u"PIN 5", None))
        self.OutBtn1_6.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_6.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_6.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_6.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_6.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_6.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_6.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_6.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_6.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_6.setText("")
        self.defultNameCheckBox1_6.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.label_21.setText(QCoreApplication.translate("MainWidget", u"Pin 6 - Pin 11", None))
        self.pinGroupBox1_7.setTitle(QCoreApplication.translate("MainWidget", u"PIN 6", None))
        self.OutBtn1_7.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_7.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_7.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_7.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_7.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_7.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_7.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_7.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_7.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_7.setText("")
        self.defultNameCheckBox1_7.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_8.setTitle(QCoreApplication.translate("MainWidget", u"PIN 7", None))
        self.OutBtn1_8.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_8.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_8.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_8.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_8.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_8.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_8.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_8.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_8.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_8.setText("")
        self.defultNameCheckBox1_8.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_9.setTitle(QCoreApplication.translate("MainWidget", u"PIN 8", None))
        self.OutBtn1_9.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_9.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_9.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_9.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_9.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_9.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_9.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_9.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_9.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_9.setText("")
        self.defultNameCheckBox1_9.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_10.setTitle(QCoreApplication.translate("MainWidget", u"PIN 9", None))
        self.OutBtn1_10.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_10.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_10.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_10.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_10.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_10.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_10.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_10.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_10.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_10.setText("")
        self.defultNameCheckBox1_10.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_11.setTitle(QCoreApplication.translate("MainWidget", u"PIN 10", None))
        self.OutBtn1_11.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_11.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_11.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_11.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_11.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_11.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_11.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_11.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_11.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_11.setText("")
        self.defultNameCheckBox1_11.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_12.setTitle(QCoreApplication.translate("MainWidget", u"PIN 11", None))
        self.OutBtn1_12.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_12.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_12.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_12.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_12.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_12.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_12.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_12.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_12.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_12.setText("")
        self.defultNameCheckBox1_12.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_13.setTitle(QCoreApplication.translate("MainWidget", u"PIN 12", None))
        self.OutBtn1_13.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_13.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_13.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_13.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_13.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_13.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_13.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_13.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_13.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_13.setText("")
        self.defultNameCheckBox1_13.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_14.setTitle(QCoreApplication.translate("MainWidget", u"PIN 13", None))
        self.OutBtn1_14.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_14.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_14.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_14.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_14.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_14.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_14.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_14.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_14.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_14.setText("")
        self.defultNameCheckBox1_14.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_15.setTitle(QCoreApplication.translate("MainWidget", u"PIN 14", None))
        self.OutBtn1_15.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_15.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_15.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_15.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_15.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_15.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_15.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_15.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_15.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_15.setText("")
        self.defultNameCheckBox1_15.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_16.setTitle(QCoreApplication.translate("MainWidget", u"PIN 15", None))
        self.OutBtn1_16.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_16.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_16.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_16.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_16.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_16.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_16.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_16.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_16.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_16.setText("")
        self.defultNameCheckBox1_16.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_17.setTitle(QCoreApplication.translate("MainWidget", u"PIN 16", None))
        self.OutBtn1_17.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_17.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_17.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_17.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_17.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_17.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_17.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_17.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_17.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_17.setText("")
        self.defultNameCheckBox1_17.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_18.setTitle(QCoreApplication.translate("MainWidget", u"PIN 17", None))
        self.OutBtn1_18.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_18.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_18.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_18.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_18.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_18.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_18.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_18.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_18.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_18.setText("")
        self.defultNameCheckBox1_18.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWidget", u"Pin 12 - Pin 17", None))
        self.pinGroupBox1_19.setTitle(QCoreApplication.translate("MainWidget", u"PIN 18", None))
        self.OutBtn1_19.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_19.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_19.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_19.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_19.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_19.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_19.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_19.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_19.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_19.setText("")
        self.defultNameCheckBox1_19.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_20.setTitle(QCoreApplication.translate("MainWidget", u"PIN 19", None))
        self.OutBtn1_20.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_20.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_20.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_20.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_20.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_20.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_20.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_20.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_20.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_20.setText("")
        self.defultNameCheckBox1_20.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_21.setTitle(QCoreApplication.translate("MainWidget", u"PIN 20", None))
        self.OutBtn1_21.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_21.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_21.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_21.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_21.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_21.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_21.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_21.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_21.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_21.setText("")
        self.defultNameCheckBox1_21.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_22.setTitle(QCoreApplication.translate("MainWidget", u"PIN 21", None))
        self.OutBtn1_22.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_22.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_22.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_22.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_22.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_22.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_22.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_22.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_22.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_22.setText("")
        self.defultNameCheckBox1_22.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_23.setTitle(QCoreApplication.translate("MainWidget", u"PIN 22", None))
        self.OutBtn1_23.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_23.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_23.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_23.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_23.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_23.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_23.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_23.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_23.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_23.setText("")
        self.defultNameCheckBox1_23.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_24.setTitle(QCoreApplication.translate("MainWidget", u"PIN 23", None))
        self.OutBtn1_24.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_24.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_24.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_24.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_24.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_24.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_24.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_24.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_24.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_24.setText("")
        self.defultNameCheckBox1_24.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWidget", u"Pin 18 - Pin 23", None))
        self.pinGroupBox1_25.setTitle(QCoreApplication.translate("MainWidget", u"PIN 24", None))
        self.OutBtn1_25.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_25.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_25.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_25.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_25.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_25.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_25.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_25.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_25.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_25.setText("")
        self.defultNameCheckBox1_25.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_26.setTitle(QCoreApplication.translate("MainWidget", u"PIN 25", None))
        self.OutBtn1_26.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_26.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_26.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_26.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_26.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_26.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_26.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_26.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_26.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_26.setText("")
        self.defultNameCheckBox1_26.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_27.setTitle(QCoreApplication.translate("MainWidget", u"PIN 26", None))
        self.OutBtn1_27.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_27.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_27.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_27.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_27.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_27.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_27.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_27.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_27.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_27.setText("")
        self.defultNameCheckBox1_27.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_28.setTitle(QCoreApplication.translate("MainWidget", u"PIN 27", None))
        self.OutBtn1_28.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_28.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_28.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_28.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_28.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_28.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_28.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_28.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_28.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_28.setText("")
        self.defultNameCheckBox1_28.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_29.setTitle(QCoreApplication.translate("MainWidget", u"PIN 28", None))
        self.OutBtn1_29.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_29.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_29.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_29.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_29.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_29.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_29.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_29.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_29.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_29.setText("")
        self.defultNameCheckBox1_29.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_30.setTitle(QCoreApplication.translate("MainWidget", u"PIN 29", None))
        self.OutBtn1_30.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_30.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_30.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_30.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_30.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_30.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_30.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_30.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_30.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_30.setText("")
        self.defultNameCheckBox1_30.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.label_24.setText(QCoreApplication.translate("MainWidget", u"Pin 24 - Pin 29", None))
        self.pinGroupBox1_31.setTitle(QCoreApplication.translate("MainWidget", u"PIN 30", None))
        self.OutBtn1_31.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_31.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_31.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_31.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_31.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_31.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_31.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_31.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_31.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_31.setText("")
        self.defultNameCheckBox1_31.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.pinGroupBox1_32.setTitle(QCoreApplication.translate("MainWidget", u"PIN 31", None))
        self.OutBtn1_32.setText(QCoreApplication.translate("MainWidget", u"Output", None))
        self.InBtn1_32.setText(QCoreApplication.translate("MainWidget", u"Input", None))
        self.OutGroupBox1_32.setTitle(QCoreApplication.translate("MainWidget", u"Output Level", None))
        self.OutHighBtn1_32.setText(QCoreApplication.translate("MainWidget", u"High", None))
        self.OutLowBtn1_32.setText(QCoreApplication.translate("MainWidget", u"Low", None))
        self.InGroupBox1_32.setTitle(QCoreApplication.translate("MainWidget", u"Input Configuration", None))
        self.HighImpBtn1_32.setText(QCoreApplication.translate("MainWidget", u"High Impedance", None))
        self.PullUpBtn1_32.setText(QCoreApplication.translate("MainWidget", u"Pull Up", None))
        self.label1_32.setText(QCoreApplication.translate("MainWidget", u"Pin Name", None))
        self.lineEdit1_32.setText("")
        self.defultNameCheckBox1_32.setText(QCoreApplication.translate("MainWidget", u"Default Name", None))
        self.GenerateBtn.setText(QCoreApplication.translate("MainWidget", u"Generate", None))
        self.Path.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWidget", u"Pin 30 - Pin 31", None))
        self.ITILogo.setText("")
        self.AboutUsText.setText(QCoreApplication.translate("MainWidget", u"Copyright \u00a9 2022 by Aya Adel", None))
        self.AboutUsText_2.setText(QCoreApplication.translate("MainWidget", u"Intake42 - Area51 - Embedded system Track", None))
        self.Pin6_11Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 6 - Pin 11", None))
        self.Pin12_17Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 12 - Pin 17", None))
        self.Pin0_5Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 0 - Pin 5", None))
        self.Pin18_23Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 18 - Pin 23", None))
        self.Pin24_28Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 24 - Pin 29", None))
        self.Pin30_32Btn.setText(QCoreApplication.translate("MainWidget", u"Pin 30 - Pin 32", None))
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_MainWidget()
Form.setupUi(Widget)
Widget.setWindowFlag(Qt.FramelessWindowHint)
Widget.show()
sys.exit(app.exec_())