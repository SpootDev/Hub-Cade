import wx

# misc settings that are not saved to config file

# MAME display pages
auinotebook_mame_list = []  # 1-Title/snap, 2-title, 3-snap, 4-cabinet, 5-cpanel, 6-marquee, 7-pcb, 8-video, 9-manual

# MESS display pages
auinotebook_mess_list = []  # 1-title/snap, 2-title, 3-snap, 4-box, 5-cart, 6-label, 7-cart top, 8-video, 9-manual

mame_mess = True
# fonts for interface
chat_font = "Verdana"
chat_font_size = 8
chat_font_color = "(0,0,0)"
user_list_font = "Verdana"
user_list_font_size = 10
user_list_font_color = "(0,0,0)"
gamelist_font = "Verdana"
gamelist_font_size = 8
gamelist_font_color = "(0,0,0)"
gameinfo_font = "Verdana"
gameinfo_font_size = 8
gameinfo_font_color = "(0,0,0)"

# image settings
autodown_image = True
file_save_method = False
# mame image settings
mame_info_display_tab = True
mame_title_snap_display_tab = True
mame_title_display_tab = False
mame_snap_display_tab = False
mame_cabinet_display_tab = False
mame_control_panel_display_tab = False
mame_marque_display_tab = False
mame_pcb_display_tab = False
mame_video_playback_display_tab = False
mame_manual_display_tab = False

#mess image settings
mess_info_display_tab = True
mess_title_snap_display_tab = True
mess_title_display_tab = False
mess_snap_display_tab = False
mess_box_display_tab = False
mess_cart_display_tab = False
mess_label_display_tab = False
mess_cart_top_display_tab = False
mess_video_playback_display_tab = False
mess_manual_display_tab = False

# theme/app settings
start_screen_option = 0   # 0 - max, 1 - minimized, 2 - last position
mainframe_position_x = 0
mainframe_position_y = 0
mainframe_width = 1024
mainframe_height = 768
html_chat_window_lines = 0
user_list_sort = 1
theme = 0
hubcad_layout = None
left_splitter_location = 250
right_splitter_location = 250
center_splitter_location = 250

# video playback option
video_download = False
video_mute = False
video_volume = 1
video_repeat = True

# misc settings
chat_save_to_db = False
chat_export_on_disco = False
display_emote_in_chat = True
allow_client_downloads = True
mute_chat_sounds = False
chime_on_chat_name = False
use_miniupnpc = True
chime_on_friend = False
display_clock_24 = True
record_inp_on_mame = False
ping_timeframe = 0

# audit settings
skip_mechanical = True
skip_adult = False
scan_choice = 0
skip_clones = False
skip_gambling = True
skip_mahjong = False
rename_files = False