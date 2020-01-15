#from PIL import Image, ImageFont, ImageDraw
#from saenews.sae3 import *
from saenews.sutils import quote, put_quote


title = "Kashmir Mein Rehna Hoga to Allah ho Akbar Kehna Hoga"
tag_line = "If you wan't to live in Kashmir you need to pray 'Allah ho Akbar'"
input_file_orig = "last.png"

put_quote(title=title, tag_line=tag_line, black_strip_dims=(0, 0, 0, 3), input_file_orig=input_file_orig, output_file='', title_cord=(0.035, 0.166), title_font_size=90, tag_font_size=50, title_width_ratio=0.5, border_width='', logo_border='', border_color='red', title_text_font='ArabDances.ttf', tag_text_font='fonts/PTS75F.ttf', tag_width_ratio=0.44, tag_cord=(0.035, 0.766), focus='false')

