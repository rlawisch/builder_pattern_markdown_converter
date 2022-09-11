from markdown_reader import MarkdownReader

if __name__ == '__main__':
    file_name = input("Type in the name of the markdown-formatted file to be converted to HTML:\n")

    with open(file_name, 'r') as file:
        markdown_data = file.read()

    if markdown_data:
        parser = MarkdownReader(markdown_data).to_html()
        parsed_html = parser.convert()

        if file_name.endswith('.md'):
            html_file_name = f"{file_name[:len(file_name)-3]}.html"
        else:
            html_file_name = f"{file_name}.html"

        with open(html_file_name, 'w') as output_file:
            output_file.write(parsed_html)

        print(f"\n {html_file_name} file sucessfully created")

    else:
        print(f"Error in file {file_name}")
