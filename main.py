import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()  # calls the parent or original __init__ method of supper class QWidget
        grid = QGridLayout()

        # Create widgets
        name_lable = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        date_birth_lable = QLabel("Date of Birth MM/DD/YYYY:")
        self.date_birth_line_edit = QLineEdit()  # to make this local varialbe accessible for other methods, add "self" to convert to instance variable!

        calculate_button = QPushButton()
        calculate_button.clicked.connect(self.calculate_age)
        self.output_lable = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_lable,0,0)  #in position 0,0 like x , y
        grid.addWidget(self.name_line_edit,0,1)  #in position 0,0 like x , y
        grid.addWidget(date_birth_lable,1,0)  #in position 0,0 like x , y
        grid.addWidget(self.date_birth_line_edit,1,1)  #in position 0,0 like x , y
        grid.addWidget(calculate_button, 2, 0, 1, 2)  #in position 2,0,  1 row and span in 2 columns
        grid.addWidget(self.output_lable, 3, 0, 1, 2)  #in position 2,0,  1 row and span in 2 columns


        self.setLayout(grid)  # if not called like this, it will show empty frame!

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_lable.setText(f"{self.name_line_edit.text()} is {age} years old.")



app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())