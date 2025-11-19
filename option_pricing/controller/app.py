from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QIntValidator, QDoubleValidator
from ui.calculator_ui import Ui_MainWindow
from controller.input_parser import parse_common_inputs
from controller.pricing_service import PricingService
from controller.display_result import TableManager
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize managers
        self.table_manager = TableManager(self.ui.tableWidget)
        
        # Option Style Radio Buttons
        self.ui.EuropeanStyle_RadioButton.toggled.connect(self.on_option_style_changed)   # European
        self.ui.AmericanStyle_RadioButton.toggled.connect(self.on_option_style_changed) # American

        # Set European as default on startup
        self.ui.EuropeanStyle_RadioButton.setChecked(True)
        
        # Validators
        float_validator = QDoubleValidator()
        self.ui.StockPriceInput.setValidator(float_validator)
        self.ui.StrikeInput.setValidator(float_validator)
        self.ui.TimeInput.setValidator(float_validator)
        self.ui.RiskFreeInput.setValidator(float_validator)
        self.ui.sigmaInput.setValidator(float_validator)

        MAX_VAL_BT = 9999
        MAX_VAL_MC = 9999999
        bt_int_validator = QIntValidator(1, MAX_VAL_BT)
        mc_int_validator = QIntValidator(1, MAX_VAL_MC)
        self.ui.TimeStep_Input.setValidator(bt_int_validator)
        self.ui.NumSim_Input.setValidator(mc_int_validator)

        # Max Buttons
        self.ui.TimeStepMax_Button.clicked.connect(lambda: self.ui.TimeStep_Input.setText(str(MAX_VAL_BT)))
        self.ui.NumSimMax_Button.clicked.connect(lambda: self.ui.NumSim_Input.setText(str(MAX_VAL_MC)))

        # Checkbox change signals
        self.ui.BS_CheckBox.stateChanged.connect(self.on_bs_checkbox_changed)
        self.ui.BT_CheckBox.stateChanged.connect(self.on_bt_checkbox_changed)
        self.ui.MC_CheckBox.stateChanged.connect(self.on_mc_checkbox_changed)

        # Shared Inputs Update All
        for inp in [
            self.ui.StockPriceInput,
            self.ui.StrikeInput,
            self.ui.TimeInput,
            self.ui.RiskFreeInput,
            self.ui.sigmaInput
        ]:
            inp.textChanged.connect(self.update_all_results)

        # Individual method inputs
        self.ui.TimeStep_Input.textChanged.connect(lambda: self.update_bt_results())
        self.ui.NumSim_Input.textChanged.connect(lambda: self.update_mc_results())

        # Initial UI state
        self.ui.BS_CheckBox.setChecked(True)
        self.ui.BT_GroupBox.setEnabled(self.ui.BT_CheckBox.isChecked())
        self.ui.MC_GroupBox.setEnabled(self.ui.MC_CheckBox.isChecked())
        self.update_all_results()
        
    def on_option_style_changed(self):
        if self.ui.AmericanStyle_RadioButton.isChecked():  # American style selected
            self.ui.BS_CheckBox.setEnabled(False)
            self.ui.MC_CheckBox.setEnabled(False)
            self.ui.BS_CheckBox.setChecked(False)
            self.ui.MC_CheckBox.setChecked(False)
            self.update_bt_results()
        else:  # European style selected
            self.ui.BS_CheckBox.setEnabled(True)
            self.ui.MC_CheckBox.setEnabled(True)
            self.update_bt_results()

    def on_bs_checkbox_changed(self):  # Black-Scholes
        if self.ui.BS_CheckBox.isChecked():
            self.update_bs_results()
        else:
            self.table_manager.clear_column(0)
            
    def on_bt_checkbox_changed(self):  # Binomial Tree
        checked = self.ui.BT_CheckBox.isChecked()
        self.ui.BT_GroupBox.setEnabled(checked)
        if checked:
            self.update_bt_results()
        else:
            self.table_manager.clear_column(1)
            
    def on_mc_checkbox_changed(self):  # Monte Carlo
        checked = self.ui.MC_CheckBox.isChecked()
        self.ui.MC_GroupBox.setEnabled(checked)
        if checked:
            self.update_mc_results()
        else:
            self.table_manager.clear_column(2)

    def update_all_results(self):
        try:
            params = parse_common_inputs(self.ui)
            self.update_bs_results(params)
            self.update_bt_results(params)
            self.update_mc_results(params)
        except (ValueError, Exception):
            self.table_manager.clear_column(0)
            self.table_manager.clear_column(1)
            self.table_manager.clear_column(2)

    def update_bs_results(self, params=None):  # Black-Scholes column (0)
        if not self.ui.BS_CheckBox.isChecked():
            self.table_manager.clear_column(0)
            return
        
        try:
            if params is None:
                params = parse_common_inputs(self.ui)
            prices = PricingService.calculate_bs(params)
            if prices:
                self.table_manager.update_column(0, prices['call'], prices['put'])
            else:
                self.table_manager.clear_column(0)
        except (ValueError, Exception):
            self.table_manager.clear_column(0)

    def update_bt_results(self, params=None):  # Binomial Tree column (1)
        if not self.ui.BT_CheckBox.isChecked():
            self.table_manager.clear_column(1)
            return
        
        try:
            if params is None:
                params = parse_common_inputs(self.ui)
            time_steps = int(self.ui.TimeStep_Input.text())
            style = 'american' if self.ui.AmericanStyle_RadioButton.isChecked() else 'european'
            
            prices = PricingService.calculate_bt(params, time_steps, style)
            if prices:
                self.table_manager.update_column(1, prices['call'], prices['put'])
            else:
                self.table_manager.clear_column(1)
        except (ValueError, Exception):
            self.table_manager.clear_column(1)

    def update_mc_results(self, params=None):  # Monte Carlo column (2)
        if not self.ui.MC_CheckBox.isChecked():
            self.table_manager.clear_column(2)
            return
        
        try:
            if params is None:
                params = parse_common_inputs(self.ui)
            num_sim = int(self.ui.NumSim_Input.text())
            
            prices = PricingService.calculate_mc(params, num_sim)
            if prices:
                self.table_manager.update_column(2, prices['call'], prices['put'])
            else:
                self.table_manager.clear_column(2)
        except (ValueError, Exception):
            self.table_manager.clear_column(2)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec()