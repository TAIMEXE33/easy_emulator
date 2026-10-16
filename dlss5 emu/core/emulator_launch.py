import os
import subprocess
import yaml
from pathlib import Path
from typing import Optional

class EmulatorLauncher:
    def __init__(self, config_path: str = "config/emulators.yaml"):
        self.config_path = config_path
        self.emulators = self.load_config()

    def load_config(self) -> dict:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"لم يتم العثور على ملف: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("emulators", {})

    def launch_game(self, emulator_id: str, game_path: str, extra_args: Optional[list] = None) -> subprocess.Popen:
        if emulator_id not in self.emulators:
            raise ValueError(f"المحاكي {emulator_id} غير مسجل")

        emu_info = self.emulators[emulator_id]
        exe_path = Path(emu_info["executable"])

        raw_args = emu_info.get("launch_args", [])
        command = [str(exe_path)]

        for arg in raw_args:
            if "{game_path}" in arg:
                command.append(arg.format(game_path=game_path))
            else:
                command.append(arg)

        if extra_args:
            command.extend(extra_args)

        print(f"[تشغيل المحاكي]: {' '.join(command)}")
        return subprocess.Popen(
            command,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )