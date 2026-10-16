import shutil
from pathlib import Path

class GraphicsEnhancementEngine:
    def __init__(self, preset_path: str = "assets/shaders/rtgi_pathtrace.ini"):
        self.preset_path = Path(preset_path)

    def inject_reshade_to_emulator(self, emulator_folder: str) -> bool:
        target_dir = Path(emulator_folder)
        if not target_dir.exists():
            return False

        dest_preset = target_dir / "ReShadePreset.ini"
        if self.preset_path.exists():
            shutil.copy(self.preset_path, dest_preset)
            print(f"[رسومات] تم نسخ إعدادات تتبع الأشعة RTGI إلى: {dest_preset}")
            return True
        return False

    def generate_dlss_config(self, mode: str = "quality") -> dict:
        scaling_ratios = {
            "ultra_performance": 0.33,
            "performance": 0.50,
            "balanced": 0.58,
            "quality": 0.67,
            "dlaa": 1.00
        }
        return {
            "mode": mode,
            "scale_factor": scaling_ratios.get(mode, 0.67),
            "sharpening": 0.35,
            "ray_tracing_bounces": 2 if mode in ["quality", "dlaa"] else 1
        }