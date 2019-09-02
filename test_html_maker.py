def makes_html_blog_post_bit(date, ipynb_title):
    title = input('input blog post title: ')
    date = date
    description = input('write short description: ')
    type = input('classify type of post (#100daysofcode, etc): ')
    url = ipynb_title



    return title, date, description, type, url

print(makes_html_blog_post_bit('Sun Sep  1 01:29:31 CDT 2019', 'file'))