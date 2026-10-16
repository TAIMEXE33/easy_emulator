import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from gui.main_window import OmniLauncherWindow

def main():
    # التأكد من وجود مجلدات العمل الأساسية
    Path("assets/covers").mkdir(parents=True, exist_ok=True)
    Path("downloads").mkdir(parents=True, exist_ok=True)

    app = QApplication(sys.argv)
    
    # تحميل الثيم الداكن الأسطوري
    qss_path = Path("gui/styles/dark_legendary.qss")
    if qss_path.exists():
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
            
    window = OmniLauncherWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()