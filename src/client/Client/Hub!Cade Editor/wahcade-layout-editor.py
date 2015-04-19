#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
###
# Application: wah!cade
# File:        wahcade-layout-editor
# Description: starts the wah!cade layout editor
# Copyright (c) 2005-2010   Andy Balcombe <http://www.anti-particle.com>
###
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
import os,sys
assert(sys.version_info) >= (2, 4, 0), 'python >= 2.4 required'
from optparse import OptionParser
from layout_editor import WinLayout, gtk
import wc_constants
import exception
import locale
import gettext
_ = gettext.gettext

if __name__ == "__main__":
    #set to unicode encoding
    try:
        sys.setappdefaultencoding('utf-8')
    except AttributeError:
        pass
    #define options
    usage = "usage: %prog [options] [wahcade_layout_file] [cpviewer_layout_file]"
    parser = OptionParser(usage=usage, version='%s %s "%s"' % ("%prog", sys.version, sys.version_info))
    parser.add_option("-u", "--use-app-config",
                        action="store_true",
                        dest="use_app_config",
                        default=False,
                        help=("Use application config location (i.e. wahcade/config instead of the default ~/.wahcade)"))
    parser.add_option("-d", "--debug",
                        action="store_true",
                        dest="debug",
                        default=False,
                        help=("Set debug mode (disables psyco)"))
    #get options & arguments
    options, args = parser.parse_args()
##    # build the constants (pyinstaller issues so moved to here)
##    APP_PATH = os.path.abspath(os.getcwd())
##    hub_constants.layout_glade_file = os.path.join(APP_PATH, 'glade', 'layout_editor.glade')
##    hub_constants.setup_glade_file = os.path.join(APP_PATH, 'glade', 'wahcade_setup.glade')
##    LOCALE_DIR = os.path.join(APP_PATH, 'locale')
##    if os.path.exists(os.path.join(APP_PATH,'portable.mode')):
##        CONFIG_DIR = os.path.expanduser(os.path.join(APP_PATH,'.wahcade'))
##    else:
##        CONFIG_DIR = os.path.expanduser('~/.wahcade')
##    #locale stuff
##    try:
##        locale.setlocale(locale.LC_ALL, '')
##        gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
##        gettext.bind_textdomain_codeset(APP_NAME, 'UTF-8')
##        gettext.textdomain(APP_NAME)
##    #except locale.Error:
##    except:
##        print 'Warning: Unsupported locale: Defaulting to English'
    #debug mode set?
    if not options.debug:
        #import psyco if available
        try:
            import psyco
            psyco.full()
        except ImportError:
            pass
        #set exception handler to gtk2 handler
        #sys.excepthook = exception._info    # removed atm to help debug my app
    #instantiate main GUI window class
    app = WinLayout(wc_constants.LAYOUT_GLADE_FILE, 'winMain', options, args)
    #and... go...
    gtk.main()
