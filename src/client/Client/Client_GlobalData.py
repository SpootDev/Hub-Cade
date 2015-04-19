# software revision to post within the app
software_rev = '0.1'
software_rom_rev = '0.144'

# app info
application_launch_directory = ""

# sqlite3 fields
conn_player = None
curs_player = None
conn_chat = None
curs_chat = None
##conn_mess = None
##curs_mess = None
conn_game = None
curs_game = None

# can OS playback the video
os_video_playback = True

# upnpc
u = None

# global app self
app = None

# hold the pid for launched emu
mamePopen = None

# audit gloals
skipped_files = []

# motd text
motd_value = ""

# misc
generic_string = ""

# weither connected to central server or not
Connected_Status = False

# port is forwarded or not so can host or be 3rd+ player
hasPortForwarded = True

# debug the application
DEBUG_APP = False

# hosted game info
host_game_max_players = 4
host_game_max_observers = 4
game_start_time = None
game_id = None
game_tree_id = {}

# files transfer threads
fileReceiverThread = None
fileReceiverProgressDialog = None
fileSenderThreads = []

# fields to determine/deal with auditing
needAudit=False

# newer webkit html2 enabled
webkit_enabled = True

# audit data
audit_files_to_audit = 0
audit_on_file = 0
matching_files_to_audit = 0
matching_on_file = 0
found_rom_ids = []
found_rom_paths = []

# audit info
audited_games = 0
auditData = None
audit_gameList = {}
audit_gameList_filtered = {}

# favorite game data
favorite_game_id = []

# category id data
#category_id = []

# master server info
serverName = None
selfPort = None

# emulator to run
messName = None
mameName = None

# editor to run
editorName = None

# hold media types for application
systemMediaTypes = {}

# seleced grid number for context menu
grid_cell_row = 0

# os of running client
computer_os = None

# gui update so don't have to do the dirty checks
gui_update_user_grid = False
gui_update_game_tree = False
gui_update_hosted_game_grid = False
gui_update_favorite = True

# who knows
playerID = 0
playerName= ""
database = None
messageBoxQueue = []
player = None
networkProtocol = None

# chat html data
chatHTML = ""
privHTML = ""
adminHTML  = ""
