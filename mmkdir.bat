@echo off
python -c "import os, sys; main_folder = sys.argv[1]; sub_folders = ['texture', 'model', 'lookdev', 'ref', 'export/model', 'export/maps']; [os.makedirs(main_folder + '/' + folder, exist_ok=True) for folder in sub_folders];" %1
pause
