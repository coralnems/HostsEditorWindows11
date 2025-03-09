import sys
import os
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import Qt

# Determine the hosts file location based on your operating system.
if os.name == 'nt':
    HOSTS_PATH = r'C:\Windows\System32\drivers\etc\hosts'
else:
    HOSTS_PATH = '/etc/hosts'

# URL for a sample block list. Replace with your preferred URL if needed.
BLOCK_LIST_URL = "https://someonewhocares.org/hosts/hosts"

class HostEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hosts File Editor")
        self.resize(800, 600)

        # Central widget and layout.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Info label.
        info_label = QLabel("Edit your hosts file and merge remote block lists.")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)

        # Text editor for hosts file content.
        self.hosts_edit = QTextEdit()
        main_layout.addWidget(self.hosts_edit)

        # Button layout.
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # Button to load hosts file.
        load_button = QPushButton("Load Hosts File")
        load_button.clicked.connect(self.load_hosts_file)
        button_layout.addWidget(load_button)

        # Button to pull and merge block list.
        pull_button = QPushButton("Pull & Merge Block List")
        pull_button.clicked.connect(self.pull_and_merge_blocklist)
        button_layout.addWidget(pull_button)

        # Button to save hosts file.
        save_button = QPushButton("Save Hosts File")
        save_button.clicked.connect(self.save_hosts_file)
        button_layout.addWidget(save_button)

        # Load hosts file initially.
        self.load_hosts_file()

    def load_hosts_file(self):
        """Load the current hosts file into the text editor."""
        try:
            with open(HOSTS_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
            self.hosts_edit.setPlainText(content)
        except Exception as e:
            QMessageBox.critical(self, "Error Loading File", f"Unable to load hosts file:\n{e}")

    def pull_and_merge_blocklist(self):
        """Fetch a remote block list and append it to the hosts content."""
        try:
            response = requests.get(BLOCK_LIST_URL)
            response.raise_for_status()
            blocklist_content = response.text

            # Create a marker for where the block list is inserted.
            marker = "\n\n# --- Begin Merged Block List ---\n"
            end_marker = "\n# --- End Merged Block List ---\n"
            current_text = self.hosts_edit.toPlainText()

            # Remove previous merged block list if present.
            if "# --- Begin Merged Block List ---" in current_text:
                start = current_text.find("# --- Begin Merged Block List ---")
                current_text = current_text[:start].rstrip()

            merged_content = current_text + marker + blocklist_content + end_marker
            self.hosts_edit.setPlainText(merged_content)
            QMessageBox.information(self, "Merge Complete", "The block list was successfully merged!")
        except Exception as e:
            QMessageBox.critical(self, "Error Fetching Block List", f"Failed to fetch block list:\n{e}")

    def save_hosts_file(self):
        """Save the contents of the text editor to the hosts file."""
        try:
            # Writing to the hosts file typically requires elevated privileges.
            with open(HOSTS_PATH, 'w', encoding='utf-8') as f:
                f.write(self.hosts_edit.toPlainText())
            QMessageBox.information(self, "Save Successful", "Hosts file saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error Saving File", f"Unable to save hosts file:\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HostEditorWindow()
    window.show()
    sys.exit(app.exec())
