print ('Build site!')

# Opening template HTML files
top_html = open ('templates/top.html').read()
bottom_html = open ('templates/bottom.html').read()

# Read index HTML file
index_html = open ('content/index.html').read()

# Combine index HTML with top and bottom templates


index_html = top_html + index_html + bottom_html
open('docs/index.html', 'w+').write(index_html)


