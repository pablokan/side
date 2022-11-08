
#Imports.

import os, sys
sys.path.append(os.path.abspath('Resources'))

from controller import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Resources.Stylesjj import Text, Input, Button

 

class WindowThree(QMainWindow):                 #Window 3 - calculate and pay.
    def __init__(self):
        super().__init__()
        
        
        #Window properties - 1. Title - 2.Style - 3. Fixed size.
        
        self.setWindowTitle("SubStore - Sistema de pago.")
        self.setStyleSheet("background-color: #272727;")
        self.setFixedSize(QSize(480, 480))

        #-----------------------------------------------------------

        #Frame Title/Header whit Vertical Layout.
        #Define Frame Settings.
        self.frame1= QFrame(self)
        self.frame1.setGeometry(57,30,368,105)
        
        #Create layout.
        upperLayout =QVBoxLayout() 
        #QLabel creation to store icon.
        iconLabel= QLabel(self)
        #Import Logo.png.
        logo= QPixmap("Resources/pagos.png")
        iconLabel.setPixmap(logo)
        #Scaling for logo.
        iconLabel.setScaledContents(True)
        #Add Qlabel whit Widget.
        upperLayout.addWidget(iconLabel)
        
        #Add layout to frame.
        self.frame1.setLayout(upperLayout)

        #----------------------------------------------------------

        #Frame list of products add to cart whit vertical layout.
        
        #Define frame settings.
        
        self.frame2= QFrame(self)
        self.frame2.setGeometry(0, 140, 480, 620)
        #Define other Frames
        self.frame2Layout= QVBoxLayout()
        self.frame2QFL= QFormLayout()

        self.subtotal= 0

        self.phonecartList= readCart()
        for phone in self.phonecartList:
            self.subtotal+= phone[1]

        #------------------------------------------------------------

        # Calculate total.
        #Icome Tax - IVA And conversion to local money whith icome.
        icomeIVA= 1.21
        icomePAIS= 1.30
        priceTuristDollar= 242
        priceDollar= 155
        if self.subtotal >= 300: 
            self.total= (round(((self.subtotal * icomeIVA)*icomePAIS),2))
            self.totalPesoArgentino = round(self.total * priceTuristDollar, 2)
        else:
            self.total= (round(((self.subtotal * icomeIVA)*icomePAIS),2))
            self.totalPesoArgentino= round(self.total * priceDollar, 2)
            
        #---------------------------------------------------------------------------

        #Create Total QLabel and Total texts
        self.textSub= Text(f"SUBTOTAL:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aL")
        self.subtotal= Text(f"U$D {self.subtotal}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aR")
        self.textSub1 = Text(f"(Este valor no contiene impuestos.)",fontS= 5,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign= "aR", vAlign= "aR" )
        self.totaltext= Text(f"TOTAL:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aL")
        self.total= Text(f"U$D {self.total}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aR")
        self.totaltextPeso= Text(f"TOTAL EN AR$:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aL", vAlign= "aL")
        self.totalInPeso = Text(f"AR$ {self.totalPesoArgentino}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aR")
        self.textTotal = Text(f"(Valor final de compra.)",fontS= 5,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign= "aR", vAlign= "aR" )
        
        #Add Labels to QFormLayout
        self.frame2QFL.addRow(self.textSub, self.subtotal)
        self.frame2QFL.addRow(self.textSub1)
        self.frame2QFL.addRow(self.totaltext, self.total)
        self.frame2QFL.addRow(self.totaltextPeso, self.totalInPeso)
        self.frame2QFL.addRow(self.textTotal)
        

        #Add QFormLayout to Vertical Layout
        self.frame2Layout.addLayout(self.frame2QFL)
            
        #Add layout to frame.
        self.frame2.setLayout(self.frame2Layout)

        #------------------------------------------------------------------------

        #Frame Button payments or return whit horizontal layout.
        #Define Frame Settings.
        self.frame3=QFrame(self)
        self.frame3.setGeometry(0,400,480, 80)

        #Create "Button Panel" layout.
        button_panel= QHBoxLayout()
        buttonReturn = Button('REGRESAR', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#00FCA8", radius=11)  #Create button.
        buttonPay = Button('PAGAR', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#1ADDF9", radius=11)  #Create button.
        button_panel.addWidget(buttonReturn)         #Add button to layout.
        button_panel.addWidget(buttonPay)           #Add button to layout.

        #Connect button to function.
        buttonReturn.clicked.connect(self.backToPreviousWindow)
        buttonPay.clicked.connect(self.paymentCompleted) 
        
        #Add layout to Frame.
        self.frame3.setLayout(button_panel)

        #-------------------------------------------------------------------------


    def  paymentCompleted(self):
        self.close() # cerrar tercera ventana cuando paga
        finishmsgb = QMessageBox()

        finishmsgb.setGeometry(250,400, 240,240)
        finishmsgb.setStyleSheet("background-color: #272727; color: #F8F8FF")
        finishmsgb.setText(f"Usted ha finalizado la compra!! \nPago total de: AR${self.totalPesoArgentino}")
        finishmsgb.setFont(QFont("Italic", 10))
        finishmsgb.setWindowTitle("Compra finalizada!")
        finishmsgb.setStandardButtons(QMessageBox.Close)
        finishmsgb.exec()

        deleteCart()

    #------------------------------------------------------


    def backToPreviousWindow(self):
        self.close()
  


class WindowTwo(QMainWindow):                   #Window 2 - Shopping Cart prosecution.
    def __init__(self):
        super().__init__()
        
        #Window properties - 1. Title - 2.Style - 3. Fixed size.

        self.setWindowTitle("SubStore - Carrito de compras.")
        self.setStyleSheet("background-color: #272727;")
        self.setFixedSize(QSize(480, 720))
        
        #------------------------------------------------------

        #Frame Title/Header whit Vertical Layout.

        #Define Frame Settings.

        self.frame1= QFrame(self)
        self.frame1.setGeometry(57,30,368,105)
        
        #Create layout.

        upperLayout =QVBoxLayout() 

        #QLabel creation to store icon.

        iconLabel= QLabel(self)

        #Import Logo.png.

        logo= QPixmap("Resources/carry.png")
        iconLabel.setPixmap(logo)
        
        #Scaling for logo.

        iconLabel.setScaledContents(True)

        #Add Qlabel whit Widget.

        upperLayout.addWidget(iconLabel)
        
        #Add layout to frame.

        self.frame1.setLayout(upperLayout)


        #--------------------------------------------------------       
    
        #Frame list of products add to cart whit vertical layout.

        #Define frame settings.

        self.frame2= QFrame(self)
        self.frame2.setGeometry(0, 140, 480, 620)
        
        #Define other Frames

        self.frame2Layout= QVBoxLayout()
        self.frame2QFL= QFormLayout()
        
        #Subtotal: Phone shell.

        self.subTotal=0
        
        #Read Cart from phonesDb.

        self.phonecartList= readCart()
        for phone in self.phonecartList:
            
            #Create QLabel from each selected phone.

            self.textbx=Text(f"{phone[0]}:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign="aT", vAlign= "aT")
            self.priceStr= Text(f"U$D {phone[1]}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF",hAlign="aR", vAlign= "aT")
            
            #Add Labels to QFromLayout.

            self.frame2QFL.addRow(self.textbx, self.priceStr)
            
            # Addition to subtotal.

            self.subTotal+= phone[1]
        
        
        #Create SubTotal QLabel and SubTotal texts

        self.textSub= Text(f"SUBTOTAL:",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aL")
        self.subtotal= Text(f"U$D {self.subTotal}",fontS= 13,fontF= "Italic", backg= "#272727", foreg= "#F8F8FF", hAlign= "aT", vAlign= "aR")
        self.textSub1 = Text(f"(Este valor no contiene impuestos.)",fontS= 5,fontF= "Arial Black", backg= "#272727", foreg= "#F8F8FF",hAlign= "aR", vAlign= "aR" )
        
        #Add Labels to QFormLayout

        self.frame2QFL.addRow(self.textSub, self.subtotal)
        self.frame2QFL.addRow("",self.textSub1)

        #Add QFormLayout to Vertical Layout

        self.frame2Layout.addLayout(self.frame2QFL)
            
        #Add layout to frame.

        self.frame2.setLayout(self.frame2Layout)

        #----------------------------------------------------------

        #Frame Button payments or return whit horizontal layout.
        
        #Define Frame Settings.

        self.frame3=QFrame(self)
        self.frame3.setGeometry(0,640,480, 80)

        #Create "Button Panel" layout.

        button_panel= QHBoxLayout()
        buttonClear = Button('LIMPIAR Y REGRESAR', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#00FCA8", radius=11)  #Create button.
        buttonPay = Button('IR A PAGOS', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#1ADDF9", radius=11)            #Create button.
        button_panel.addWidget(buttonClear)                                                                                 #Add button to layout.
        button_panel.addWidget(buttonPay)                                                                                   #Add button to layout.
        buttonClear.clicked.connect(self.clearCart)                                                                         #Connect button to function.
        buttonPay.clicked.connect(self.openPayments)                                                                        #Connect button to function.
        
       
        #Add layout to Frame.

        self.frame3.setLayout(button_panel)

    
    def openPayments(self):
        self.hide() # ocultar la segunda ventana cuando va a pagos
        #Window opening function 3 to add to cart.
        self.wThree = WindowThree()
        self.wThree.show()
    
    def clearCart(self):                                                                                                    #Delete cart function, clear Database and Close Window to go back. 
        deleteCart()
        self.close()
                




class MainWindow(QMainWindow):                  #Window 1 - Produccts addition to Shopping Cart
    def __init__(self):
        super().__init__()
        
        #Window properties - 1. Title - 2.Style - 3. Fixed size.

        self.setWindowTitle("SubStore - App de compras")
        self.setStyleSheet("background-color: #272727;")
        self.setFixedSize(QSize(480, 480))
        
        #Frame Title/Header whit Vertical Layout.
       
        #Define Frame Settings.

        self.frame1= QFrame(self)
        self.frame1.setGeometry(56,0,368,105)
        
        #Create layout.
        
        upperLayout =QVBoxLayout() 

        #QLabel creation to store icon.
        
        iconLabel= QLabel(self)

        #Import Logo.png.

        logo= QPixmap("Resources/logo.png")
        iconLabel.setPixmap(logo)
        
        #Scaling for logo.

        iconLabel.setScaledContents(True)
        
        #Add Qlabel whit Widget.

        upperLayout.addWidget(iconLabel)
        
        #Add layout to frame.

        self.frame1.setLayout(upperLayout)


       #-------------------------------------------------------
        
        #Frame Buttons whit horizontal layout.
        
        #Define frame settings.

        self.frame2=QFrame(self)
        self.frame2.setGeometry(0,80,480, 100)
        
        #Create "Button Panel" layout.

        button_panel= QHBoxLayout() 
        addProducts = Button("AGREGAR PRODUCTO", fontS= 10,fontF= "Italic", foreg= "#272727",backg= "#00FCA8", radius=11) #Create button.
        button_panel.addWidget(addProducts)                                                                               #Add button to layout.
        showCart = Button('VER MI CARRITO', fontS= 10,fontF= "Italic",foreg= "#272727",backg= "#1ADDF9", radius=11)       #Create Button.
        button_panel.addWidget(showCart)                                                                                  #Add button to layout.
        
        #Connect buttons to Functions.

        showCart.clicked.connect(self.openWindow)
        addProducts.clicked.connect(self.addToCart)
        addProducts.clicked.connect(self.countClick)

        
        #Add layout to Frame.

        self.frame2.setLayout(button_panel)
        

        #---------------------------------------------

        #Frame Combobox whit vertical layout for smartphones products.

        #Define frame settings.
        
        self.frame3= QFrame(self)
        self.frame3.setGeometry(0,150,480,100)
        
        #Create layout.

        frame3layout= QVBoxLayout()
        
        #Create and add items to Combobox.

        self.products = QComboBox() 
        self.products.setStyleSheet("background-color: #808080")
        self.products.setStyleSheet("color: #FFFFE0")

        
        #Data from database phones.- Celulares.db.

        phones_list= readRows() 
        for phone in phones_list:
            self.products.addItem(f"{phone[1]}"  + f"   -   {phone[2]}")
            

        frame3layout.addWidget(self.products)                               #Add widget to layout.
        
        #Add layout to frame.

        self.frame3.setLayout(frame3layout)


        #---------------------------------------------------
        
        #Create variable count click.

        self.counter= 0

    def countClick(self):
        self.counter +=1 

    def addToCart(self):                                    #Function add products to shopping cart.
        #Create List Cart.
        item= self.products.currentText()
        smartphone= item.split("   -")
        model, price = smartphone[0], smartphone[1]
        price= int(price[4:])
        createCartTable()
        insertProdToCart(model, price)

        
    def openWindow(self):
        #Window opening function 2 to add to cart.
        self.wTwo = WindowTwo()
        self.wTwo.show()





if __name__ == '__main__':                      #App Execution.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()