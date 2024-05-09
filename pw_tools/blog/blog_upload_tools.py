import os
from bs4 import BeautifulSoup
import re
from .._common.config_and_logger import logger_pw_tools, config
import shutil
import zipfile


def replace_img_src_jinja(blog_post_index_file_path_and_name):
    
    logger_pw_tools.info(f"- Reading file to replace img src jinja: {blog_post_index_file_path_and_name} -")
    logger_pw_tools.info(blog_post_index_file_path_and_name)
    
    try:
        #read html into beautifulsoup
        with open(blog_post_index_file_path_and_name) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    except FileNotFoundError:
        return "Error opening index.html"

    #get all images tags in html
    image_list = soup.find_all('img')


    # check all images have src or remove
    # for img in image_list:
    for img in soup.find_all('img'):
        # temp_dict = {}
        try:
            if img.get('src') == "":
                image_list.remove(img)
                # print("removed img")
            else:
                img['src'] = "{{ url_for('bp_blog.get_post_files', post_dir_name=post_dir_name,img_dir_name='" + \
                    "images', filename='"+ img['src'][img['src'].find("/")+1:]+"')}}"
        except AttributeError:
            image_list.remove(img)
            # print('removed img with exception')

    # print(soup)
    return str(soup)



#
def replace_code_snippet_filename_with_jinja_include_block(blog_post_index_file_path_and_name,
    new_post_dir_name):
    try:
        #read html into beautifulsoup
        with open(blog_post_index_file_path_and_name) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    except FileNotFoundError:
        return "Error opening index.html"

    # path_to_blog_post_code_snippets = os.path.join(current_app.config.get("DIR_BLOG_POSTS"),new_post_dir_name,"code_snippets")
    path_to_blog_post_code_snippets = os.path.join(config.DIR_BLOG_POSTS,new_post_dir_name,"code_snippets")
    code_snippet_filename_list = os.listdir(path_to_blog_post_code_snippets)

    # p_tags = soup.find_all('p')

    # Iterate over all <p> tags
    for p in soup.find_all('p'):
        if p.text in code_snippet_filename_list:
            # Create a new div element
            new_div = soup.new_tag('div')
            new_div['class'] = 'div_code_super'
            # Insert the f-string with the file name
            new_div.string = f"{{% include 'code_snippets/{p.text}' %}}"
            # Replace the <p> tag with the new <div>
            p.replace_with(new_div)


    # for p_tag in p_tags:
    #     for element in p_tag.contents:
    #         try:

    #             if code_snippet_filename_list.index(str(element))==0:
    #                 new_div_code_super = soup.new_tag('div', **{'class': 'div_code_super'})
    #                 # {% include 'code_snippets/codeSnippet01-setupUbuntu.html' %}
    #                 new_div_code_super.append(f"{{% include 'code_snippets/{str(element)}' %}}")
                    
    #                 p_tag.replace_with(new_div_code_super)
    #         except Exception as e:
    #             # logger_pw_tools.info(f"{type(e).__name__}:{e}")
    #             pass
    return str(soup)




def get_title(html_file_path_and_name, index_source):
    print("- In: blog/utils/get_title() -")
    title = ""
    #read html into beautifulsoup
    with open(html_file_path_and_name) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    # if index_source == "ms_word":
    if index_source == "origin_from_word":
        try:
            title = soup.p.find('span').contents[0]
        except:
            logger_pw_tools.info(f"- No title found ms_word -")

    # elif index_source == "original_html":
    elif index_source == "origin_from_html":
        list_of_soup_searches = ["h1", "h2", "h3", "h4"]
        
        for tag in list_of_soup_searches:
            title_tag = soup.find(tag)
            print("title_tag: ", title_tag)
            print("Examining tag: ", tag)
            if title_tag != None:
                break
        try:
            print("Getting contents for tag: ", tag)
            print(title_tag.contents[0])
            title=title_tag.contents[0]
        except:
            logger_pw_tools.info(f"- No title found origina_html  -")


    return title


def sanitize_directory_name(directory_path):
    # cleans file directory_path name, renames dir if necessary, returns directory_path string
    logger_pw_tools.info(f"- in sanitize_directory_name  -")
    # Get the directory name from the path
    directory_name = os.path.basename(directory_path)
    print("directory_name: ", directory_name)

    # # Remove non-alphanumeric characters
    # directory_name = re.sub(r'\W+', '', directory_name)

    # Remove .fld
    directory_name = re.sub('.fld', '', directory_name)


    # Replace spaces with underscores
    directory_name = directory_name.replace(' ', '_')
    print("directory_name (sanatized): ", directory_name)

    # Create the new directory path with the sanitized name
    new_directory_path = os.path.join(os.path.dirname(directory_path), directory_name)
    print("new_directory_path (sanatized): ", new_directory_path)

    # Rename the directory if the sanitized name is different
    if directory_path != new_directory_path:
        os.rename(directory_path, new_directory_path)
        print("Directory name sanitized and renamed successfully.")
    else:
        print("No changes needed.")
    
    return directory_name

def read_html_to_soup(blog_post_index_file_path_and_name):
    # Read the HTML file
    with open(blog_post_index_file_path_and_name, 'r', encoding='utf-8') as file:
        html_content = file.read()
    # Parse with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')
    return str(soup)

def remove_head(html_content):
    # # Read the HTML file
    # with open(blog_post_index_file_path_and_name, 'r', encoding='utf-8') as file:
    #     html_content = file.read()

    # Parse with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove the <head> element
    if soup.head:
        soup.head.decompose()

    return str(soup)


def remove_body_tags(html_content):
    # # Read the HTML file
    # with open(blog_post_index_file_path_and_name, 'r', encoding='utf-8') as file:
    #     html_content = file.read()

    # Parse with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract content within <body> tags
    body_contents = ''.join(str(tag) for tag in soup.body.contents) if soup.body else str(soup)

    return str(body_contents)


def replace_p_elements_with_img(html_content):
    # Parse with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all 'p' tags 
    p_tags = soup.find_all('p')

    for p_tag in p_tags:
        # Check if 'p' tag contains an 'img' element
        img = p_tag.find('img')
        if img:
            # Create a new 'div' with class 'blog_img'
            new_div = soup.new_tag('div', **{'class': 'blog_img'})
            # Move the 'img' element to the new 'div'
            new_div.append(img.extract())

            # Check if there is a caption - remove color around number due to span tag style
            if p_tag.find('font'):
                font_element = p_tag.find('font')
                # Append "width:100%" to the style attribute of the 'font' element
                current_style = font_element['style']
                font_element['style'] = current_style + "; width:100%"
                # check for i element, if yes, assume the rest...
                # Find the 'i' element (since your HTML indicates there's only one such element, we can safely use find())
                i_element = font_element.find('i')
                if i_element:
                    # Find the 'span' element within the 'i' element
                    span_element = i_element.find('span')
                    # Extract the text from the span element
                    span_text = span_element.text
                    
                    # Replace the span element with its own text
                    span_element.replace_with(span_text)

                # Append illustration
                new_div.append(p_tag.find('font'))

            # Replace the 'p' tag with the new 'div'
            p_tag.replace_with(new_div)

    return str(soup)

def remove_line_height_from_p_tags(html_content):

    # Parse with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Iterate through each 'p' tag and modify its 'style' attribute
    for p_tag in soup.find_all('p'):
        style = p_tag.get('style', '')  # Get the current 'style' attribute
        if 'line-height: 100%;' in style:
            # Remove 'line-height: 100%;' from the style
            new_style = style.replace('line-height: 100%;', '')
            # Update the 'style' attribute of the 'p' tag
            p_tag['style'] = new_style

    # Convert the modified soup_body back to string
    final_html_content = str(soup)

    return str(soup)


def replace_span_with_background_styling_with_contents(html_content):
        
    soup = BeautifulSoup(html_content, 'html.parser')
    # Iterate over all span tags
    for span in soup.find_all('span', style="background: #c0c0c0"):
        # Replace the span element with its own text content
        span.replace_with(span.get_text())

    return str(soup)



