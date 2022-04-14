from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

ffmpeg_extract_subclip(os.path.join(os.path.dirname(__file__), './sad_test.mkv'), 4, 84, targetname=r"C:\Users\Digi Max\Desktop\programming\CS50fair\Demo\sad.mkv")
