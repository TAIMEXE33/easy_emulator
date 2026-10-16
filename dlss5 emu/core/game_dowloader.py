import aiohttp
import zipfile
from pathlib import Path

class GameDownloader:
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    async def download_file(self, url: str, filename: str, progress_callback=None):
        dest_file = self.download_dir / filename
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                total_size = int(response.headers.get("content-length", 0))
                downloaded = 0

                with open(dest_file, "wb") as f:
                    async for chunk in response.content.iter_chunked(1024 * 64):
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0 and progress_callback:
                            percent = int((downloaded / total_size) * 100)
                            progress_callback(percent, downloaded, total_size)

        print(f"[تحميل] اكتمل تنزيل {filename}")
        return dest_file

    def extract_if_archive(self, file_path: Path, extract_to: Path):
        if file_path.suffix.lower() == ".zip":
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"[فك ضغط] تم استخراج اللعبة إلى: {extract_to}")