import os
import markdownify
import re

# Define the paths to the source and destination folders
src_folder = '/Users/farruhkushnazarov/Downloads/temp/medium-export/posts'
dst_folder = '_posts'

# Create the destination folder if it doesn't exist
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# Loop through all files in the source folder
for filename in os.listdir(src_folder):
    # Check if the file is an HTML file
    if filename.endswith('.html'):
        # Construct the paths to the source and destination files
        src_path = os.path.join(src_folder, filename)
        # split the file name and extension
        new_file_name, file_ext = os.path.splitext(filename)

        # remove the unique identifier from the file name
        new_file_name = new_file_name[:-13]

        # Extract the title and date from the file name
        title = new_file_name.replace('-', ' ')[11:]
        title = re.sub(' +', ' ', title)

        date_str = new_file_name[:10]
        date = '-'.join(date_str.split('-')[::-1])

        # Generate the permalink from the file name
        save_filename = '-'.join(new_file_name.split('_')[1].split('-')[:2])
        permalink = '/posts/' + date_str[:-3] + '/' + save_filename + '/'

        # Read the contents of the HTML file
        with open(src_path, 'r') as f:
            html_content = f.read()

        # Convert the HTML content to Markdown format
        md_content = markdownify.markdownify(html_content)

        # Add the front matter to the Markdown content
        front_matter = '---\n'
        front_matter += 'title: \'' + title.title() + '\'\n'
        front_matter += 'date: ' + date_str + '\n'
        front_matter += 'permalink: ' + permalink + '\n'
        front_matter += 'tags:\n'
        front_matter += '  - cool posts\n'
        front_matter += '  - category1\n'
        front_matter += '  - category2\n'
        front_matter += '---\n\n'

        md_content = front_matter + md_content


        # rename the file
        dst_path = os.path.join(dst_folder, date_str + '-' + save_filename + '.md')

        # Write the Markdown content to the destination file
        with open(dst_path, 'w') as f:
            f.write(md_content)
