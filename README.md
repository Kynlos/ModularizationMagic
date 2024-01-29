# Modularization Magic ✨

This tool is designed to help web developers modularize their HTML files by extracting inline JavaScript and CSS into separate files. It also provides options to minify the extracted CSS and JS files and to compress the HTML content.

## Features

- Extract inline JavaScript and CSS from an HTML file.
- Minify JavaScript and CSS if desired.
- Compress HTML content if desired.
- Create backups of the original HTML file.
- Validate the resulting HTML using the `html5validator` tool.
- Logging of the modularization process.

## Requirements

- Python 3.x
- BeautifulSoup4: `pip install beautifulsoup4`
- cssmin: `pip install cssmin`
- jsmin: `pip install jsmin`
- htmlmin: `pip install htmlmin`
- html5validator (optional for validation): Install with `npm install -g html5validator`

## Usage

To use the HTML Modularization Tool, simply run the script and follow the prompts:

```bash
python convert.py
```

You will be asked to provide paths for the input HTML file and the output files for HTML, CSS, and JS. You can also choose whether to minify the JavaScript and CSS and whether to compress the HTML content.

## Input Prompts

- Enter the path of the input HTML file.
- Enter the path for the output HTML file (default: output.html).
- Enter the path for the output CSS file (default: styles.css).
- Enter the path for the output JS file (default: scripts.js).
- Confirm overwriting if output files already exist.
- Choose whether to minify JS (y/n).
- Choose whether to minify CSS (y/n).
- Enter a custom title for the HTML document (optional).
- Choose whether to compress HTML (y/n).

## Output

The script will generate the following files:

- A new HTML file with links to the external CSS and JS files.
- An external CSS file containing all styles extracted from the HTML.
- An external JS file containing all scripts extracted from the HTML.
- Backup files of the original HTML content.

## Validation

If you have html5validator installed, the script will validate the modified HTML file and report any issues.

## Logging

The script logs the modularization process to modularization.log.

## License
This project is open source and available under the MIT License.

## Contributions

Contributions are welcome! Please feel free to submit a pull request.

## Support

If you encounter any problems or have suggestions, please open an issue on the project's GitHub page.

---

# About Modularization Magic ✨

Welcome to the world of Modularization Magic, where your HTML files undergo a transformation like never before! 🚀

Do you find yourself drowning in a sea of tangled HTML, tangled scripts, and messy styles? Fear not! Our Python script is here to rescue you from the chaos and bring order to your web development endeavors.

## What is Modularization Magic?

This enchanting script empowers you to wave a wand (or a keyboard) and effortlessly modularize your HTML files. It extracts JavaScript and CSS elements, creating separate files for a cleaner, more organized codebase.

But that's not all! With options for minification, compression, and customization, this script adds a touch of wizardry to your web development toolkit.

## How to Unleash the Magic

Simply run the script, answer a few prompts, and watch as it performs its spellbinding feats:

1. **Extracting Scripts and Styles:** The script gracefully separates scripts and styles, turning chaos into clarity.

2. **Creating Backups:** Fear not the unknown! The script creates backups of your original HTML, CSS, and JS files with timestamps.

3. **Minification and Compression:** Choose to minify your JavaScript and CSS for a streamlined, efficient enchantment. You can also compress the HTML for an added touch of magic.

4. **Customization:** Give your HTML document a unique identity with a custom title.

5. **Validation:** The script ensures your magic is in harmony with HTML5 standards by validating the modified HTML.

## Abracadabra, Your Code is Transformed!

Let the Modularization Magic script be your trusted companion on your web development adventures. Embrace the magic, organize your code, and watch your projects sparkle with newfound brilliance!

🧙 Happy Coding and May the Modularization Magic Be Ever in Your Favor! 🌟

