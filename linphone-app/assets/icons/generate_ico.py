#!/usr/bin/env python3
"""
Generate Windows .ico file from PNG logo
"""
from PIL import Image
import sys

def create_ico(source_png, output_ico):
    """Convert PNG to ICO with multiple resolutions"""
    img = Image.open(source_png)

    # Ensure it's square and has proper alpha channel
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Create different sizes for the icon
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # Save as ICO with multiple resolutions
    img.save(output_ico, format='ICO', sizes=sizes)
    print(f"Successfully created {output_ico}")

if __name__ == "__main__":
    source = "../images/nm-pbx-logo-256.png"
    output = "../icon.ico"

    try:
        create_ico(source, output)
    except ImportError:
        print("ERROR: Pillow library not installed. Install with: pip install Pillow")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
