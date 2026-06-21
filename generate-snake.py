import urllib.request
import os

username = "whyuardi"
output_dir = "output"

# Generate dark snake
dark_url = f"https://raw.githubusercontent.com/whyuardi/whyuardi/output/github-contribution-grid-snake-dark.svg"
try:
    urllib.request.urlretrieve(dark_url, f"{output_dir}/github-contribution-grid-snake-dark.svg")
    print("Snake SVG downloaded")
except:
    print("Using placeholder - snake will generate after first push")
    # Create placeholder
    with open(f"{output_dir}/github-contribution-grid-snake-dark.svg", "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"/>')
