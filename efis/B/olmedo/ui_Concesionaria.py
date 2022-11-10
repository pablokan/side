# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Concesionaria.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(626, 486)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(61,61,61);\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(61,61,61);\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.frame_superior)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"../../Users/GoodGame/Downloads/menu-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.frame_superior)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"../../Users/GoodGame/Downloads/minimize-svgrepo-com (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_superior)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"../../Users/GoodGame/Downloads/minimize-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(28, 38))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_superior)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../Users/GoodGame/Downloads/maximize-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(28, 38))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_superior)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"../../Users/GoodGame/Downloads/icons8-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_stock = QPushButton(self.frame_control)
        self.bt_stock.setObjectName(u"bt_stock")
        self.bt_stock.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"../../Users/GoodGame/Downloads/garage-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_stock.setIcon(icon5)
        self.bt_stock.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_stock)

        self.bt_agregar = QPushButton(self.frame_control)
        self.bt_agregar.setObjectName(u"bt_agregar")
        self.bt_agregar.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"../../Users/GoodGame/Downloads/add-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_agregar.setIcon(icon6)
        self.bt_agregar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_agregar)

        self.bt_actualizar_stock = QPushButton(self.frame_control)
        self.bt_actualizar_stock.setObjectName(u"bt_actualizar_stock")
        self.bt_actualizar_stock.setMinimumSize(QSize(0, 40))
        icon7 = QIcon()
        icon7.addFile(u"../../Users/GoodGame/Downloads/refresh-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_actualizar_stock.setIcon(icon7)
        self.bt_actualizar_stock.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_actualizar_stock)

        self.bt_eliminar = QPushButton(self.frame_control)
        self.bt_eliminar.setObjectName(u"bt_eliminar")
        self.bt_eliminar.setMinimumSize(QSize(0, 40))
        icon8 = QIcon()
        icon8.addFile(u"../../Users/GoodGame/Downloads/delete-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminar.setIcon(icon8)
        self.bt_eliminar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_eliminar)

        self.bt_ajustes = QPushButton(self.frame_control)
        self.bt_ajustes.setObjectName(u"bt_ajustes")
        self.bt_ajustes.setMinimumSize(QSize(0, 40))
        icon9 = QIcon()
        icon9.addFile(u"../../Users/GoodGame/Downloads/settings-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ajustes.setIcon(icon9)
        self.bt_ajustes.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_ajustes)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
"background-color:rgb(61,61,61);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color:rgb(0,206,151);\n"
"border:0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color:rgb(255,255,255);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-radius: 15px;\n"
"color: rgb(255,255,255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0,206,151);\n"
"border-radius: 15px;\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb (255,255,255);\n"
"color: rgb(0,0,0);\n"
"gridline-color: rgb(0,206,151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: (0,206,151);\n"
"border: 1px solid rgb(0,0,0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color"
                        ": rgb(0,0,0);\n"
"border: 1px solid rgb(0,206,151);\n"
"}")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.page_Stock = QWidget()
        self.page_Stock.setObjectName(u"page_Stock")
        self.verticalLayout_5 = QVBoxLayout(self.page_Stock)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_Stock)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(209,69,88);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.table_Cars = QTableWidget(self.page_Stock)
        if (self.table_Cars.columnCount() < 7):
            self.table_Cars.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_Cars.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_Cars.setObjectName(u"table_Cars")
        self.table_Cars.setStyleSheet(u"color: black")

        self.verticalLayout_5.addWidget(self.table_Cars)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.button_refresh = QPushButton(self.page_Stock)
        self.button_refresh.setObjectName(u"button_refresh")
        self.button_refresh.setMinimumSize(QSize(120, 30))
        self.button_refresh.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.button_refresh.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.button_refresh)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_Stock)
        self.page_Agregar = QWidget()
        self.page_Agregar.setObjectName(u"page_Agregar")
        self.verticalLayout = QVBoxLayout(self.page_Agregar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_Agregar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_Agregar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_Agregar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_Agregar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_Agregar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.page_Agregar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_Agregar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_6.addWidget(self.label_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.registrar_marca = QLineEdit(self.page_Agregar)
        self.registrar_marca.setObjectName(u"registrar_marca")

        self.verticalLayout_7.addWidget(self.registrar_marca)

        self.registrar_modelo = QLineEdit(self.page_Agregar)
        self.registrar_modelo.setObjectName(u"registrar_modelo")

        self.verticalLayout_7.addWidget(self.registrar_modelo)

        self.registrar_dominio = QLineEdit(self.page_Agregar)
        self.registrar_dominio.setObjectName(u"registrar_dominio")

        self.verticalLayout_7.addWidget(self.registrar_dominio)

        self.registrar_year = QLineEdit(self.page_Agregar)
        self.registrar_year.setObjectName(u"registrar_year")

        self.verticalLayout_7.addWidget(self.registrar_year)

        self.registrar_km = QLineEdit(self.page_Agregar)
        self.registrar_km.setObjectName(u"registrar_km")

        self.verticalLayout_7.addWidget(self.registrar_km)

        self.registrar_color = QLineEdit(self.page_Agregar)
        self.registrar_color.setObjectName(u"registrar_color")

        self.verticalLayout_7.addWidget(self.registrar_color)

        self.registrar_precio = QLineEdit(self.page_Agregar)
        self.registrar_precio.setObjectName(u"registrar_precio")

        self.verticalLayout_7.addWidget(self.registrar_precio)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(37, 196, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.signal_agregar = QLabel(self.page_Agregar)
        self.signal_agregar.setObjectName(u"signal_agregar")
        self.signal_agregar.setMinimumSize(QSize(180, 0))
        self.signal_agregar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.signal_agregar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.bt_refrescar = QPushButton(self.page_Agregar)
        self.bt_refrescar.setObjectName(u"bt_refrescar")
        self.bt_refrescar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.bt_refrescar.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.bt_refrescar)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.page_Agregar)
        self.page_Actualizar = QWidget()
        self.page_Actualizar.setObjectName(u"page_Actualizar")
        self.act_buscar = QLineEdit(self.page_Actualizar)
        self.act_buscar.setObjectName(u"act_buscar")
        self.act_buscar.setGeometry(QRect(12, 20, 251, 21))
        self.bt_actualizar_tabla = QPushButton(self.page_Actualizar)
        self.bt_actualizar_tabla.setObjectName(u"bt_actualizar_tabla")
        self.bt_actualizar_tabla.setGeometry(QRect(260, 360, 121, 21))
        self.bt_actualizar_tabla.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.bt_actualizar_tabla.setIcon(icon7)
        self.bt_buscar_act = QPushButton(self.page_Actualizar)
        self.bt_buscar_act.setObjectName(u"bt_buscar_act")
        self.bt_buscar_act.setGeometry(QRect(290, 20, 75, 23))
        self.bt_buscar_act.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.signal_actualizar = QLabel(self.page_Actualizar)
        self.signal_actualizar.setObjectName(u"signal_actualizar")
        self.signal_actualizar.setGeometry(QRect(10, 360, 111, 21))
        self.widget = QWidget(self.page_Actualizar)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 70, 125, 271))
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.act_marca = QLineEdit(self.widget)
        self.act_marca.setObjectName(u"act_marca")

        self.verticalLayout_9.addWidget(self.act_marca)

        self.act_modelo = QLineEdit(self.widget)
        self.act_modelo.setObjectName(u"act_modelo")

        self.verticalLayout_9.addWidget(self.act_modelo)

        self.act_dominio = QLineEdit(self.widget)
        self.act_dominio.setObjectName(u"act_dominio")

        self.verticalLayout_9.addWidget(self.act_dominio)

        self.act_year = QLineEdit(self.widget)
        self.act_year.setObjectName(u"act_year")

        self.verticalLayout_9.addWidget(self.act_year)

        self.act_km = QLineEdit(self.widget)
        self.act_km.setObjectName(u"act_km")

        self.verticalLayout_9.addWidget(self.act_km)

        self.act_color = QLineEdit(self.widget)
        self.act_color.setObjectName(u"act_color")

        self.verticalLayout_9.addWidget(self.act_color)

        self.act_precio = QLineEdit(self.widget)
        self.act_precio.setObjectName(u"act_precio")

        self.verticalLayout_9.addWidget(self.act_precio)

        self.widget1 = QWidget(self.page_Actualizar)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 70, 121, 261))
        self.verticalLayout_8 = QVBoxLayout(self.widget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(209,69,88);")

        self.verticalLayout_8.addWidget(self.label_16)

        self.stackedWidget.addWidget(self.page_Actualizar)
        self.page_Eliminar = QWidget()
        self.page_Eliminar.setObjectName(u"page_Eliminar")
        self.label_17 = QLabel(self.page_Eliminar)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 30, 101, 16))
        self.label_17.setStyleSheet(u"color: rgb(209,69,88);")
        self.eliminar_buscar = QLineEdit(self.page_Eliminar)
        self.eliminar_buscar.setObjectName(u"eliminar_buscar")
        self.eliminar_buscar.setGeometry(QRect(120, 30, 181, 20))
        self.bt_buscar_borrar = QPushButton(self.page_Eliminar)
        self.bt_buscar_borrar.setObjectName(u"bt_buscar_borrar")
        self.bt_buscar_borrar.setGeometry(QRect(310, 30, 75, 23))
        self.bt_buscar_borrar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.tabla_borrar = QTableWidget(self.page_Eliminar)
        if (self.tabla_borrar.columnCount() < 8):
            self.tabla_borrar.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.tabla_borrar.setObjectName(u"tabla_borrar")
        self.tabla_borrar.setGeometry(QRect(5, 81, 381, 241))
        self.bt_borrar = QPushButton(self.page_Eliminar)
        self.bt_borrar.setObjectName(u"bt_borrar")
        self.bt_borrar.setGeometry(QRect(290, 350, 75, 23))
        self.bt_borrar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(209, 8, 88);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(209,69,88);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.signal_eliminacion = QLabel(self.page_Eliminar)
        self.signal_eliminacion.setObjectName(u"signal_eliminacion")
        self.signal_eliminacion.setGeometry(QRect(10, 352, 91, 21))
        self.stackedWidget.addWidget(self.page_Eliminar)
        self.page_Ajustes = QWidget()
        self.page_Ajustes.setObjectName(u"page_Ajustes")
        self.stackedWidget.addWidget(self.page_Ajustes)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.horizontalLayout_6.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.bt_stock.setText(QCoreApplication.translate("MainWindow", u"STOCK", None))
        self.bt_agregar.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR", None))
        self.bt_actualizar_stock.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.bt_eliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.bt_ajustes.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VEH\u00cdCULOS", None))
        ___qtablewidgetitem = self.table_Cars.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"MARCA", None));
        ___qtablewidgetitem1 = self.table_Cars.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MODELO", None));
        ___qtablewidgetitem2 = self.table_Cars.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DOMINIO", None));
        ___qtablewidgetitem3 = self.table_Cars.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"A\u00d1O", None));
        ___qtablewidgetitem4 = self.table_Cars.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"KILOMETROS", None));
        ___qtablewidgetitem5 = self.table_Cars.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"COLOR", None));
        ___qtablewidgetitem6 = self.table_Cars.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        self.button_refresh.setText(QCoreApplication.translate("MainWindow", u"REFRESCAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MARCA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MODELO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DOMINIO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"A\u00d1O", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"KM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COLOR", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.signal_agregar.setText("")
        self.bt_refrescar.setText(QCoreApplication.translate("MainWindow", u"REFRESCAR", None))
        self.bt_actualizar_tabla.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR ", None))
        self.bt_buscar_act.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.signal_actualizar.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MARCA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MODELO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"DOMINIO", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"A\u00d1O", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"KM", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"COLOR", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"NOMBRE:", None))
        self.bt_buscar_borrar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem7 = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MARCA", None));
        ___qtablewidgetitem8 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"MODELO", None));
        ___qtablewidgetitem9 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"A\u00d1O", None));
        ___qtablewidgetitem10 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DOMINIO", None));
        ___qtablewidgetitem11 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"KM", None));
        ___qtablewidgetitem12 = self.tabla_borrar.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CONDICION", None));
        ___qtablewidgetitem13 = self.tabla_borrar.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        self.bt_borrar.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.signal_eliminacion.setText("")
    # retranslateUi

app = QApplication()
w = Ui_MainWindow()
w.setupUi()
app.exec()
