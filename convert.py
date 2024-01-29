print('Modularization complete. Files created:')
print(output_html_path)
print(output_css_path)
print(output_js_path)

# Save the modified HTML content to a temporary file for validation
temp_html_path = 'temp_validation.html'
with open(temp_html_path, 'w', encoding='utf-8') as temp_file:
    temp_file.write(str(soup))

# Validate the temporary HTML file using the html5validator command-line tool
try:
    subprocess.run(['html5validator', '--file', temp_html_path], check=True)
    print("The modified HTML is valid according to HTML5 standards.")
except subprocess.CalledProcessError as e:
    print("Warning: The modified HTML is not valid according to HTML5 standards.")
    print(e)

# Remove the temporary file after validation
os.remove(temp_html_path)

# Log messages throughout the process
logging.info('Modularization started.')
logging.info('Backup files created:')
logging.info(backup_html_path)
logging.info(backup_css_path)
logging.info(backup_js_path)
logging.info('Modularization complete. Files created:')
logging.info(output_html_path)
logging.info(output_css_path)
logging.info(output_js_path)

print('Modularization complete. Backup files created:')
print(backup_html_path)
print(backup_css_path)
print(backup_js_path)
print('Output files created:')
print(output_html_path)
print(output_css_path)
print(output_js_path)
