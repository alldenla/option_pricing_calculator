from PySide6.QtWidgets import QTableWidgetItem

class TableManager:
    """Manages updates to the pricing results table."""
    
    def __init__(self, table_widget):
        """Initialize with reference to QTableWidget."""
        self.table = table_widget
    
    def update_column(self, col, call_price, put_price):
        """Update a column with call and put prices.
        
        Args:
            col: int column index (0=BS, 1=BT, 2=MC)
            call_price: float or str for call price
            put_price: float or str for put price
        """
        self.table.setItem(0, col, QTableWidgetItem(str(call_price)))
        self.table.setItem(1, col, QTableWidgetItem(str(put_price)))
    
    def clear_column(self, col):
        """Clear a column (set to empty strings).
        
        Args:
            col: int column index (0=BS, 1=BT, 2=MC)
        """
        self.table.setItem(0, col, QTableWidgetItem(""))
        self.table.setItem(1, col, QTableWidgetItem(""))