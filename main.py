from PyQt5 import QtCore, QtGui, QtWidgets
import os
from ui.graduated import Ui_graduate_window
from ui.founders import Ui_founders
from ui.start import Ui_Window
import sqlite3



# ===== START CLASS =====
class UniversityStyles:
    BACKGROUND_COLOR = "rgb(0, 37, 64)"
    ACCENT_COLOR = "rgb(185, 99, 36)"
    BUTTON_COLOR = "rgb(217, 217, 217)"
    ORANGE_BUTTON = "rgb(239, 170, 79)"
    WHITE_TEXT = "rgb(255, 255, 255)"
    DARK_TEXT = "rgb(0, 0, 0)"

    DIALOG_STYLE = f"""
        QDialog {{
            background-color: {BACKGROUND_COLOR};
            color: {WHITE_TEXT};
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
    """

    TABLE_STYLE = f"""
        QTableWidget {{
            background-color: {WHITE_TEXT};
            alternate-background-color: rgb(245, 245, 245);
            gridline-color: {ACCENT_COLOR};
            selection-background-color: {ACCENT_COLOR};
            selection-color: {WHITE_TEXT};
            color: {DARK_TEXT};
            border: 2px solid {ACCENT_COLOR};
            border-radius: 8px;
        }}
        QTableWidget::item {{
            padding: 8px;
            border-bottom: 1px solid rgb(230, 230, 230);
        }}
        QTableWidget::item:selected {{
            background-color: {ACCENT_COLOR};
            color: {WHITE_TEXT};
        }}
        QHeaderView::section {{
            background-color: {ACCENT_COLOR};
            color: {WHITE_TEXT};
            padding: 10px;
            font-weight: bold;
            font-size: 12px;
            border: none;
            border-right: 1px solid rgb(160, 80, 30);
        }}
        QHeaderView::section:hover {{
            background-color: rgb(200, 110, 40);
        }}
    """
    SEARCH_STYLE = f"""
        QLineEdit {{
            background-color: {WHITE_TEXT};
            border: 2px solid {ACCENT_COLOR};
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
            color: {DARK_TEXT};
        }}
        QLineEdit:focus {{
            border-color: {ORANGE_BUTTON};
            box-shadow: 0 0 5px rgba(239, 170, 79, 0.5);
        }}
        QLineEdit::placeholder {{
            color: rgb(120, 120, 120);
            font-style: italic;
        }}
    """

    FORM_STYLE = f"""
        QWidget {{
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 20px;
        }}
        QLabel {{
            color: {WHITE_TEXT};
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        QLineEdit, QSpinBox, QComboBox {{
            background-color: {WHITE_TEXT};
            border: 2px solid {ACCENT_COLOR};
            border-radius: 6px;
            padding: 8px;
            font-size: 12px;
            color: {DARK_TEXT};
        }}
        QLineEdit:focus, QSpinBox:focus, QComboBox:focus {{
            border-color: {ORANGE_BUTTON};
        }}
        QComboBox::drop-down {{
            border: none;
            background-color: {ACCENT_COLOR};
            width: 30px;
        }}
        QComboBox::down-arrow {{
            image: none;
            border: 5px solid transparent;
            border-top: 8px solid {WHITE_TEXT};
            margin-right: 5px;
        }}
    """

    BUTTON_STYLE = f"""
        QPushButton {{
            background-color: {ORANGE_BUTTON};
            color: {WHITE_TEXT};
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 13px;
            font-weight: bold;
            min-width: 100px;
        }}
        QPushButton:hover {{
            background-color: rgb(220, 150, 60);
            transform: translateY(-1px);
        }}
        QPushButton:pressed {{
            background-color: rgb(200, 130, 40);
            transform: translateY(1px);
        }}
    """

    CANCEL_BUTTON_STYLE = f"""
        QPushButton {{
            background-color: rgb(120, 120, 120);
            color: {WHITE_TEXT};
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 13px;
            font-weight: bold;
            min-width: 100px;
        }}
        QPushButton:hover {{
            background-color: rgb(140, 140, 140);
        }}
        QPushButton:pressed {{
            background-color: rgb(100, 100, 100);
        }}
    """

class BaseUniversityDialog(QtWidgets.QDialog):
    def __init__(self, title, width=1660, height=720):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)
        self.setStyleSheet(UniversityStyles.DIALOG_STYLE)

        try:
            icon = QtGui.QIcon()
            current_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(current_dir, "ui", "img", "logo.png")
            if os.path.exists(icon_path):
                icon.addPixmap(QtGui.QPixmap(icon_path))
                self.setWindowIcon(icon)
        except:
            pass

    def setup_search_table_layout(self, search_placeholder):
        """Creates the standard search + table layout"""
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        title_label = QtWidgets.QLabel(self.windowTitle())
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {UniversityStyles.ACCENT_COLOR};
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
        """)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)

        search_input = QtWidgets.QLineEdit()
        search_input.setPlaceholderText(search_placeholder)
        search_input.setStyleSheet(UniversityStyles.SEARCH_STYLE)
        layout.addWidget(search_input)

        table = QtWidgets.QTableWidget()
        table.setStyleSheet(UniversityStyles.TABLE_STYLE)
        table.setAlternatingRowColors(True)
        table.setSortingEnabled(True)
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        layout.addWidget(table)

        return layout, search_input, table

    def setup_form_layout(self):
        """Creates a styled form layout"""
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        title_label = QtWidgets.QLabel(self.windowTitle())
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {UniversityStyles.ACCENT_COLOR};
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 15px;
            }}
        """)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(title_label)

        form_widget = QtWidgets.QWidget()
        form_widget.setStyleSheet(UniversityStyles.FORM_STYLE)
        form_layout = QtWidgets.QFormLayout(form_widget)
        form_layout.setSpacing(15)

        main_layout.addWidget(form_widget)

        button_widget = QtWidgets.QWidget()
        button_widget.setStyleSheet("background: transparent;")
        button_layout = QtWidgets.QHBoxLayout(button_widget)
        button_layout.setSpacing(15)

        main_layout.addWidget(button_widget)

        return main_layout, form_layout, button_layout

class Ui_Window(Ui_Window):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1020, 700)
        Window.setMaximumSize(QtCore.QSize(1020, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.get_image_path("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("background-color: rgb(0, 37, 64);")
        self.label_3 = QtWidgets.QLabel(Window)
        self.label_3.setGeometry(QtCore.QRect(190, 660, 611, 49))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(185, 99, 36);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(0, 10, 1020, 150))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Window)
        self.label_2.setGeometry(QtCore.QRect(0, 170, 1020, 13))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 431, 309))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Window)
        self.label_5.setGeometry(QtCore.QRect(540, 260, 431, 309))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Window)
        self.label_6.setGeometry(QtCore.QRect(-40, 310, 211, 317))
        self.label_6.setStyleSheet("background-color: none;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Window)
        self.label_7.setGeometry(QtCore.QRect(880, 340, 184, 276))
        self.label_7.setStyleSheet("background-color: none;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Window)
        self.label_8.setGeometry(QtCore.QRect(610, 340, 85, 85))
        self.label_8.setStyleSheet("background-color: none;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Window)
        self.label_9.setGeometry(QtCore.QRect(720, 350, 72, 72))
        self.label_9.setStyleSheet("background-color: none;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Window)
        self.label_10.setGeometry(QtCore.QRect(800, 330, 118, 118))
        self.label_10.setStyleSheet("background-color: none;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Window)
        self.label_11.setGeometry(QtCore.QRect(600, 440, 98, 98))
        self.label_11.setStyleSheet("background-color: none;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Window)
        self.label_12.setGeometry(QtCore.QRect(710, 440, 96, 98))
        self.label_12.setStyleSheet("background-color: none;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Window)
        self.label_13.setGeometry(QtCore.QRect(830, 450, 70, 83))
        self.label_13.setStyleSheet("background-color: none;\n"
                                    "")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Window)
        self.label_14.setGeometry(QtCore.QRect(620, 300, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: none;\n"
                                    "color: #B96324;")
        self.label_14.setObjectName("label_14")
        self.graduated_btn = QtWidgets.QPushButton(Window)
        self.graduated_btn.setGeometry(QtCore.QRect(112, 107, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graduated_btn.setFont(font)
        self.graduated_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                         "border-radius: 11px;")
        self.graduated_btn.setObjectName("graduated_btn")
        self.students_btn = QtWidgets.QPushButton(Window)
        self.students_btn.setGeometry(QtCore.QRect(112, 69, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.students_btn.setFont(font)
        self.students_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                        "border-radius: 11px;")
        self.students_btn.setObjectName("students_btn")
        self.lecturer_btn = QtWidgets.QPushButton(Window)
        self.lecturer_btn.setGeometry(QtCore.QRect(112, 30, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lecturer_btn.setFont(font)
        self.lecturer_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                        "border-radius: 11px;")
        self.lecturer_btn.setObjectName("lecturer_btn")
        self.heads_btn = QtWidgets.QPushButton(Window)
        self.heads_btn.setGeometry(QtCore.QRect(685, 107, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heads_btn.setFont(font)
        self.heads_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "border-radius: 11px;")
        self.heads_btn.setObjectName("heads_btn")
        self.courses_btn = QtWidgets.QPushButton(Window)
        self.courses_btn.setGeometry(QtCore.QRect(685, 69, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.courses_btn.setFont(font)
        self.courses_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                       "border-radius: 11px;")
        self.courses_btn.setObjectName("courses_btn")
        self.subject_chois_btn = QtWidgets.QPushButton(Window)
        self.subject_chois_btn.setGeometry(QtCore.QRect(685, 30, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_chois_btn.setFont(font)
        self.subject_chois_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                             "border-radius: 11px;")
        self.subject_chois_btn.setObjectName("subject_chois_btn")
        self.add_student_btn = QtWidgets.QPushButton(Window)
        self.add_student_btn.setGeometry(QtCore.QRect(150, 370, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_student_btn.setFont(font)
        self.add_student_btn.setStyleSheet("background-color: rgb(239, 170, 79);\n"
                                           "border-radius: 11px;\n"
                                           "color: rgb(255, 255, 255);")
        self.add_student_btn.setObjectName("add_student_btn")
        self.add_lecturer_btn = QtWidgets.QPushButton(Window)
        self.add_lecturer_btn.setGeometry(QtCore.QRect(150, 410, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_lecturer_btn.setFont(font)
        self.add_lecturer_btn.setStyleSheet("background-color: rgb(239, 170, 79);\n"
                                            "border-radius: 11px;\n"
                                            "color: rgb(255, 255, 255);")
        self.add_lecturer_btn.setObjectName("add_lecturer_btn")
        self.add_course_btn = QtWidgets.QPushButton(Window)
        self.add_course_btn.setGeometry(QtCore.QRect(150, 450, 224, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_course_btn.setFont(font)
        self.add_course_btn.setStyleSheet("background-color: rgb(239, 170, 79);\n"
                                          "border-radius: 11px;\n"
                                          "color: rgb(255, 255, 255);")
        self.add_course_btn.setObjectName("add_course_btn")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        self.connect_buttons()

    def get_image_path(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "ui", "img", filename)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "უნი. მართვის სისტემა"))
        self.label_3.setText(_translate("Window", "© სულხან კვერნაძის უნივერსიტეტი - ყველა უფლება დაცულია."))

        self.label.setPixmap(QtGui.QPixmap(self.get_image_path("Group 22.png")))
        self.label_2.setPixmap(QtGui.QPixmap(self.get_image_path("Line 4.png")))
        self.label_4.setPixmap(QtGui.QPixmap(self.get_image_path("div1.png")))
        self.label_5.setPixmap(QtGui.QPixmap(self.get_image_path("div1.png")))
        self.label_6.setPixmap(QtGui.QPixmap(self.get_image_path("kverna1.png")))
        self.label_7.setPixmap(QtGui.QPixmap(self.get_image_path("kverna3.png")))
        self.label_8.setPixmap(QtGui.QPixmap(self.get_image_path("harvar 1.png")))
        self.label_9.setPixmap(QtGui.QPixmap(self.get_image_path("GTU 1.png")))
        self.label_10.setPixmap(QtGui.QPixmap(self.get_image_path("lomebi 1.png")))
        self.label_11.setPixmap(QtGui.QPixmap(self.get_image_path("stanford 1.png")))
        self.label_12.setPixmap(QtGui.QPixmap(self.get_image_path("tavisufali 1.png")))
        self.label_13.setPixmap(QtGui.QPixmap(self.get_image_path("oxford 1.png")))
        self.label_14.setText(_translate("Window", "პარტნიორი უნივერსიტეტები"))
        self.graduated_btn.setText(_translate("Window", "კურსდამთავრებულები"))
        self.students_btn.setText(_translate("Window", "სტუდენტები"))
        self.lecturer_btn.setText(_translate("Window", "ლექტორები"))
        self.heads_btn.setText(_translate("Window", "დამფუძნებლები"))
        self.courses_btn.setText(_translate("Window", "კურსები"))
        self.subject_chois_btn.setText(_translate("Window", "საგნის არჩევა"))
        self.add_student_btn.setText(_translate("Window", "სტუდ დამ/გან/წაშ"))
        self.add_lecturer_btn.setText(_translate("Window", "ლექტ დამ/გან/წაშ"))
        self.add_course_btn.setText(_translate("Window", "კურსის დამ/გან/წაშ"))

    def connect_buttons(self):
        self.lecturer_btn.clicked.connect(self.show_lecturers)
        self.students_btn.clicked.connect(self.show_students)
        self.graduated_btn.clicked.connect(self.show_graduated)
        self.subject_chois_btn.clicked.connect(self.show_subject_choice)
        self.courses_btn.clicked.connect(self.show_courses)
        self.heads_btn.clicked.connect(self.show_heads)

        self.add_student_btn.clicked.connect(self.manage_student)
        self.add_lecturer_btn.clicked.connect(self.manage_lecturer)
        self.add_course_btn.clicked.connect(self.manage_course)

    def show_lecturers(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM professors")
            lecturers = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"ვერ მოხერხდა ბაზასთან დაკავშირება:\n{str(e)}")
            return

        dialog = BaseUniversityDialog("ლექტორების სია")
        layout, search_input, table = dialog.setup_search_table_layout(
            "ძებნა სახელით, გვარით, ტელეფონით ან ელფოსტით..."
        )

        table.setRowCount(len(lecturers))
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)

        for row_index, row_data in enumerate(lecturers):
            for col_index, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data) if cell_data is not None else "")
                table.setItem(row_index, col_index, item)

        table.resizeColumnsToContents()
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        searchable_columns = []
        for name in ['first_name', 'last_name', 'phone', 'email', 'name']:
            if name in column_names:
                searchable_columns.append(column_names.index(name))

        def filter_table(text):
            text = text.lower()
            for row in range(table.rowCount()):
                combined_text = " ".join(
                    table.item(row, col).text().lower()
                    for col in searchable_columns
                    if table.item(row, col)
                )
                match = text in combined_text
                table.setRowHidden(row, not match)

        search_input.textChanged.connect(filter_table)
        dialog.exec_()

    def show_students(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"ვერ მოხერხდა ბაზასთან დაკავშირება:\n{str(e)}")
            return

        dialog = BaseUniversityDialog("სტუდენტების სია")
        layout, search_input, table = dialog.setup_search_table_layout(
            "ძებნა სახელით, გვარით, ტელეფონით ან ელფოსტით..."
        )

        table.setRowCount(len(students))
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)

        for row_index, row_data in enumerate(students):
            for col_index, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data) if cell_data is not None else "")
                table.setItem(row_index, col_index, item)

        table.resizeColumnsToContents()
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        searchable_columns = []
        for name in ['first_name', 'last_name', 'phone', 'email']:
            if name in column_names:
                searchable_columns.append(column_names.index(name))

        def filter_table(text):
            text = text.lower()
            for row in range(table.rowCount()):
                combined_text = " ".join(
                    table.item(row, col).text().lower()
                    for col in searchable_columns
                    if table.item(row, col)
                )
                match = text in combined_text
                table.setRowHidden(row, not match)

        search_input.textChanged.connect(filter_table)
        dialog.exec_()

    def show_graduated(self):

        try:
            from ui.graduated import Ui_graduate_window

            self.graduate_dialog = QtWidgets.QDialog()

            self.graduate_ui = Ui_graduate_window()
            self.graduate_ui.setupUi(self.graduate_dialog)

            self.graduate_ui.back_btn.clicked.connect(self.graduate_dialog.close)

            self.graduate_dialog.exec_()

        except ImportError as e:
            print(f"Import Error: {e}")
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"ვერ ვტვირთავ graduated.py ფაილს: {e}")
        except Exception as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"შეცდომა ფანჯრის გახსნისას: {e}")

    def show_subject_choice(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("საგნის არჩევა")
        dialog.resize(500, 200)

        layout = QtWidgets.QFormLayout(dialog)

        student_id_input = QtWidgets.QLineEdit()
        layout.addRow("სტუდენტის ID:", student_id_input)

        course_combo = QtWidgets.QComboBox()

        try:
            course_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'courses_db.sqlite3')
            conn = sqlite3.connect(course_path)
            cursor = conn.cursor()
            cursor.execute("SELECT course_id, course_name FROM courses WHERE status = 'active'")
            courses = cursor.fetchall()
            conn.close()

            course_map = {}
            for course_id, name in courses:
                course_combo.addItem(name)
                course_map[name] = course_id
        except Exception as e:
            QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"კურსების ჩატვირთვა ვერ მოხერხდა:\n{str(e)}")
            return

        layout.addRow("აირჩიეთ კურსი:", course_combo)

        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        layout.addRow(buttons)

        def enroll_course():
            student_id = student_id_input.text()
            course_name = course_combo.currentText()
            course_id = course_map.get(course_name)

            if not student_id.isdigit():
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სტუდენტის ID უნდა იყოს რიცხვი.")
                return

            try:
                db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'students_db.sqlite3')
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute('''
                    INSERT INTO enrollments (student_id, course_id, enrollment_status)
                    VALUES (?, ?, 'enrolled')
                ''', (int(student_id), course_id))

                conn.commit()
                conn.close()
                QtWidgets.QMessageBox.information(dialog, "წარმატება", f"{course_name} დაემატა სტუდენტს.")
                dialog.accept()
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", str(e))

        buttons.accepted.connect(enroll_course)
        buttons.rejected.connect(dialog.reject)

        dialog.exec_()

    def show_courses(self):
        db_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'courses_db.sqlite3'))

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"ვერ ჩაიტვირთა კურსების სია:\n{str(e)}")
            return

        dialog = BaseUniversityDialog("კურსების სია", 1200, 600)
        layout, search_input, table = dialog.setup_search_table_layout(
            "ძებნა კურსის სახელით ან დეპარტამენტით..."
        )


        table.setRowCount(len(courses))
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)


        for row_index, row_data in enumerate(courses):
            for col_index, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data) if cell_data is not None else "")
                table.setItem(row_index, col_index, item)

        table.resizeColumnsToContents()
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        searchable_columns = []
        for name in ['course_name', 'department']:
            if name in column_names:
                searchable_columns.append(column_names.index(name))

        def filter_table(text):
            text = text.lower()
            for row in range(table.rowCount()):
                combined_text = " ".join(
                    table.item(row, col).text().lower()
                    for col in searchable_columns
                    if table.item(row, col)
                )
                match = text in combined_text
                table.setRowHidden(row, not match)

        search_input.textChanged.connect(filter_table)
        dialog.exec_()

    def show_heads(self):
        try:
            from ui.founders import Ui_founders

            self.founders_dialog = QtWidgets.QDialog()
            self.founders_ui = Ui_founders()
            self.founders_ui.setupUi(self.founders_dialog)

            self.founders_ui.back_btn.clicked.connect(self.founders_dialog.close)

            self.founders_dialog.exec_()

        except ImportError as e:
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"ვერ ვტვირთავ founders.py ფაილს: {e}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "შეცდომა", f"შეცდომა ფანჯრის გახსნისას: {e}")

    def show_subject_choice(self):
        dialog = BaseUniversityDialog("საგნის არჩევა", 450, 300)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()


        student_id_input = QtWidgets.QLineEdit()
        student_id_input.setPlaceholderText("შეიყვანეთ სტუდენტის ID...")

        course_combo = QtWidgets.QComboBox()
        course_combo.setStyleSheet(UniversityStyles.FORM_STYLE)

        try:
            course_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'courses_db.sqlite3')
            conn = sqlite3.connect(course_path)
            cursor = conn.cursor()
            cursor.execute("SELECT course_id, course_name FROM courses WHERE status = 'active'")
            courses = cursor.fetchall()
            conn.close()

            course_map = {}
            for course_id, name in courses:
                course_combo.addItem(name)
                course_map[name] = course_id
        except Exception as e:
            QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"კურსების ჩატვირთვა ვერ მოხერხდა:\n{str(e)}")
            return

        form_layout.addRow("სტუდენტის ID:", student_id_input)
        form_layout.addRow("აირჩიეთ კურსი:", course_combo)

        enroll_btn = QtWidgets.QPushButton("ჩარიცხვა")
        enroll_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(enroll_btn)

        def enroll_course():
            student_id = student_id_input.text().strip()
            course_name = course_combo.currentText()
            course_id = course_map.get(course_name)

            if not student_id:
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "გთხოვთ შეიყვანოთ სტუდენტის ID.")
                return

            if not student_id.isdigit():
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სტუდენტის ID უნდა იყოს რიცხვი.")
                return

            try:
                db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'students_db.sqlite3')
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute('''
                    INSERT INTO enrollments (student_id, course_id, enrollment_status)
                    VALUES (?, ?, 'enrolled')
                ''', (int(student_id), course_id))

                conn.commit()
                conn.close()
                QtWidgets.QMessageBox.information(dialog, "წარმატება", f"{course_name} დაემატა სტუდენტს.")
                dialog.accept()
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", str(e))

        enroll_btn.clicked.connect(enroll_course)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def manage_student(self):
        choice_dialog = BaseUniversityDialog("სტუდენტის მართვა", 400, 300)
        main_layout, form_layout, button_layout = choice_dialog.setup_form_layout()

        add_btn = QtWidgets.QPushButton("ახალი სტუდენტის დამატება")
        add_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        add_btn.setMinimumHeight(50)

        edit_btn = QtWidgets.QPushButton("სტუდენტის რედაქტირება")
        edit_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        edit_btn.setMinimumHeight(50)

        delete_btn = QtWidgets.QPushButton("სტუდენტის წაშლა")
        delete_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)
        delete_btn.setMinimumHeight(50)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        form_layout.addRow(add_btn)
        form_layout.addRow(edit_btn)
        form_layout.addRow(delete_btn)

        button_layout.addWidget(cancel_btn)

        def add_student():
            choice_dialog.accept()
            self._add_student_form()

        def edit_student():
            choice_dialog.accept()
            self._edit_student_form()

        def delete_student():
            choice_dialog.accept()
            self._delete_student_form()

        add_btn.clicked.connect(add_student)
        edit_btn.clicked.connect(edit_student)
        delete_btn.clicked.connect(delete_student)
        cancel_btn.clicked.connect(choice_dialog.reject)

        choice_dialog.exec_()

    def _add_student_form(self):
        dialog = BaseUniversityDialog("ახალი სტუდენტის დამატება", 500, 450)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        first_name_input = QtWidgets.QLineEdit()
        first_name_input.setPlaceholderText("სახელი...")

        last_name_input = QtWidgets.QLineEdit()
        last_name_input.setPlaceholderText("გვარი...")

        phone_input = QtWidgets.QLineEdit()
        phone_input.setPlaceholderText("ტელეფონის ნომერი...")

        student_id_input = QtWidgets.QLineEdit()
        student_id_input.setPlaceholderText("სტუდენტის ID...")

        status_input = QtWidgets.QLineEdit()
        status_input.setPlaceholderText("სტატუსი...")
        status_input.setText("active")

        email_label = QtWidgets.QLabel("ელ-ფოსტა გენერირებული იქნება ავტომატურად")
        email_label.setStyleSheet(f"""
            QLabel {{
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid {UniversityStyles.ACCENT_COLOR};
                border-radius: 6px;
                padding: 8px;
                color: {UniversityStyles.DARK_TEXT};
                font-style: italic;
            }}
        """)

        def generate_email():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()
            if first_name and last_name:
                georgian_to_english = {
                    'ა': 'a', 'ბ': 'b', 'გ': 'g', 'დ': 'd', 'ე': 'e', 'ვ': 'v', 'ზ': 'z',
                    'თ': 't', 'ი': 'i', 'კ': 'k', 'ლ': 'l', 'მ': 'm', 'ნ': 'n', 'ო': 'o',
                    'პ': 'p', 'ჟ': 'zh', 'რ': 'r', 'ს': 's', 'ტ': 't', 'უ': 'u', 'ფ': 'f',
                    'ქ': 'q', 'ღ': 'gh', 'ყ': 'y', 'შ': 'sh', 'ჩ': 'ch', 'ც': 'ts', 'ძ': 'dz',
                    'წ': 'w', 'ჭ': 'ch', 'ხ': 'x', 'ჯ': 'j', 'ჰ': 'h'
                }

                eng_first = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in first_name if c.isalpha())
                eng_last = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in last_name if c.isalpha())

                if eng_first and eng_last:
                    base_email = f"{eng_first}.{eng_last}"
                    email = f"{base_email}1@sku.edu.ge"

                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()
                        cursor.execute("SELECT COUNT(*) FROM students WHERE email LIKE ?",
                                       (f"{base_email}%@sku.edu.ge",))
                        count = cursor.fetchone()[0]
                        conn.close()

                        if count > 0:
                            email = f"{base_email}.{count + 1}@sku.edu.ge"

                    except Exception:
                        email = f"{base_email}.1@sku.edu.ge"

                    email_label.setText(email)
                else:
                    email_label.setText("გთხოვთ შეიყვანეთ ვალიდური სახელი და გვარი")
            else:
                email_label.setText("ელ-ფოსტა გენერირებული იქნება ავტომატურად")

        first_name_input.textChanged.connect(generate_email)
        last_name_input.textChanged.connect(generate_email)

        form_layout.addRow("სახელი:", first_name_input)
        form_layout.addRow("გვარი:", last_name_input)
        form_layout.addRow("ტელეფონი:", phone_input)
        form_layout.addRow("სტუდენტის ID:", student_id_input)
        form_layout.addRow("სტატუსი:", status_input)
        form_layout.addRow("ელ-ფოსტა:", email_label)

        save_btn = QtWidgets.QPushButton("შენახვა")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def save_student():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()
            student_id = student_id_input.text().strip()

            if not first_name or not last_name or not student_id:
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სახელი, გვარი და სტუდენტის ID სავალდებულოა!")
                return

            email = email_label.text()
            if email in ["ელ-ფოსტა გენერირებული იქნება ავტომატურად", "გთხოვთ შეიყვანეთ ვალიდური სახელი და გვარი"]:
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა",
                                              "გთხოვთ შეავსეთ სახელი და გვარი ელ-ფოსტის გენერაციისთვის!")
                return

            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))

                if not os.path.exists(db_path):
                    QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"მონაცემთა ბაზა ვერ მოიძებნა: {db_path}")
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = ?", (student_id,))
                if cursor.fetchone()[0] > 0:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ID-ით სტუდენტი უკვე არსებობს!")
                    conn.close()
                    return

                cursor.execute("SELECT COUNT(*) FROM students WHERE email = ?", (email,))
                if cursor.fetchone()[0] > 0:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ელ-ფოსტით სტუდენტი უკვე არსებობს!")
                    conn.close()
                    return

                cursor.execute('''
                    INSERT INTO students 
                    (first_name, last_name, email, phone, student_id, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    first_name,
                    last_name,
                    email,
                    phone_input.text().strip() or None,
                    student_id,
                    status_input.text().strip() or 'active'
                ))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(dialog, "წარმატება", "სტუდენტი წარმატებით დაემატა!")
                dialog.accept()

            except sqlite3.IntegrityError as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

        save_btn.clicked.connect(save_student)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def  _edit_student_form(self):
        student_data = self._select_student_dialog("რედაქტირებისთვის")
        if not student_data:
            return

        dialog = BaseUniversityDialog("სტუდენტის რედაქტირება", 500, 450)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        first_name_input = QtWidgets.QLineEdit(str(student_data.get('first_name', '')))
        last_name_input = QtWidgets.QLineEdit(str(student_data.get('last_name', '')))
        phone_input = QtWidgets.QLineEdit(str(student_data.get('phone', '') or ''))
        student_id_input = QtWidgets.QLineEdit(str(student_data.get('student_id', '')))
        status_input = QtWidgets.QLineEdit(str(student_data.get('status', 'active')))

        email_label = QtWidgets.QLabel(str(student_data.get('email', '')))
        email_label.setStyleSheet(f"""
            QLabel {{
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid {UniversityStyles.ACCENT_COLOR};
                border-radius: 6px;
                padding: 8px;
                color: {UniversityStyles.DARK_TEXT};
                font-style: italic;
            }}
        """)

        def generate_new_email():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()
            if first_name and last_name:
                georgian_to_english = {
                    'ა': 'a', 'ბ': 'b', 'გ': 'g', 'დ': 'd', 'ე': 'e', 'ვ': 'v', 'ზ': 'z',
                    'თ': 't', 'ი': 'i', 'კ': 'k', 'ლ': 'l', 'მ': 'm', 'ნ': 'n', 'ო': 'o',
                    'პ': 'p', 'ჟ': 'zh', 'რ': 'r', 'ს': 's', 'ტ': 't', 'უ': 'u', 'ფ': 'f',
                    'ქ': 'q', 'ღ': 'gh', 'ყ': 'y', 'შ': 'sh', 'ჩ': 'ch', 'ც': 'ts', 'ძ': 'dz',
                    'წ': 'w', 'ჭ': 'ch', 'ხ': 'x', 'ჯ': 'j', 'ჰ': 'h'
                }

                eng_first = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in first_name if c.isalpha())
                eng_last = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in last_name if c.isalpha())

                if eng_first and eng_last:
                    base_email = f"{eng_first}.{eng_last}"
                    new_email = f"{base_email}1@sku.edu.ge"

                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()

                        cursor.execute("SELECT COUNT(*) FROM students WHERE email LIKE ? AND person_id != ?",
                                       (f"{base_email}%@sku.edu.ge", student_data.get('id')))
                        count = cursor.fetchone()[0]
                        conn.close()

                        if count > 0:
                            new_email = f"{base_email}.{count + 1}@sku.edu.ge"

                    except Exception:
                        new_email = f"{base_email}.1@sku.edu.ge"

                    email_label.setText(new_email)

        first_name_input.textChanged.connect(generate_new_email)
        last_name_input.textChanged.connect(generate_new_email)

        form_layout.addRow("სახელი:", first_name_input)
        form_layout.addRow("გვარი:", last_name_input)
        form_layout.addRow("ტელეფონი:", phone_input)
        form_layout.addRow("სტუდენტის ID:", student_id_input)
        form_layout.addRow("სტატუსი:", status_input)
        form_layout.addRow("ელ-ფოსტა:", email_label)

        save_btn = QtWidgets.QPushButton("განახლება")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def update_student():
            try:
                first_name = first_name_input.text().strip()
                last_name = last_name_input.text().strip()
                student_id = student_id_input.text().strip()

                if not first_name or not last_name or not student_id:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სახელი, გვარი და სტუდენტის ID სავალდებულოა!")
                    return

                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))

                if not os.path.exists(db_path):
                    QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"მონაცემთა ბაზა ვერ მოიძებნა: {db_path}")
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                if student_id != student_data.get('student_id'):
                    cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = ?", (student_id,))
                    if cursor.fetchone()[0] > 0:
                        QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ID-ით სტუდენტი უკვე არსებობს!")
                        conn.close()
                        return

                new_email = email_label.text()
                if new_email != student_data.get('email'):
                    cursor.execute("SELECT COUNT(*) FROM students WHERE email = ?", (new_email,))
                    if cursor.fetchone()[0] > 0:
                        QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ელ-ფოსტით სტუდენტი უკვე არსებობს!")
                        conn.close()
                        return

                cursor.execute('''
                    UPDATE students 
                    SET first_name = ?, last_name = ?, email = ?, phone = ?, student_id = ?, status = ?
                    WHERE person_id = ?
                ''', (
                    first_name,
                    last_name,
                    new_email,
                    phone_input.text().strip() or None,
                    student_id,
                    status_input.text().strip() or 'active',
                    student_data.get('id')
                ))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(dialog, "წარმატება", "სტუდენტის მონაცემები წარმატებით განახლდა!")
                dialog.accept()

            except sqlite3.IntegrityError as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

        save_btn.clicked.connect(update_student)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def _delete_student_form(self):
        student_data = self._select_student_dialog("წაშლისთვის")
        if not student_data:
            return

        reply = QtWidgets.QMessageBox.question(
            None,
            "სტუდენტის წაშლა",
            f"დარწმუნებული ხართ, რომ გსურთ სტუდენტის წაშლა?\n\n"
            f"სახელი: {student_data['first_name']} {student_data['last_name']}\n"
            f"ID: {student_data['student_id']}\n"
            f"ელ-ფოსტა: {student_data['email']}\n\n"
            f"ეს მოქმედება უკან დაბრუნება არ შეიძლება!",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM students WHERE person_id = ?", (student_data['id'],))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(None, "წარმატება", "სტუდენტი წარმატებით წაიშალა!")

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

    def _select_student_dialog(self, purpose):
        dialog = BaseUniversityDialog(f"სტუდენტის შერჩევა {purpose}", 600, 400)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        search_input = QtWidgets.QLineEdit()
        search_input.setPlaceholderText("ძიება (სახელი, გვარი, ID ან ელ-ფოსტა)...")

        student_list = QtWidgets.QListWidget()
        student_list.setMinimumHeight(250)

        def load_students(search_text=""):
            student_list.clear()
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'students_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                if search_text:
                    cursor.execute('''
                        SELECT person_id,first_name, last_name, email, phone, student_id, status
                        FROM students 
                        WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR student_id LIKE ?
                        ORDER BY first_name, last_name
                    ''', (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
                else:
                    cursor.execute('''
                        SELECT person_id, first_name, last_name, email, phone, student_id, status
                        FROM students 
                        ORDER BY first_name, last_name
                    ''')

                students = cursor.fetchall()
                conn.close()

                for student in students:
                    item_text = f"{student[1]} {student[2]} (ID: {student[4]}) - {student[3]}"
                    item = QtWidgets.QListWidgetItem(item_text)
                    item.setData(QtCore.Qt.UserRole, {
                        'id': student[0],
                        'first_name': student[1],
                        'last_name': student[2],
                        'email': student[3],
                        'phone': student[4], 
                        'student_id': student[5],
                        'status': student[6]
                    })
                    student_list.addItem(item)

            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"სტუდენტების ჩატვირთვისას მოხდა შეცდომა: {str(e)}")

        def search_students():
            load_students(search_input.text().strip())

        search_input.textChanged.connect(search_students)

        select_btn = QtWidgets.QPushButton("არჩევა")
        select_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        select_btn.setEnabled(False)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        def on_selection_changed():
            select_btn.setEnabled(bool(student_list.currentItem()))

        student_list.itemSelectionChanged.connect(on_selection_changed)

        def on_double_click():
            if student_list.currentItem():
                dialog.accept()

        student_list.itemDoubleClicked.connect(on_double_click)

        form_layout.addRow("ძიება:", search_input)
        form_layout.addRow("სტუდენტები:", student_list)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(select_btn)

        select_btn.clicked.connect(dialog.accept)
        cancel_btn.clicked.connect(dialog.reject)

        load_students()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            current_item = student_list.currentItem()
            if current_item:
                return current_item.data(QtCore.Qt.UserRole)

        return None

    def manage_lecturer(self):
        choice_dialog = BaseUniversityDialog("ლექტორის მართვა", 400, 300)
        main_layout, form_layout, button_layout = choice_dialog.setup_form_layout()

        add_btn = QtWidgets.QPushButton("ახალი ლექტორის დამატება")
        add_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        add_btn.setMinimumHeight(50)

        edit_btn = QtWidgets.QPushButton("ლექტორის რედაქტირება")
        edit_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        edit_btn.setMinimumHeight(50)

        delete_btn = QtWidgets.QPushButton("ლექტორის წაშლა")
        delete_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)
        delete_btn.setMinimumHeight(50)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        form_layout.addRow(add_btn)
        form_layout.addRow(edit_btn)
        form_layout.addRow(delete_btn)

        button_layout.addWidget(cancel_btn)

        def add_lecturer():
            choice_dialog.accept()
            self._add_lecturer_form()

        def edit_lecturer():
            choice_dialog.accept()
            self._edit_lecturer_form()

        def delete_lecturer():
            choice_dialog.accept()
            self._delete_lecturer_form()

        add_btn.clicked.connect(add_lecturer)
        edit_btn.clicked.connect(edit_lecturer)
        delete_btn.clicked.connect(delete_lecturer)
        cancel_btn.clicked.connect(choice_dialog.reject)

        choice_dialog.exec_()

    def _add_lecturer_form(self):
        dialog = BaseUniversityDialog("ახალი ლექტორის დამატება", 500, 550)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        first_name_input = QtWidgets.QLineEdit()
        first_name_input.setPlaceholderText("სახელი...")

        last_name_input = QtWidgets.QLineEdit()
        last_name_input.setPlaceholderText("გვარი...")

        phone_input = QtWidgets.QLineEdit()
        phone_input.setPlaceholderText("ტელეფონის ნომერი...")

        professor_id_input = QtWidgets.QLineEdit()
        professor_id_input.setPlaceholderText("ლექტორის ID...")

        department_input = QtWidgets.QLineEdit()
        department_input.setPlaceholderText("დეპარტამენტი...")

        rank_input = QtWidgets.QLineEdit()
        rank_input.setPlaceholderText("რანკი/წოდება...")

        salary_input = QtWidgets.QLineEdit()
        salary_input.setPlaceholderText("ხელფასი...")

        status_input = QtWidgets.QLineEdit()
        status_input.setPlaceholderText("სტატუსი...")
        status_input.setText("active")

        email_label = QtWidgets.QLabel("ელ-ფოსტა გენერირებული იქნება ავტომატურად")
        email_label.setStyleSheet(f"""
            QLabel {{
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid {UniversityStyles.ACCENT_COLOR};
                border-radius: 6px;
                padding: 8px;
                color: {UniversityStyles.DARK_TEXT};
                font-style: italic;
            }}
        """)

        def generate_email():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()

            if first_name and last_name:
                georgian_to_english = {
                    'ა': 'a', 'ბ': 'b', 'გ': 'g', 'დ': 'd', 'ე': 'e', 'ვ': 'v', 'ზ': 'z',
                    'თ': 't', 'ი': 'i', 'კ': 'k', 'ლ': 'l', 'მ': 'm', 'ნ': 'n', 'ო': 'o',
                    'პ': 'p', 'ჟ': 'zh', 'რ': 'r', 'ს': 's', 'ტ': 't', 'უ': 'u', 'ფ': 'f',
                    'ქ': 'q', 'ღ': 'gh', 'ყ': 'y', 'შ': 'sh', 'ჩ': 'ch', 'ც': 'ts', 'ძ': 'dz',
                    'წ': 'w', 'ჭ': 'ch', 'ხ': 'x', 'ჯ': 'j', 'ჰ': 'h'
                }

                eng_first = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in first_name if c.isalpha())
                eng_last = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in last_name if c.isalpha())

                if eng_first and eng_last:
                    base_email = f"{eng_first}.{eng_last}"
                    email = f"{base_email}@sku.edu.ge"

                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()
                        cursor.execute("SELECT COUNT(*) FROM professors WHERE email LIKE ?",
                                       (f"{base_email}%@sku.edu.ge",))
                        count = cursor.fetchone()[0]
                        conn.close()

                        if count > 0:
                            email = f"{base_email}.{count + 1}@sku.edu.ge"

                    except Exception:
                        email = f"{base_email}.1@sku.edu.ge"

                    email_label.setText(email)
                else:
                    email_label.setText("გთხოვთ შეიყვანეთ ვალიდური სახელი და გვარი")
            else:
                email_label.setText("ელ-ფოსტა გენერირებული იქნება ავტომატურად")

        first_name_input.textChanged.connect(generate_email)
        last_name_input.textChanged.connect(generate_email)

        form_layout.addRow("სახელი:", first_name_input)
        form_layout.addRow("გვარი:", last_name_input)
        form_layout.addRow("ტელეფონი:", phone_input)
        form_layout.addRow("ლექტორის ID:", professor_id_input)
        form_layout.addRow("დეპარტამენტი:", department_input)
        form_layout.addRow("რანკი:", rank_input)
        form_layout.addRow("ხელფასი:", salary_input)
        form_layout.addRow("სტატუსი:", status_input)
        form_layout.addRow("ელ-ფოსტა:", email_label)

        save_btn = QtWidgets.QPushButton("შენახვა")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def save_lecturer():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()
            professor_id = professor_id_input.text().strip()

            if not first_name or not last_name or not professor_id:
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სახელი, გვარი და ლექტორის ID სავალდებულოა!")
                return

            email = email_label.text()
            if email in ["ელ-ფოსტა გენერირებული იქნება ავტომატურად", "გთხოვთ შეიყვანეთ ვალიდური სახელი და გვარი"]:
                QtWidgets.QMessageBox.warning(dialog, "შეცდომა",
                                              "გთხოვთ შეავსეთ სახელი და გვარი ელ-ფოსტის გენერაციისთვის!")
                return

            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

                if not os.path.exists(db_path):
                    QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"მონაცემთა ბაზა ვერ მოიძებნა: {db_path}")
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute("SELECT COUNT(*) FROM professors WHERE professor_id = ?", (professor_id,))
                if cursor.fetchone()[0] > 0:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ID-ით ლექტორი უკვე არსებობს!")
                    conn.close()
                    return

                cursor.execute("SELECT COUNT(*) FROM professors WHERE email = ?", (email,))
                if cursor.fetchone()[0] > 0:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ელ-ფოსტით ლექტორი უკვე არსებობს!")
                    conn.close()
                    return

                cursor.execute('''
                    INSERT INTO professors 
                    (name, last_name, email, phone, professor_id, department, rank, salary, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    first_name,
                    last_name,
                    email,
                    phone_input.text().strip() or None,
                    professor_id,
                    department_input.text().strip() or None,
                    rank_input.text().strip() or None,
                    salary_input.text().strip() or None,
                    status_input.text().strip() or 'active'
                ))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(dialog, "წარმატება", "ლექტორი წარმატებით დაემატა!")
                dialog.accept()

            except sqlite3.IntegrityError as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

        save_btn.clicked.connect(save_lecturer)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def _edit_lecturer_form(self):
        lecturer_data = self._select_lecturer_dialog("რედაქტირებისთვის")
        if not lecturer_data:
            return

        dialog = BaseUniversityDialog("ლექტორის რედაქტირება", 500, 550)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()


        first_name_input = QtWidgets.QLineEdit(str(lecturer_data.get('name', '')))
        last_name_input = QtWidgets.QLineEdit(str(lecturer_data.get('last_name', '')))
        phone_input = QtWidgets.QLineEdit(str(lecturer_data.get('phone', '') or ''))
        professor_id_input = QtWidgets.QLineEdit(str(lecturer_data.get('professor_id', '')))
        department_input = QtWidgets.QLineEdit(str(lecturer_data.get('department', '') or ''))
        rank_input = QtWidgets.QLineEdit(str(lecturer_data.get('rank', '') or ''))
        salary_input = QtWidgets.QLineEdit(str(lecturer_data.get('salary', '') or ''))
        status_input = QtWidgets.QLineEdit(str(lecturer_data.get('status', 'active')))


        email_label = QtWidgets.QLabel(str(lecturer_data.get('email', '')))
        email_label.setStyleSheet(f"""
            QLabel {{
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid {UniversityStyles.ACCENT_COLOR};
                border-radius: 6px;
                padding: 8px;
                color: {UniversityStyles.DARK_TEXT};
                font-style: italic;
            }}
        """)

        def generate_new_email():
            first_name = first_name_input.text().strip()
            last_name = last_name_input.text().strip()
            if first_name and last_name:
                georgian_to_english = {
                    'ა': 'a', 'ბ': 'b', 'გ': 'g', 'დ': 'd', 'ე': 'e', 'ვ': 'v', 'ზ': 'z',
                    'თ': 't', 'ი': 'i', 'კ': 'k', 'ლ': 'l', 'მ': 'm', 'ნ': 'n', 'ო': 'o',
                    'პ': 'p', 'ჟ': 'zh', 'რ': 'r', 'ს': 's', 'ტ': 't', 'უ': 'u', 'ფ': 'f',
                    'ქ': 'q', 'ღ': 'gh', 'ყ': 'y', 'შ': 'sh', 'ჩ': 'ch', 'ც': 'ts', 'ძ': 'dz',
                    'წ': 'w', 'ჭ': 'ch', 'ხ': 'x', 'ჯ': 'j', 'ჰ': 'h'
                }

                eng_first = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in first_name if c.isalpha())
                eng_last = ''.join(georgian_to_english.get(c.lower(), c.lower()) for c in last_name if c.isalpha())

                if eng_first and eng_last:
                    base_email = f"{eng_first}.{eng_last}"
                    new_email = f"{base_email}@sku.edu.ge"

                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()

                        cursor.execute("SELECT COUNT(*) FROM professors WHERE email LIKE ? AND professor_id != ?",
                                       (f"{base_email}%@sku.edu.ge", lecturer_data.get('professor_id')))
                        count = cursor.fetchone()[0]
                        conn.close()

                        if count > 0:
                            new_email = f"{base_email}.{count + 1}@sku.edu.ge"

                    except Exception:
                        new_email = f"{base_email}.1@sku.edu.ge"

                    email_label.setText(new_email)

        first_name_input.textChanged.connect(generate_new_email)
        last_name_input.textChanged.connect(generate_new_email)

        form_layout.addRow("სახელი:", first_name_input)
        form_layout.addRow("გვარი:", last_name_input)
        form_layout.addRow("ტელეფონი:", phone_input)
        form_layout.addRow("ლექტორის ID:", professor_id_input)
        form_layout.addRow("დეპარტამენტი:", department_input)
        form_layout.addRow("რანკი:", rank_input)
        form_layout.addRow("ხელფასი:", salary_input)
        form_layout.addRow("სტატუსი:", status_input)
        form_layout.addRow("ელ-ფოსტა:", email_label)

        save_btn = QtWidgets.QPushButton("განახლება")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def update_lecturer():
            try:
                first_name = first_name_input.text().strip()
                last_name = last_name_input.text().strip()
                professor_id = professor_id_input.text().strip()

                if not first_name or not last_name or not professor_id:
                    QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "სახელი, გვარი და ლექტორის ID სავალდებულოა!")
                    return

                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

                if not os.path.exists(db_path):
                    QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"მონაცემთა ბაზა ვერ მოიძებნა: {db_path}")
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                if professor_id != lecturer_data.get('professor_id'):
                    cursor.execute("SELECT COUNT(*) FROM professors WHERE professor_id = ?", (professor_id,))
                    if cursor.fetchone()[0] > 0:
                        QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ID-ით ლექტორი უკვე არსებობს!")
                        conn.close()
                        return


                new_email = email_label.text()
                if new_email != lecturer_data.get('email'):
                    cursor.execute("SELECT COUNT(*) FROM professors WHERE email = ?", (new_email,))
                    if cursor.fetchone()[0] > 0:
                        QtWidgets.QMessageBox.warning(dialog, "შეცდომა", "ამ ელ-ფოსტით ლექტორი უკვე არსებობს!")
                        conn.close()
                        return

                cursor.execute('''
                    UPDATE professors 
                    SET name = ?, last_name = ?, email = ?, phone = ?, professor_id = ?, 
                        department = ?, rank = ?, salary = ?, status = ?
                    WHERE person_id = ?
                ''', (
                    first_name,
                    last_name,
                    new_email,
                    phone_input.text().strip() or None,
                    professor_id,
                    department_input.text().strip() or None,
                    rank_input.text().strip() or None,
                    salary_input.text().strip() or None,
                    status_input.text().strip() or 'active',
                    lecturer_data.get('id')
                ))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(dialog, "წარმატება", "ლექტორის მონაცემები წარმატებით განახლდა!")
                dialog.accept()

            except sqlite3.IntegrityError as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(dialog, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

        save_btn.clicked.connect(update_lecturer)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def _delete_lecturer_form(self):
        lecturer_data = self._select_lecturer_dialog("წაშლისთვის")
        if not lecturer_data:
            return

        reply = QtWidgets.QMessageBox.question(
            None,
            "ლექტორის წაშლა",
            f"დარწმუნებული ხართ, რომ გსურთ ლექტორის წაშლა?\n\n"
            f"სახელი: {lecturer_data['name']} {lecturer_data['last_name']}\n"
            f"ID: {lecturer_data['professor_id']}\n"
            f"ელ-ფოსტა: {lecturer_data['email']}\n"
            f"დეპარტამენტი: {lecturer_data.get('department', 'N/A')}\n\n"
            f"ეს მოქმედება უკან დაბრუნება არ შეიძლება!",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM professors WHERE person_id = ?", (lecturer_data['id'],))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(None, "წარმატება", "ლექტორი წარმატებით წაიშალა!")

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

    def _select_lecturer_dialog(self, purpose):
        dialog = BaseUniversityDialog(f"ლექტორის შერჩევა {purpose}", 700, 400)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        search_input = QtWidgets.QLineEdit()
        search_input.setPlaceholderText("ძიება (სახელი, გვარი, ID, ელ-ფოსტა ან დეპარტამენტი)...")

        lecturer_list = QtWidgets.QListWidget()
        lecturer_list.setMinimumHeight(250)

        def load_lecturers(search_text=""):
            lecturer_list.clear()
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                if search_text:
                    cursor.execute('''
                        SELECT person_id, name, last_name, email, phone, professor_id, department, rank, salary, status
                        FROM professors 
                        WHERE name LIKE ? OR last_name LIKE ? OR email LIKE ? OR professor_id LIKE ? OR department LIKE ?
                        ORDER BY name, last_name
                    ''', (
                    f"%{search_text}%", f"%{search_text}%", f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
                else:
                    cursor.execute('''
                        SELECT person_id, name, last_name, email, phone, professor_id, department, rank, salary, status
                        FROM professors 
                        ORDER BY name, last_name
                    ''')

                lecturers = cursor.fetchall()
                conn.close()

                for lecturer in lecturers:
                    item_text = f"{lecturer[1]} {lecturer[2]} (ID: {lecturer[5]}) - {lecturer[3]}"
                    if lecturer[6]: 
                        item_text += f" - {lecturer[6]}"

                    item = QtWidgets.QListWidgetItem(item_text)
                    item.setData(QtCore.Qt.UserRole, {
                        'id': lecturer[0],
                        'name': lecturer[1],
                        'last_name': lecturer[2],
                        'email': lecturer[3],
                        'phone': lecturer[4],
                        'professor_id': lecturer[5],
                        'department': lecturer[6],
                        'rank': lecturer[7],
                        'salary': lecturer[8],
                        'status': lecturer[9]
                    })
                    lecturer_list.addItem(item)

            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"ლექტორების ჩატვირთვისას მოხდა შეცდომა: {str(e)}")

        def search_lecturers():
            load_lecturers(search_input.text().strip())

        search_input.textChanged.connect(search_lecturers)

        select_btn = QtWidgets.QPushButton("არჩევა")
        select_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        select_btn.setEnabled(False)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        def on_selection_changed():
            select_btn.setEnabled(bool(lecturer_list.currentItem()))

        lecturer_list.itemSelectionChanged.connect(on_selection_changed)

        def on_double_click():
            if lecturer_list.currentItem():
                dialog.accept()

        lecturer_list.itemDoubleClicked.connect(on_double_click)

        form_layout.addRow("ძიება:", search_input)
        form_layout.addRow("ლექტორები:", lecturer_list)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(select_btn)

        select_btn.clicked.connect(dialog.accept)
        cancel_btn.clicked.connect(dialog.reject)

        load_lecturers()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            current_item = lecturer_list.currentItem()
            if current_item:
                return current_item.data(QtCore.Qt.UserRole)

        return None

    def manage_course(self):
        choice_dialog = BaseUniversityDialog("კურსის მართვა", 400, 300)
        main_layout, form_layout, button_layout = choice_dialog.setup_form_layout()

        add_btn = QtWidgets.QPushButton("ახალი კურსის დამატება")
        add_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        add_btn.setMinimumHeight(50)

        edit_btn = QtWidgets.QPushButton("კურსის რედაქტირება")
        edit_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        edit_btn.setMinimumHeight(50)

        delete_btn = QtWidgets.QPushButton("კურსის წაშლა")
        delete_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)
        delete_btn.setMinimumHeight(50)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        form_layout.addRow(add_btn)
        form_layout.addRow(edit_btn)
        form_layout.addRow(delete_btn)

        button_layout.addWidget(cancel_btn)

        def add_course():
            choice_dialog.accept()
            self.add_course_form()

        def edit_course():
            choice_dialog.accept()
            self._edit_course_form()

        def delete_course():
            choice_dialog.accept()
            self._delete_course_form()

        add_btn.clicked.connect(add_course)
        edit_btn.clicked.connect(edit_course)
        delete_btn.clicked.connect(delete_course)
        cancel_btn.clicked.connect(choice_dialog.reject)

        choice_dialog.exec_()

    def add_course_form(self):
        dialog = BaseUniversityDialog("ახალი კურსის დამატება", 500, 400)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        name_input = QtWidgets.QLineEdit()
        name_input.setPlaceholderText("კურსის დასახელება...")
        name_input.setStyleSheet(UniversityStyles.FORM_STYLE)

        dept_input = QtWidgets.QLineEdit()
        dept_input.setPlaceholderText("დეპარტამენტი...")
        dept_input.setStyleSheet(UniversityStyles.FORM_STYLE)

        credits_input = QtWidgets.QSpinBox()
        credits_input.setRange(1, 10)
        credits_input.setValue(3)
        credits_input.setStyleSheet(UniversityStyles.FORM_STYLE)

        professor_combo = QtWidgets.QComboBox()
        professor_combo.setStyleSheet(UniversityStyles.FORM_STYLE)
        professor_map = {}

        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            prof_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

            if not os.path.exists(prof_path):
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText(f"ლექტორების ბაზა ვერ მოიძებნა: {prof_path}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                return

            conn = sqlite3.connect(prof_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='professors'")
            if not cursor.fetchone():
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText("professors ტაბელი ვერ მოიძებნა!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                conn.close()
                return

            possible_queries = [
                "SELECT person_id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT professor_id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT rowid, name, last_name FROM professors"
            ]

            professors_found = False
            for query in possible_queries:
                try:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    if results:
                        professor_combo.addItem("-- აირჩიეთ ლექტორი --")
                        professor_map["-- აირჩიეთ ლექტორი --"] = None

                        for pid, name, lname in results:
                            label = f"{name} {lname} (ID: {pid})"
                            professor_combo.addItem(label)
                            professor_map[label] = pid

                        professors_found = True
                        break
                except sqlite3.Error:
                    continue

            conn.close()

            if not professors_found:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ყურადღება")
                msg.setText("აქტიური ლექტორები ვერ მოიძებნა!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                professor_combo.addItem("ლექტორები ვერ ჩაიტვირთა")

        except Exception as e:
            msg = QtWidgets.QMessageBox(dialog)
            msg.setWindowTitle("შეცდომა")
            msg.setText(f"ლექტორების ჩატვირთვა ვერ მოხერხდა:\n{str(e)}")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setStyleSheet(f"""
                QMessageBox {{
                    background-color: {UniversityStyles.BACKGROUND_COLOR};
                    color: {UniversityStyles.WHITE_TEXT};
                }}
                QMessageBox QPushButton {{
                    {UniversityStyles.BUTTON_STYLE}
                    min-width: 80px;
                }}
            """)
            msg.exec_()
            return

        form_layout.addRow("კურსის დასახელება:", name_input)
        form_layout.addRow("დეპარტამენტი:", dept_input)
        form_layout.addRow("კრედიტები:", credits_input)
        form_layout.addRow("ლექტორი:", professor_combo)

        save_btn = QtWidgets.QPushButton("შენახვა")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def save_course():
            try:
                name = name_input.text().strip()
                dept = dept_input.text().strip()
                credits = credits_input.value()
                prof_label = professor_combo.currentText()
                professor_id = professor_map.get(prof_label)

                if not name:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("კურსის დასახელება სავალდებულოა!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                if not dept:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("დეპარტამენტი სავალდებულოა!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                if professor_id is None or prof_label == "-- აირჩიეთ ლექტორი --":
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("გთხოვთ აირჩიეთ ლექტორი!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return


                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'courses_db.sqlite3'))

                if not os.path.exists(db_path):
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText(f"კურსების ბაზა ვერ მოიძებნა: {db_path}")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()


                cursor.execute("SELECT COUNT(*) FROM courses WHERE course_name = ? AND department = ?", (name, dept))
                if cursor.fetchone()[0] > 0:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("ამ დასახელებით კურსი უკვე არსებობს ამ დეპარტამენტში!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    conn.close()
                    return

                cursor.execute('''
                    INSERT INTO courses (course_name, department, credits, professor_id, status)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, dept, credits, professor_id, 'active'))

                conn.commit()
                conn.close()

                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("წარმატება")
                msg.setText("კურსი წარმატებით დაემატა!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                dialog.accept()

            except sqlite3.IntegrityError as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ბაზის შეცდომა")
                msg.setText(f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
            except sqlite3.Error as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ბაზის შეცდომა")
                msg.setText(f"SQL შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
            except Exception as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText(f"გაუთვალისწინებელი შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()

        save_btn.clicked.connect(save_course)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def _edit_course_form(self):
        course_data = self._select_course_dialog("რედაქტირებისთვის")
        if not course_data:
            return

        dialog = BaseUniversityDialog("კურსის რედაქტირება", 500, 400)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        name_input = QtWidgets.QLineEdit(str(course_data.get('course_name', '')))
        name_input.setPlaceholderText("კურსის დასახელება...")

        dept_input = QtWidgets.QLineEdit(str(course_data.get('department', '')))
        dept_input.setPlaceholderText("დეპარტამენტი...")

        credits_input = QtWidgets.QSpinBox()
        credits_input.setRange(1, 10)
        credits_input.setValue(course_data.get('credits', 3))
        credits_input.setStyleSheet(UniversityStyles.FORM_STYLE)

        professor_combo = QtWidgets.QComboBox()
        professor_combo.setStyleSheet(UniversityStyles.FORM_STYLE)
        professor_map = {}

        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            prof_path = os.path.normpath(os.path.join(current_dir, 'db', 'professors_db.sqlite3'))

            if not os.path.exists(prof_path):
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText(f"ლექტორების ბაზა ვერ მოიძებნა: {prof_path}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                return

            conn = sqlite3.connect(prof_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='professors'")
            if not cursor.fetchone():
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText("professors ტაბელი ვერ მოიძებნა!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                conn.close()
                return

            possible_queries = [
                "SELECT person_id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT professor_id, name, last_name FROM professors WHERE status = 'active' OR status IS NULL",
                "SELECT rowid, name, last_name FROM professors"
            ]

            professors_found = False
            current_professor_index = 0
            for query in possible_queries:
                try:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    if results:
                        professor_combo.addItem("-- აირჩიეთ ლექტორი --")
                        professor_map["-- აირჩიეთ ლექტორი --"] = None

                        for i, (pid, name, lname) in enumerate(results):
                            label = f"{name} {lname} (ID: {pid})"
                            professor_combo.addItem(label)
                            professor_map[label] = pid

                            if pid == course_data.get('professor_id'):
                                current_professor_index = i + 1

                        professor_combo.setCurrentIndex(current_professor_index)
                        professors_found = True
                        break
                except sqlite3.Error:
                    continue

            conn.close()

            if not professors_found:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ყურადღება")
                msg.setText("აქტიური ლექტორები ვერ მოიძებნა!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                professor_combo.addItem("ლექტორები ვერ ჩაიტვირთა")

        except Exception as e:
            msg = QtWidgets.QMessageBox(dialog)
            msg.setWindowTitle("შეცდომა")
            msg.setText(f"ლექტორების ჩატვირთვა ვერ მოხერხდა:\n{str(e)}")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setStyleSheet(f"""
                QMessageBox {{
                    background-color: {UniversityStyles.BACKGROUND_COLOR};
                    color: {UniversityStyles.WHITE_TEXT};
                }}
                QMessageBox QPushButton {{
                    {UniversityStyles.BUTTON_STYLE}
                    min-width: 80px;
                }}
            """)
            msg.exec_()
            return

        form_layout.addRow("კურსის დასახელება:", name_input)
        form_layout.addRow("დეპარტამენტი:", dept_input)
        form_layout.addRow("კრედიტები:", credits_input)
        form_layout.addRow("ლექტორი:", professor_combo)

        save_btn = QtWidgets.QPushButton("განახლება")
        save_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        def update_course():
            try:
                name = name_input.text().strip()
                dept = dept_input.text().strip()
                credits = credits_input.value()
                prof_label = professor_combo.currentText()
                professor_id = professor_map.get(prof_label)

                if not name:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("კურსის დასახელება სავალდებულოა!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                if not dept:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("დეპარტამენტი სავალდებულოა!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                if professor_id is None or prof_label == "-- აირჩიეთ ლექტორი --":
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("გთხოვთ აირჩიეთ ლექტორი!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'courses_db.sqlite3'))

                if not os.path.exists(db_path):
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText(f"კურსების ბაზა ვერ მოიძებნა: {db_path}")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    return

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT COUNT(*) FROM courses WHERE course_name = ? AND department = ? AND course_id != ?",
                    (name, dept, course_data.get('course_id')))
                if cursor.fetchone()[0] > 0:
                    msg = QtWidgets.QMessageBox(dialog)
                    msg.setWindowTitle("შეცდომა")
                    msg.setText("ამ დასახელებით კურსი უკვე არსებობს ამ დეპარტამენტში!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setStyleSheet(f"""
                        QMessageBox {{
                            background-color: {UniversityStyles.BACKGROUND_COLOR};
                            color: {UniversityStyles.WHITE_TEXT};
                        }}
                        QMessageBox QPushButton {{
                            {UniversityStyles.BUTTON_STYLE}
                            min-width: 80px;
                        }}
                    """)
                    msg.exec_()
                    conn.close()
                    return

                cursor.execute('''
                    UPDATE courses 
                    SET course_name = ?, department = ?, credits = ?, professor_id = ?
                    WHERE course_id = ?
                ''', (name, dept, credits, professor_id, course_data.get('course_id')))

                conn.commit()
                conn.close()

                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("წარმატება")
                msg.setText("კურსის მონაცემები წარმატებით განახლდა!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
                dialog.accept()

            except sqlite3.IntegrityError as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ბაზის შეცდომა")
                msg.setText(f"მონაცემთა მთლიანობის შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
            except sqlite3.Error as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("ბაზის შეცდომა")
                msg.setText(f"SQL შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()
            except Exception as e:
                msg = QtWidgets.QMessageBox(dialog)
                msg.setWindowTitle("შეცდომა")
                msg.setText(f"გაუთვალისწინებელი შეცდომა: {str(e)}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setStyleSheet(f"""
                    QMessageBox {{
                        background-color: {UniversityStyles.BACKGROUND_COLOR};
                        color: {UniversityStyles.WHITE_TEXT};
                    }}
                    QMessageBox QPushButton {{
                        {UniversityStyles.BUTTON_STYLE}
                        min-width: 80px;
                    }}
                """)
                msg.exec_()

        save_btn.clicked.connect(update_course)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()

    def _delete_course_form(self):
        course_data = self._select_course_dialog("წაშლისთვის")
        if not course_data:
            return

        reply = QtWidgets.QMessageBox.question(
            None,
            "კურსის წაშლა",
            f"დარწმუნებული ხართ, რომ გსურთ კურსის წაშლა?\n\n"
            f"დასახელება: {course_data['course_name']}\n"
            f"დეპარტამენტი: {course_data['department']}\n"
            f"კრედიტები: {course_data['credits']}\n\n"
            f"ეს მოქმედება უკან დაბრუნება არ შეიძლება!",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'courses_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_data['course_id'],))

                conn.commit()
                conn.close()

                QtWidgets.QMessageBox.information(None, "წარმატება", "კურსი წარმატებით წაიშალა!")

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "ბაზის შეცდომა", f"SQL შეცდომა: {str(e)}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "შეცდომა", f"გაუთვალისწინებელი შეცდომა: {str(e)}")

    def _select_course_dialog(self, purpose):
        dialog = BaseUniversityDialog(f"კურსის შერჩევა {purpose}", 700, 400)
        main_layout, form_layout, button_layout = dialog.setup_form_layout()

        search_input = QtWidgets.QLineEdit()
        search_input.setPlaceholderText("ძიება (დასახელება, დეპარტამენტი)...")

        course_list = QtWidgets.QListWidget()
        course_list.setMinimumHeight(250)

        def load_courses(search_text=""):
            course_list.clear()
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.normpath(os.path.join(current_dir, 'db', 'courses_db.sqlite3'))

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                if search_text:
                    cursor.execute('''
                        SELECT course_id, course_name, department, credits, professor_id, status
                        FROM courses 
                        WHERE course_name LIKE ? OR department LIKE ?
                        ORDER BY course_name
                    ''', (f"%{search_text}%", f"%{search_text}%"))
                else:
                    cursor.execute('''
                        SELECT course_id, course_name, department, credits, professor_id, status
                        FROM courses 
                        ORDER BY course_name
                    ''')

                courses = cursor.fetchall()
                conn.close()

                for course in courses:
                    item_text = f"{course[1]} - {course[2]} ({course[3]} კრედიტი)"

                    item = QtWidgets.QListWidgetItem(item_text)
                    item.setData(QtCore.Qt.UserRole, {
                        'course_id': course[0],
                        'course_name': course[1],
                        'department': course[2],
                        'credits': course[3],
                        'professor_id': course[4],
                        'status': course[5]
                    })
                    course_list.addItem(item)

            except Exception as e:
                QtWidgets.QMessageBox.critical(dialog, "შეცდომა", f"კურსების ჩატვირთვისას მოხდა შეცდომა: {str(e)}")

        def search_courses():
            load_courses(search_input.text().strip())

        search_input.textChanged.connect(search_courses)

        select_btn = QtWidgets.QPushButton("არჩევა")
        select_btn.setStyleSheet(UniversityStyles.BUTTON_STYLE)
        select_btn.setEnabled(False)

        cancel_btn = QtWidgets.QPushButton("გაუქმება")
        cancel_btn.setStyleSheet(UniversityStyles.CANCEL_BUTTON_STYLE)

        def on_selection_changed():
            select_btn.setEnabled(bool(course_list.currentItem()))

        course_list.itemSelectionChanged.connect(on_selection_changed)

        def on_double_click():
            if course_list.currentItem():
                dialog.accept()

        course_list.itemDoubleClicked.connect(on_double_click)

        form_layout.addRow("ძიება:", search_input)
        form_layout.addRow("კურსები:", course_list)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(select_btn)

        select_btn.clicked.connect(dialog.accept)
        cancel_btn.clicked.connect(dialog.reject)

        load_courses()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            current_item = course_list.currentItem()
            if current_item:
                return current_item.data(QtCore.Qt.UserRole)

        return None


# ===== GRADUATED CLASS =====
class MainGraduate(Ui_graduate_window):

    def setupUi(self, graduate_window):
        super().setupUi(graduate_window)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.get_image_path("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        graduate_window.setWindowIcon(icon)

        self._load_all_images()

        graduate_window.update()

    def get_image_path(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_dir, "ui", "img", filename)

        print(f"Looking for: {filename}")
        print(f"Full path: {img_path}")
        print(f"File exists: {os.path.exists(img_path)}")

        if os.path.exists(img_path):
            return img_path
        else:
            alt_paths = [
                os.path.join(current_dir, "img", filename),
                os.path.join(os.getcwd(), "ui", "img", filename),
                os.path.join(os.getcwd(), "img", filename)
            ]

            for alt_path in alt_paths:
                print(f"Trying alternative: {alt_path}")
                if os.path.exists(alt_path):
                    print(f"Found at: {alt_path}")
                    return alt_path

            print(f"ERROR: Image not found anywhere: {filename}")
            return img_path

    def _load_all_images(self):


        graduated_path = self.get_image_path("graduated.png")
        pixmap1 = QtGui.QPixmap(graduated_path)
        print(f"graduated.png pixmap isNull: {pixmap1.isNull()}")
        if not pixmap1.isNull():
            self.label.clear()
            self.label.setPixmap(pixmap1)
            self.label.setScaledContents(True)

        hah_path = self.get_image_path("hah.png")
        pixmap2 = QtGui.QPixmap(hah_path)
        print(f"hah.png pixmap isNull: {pixmap2.isNull()}")
        if not pixmap2.isNull():
            self.label_4.clear()
            self.label_4.setPixmap(pixmap2)
            self.label_4.setScaledContents(True)

        rect_path = self.get_image_path("Rectangle 4.png")
        pixmap3 = QtGui.QPixmap(rect_path)
        print(f"Rectangle 4.png pixmap isNull: {pixmap3.isNull()}")
        if not pixmap3.isNull():
            self.label_3.clear()
            self.label_3.setPixmap(pixmap3)
            self.label_3.setScaledContents(True)

        gela_path = self.get_image_path("gela.png")
        pixmap4 = QtGui.QPixmap(gela_path)
        print(f"gela.png pixmap isNull: {pixmap4.isNull()}")
        if not pixmap4.isNull():
            self.label_6.clear()
            self.label_6.setPixmap(pixmap4)
            self.label_6.setScaledContents(True)


    def retranslateUi(self, graduate_window):
        _translate = QtCore.QCoreApplication.translate
        graduate_window.setWindowTitle(_translate("graduate_window", "კურსდამთავრებულები"))

        self.label_2.setText(_translate("graduate_window", "'მთავარია კაცობაში არ\nჩაიჭრა თორე უმაღლესის ...'"))
        self.raodenoba_stud.setText(_translate("graduate_window", "დაამთავრა 286927 სტუდენტმა"))
        self.back_btn.setText(_translate("graduate_window", "უკან"))
        self.label_5.setText(_translate("graduate_window", "წარჩინებული სტუდენტები"))

class MainGraduateCustomized(Ui_graduate_window):

    def setupUi(self, graduate_window):
        super().setupUi(graduate_window)
        self._apply_custom_styling()

    def _apply_custom_styling(self):
        pass

    def retranslateUi(self, graduate_window):
        super().retranslateUi(graduate_window)

class MainGraduateCustomized(Ui_graduate_window):

    def setupUi(self, graduate_window):
        super().setupUi(graduate_window)
        self._apply_custom_styling()

    def _apply_custom_styling(self):
        pass

    def retranslateUi(self, graduate_window):
        super().retranslateUi(graduate_window)

class MainGraduateCustomized(Ui_graduate_window):

    def setupUi(self, graduate_window):
        super().setupUi(graduate_window)
        self._apply_custom_styling()

    def _apply_custom_styling(self):
        pass

    def retranslateUi(self, graduate_window):
        super().retranslateUi(graduate_window)

class MainGraduateCustomized(Ui_graduate_window):

    def setupUi(self, graduate_window):
        super().setupUi(graduate_window)
        self._apply_custom_styling()

    def _apply_custom_styling(self):
        pass

    def retranslateUi(self, graduate_window):
        super().retranslateUi(graduate_window)


# ===== FOUNDERS CLASS =====
class MainFounders(Ui_founders):

    def setupUi(self, founders):
        super().setupUi(founders)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.get_image_path("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        founders.setWindowIcon(icon)

        self._load_all_images()

        founders.update()

    def get_image_path(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_dir, "ui", "img", filename)

        print(f"Looking for: {filename}")
        print(f"Full path: {img_path}")
        print(f"File exists: {os.path.exists(img_path)}")

        if os.path.exists(img_path):
            return img_path
        else:
            alt_paths = [
                os.path.join(current_dir, "img", filename),
                os.path.join(os.getcwd(), "ui", "img", filename),
                os.path.join(os.getcwd(), "img", filename)
            ]

            for alt_path in alt_paths:
                print(f"Trying alternative: {alt_path}")
                if os.path.exists(alt_path):
                    print(f"Found at: {alt_path}")
                    return alt_path

            print(f"ERROR: Image not found anywhere: {filename}")
            return img_path



    def _load_all_images(self):

        founders_logo_path = self.get_image_path("founders_logo.png")
        pixmap1 = QtGui.QPixmap(founders_logo_path)
        print(f"founders_logo.png pixmap isNull: {pixmap1.isNull()}")
        if not pixmap1.isNull():
            self.label.clear()
            self.label.setPixmap(pixmap1)
            self.label.setScaledContents(True)

        founders_path = self.get_image_path("founders.png")
        pixmap2 = QtGui.QPixmap(founders_path)
        print(f"founders.png pixmap isNull: {pixmap2.isNull()}")
        if not pixmap2.isNull():
            self.label_2.clear()
            self.label_2.setPixmap(pixmap2)
            self.label_2.setScaledContents(True)

        foundres_txt_path = self.get_image_path("foundres_txt.png")
        pixmap3 = QtGui.QPixmap(foundres_txt_path)
        print(f"foundres_txt.png pixmap isNull: {pixmap3.isNull()}")
        if not pixmap3.isNull():
            self.label_3.clear()
            self.label_3.setPixmap(pixmap3)
            self.label_3.setScaledContents(True)

        title_founders_path = self.get_image_path("title_founders.png")
        pixmap4 = QtGui.QPixmap(title_founders_path)
        print(f"title_founders.png pixmap isNull: {pixmap4.isNull()}")
        if not pixmap4.isNull():
            self.label_4.clear()
            self.label_4.setPixmap(pixmap4)
            self.label_4.setScaledContents(True)

    def retranslateUi(self, founders):
        _translate = QtCore.QCoreApplication.translate
        founders.setWindowTitle(_translate("founders", "დამფუძნებლები"))

class MainFoundersCustomized(Ui_founders):

    def setupUi(self, founders):
        super().setupUi(founders)

    def retranslateUi(self, founders):
        super().retranslateUi(founders)
        pass

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QDialog()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
