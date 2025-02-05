import subprocess
import os
import glob

# Замените этот путь на директорию, где находятся ваши видеофайлы
source_folder = 'input'

# Замените этот путь на директорию, куда будут сохраняться обновленные видеофайлы
output_folder = 'output'

# Убедитесь, что папка вывода существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Получение списка всех MP4 файлов в папке
video_files = glob.glob(os.path.join(source_folder, '*.mp4'))

for video_file in video_files:
    # Создаем новое имя файла для сохранения уникализированного видео
    output_file_path = os.path.join(output_folder, os.path.basename(video_file))
    
    # Замените значения метаданных на желаемые
    metadata_to_change = {
        "title": "sudgfkjagfkjwh",
        "artist": "gkljalhskgjnl",
        "comment": "dfklgdgjhlkw"   
    }
    
    # Формирование команды для ffmpeg
    metadata_params = sum([['-metadata', f'{key}={value}'] for key, value in metadata_to_change.items()], [])
    command = ['ffmpeg', '-i', video_file, *metadata_params, '-codec', 'copy', output_file_path]
    
    # Выполнение команды
    subprocess.run(command)

    print(f'Файл обновлен: {output_file_path}')
