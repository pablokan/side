import os
import sys

from PySide6.QtCore import QSize, QSortFilterProxyModel, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDataWidgetMapper,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTableView,
    QVBoxLayout,
    QWidget,
)


basedir = os.path.dirname(__file__)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(basedir, "Alumno.db"))
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        hlayout = QHBoxLayout()

        layout = QVBoxLayout()

        self.filtert = QLineEdit()
        self.filtert.setPlaceholderText("Search...")
        self.table = QTableView()

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.filtert)
        vlayout.addWidget(self.table)

        # Left/right pane.
        hlayout.addLayout(vlayout)
        hlayout.addLayout(layout)

        form = QFormLayout()

        self.id = QSpinBox()
        self.id.setDisabled(True)
        self.id.setRange(0, 2147483647)
        self.nombre = QLineEdit()
        self.fecha_nac = QComboBox()
        self.comision = QComboBox()
        self.nota = QComboBox()

        form.addRow(QLabel("ID"), self.id)
        form.addRow(QLabel("nombre"), self.nombre)
        form.addRow(QLabel("fecha_nac"), self.fecha_nac)
        form.addRow(QLabel("comision"), self.comision)
        form.addRow(QLabel("nota"), self.nota)
        
        self.model = QSqlTableModel(db=db)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.sort(1, Qt.AscendingOrder)
        self.proxy_model.setFilterKeyColumn(-1)  # all columns
        self.table.setModel(self.proxy_model)

        # Update search when filter changes.
        self.filtert.textChanged.connect(
            self.proxy_model.setFilterFixedString
        )

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.proxy_model)

        self.mapper.addMapping(self.id, 0)
        self.mapper.addMapping(self.nombre, 1)
        self.mapper.addMapping(self.fecha_nac, 5)
        self.mapper.addMapping(self.comision, 6)
        self.mapper.addMapping(self.nota, 7)
        
        self.model.setTable("Track")
        self.model.select()

        # Change the mapper selection using the table.
        self.table.selectionModel().currentRowChanged.connect(
            self.mapper.setCurrentModelIndex
        )

        self.mapper.toFirst()

        # tag::controls[]
        self.setMinimumSize(QSize(800, 400))

        controls = QHBoxLayout()

        prev_rec = QPushButton("Previous")
        prev_rec.clicked.connect(self.mapper.toPrevious)

        next_rec = QPushButton("Next")
        next_rec.clicked.connect(self.mapper.toNext)

        save_rec = QPushButton("Save Changes")
        save_rec.clicked.connect(self.mapper.submit)

        controls.addWidget(prev_rec)
        controls.addWidget(next_rec)
        controls.addWidget(save_rec)

        layout.addLayout(form)
        layout.addLayout(controls)

        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)
        # end::controls[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
