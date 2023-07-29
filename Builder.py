import os
import PyInstaller.__main__

def build_exe(input_script, output_dir):
    PyInstaller.__main__.run([
        '--onefile',
        '--windowed',
        '--noconsole',  # Add this option to hide the console window
        '--add-data', f'{input_script};.',
        '--add-data', 'Cookies.py;.',
        '--add-data', 'Password.py;.',
        '--add-data', 'Token.py;.',
        input_script,
        '-p', f'{os.path.dirname(input_script)}'
    ])
    
if __name__ == "__main__":
    main_script = "Main.py"  
    output_directory = "dist" 
    build_exe(main_script, output_directory)
