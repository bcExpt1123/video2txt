import subprocess

def convert_webm_to_avi(input_file, output_file):
    """
    Converts a WebM video file to AVI format using FFmpeg.

    Args:
        input_file (str): Path to the input WebM file.
        output_file (str): Path for the output AVI file.
    """
    try:
        subprocess.run(['ffmpeg', '-i', input_file, output_file], check=True)
        print(f"Conversion successful: {input_file} converted to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Please ensure FFmpeg is installed and in your system's PATH.")

# Example usage:
input_webm = "input.webm"
output_avi = "output.avi"
convert_webm_to_avi(input_webm, output_avi)