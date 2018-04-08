import os

site = input('Site name:')
author = input('Author:')
js_folder = input('Do you want a folder for JavaScript? y or n >').lower()
css_folder = input('Do you want a folder for CSS? y or n >').lower()

template= f'''<!DOCTYPE html>
<html>
<head>
    <title>{site}</title>
    <meta name = "author", content = "{author}">
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
'''

try:
    os.makedirs(site)
    print(f'Created ./{site}')
    with open(os.path.join(site,'index'+".html"),'w') as html:
        html.write(template)
        html.close()
    print(f'Created ./{site}/index.html')
    if js_folder == ('y' or 'yes'):
        os.makedirs(os.path.join(site,'js'))
        print(f'Created ./{site}/js/')
    else:
        pass
    if css_folder == ('y' or 'yes'):
        os.makedirs(os.path.join(site,'css'))
        print(f'Created ./{site}/css')

except FileExistsError:
    print('Folder name already exist, try again')
    pass
    
