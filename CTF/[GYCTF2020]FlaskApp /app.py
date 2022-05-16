# def waf(str):
#   black_list = [ &
#     #34;flag&# 34;, & #34;os&# 34;, & #34;system&# 34;, &
#     #34;popen&# 34;, & #34;import&# 34;, & #34;eval&# 34;, &
#     #34;chr&# 34;, & #34;request&# 34;, & #34;subprocess&# 34;, &
#     #34;commands&# 34;, & #34;socket&# 34;, & #34;hex&# 34;, &
#     #34;base64&# 34;, & #34;*&# 34;, & #34;?&# 34;
# ]
#   for x in black_list:
#     if x in str.lower():
#       return 1@ app.route( &#39;/hint&# 39;, methods = [ & #39;GET&# 39;])