# encoding: UTF-8
#
# Copyright 2012-2013 Alejandro Autalán
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# For further info, check  http://pygubu.web.here
from __future__ import unicode_literals
import platform
import logging

try:
    import tkinter as tk
except:
    import Tkinter as tk

from pygubu.builder import builderobject

logger = logging.getLogger(__name__)

# translator marker
def _(x):
    return x

TK_BITMAPS = (
    'error', 'gray75', 'gray50', 'gray25', 'gray12',
    'hourglass', 'info', 'questhead', 'question', 'warning',
    )

TK_BITMAPS_MAC = (
    'document', 'stationery', 'edition', 'application', 'accessory',
    'forder', 'pfolder', 'trash', 'floppy', 'ramdisk', 'cdrom',
    'preferences', 'querydoc', 'stop', 'note', 'caution'
    )

TK_CURSORS = (
    'arrow', 'based_arrow_down', 'based_arrow_up', 'boat',
    'bogosity', 'bottom_left_corner', 'bottom_right_corner',
    'bottom_side', 'bottom_tee', 'box_spiral', 'center_ptr',
    'circle', 'clock', 'coffee_mug', 'cross', 'cross_reverse',
    'crosshair', 'diamond_cross', 'dot', 'dotbox', 'double_arrow',
    'draft_large', 'draft_small', 'draped_box', 'exchange', 'fleur',
    'gobbler', 'gumby', 'hand1', 'hand2', 'heart', 'icon',
    'iron_cross', 'left_ptr', 'left_side', 'left_tee', 'leftbutton',
    'll_angle', 'lr_angle', 'man', 'middlebutton', 'mouse', 'none',
    'pencil', 'pirate', 'plus', 'question_arrow', 'right_ptr',
    'right_side', 'right_tee', 'rightbutton', 'rtl_logo',
    'sailboat', 'sb_down_arrow', 'sb_h_double_arrow',
    'sb_left_arrow', 'sb_right_arrow', 'sb_up_arrow',
    'sb_v_double_arrow', 'shuttle', 'sizing', 'spider', 'spraycan',
    'star', 'target', 'tcross', 'top_left_arrow', 'top_left_corner',
    'top_right_corner', 'top_side', 'top_tee', 'trek', 'ul_angle',
    'umbrella', 'ur_angle', 'watch', 'xterm', 'X_cursor')

TK_CURSORS_WINDOWS = (
    'no', 'starting', 'size', 'size_ne_sw'
    'size_ns', 'size_nw_se', 'size_we','uparrow', 'wait'
    )

TK_CURSORS_MAC = (
    'copyarrow', 'aliasarrow', 'contextualmenuarrow', 'text',
    'cross-hair', 'closedhand', 'openhand', 'pointinghand',
    'resizeleft', 'resizeright', 'resizeleftright', 'resizeup',
    'resizedown', 'resizeupdown', 'notallowed', 'poof',
    'countinguphand', 'countingdownhand', 'countingupanddownhand', 'spinning'
    )

if platform.system() == 'Darwin':
    TK_BITMAPS = TK_BITMAPS + TK_BITMAPS_MAC
    TK_CURSORS = TK_CURSORS + TK_CURSORS_MAC
elif platform.system() == 'Windows':
    TK_CURSORS = TK_CURSORS + TK_CURSORS_WINDOWS

TK_RELIEFS = (tk.FLAT, tk.RAISED, tk.SUNKEN, tk.GROOVE, tk.RIDGE)

TK_WIDGET_OPTIONS = {
    'accelerator': {
        'editor': 'entry'},
    'activerelief': {
        'editor': 'choice',
        'params': {
            'values': ('', tk.FLAT, tk.RAISED, tk.SUNKEN,
                       tk.GROOVE, tk.RIDGE),
            'state': 'readonly'}},
    'activestyle': {
        'editor': 'choice',
        'params': {
            'values': ('', 'underline', 'dotbox', 'none'),
            'state': 'readonly'}},
    'activebackground': {
        'editor': 'colorentry'},
    'activeborderwidth': {
        'editor': 'dimensionentry'},
    'activeforeground': {
        'editor': 'colorentry'},
    'after': {
        'editor': 'entry'},
    # ttk.Label
    'anchor': {
        'editor': 'choice',
        'params': {'values': ('', tk.W, tk.CENTER, tk.E),
                   'state': 'readonly'},
        'tk.Button': {
            'params': {
                'values': (
                    '', 'n', 'ne', 'nw', 'e', 'w', 's', 'se', 'sw', 'center'),
                'state': 'readonly'}},
        },
    'aspect': {
        'editor': 'naturalnumber'},
    'autoseparators': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    # ttk.Label
    'background': {
        'editor': 'colorentry'},
    # ttk.Frame, ttk.Label
    'borderwidth': {
        'editor': 'dimensionentry'},
    'bigincrement': {
        'editor': 'naturalnumber'},
    'bitmap': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_BITMAPS, 'state': 'readonly'}},
    'blockcursor': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'buttonbackground': {
        'editor': 'colorentry'},
    'buttoncursor': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_CURSORS, 'state': 'readonly'}},
    'buttondownrelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    'buttonuprelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    'class_': {
        'editor': 'alphanumentry',
        },
    'closeenough': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999},
        },
    'column_anchor': { # ttk.Treeview.Column
        'editor': 'choice',
        'params': {'values': ('', tk.W, tk.CENTER, tk.E), 'state': 'readonly'},
        'default': tk.W},
    'command': {
        'editor': 'dynamic',
        'params': {'mode': 'commandentry'},
        'ttk.Scrollbar': {
             'params': {'mode': 'scrollcommandentry'}
             },
        'ttk.Scale': {
             'params': {'mode': 'scalecommandentry'}
             },
        'tk.Scale': {
             'params': {'mode': 'scalecommandentry'}
             },
        'tk.OptionMenu': {
             'params': {'mode': 'simplecommandentry'}
             },
        },
    # ttk.Label
    'compound': {
        'editor': 'choice',
        'params': {
            'values': ('', tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT),
            'state': 'readonly'}},
    # ttk.Button
    'confine': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'container': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'cursor': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_CURSORS, 'state': 'readonly'}},
    # ttk.Button
    'default': {
        'editor': 'choice',
        'params': {'values': ('', 'normal', 'active', 'disabled')}},
    'digits': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}},
    'direction': {
        'editor': 'choice',
        'tk.Menubutton': {
            'params': {'values': ('', tk.LEFT, tk.RIGHT, 'above'),
                       'state': 'readonly'}},
        'ttk.Menubutton': {
            'params': {
                'values': ('', 'above', 'below', 'flush',
                           tk.LEFT, tk.RIGHT),
                'state': 'readonly'}},
        },
    'disabledbackground': {
        'editor': 'colorentry'},
    'disabledforeground': {
        'editor': 'colorentry'},
    'elementborderwidth': {
        'editor': 'entry'},
    'endline': {
        'editor': 'entry'},
    # ttk.Checkbutton, ttk.Entry
    'exportselection': {
        'editor': 'choice',
        'params': {'values': ('', 'true', 'false'), 'state': 'readonly'}},
    # ttk.Label
    'font': { 'editor': 'fontentry'},
    # ttk.Label
    'foreground': {
        'editor': 'colorentry'},
    # ttk.Spinbox
    'format': {
        'editor': 'entry'},
    # ttk.Scale, ttk.Spinbox
    'from_': {
        'editor': 'realnumber',
        },
    'handlepad': {
        'editor': 'entry'},
    'handlesize': {
        'editor': 'entry'},
    # ttk.Treeview.Column
    'heading_anchor': {
        'editor': 'choice',
        'params': {
            'values': ('', tk.W, tk.CENTER, tk.E), 'state': 'readonly'},
        'default': tk.W},
    # ttk.Frame,
    'height': {
        'editor': 'dynamic',
        'params': {'mode': 'dimensionentry'},
        'ttk.Combobox': {
            'params': {'mode': 'naturalnumber'},
            },        
        'tk.Toplevel': {'default': 200},
        'tk.Frame': {'default': 200},
        'ttk.Frame': {'default': 200},
        'tk.LabelFrame': {'default': 200},
        'ttk.Labelframe': {'default': 200},
        'tk.Listbox': {
            'params': {'mode': 'naturalnumber'},
            },
        'tk.Menubutton': {
            'params': {'mode': 'naturalnumber'},
            },        
        'tk.PanedWindow': {'default': 200},
        'ttk.Panedwindow': {'default': 200},
        'ttk.Notebook': {'default': 200},
        'tk.Text': {
            'params': {'mode': 'naturalnumber'},
            'default': 10
            },
        'tk.Radiobutton':{
            'params': {'mode': 'naturalnumber'},
        },
        'pygubu.builder.widgets.dialog': {'default': 100}
        },
    'highlightbackground': {
        'editor': 'colorentry'},
    'highlightcolor': {
        'editor': 'colorentry'},
    'highlightthickness': {
        'editor': 'dimensionentry'},
    # ttk.Label
    'image': {
        'editor': 'imageentry'},
    'inactiveselectbackground': {
        'editor': 'colorentry'},
    # ttk.Spinbox
    'increment': {
        'editor': 'spinbox',
        'params': {'from_': -999, 'to': 999}
        },
    'indicatoron': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'insertbackground': {
        'editor': 'colorentry'},
    'insertborderwidth': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999},
        },
    'insertofftime': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 9999, 'increment': 100},
        },
    'insertontime': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 9999, 'increment': 100},
        },
    'insertunfocussed': {
        'editor': 'choice',
        'params': {
            'values': ('', 'none', 'hollow', 'solid'),
            'state': 'readonly'}},
    'insertwidth': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}},
    # ttk.Entry
    'invalidcommand': {
        'editor': 'entryvalidatecommandentry'},
    'jump': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    # ttk.Label
    'justify': {
        'editor': 'choice',
        'params': {'values': ('', 'left', 'center', 'right'),
                   'state': 'readonly'}},
    'label': {
        'editor': 'entry'},
    # ttk.Labelframe
    'labelanchor': {
        'editor': 'choice',
        'params': {
            'values': ('', 'nw', 'n', 'ne', 'en', 'e', 'es',
                       'se', 's', 'sw', 'ws', 'w'),
            'state': 'readonly'}},
    # ttk.Progressbar
    'length': {
        'editor': 'dimensionentry'},
    'listvariable': {
        'editor': 'tkvarentry'},
    # ttk.Progressbar
    'maximum': {
        'editor': 'realnumber'},
    'maxundo': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}},
    'minsize': {
        'editor': 'entry'},
    # ttk.Treeview.Column
    'minwidth': {
        'editor': 'naturalnumber',
        'default': '20'},
    # ttk.Progressbar
    'mode': {
        'editor': 'choice',
        'params': {
            'values': ('', 'determinate', 'indeterminate'),
            'state': 'readonly'}},
    'offrelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    # ttk.Checkbutton
    'offvalue': {
        'editor': 'entry',
        'help': _('offvalue_help')},
    # ttk.Checkbutton
    'onvalue': {
        'editor': 'entry'},
    'opaqueresize': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    # ttk.Panedwindow
    'orient': {
        'editor': 'choice',
        'params': {'values': (tk.VERTICAL, tk.HORIZONTAL),
                   'state': 'readonly'},
        'default': tk.HORIZONTAL
        },
    'overrelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}
        },
    # ttk.Frame, ttk.Label
    'padding': {
        'editor': 'fourdimensionentry'},
    'padx': {
        'editor': 'dimensionentry',
        },
    'pady': {
        'editor': 'dimensionentry',
        },
    # ttk.Checkbutton
    'postcommand': {
        'editor': 'simplecommandentry'},
    'readonlybackground': {
        'editor': 'colorentry'},
    # ttk.Frame,
    'relief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    'repeatdelay': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 9999, 'increment': 100},
        },
    'repeatinterval': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 9999, 'increment': 100}},
    'resolution': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999, 'increment': 0.5},
        },
    'sliderlength': {
        'editor': 'dimensionentry'},
    'sliderrelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    'sashcursor': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_CURSORS, 'state': 'readonly'}},
    'sashpad': {
        'editor': 'entry'},
    'sashrelief': {
        'editor': 'choice',
        'params': {'values': ('',) + TK_RELIEFS, 'state': 'readonly'}},
    'sashwidth': {
        'editor': 'entry'},
    'selectbackground': {
        'editor': 'colorentry'},
    'selectborderwidth': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}},
    'selectforeground': {
        'editor': 'colorentry'},
    'scrollregion': {
        'editor': 'entry'},
    'selectcolor': {
        'editor': 'colorentry'},
    'selectimage': {
        'editor': 'imageentry'},
    # ttk.Treeview
    'selectmode': {
        'editor': 'choice',
        'params': {
            'values': ('', tk.BROWSE, tk.SINGLE, tk.MULTIPLE, tk.EXTENDED),
            'state': 'readonly'},
        'ttk.Treeview': {
            'params': {
                'values': (tk.EXTENDED, tk.BROWSE, tk.NONE),
                'state': 'readonly'},
            'default': tk.EXTENDED}
        },
    'setgrid': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    # ttk.Entry
    'show': {
        'editor': 'choice',
        'tk.Entry': {
            'params': {'values': ('', '•'), 'state': 'normal'},
            },
        'ttk.Entry': {
            'params': {'values': ('', '•'), 'state': 'normal'},
            },
        'ttk.Treeview': {
            'params': {
                'values': ('', 'tree', 'headings'), 'state': 'readonly'}
            },
        'pygubu.builder.widgets.editabletreeview': {
            'params': {
                'values': ('', 'tree', 'headings'), 'state': 'readonly'}
            },
        },
    'showhandle': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'showvalue': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'spacing1': {
        'editor': 'entry'},
    'spacing2': {
        'editor': 'entry'},
    'spacing3': {
        'editor': 'entry'},
    'startline': {
        'editor': 'entry'},
    'state': {
        'editor': 'choice',
        'params': {'values': ('', tk.NORMAL, tk.DISABLED),
                   'state': 'readonly'},
        'tk.Button': {
            'params': {
                'values': ('', tk.NORMAL, tk.ACTIVE, tk.DISABLED),
                'state': 'readonly'}},
        'tk.Entry': {
            'params': {
                'values': ('', tk.NORMAL, tk.DISABLED, 'readonly'),
                'state': 'readonly'}},
        'tk.Combobox': {
            'params': {
                'values': ('', 'readonly'), 'state': 'readonly'}},
        'ttk.Entry': {
            'params': {
                'values': ('', tk.NORMAL, tk.DISABLED, 'readonly'),
                'state': 'readonly'}},
        'ttk.Combobox': {
            'params': {
                'values': ('', 'normal', 'readonly', 'disabled'),
                'state': 'readonly'}},
        'ttk.Button': {
            'params': {
                'values': ('', 'normal', 'disabled'),
                'state': 'readonly'}},
        'ttk.Notebook.Tab': {
            'params': {
                'values': ('', 'normal', 'disabled', 'hidden'),
                'state': 'readonly'
                }},
        'tk.Spinbox': {
            'params': {
                'values': ('', tk.NORMAL, tk.DISABLED, 'readonly'),
                'state': 'readonly'
                }},
    },
    # ttk.Notebook.Tab
    'sticky': {
        'editor': 'stickyentry',
        'params': {}},
    # ttk.Treeview.Column
    'stretch': {
        'editor': 'choice',
        'ttk.Treeview.Column': {
            'params': {'values': ('true', 'false'), 'state': 'readonly'},
            'default': 'true'},
        'tk.PanedWindow.Pane': {
            'params': {
                'values': ('', 'always', 'first', 'last', 'middle', 'never'),
                'state': 'readonly'}}},
    'style': {
        'editor': 'ttkstylechoice',
        'ttk.Button': {
            'params': {'values': ('', 'Toolbutton')}
            }
        },
    'tabs': {
        'editor': 'entry'},  # FIXME see tk.Text tab property
    'tabstyle': {
        'editor': 'choice',
        'params': {
            'values': ('', 'tabular', 'wordprocessor'),
            'state': 'readonly'}},
    'takefocus': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'tearoff': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'tearoffcommand': {
        'editor': 'simplecommandentry' },
    # ttk.Label
    'text': {
        'editor': 'text'},
    # ttk.Label
    'textvariable': {
        'editor': 'tkvarentry'},
    'tickinterval': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999, 'increment': 0.5},
        },
    # ttk.Scale, ttk.Spinbox
    'to': {
        'editor': 'realnumber',
        },
    'tristateimage': {
        'editor': 'imageentry'},
    'tristatevalue': {
        'editor': 'entry'},
    'troughcolor': {
        'editor': 'colorentry'},
    # ttk.Label
    'underline': {
        'editor': 'naturalnumber'},
    'undo': {
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}},
    'value': {
        'editor': 'dynamic',
        'params': {'mode': 'entry'},
        'ttk.Progressbar':{
            'params':{'mode':'realnumber'}
            },
        'ttk.Scale':{
            'params':{'mode':'realnumber'}
            },        
        },
    # ttk.Checkbutton
    'values': {
        'editor': 'entry'},
    'validate': {
        'editor': 'choice',
        'params': {
            'values': ('', 'none', 'focus', 'focusin',
                       'focusout', 'key', 'all'),
            'state': 'readonly'}},
    'validatecommand': {
        'editor': 'entryvalidatecommandentry'},
    # ttk.Checkbutton
    'variable': {
        'editor': 'tkvarentry'},
    # ttk.Panedwindow.Pane
    'weight': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999},
        'default': '1',
        },
    # ttk.Frame, ttk.Label
    'width': {
        'editor': 'dynamic',
        'params': {'mode': 'dimensionentry'},
        'tk.Button': {},
        'ttk.Button': {},
        'tk.Canvas': {
            'params': {'mode': 'entry'}
            },
        'ttk.Checkbutton': {
            'params': {'mode': 'integernumber'},
            },        
        'tk.Entry': {
            'params': {'mode': 'naturalnumber'},
            },
        'ttk.Entry': {
            'params': {'mode': 'naturalnumber'},
            },
        'tk.Menubutton': {
            'params': {'mode': 'naturalnumber'},
            },
        'ttk.Label': {
            'params': {'mode': 'integernumber'},
            },        
        'tk.Listbox': {
            'params': {'mode': 'naturalnumber'},
            },
        'tk.Frame': {
            'default': 200},
        'ttk.Frame': {
            'default': 200},
        'tk.LabelFrame': {
            'default': 200},
        'ttk.Labelframe': {
            'default': 200},
        'tk.PanedWindow': {
            'default': 200},
        'ttk.Panedwindow': {
            'default': 200},
        'ttk.Notebook': {
            'default': 200},
        'tk.Radiobutton':{
            'params': {'mode': 'naturalnumber'},
            },
        'ttk.Radiobutton':{
            'params': {'mode': 'integernumber'},
            },        
        'tk.Text': {
            'params': {'mode': 'naturalnumber'},
            'default': 50},
        'tk.Toplevel': {
            'default': 200},        
        'ttk.Treeview.Column': {
            'params': {'mode': 'naturalnumber'},
            'default': 200},
        'pygubu.builder.widgets.dialog': {
            'default': 200}},
    # ttk.Spinbox
    'wrap': {
        'editor': 'choice',
        'params': {
            'values': ('', 'false', 'true'),
            'state': 'readonly'},
        'tk.Text': {
            'params': {
                'values': ('', tk.CHAR, tk.WORD, tk.NONE),
                'state': 'readonly'}}
        },
    # ttk.Label
    'wraplength': {
        'editor': 'dimensionentry'},
    # ttk.Entry
    'xscrollcommand': {
        'editor': 'scrollsetcommandentry'},
    'xscrollincrement': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}
        },
    # ttk.Treeview
    'yscrollcommand': {
        'editor': 'scrollsetcommandentry'},
    'yscrollincrement': {
        'editor': 'spinbox',
        'params': {'from_': 0, 'to': 999}
        },
    }

REQUIRED_OPTIONS = {
    'class': {
        'editor': 'entry',
        'params': {'state': 'readonly'}},
    'id': {
        'editor': 'identifierentry'},
    }

CUSTOM_OPTIONS = {
    'geometry': {
        'editor': 'dynamic',
        'params': {
            'mode': 'geometryentry',
            'values': ('', '320x200', '320x240', '352x288', '384x288',
                       '480x320', '640x480', '768x576', '800x480', '800x600',
                       '854x480', '1024x576', '1024x600', '1024x768',
                       '1152x768', '1152x864', '1280x720', '1280x768',
                       '1280x800', '1280x854', '1280x960', '1280x1024',
                       '1366x768', '1400x1050', '1440x1080', '1440x900',
                       '1440x960', '1440x1080', '1600x900', '1600x1050',
                       '1600x1200', '1920x1080', '2048x1080'),
            },
        },
    'iconbitmap': {
        'editor': 'imageentry' },
    'iconphoto': {
        'editor': 'imageentry' },
    'maxsize': {
        'editor': 'whentry'},
    'minsize': {
        'editor': 'whentry'},
    'overrideredirect': {
        'editor': 'choice',
        'params': {'values': ('', 'True', 'False'), 'state': 'readonly'}},
    'resizable': {
        'editor': 'choice',
        'params': {
            'values': ('', 'both', 'horizontally', 'vertically', 'none'),
            'state': 'readonly'}},
    'scrolltype': {
        'editor': 'choice',
        'params': {
            'values': ('both', 'vertical', 'horizontal'),
            'state': 'readonly'},
        'default': 'both'},
    'text': {
        'editor': 'text'},
    'title': {
        'editor': 'entry'},
    'tree_column': {
        'editor': 'choice',
        'params': {'values': ('true', 'false'), 'state': 'readonly'},
        'default': 'false'},
    'usemousewheel': {
        'editor': 'choice',
        'params': {
            'values': ('true', 'false'),
            'state': 'readonly'},
        'default': 'false'},
    'visible': {
        'editor': 'choice',
        'params': {'values': ('true', 'false'), 'state': 'readonly'},
        'default': 'true'},
    'specialmenu': {
        'editor': 'choice',
        'params': {'values': ('apple', 'help', 'window', 'system'), 'state': 'readonly'}
        },
    }

WIDGET_REQUIRED_OPTIONS = ('class', 'id')
WIDGET_STANDARD_OPTIONS = (
    'activerelief', 'activestyle', 'activebackground',
    'activeborderwidth', 'activeforeground', 'after',
    'anchor', 'background', 'bitmap', 'borderwidth',
    'class_', 'compound', 'cursor', 'disabledforeground',
    'exportselection',
    'font', 'foreground', 'jump', 'highlightbackground',
    'highlightcolor', 'highlightthickness', 'image',
    'indicatoron', 'insertbackground',
    'insertborderwidth', 'insertofftime', 'insertontime', 'insertwidth',
    'justify', 'orient', 'padx', 'pady', 'relief',
    'repeatdelay', 'repeatinterval', 'selectbackground', 'selectborderwidth',
    'selectforeground', 'setgrid', 'state', 'style', 'takefocus', 'text',
    'textvariable', 'troughcolor', 'underline', 'width', 'wraplength',
    'xscrollcommand', 'yscrollcommand')

WIDGET_SPECIFIC_OPTIONS = (
    'accelerator', 'activestyle', 'activerelief', 'anchor', 'aspect',
    'autoseparators', 'background', 'bigincrement',
    'blockcursor', 'borderwidth', 'buttonbackground', 'buttoncursor',
    'buttondownrelief', 'buttonuprelief',
    'class_', 'column_anchor', 'command', 'compound', 'container',
    'closeenough', 'confine', 'default', 'digits', 'direction',
    'disabledbackground', 'disabledforeground', 'elementborderwidth',
    'endline', 'exportselection', 'font',
    'foreground', 'format', 'from_', 'to',
    'inactiveselectbackground', 'increment', 'insertunfocussed',
    'invalidcommand', 'justify', 'handlepad', 'handlesize',
    'heading_anchor', 'height', 'image', 'indicatoron',
    'label', 'labelanchor', 'listvariable', 'length',
    'maximum', 'maxundo',
    'minsize', 'minwidth', 'mode', 'offrelief', 'offvalue',
    'onvalue', 'opaqueresize', 'orient', 'overrelief',
    'padding', 'padx', 'pady',
    'postcommand', 'readonlybackground', 'relief', 'resolution',
    'scrollregion', 'sashcursor', 'sashpad', 'sashrelief', 'sashwidth',
    'selectcolor', 'selectimage', 'selectmode', 'show',
    'showhandle', 'showvalue', 'sliderlength', 'sliderrelief',
    'spacing1', 'spacing2', 'spacing3', 'startline',
    'state', 'sticky', 'stretch', 'tabs', 'tabstyle',
    'text', 'textvariable', 'tickinterval', 'tristateimage',
    'tristatevalue', 'underline', 'validate', 'undo', 'validatecommand',
    'value', 'values', 'variable', 'weight', 'width', 'wrap',
    'wraplength', 'xscrollincrement', 'yscrollincrement',
    'tearoff', 'tearoffcommand'
    )

WIDGET_CUSTOM_OPTIONS = [
    'tree_column', 'visible', 'scrolltype', 'text', 'title',
    'geometry', 'overrideredirect', 'resizable', 'minsize',
    'maxsize', 'usemousewheel', 'iconbitmap', 'iconphoto',
    'specialmenu', 
    ]

WIDGET_PROPERTIES = wp = dict(TK_WIDGET_OPTIONS)
wp.update(REQUIRED_OPTIONS)
wp.update(CUSTOM_OPTIONS)

LAYOUT_OPTIONS = {
    # pack/grid/place common properties
    'padx': {'editor': 'twodimensionentry'},
    'pady': {'editor': 'twodimensionentry'},
    'ipadx': {'editor': 'twodimensionentry'},
    'ipady': {'editor': 'twodimensionentry'},
    'propagate': {
        'editor': 'choice',
        'params': {'values': ('True', 'False'), 'state': 'readonly'},
        'default': 'True'},
    'anchor': {
        'editor': 'choice',
        'params': {
          'values': ('', 'n', 'ne', 'nw', 'e', 'w', 's', 'se', 'sw', 'center'),
          'state': 'readonly'},
        'place': {'default': 'nw'}
        },
    
    # pack properties
    'expand':{
        'editor': 'choice',
        'params': {'values': ('', 'false', 'true'), 'state': 'readonly'}
        },
    'fill':{
        'editor': 'choice',
        'params': {'values': ('', 'x', 'y', 'both'), 'state': 'readonly'}
        },
    'side':{
        'editor': 'choice',
        'params': {
            'values': ('top', 'bottom', 'left', 'right'),
            'state': 'readonly'
            },
        'default': 'top',
        },
    
    # Pack properties
    'bordermode':{
        'editor': 'choice',
        'params':{
            'values': ('', 'inside', 'outside', 'ignore'),
            'state': 'readonly'}        
        },
    'height':{
        'editor': 'pixelcoordinateentry',
        },
    'relheight':{
        'editor': 'relativeentry',
        },
    'relwidth':{
        'editor': 'relativeentry',
        },
    'relx':{
        'editor': 'relativeentry',
        },
    'rely':{
        'editor': 'relativeentry',
        },
    'width':{
        'editor': 'pixelcoordinateentry',
        },
    'x':{
        'editor': 'pixelcoordinateentry',
        'default': '0'
        },
    'y':{
        'editor': 'pixelcoordinateentry',
        'default': '0'
        },
    
    # grid packing properties
    'row': {
        'editor': 'naturalnumber',
        'default': '0'
        },
    'column': {
        'editor': 'naturalnumber',
        'default': '0'
        },
    'sticky': {
        'editor': 'stickyentry',
        'params': {}},
    'rowspan': {
        'editor': 'naturalnumber',
        },
    'columnspan': {
        'editor': 'naturalnumber',
        },
    
    #
    # grid row and column properties (can be applied to each row or column)
    #
    'minsize': {
        'editor': 'dimensionentry',
        'params': {'width': 4, 'empty_data': 0}},
    'pad': {
        'editor': 'dimensionentry',
        'params': {'width': 4, 'empty_data': 0}},
    'weight': {
        'editor': 'naturalnumber'
    },
    'uniform': {
        'editor': 'alphanumentry',
    }
}

# List properties in display order
MANAGER_PROPERTIES = (
    'anchor', 
    'relx', 'rely', 'relwidth', 'relheight',
    'x', 'y', 'width', 'height', 'bordermode',
    'side', 'expand', 'fill',
    'row', 'column', 'sticky', 'rowspan', 'columnspan', 'padx', 'pady',
    'ipadx', 'ipady', 'propagate'
)

GRID_PROPERTIES = (
    'row', 'column', 'sticky', 'rowspan', 'columnspan', 'padx', 'pady',
    'ipadx', 'ipady', 'propagate')

PACK_PROPERTIES = (
    'anchor', 'side', 'expand', 'fill', 'padx', 'pady',
    'ipadx', 'ipady', 'propagate')

PLACE_PROPERTIES = (
    'anchor', 'relx', 'rely', 'relwidth', 'relheight',
    'x', 'y', 'width', 'height', 'bordermode', 
)

GRID_RC_PROPERTIES = ('minsize', 'pad', 'weight', 'uniform')

TRANSLATABLE_PROPERTIES = (
    'label', 'text', 'title',
)


def _register_custom(name, descr):
    if name not in CUSTOM_OPTIONS:
        CUSTOM_OPTIONS[name] = descr
        WIDGET_PROPERTIES.update(CUSTOM_OPTIONS)
        WIDGET_CUSTOM_OPTIONS.append(name)
        WIDGET_CUSTOM_OPTIONS.sort()
        logger.debug('Registered property: %s', name)

def register_property(name, descr):
    _register_custom(name, descr)
    builderobject._old_register_property(name, descr)

if not hasattr(builderobject, '_register_fixed_'):
    for name, descr in builderobject.CUSTOM_PROPERTIES.items():
        _register_custom(name, descr)
    builderobject._register_fixed_ = True
    builderobject._old_register_property = builderobject.register_property
    builderobject.register_property = register_property
    logger.debug('Installed custom register_property function')
