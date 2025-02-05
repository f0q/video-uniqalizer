from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips
import os
import glob

# Пути к папкам и изображению
source_folder = 'input'
output_folder = 'output'
image_path = 'pic.jpg'

# Убедитесь, что папка вывода существует, если нет - создайте её
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Найти все MP4 файлы в папке с исходными видео
video_files = glob.glob(os.path.join(source_folder, '*.mp4'))

for video_path in video_files:
    video_clip = VideoFileClip(video_path)
    video_size = video_clip.size
    image_duration = 3 / video_clip.fps
    image_clip = ImageClip(image_path, duration=image_duration).resize(video_size)
    video_clip_cut = video_clip.subclip(image_duration)
    final_clip = concatenate_videoclips([image_clip, video_clip_cut], method="compose")

    # Определение имени выходного файла
    output_video_path = os.path.join(output_folder, os.path.basename(video_path))

    # Экспорт финального видео
    final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    print(f'Видео сохранено: {output_video_path}')

# Освободить ресурсы
video_clip.close()
image_clip.close()
