# HTML Modularization Tool

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

##Output

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
