import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QPushButton, QGridLayout, QScrollArea, QFrame, QMessageBox
)
from PySide6.QtCore import Qt

class OmniLauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OmniLauncher | محاكي الألعاب الموحد بتقنية RTX")
        self.resize(1280, 800)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)

        # الشريط العلوي
        header_layout = QHBoxLayout()
        title_label = QLabel("⚡ OMNI LAUNCHER // RTX PATH TRACING")
        title_label.setObjectName("mainTitle")
        
        rtx_btn = QPushButton("✨ RTX: ON (DLSS Quality)")
        rtx_btn.setObjectName("rtxBadgeButton")
        
        download_btn = QPushButton("⬇️ تحميل لعبة جديدة")
        download_btn.setObjectName("primaryActionButton")
        download_btn.clicked.connect(self.on_download_clicked)

        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(rtx_btn)
        header_layout.addWidget(download_btn)
        main_layout.addLayout(header_layout)

        # شبكة الألعاب
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
        grid_widget = QWidget()
        self.grid_layout = QGridLayout(grid_widget)
        self.grid_layout.setSpacing(20)
        
        self.populate_games()
        scroll.setWidget(grid_widget)
        main_layout.addWidget(scroll)

        self.setCentralWidget(central_widget)

    def populate_games(self):
        games = [
            {"title": "God of War III", "system": "RPCS3 (PS3)", "rtx": "4K Path Tracing"},
            {"title": "Zelda: Tears of the Kingdom", "system": "Ryujinx (Switch)", "rtx": "60FPS DLSS"},
            {"title": "Shadow of the Colossus", "system": "PCSX2 (PS2)", "rtx": "Ray Traced Bloom"},
            {"title": "Super Mario Galaxy", "system": "Dolphin (Wii)", "rtx": "HDR Remaster"}
        ]
        
        for idx, g in enumerate(games):
            card = QFrame()
            card.setObjectName("gameCard")
            card_layout = QVBoxLayout(card)
            
            t = QLabel(g["title"])
            t.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
            
            s = QLabel(f"🎮 {g['system']} · ✨ {g['rtx']}")
            s.setStyleSheet("color: #94A3B8; font-size: 12px;")
            
            btn = QPushButton("تشغيل الآن ⚡")
            btn.setObjectName("launchGameButton")
            btn.clicked.connect(lambda checked, name=g["title"]: self.launch_game_prompt(name))
            
            card_layout.addWidget(t)
            card_layout.addWidget(s)
            card_layout.addWidget(btn)
            
            row, col = divmod(idx, 2)
            self.grid_layout.addWidget(card, row, col)

    def launch_game_prompt(self, title):
        QMessageBox.information(self, "تشغيل اللعبة", f"جاري تشغيل لعبة: {title}\nمع حقن إعدادات RTX Path Tracing!")

    def on_download_clicked(self):
        QMessageBox.information(self, "مدير التحميل", "أدخل رابط تحميل اللعبة المباشر للبدء.")