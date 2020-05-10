# -*- coding: utf-8 -*-

""" LabView RSRC file format part definitions.

    Parts are placed on Front Panel and Block Diagram.
"""

# Copyright (C) 2019 Mefistotelis <mefistotelis@gmail.com>
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


import enum

class PARTID(enum.IntEnum):
    """ Part identifiers
    """
    NO_PARTID	= 0
    COSMETIC	= 1
    INCREMENT	= 2
    DECREMENT	= 3
    LARGE_INCREMENT	= 4
    LARGE_DECREMENT	= 5
    PIXEL_INCREMENT	= 6
    PIXEL_DECREMENT	= 7
    HOUSING	= 8
    FRAME	= 9
    NUMERIC_TEXT	= 10
    TEXT	= 11
    RING_TEXT	= 12
    SCROLLBAR	= 13
    RING_PICTURE	= 14
    RADIX	= 15
    NAME_LABEL	= 16
    SCALE	= 17
    X_SCALE	= 18
    Y_SCALE	= 19
    OUT_OF_RANGE_BOX	= 20
    BOOLEAN_BUTTON	= 21
    BOOLEAN_TEXT	= 22
    SLIDER_NEEDL_THUMB	= 23
    SET_TO_DEFAULT	= 24
    DECORATION	= 25
    LIST_AREA	= 26
    SCALE_MARKER	= 27
    CONTENT_AREA	= 28
    DDO_FRAME	= 29
    INDEX_FRAME	= 30
    FILL	= 31
    GRAPH_LEGEND	= 32
    GRAPH_PALETTE	= 33
    X_FIT_BUTTON	= 34
    Y_FIT_BUTTON	= 35
    X_FIT_LOCK_BUTTON	= 36
    Y_FIT_LOCK_BUTTON	= 37
    X_SCROLLBAR	= 38
    Y_SCROLLBAR	= 39
    SCALE_TICK	= 40
    COLOR_AREA	= 41
    PALETTE_BACKGROUND	= 42
    CONTRL_INDCTR_SYM	= 43
    EXTRA_FRAME_PART	= 44
    SCALE_MIN_TICK	= 45
    PIX_MAP_PALETTE	= 46
    SELECT_BUTTON	= 47
    TEXT_BUTTON	= 48
    ERASE_BUTTON	= 49
    PEN_BUTTON	= 50
    SUCKER_BUTTON	= 51
    BUCKET_BUTTON	= 52
    LINE_BUTTON	= 53
    RECTANGLE_BUTTON	= 54
    FILLED_RECT_BUTTON	= 55
    OVAL_BUTTON	= 56
    FILLED_OVAL_BUTTON	= 57
    PATTERN	= 58
    FOREGROUND_COLOR	= 59
    BACKGROUND_COLOR	= 60
    PIX_MAP_PAL_EXTRA	= 61
    ZOOM_BAR	= 62
    BOOLEAN_TRUE_LABEL	= 63
    BOOLEAN_FALSE_LABEL	= 64
    UNIT_LABEL	= 65
    ANNEX	= 66
    OLD_GRAPH_CURSOR	= 67
    Z_SCALE	= 68
    COLOR_RAMP	= 69
    OUTPUT_INDICATOR	= 70
    X_SCALE_UNIT_LABEL	= 71
    Y_SCALE_UNIT_LABEL	= 72
    Z_SCALE_UNIT_LABEL	= 73
    GRAPH_MOVE_TOOL	= 74
    GRAPH_ZOOM_TOOL	= 75
    GRAPH_CURSOR_TOOL	= 76
    GRAPH_X_FORMAT	= 77
    GRAPH_Y_FORMAT	= 78
    COMBO_BOX_BUTTON	= 79
    DIAGRAM_IDENTIFIER	= 80
    MENU_TITLE_LABEL	= 81
    CAPTION	= 82
    REFNUM_SYMBOL	= 83
    KUNNAMED84	= 84
    FORMERLY_ANNEX2	= 85
    BOOLEAN_LIGHT	= 86
    BOOLEAN_GLYPH	= 87
    BOOLEAN_DIVOT	= 88
    BOOLEAN_SHADOW	= 89
    TAB	= 90
    PAGE_LIST_BUTTON	= 91
    TAB_CAPTION	= 92
    TAB__BACKGROUND	= 93
    SCALE_NAME	= 94
    SLIDE_CAP	= 95
    KUNNAMED96	= 96
    CONTAINED_DATA_TYPE	= 97
    POSITION_DATA_TYPE	= 98
    TAB_GLYPH	= 99
    GRID	= 100
    NUM_LABEL	= 101
    SPLIT_BAR	= 102
    MUTLI_Y_SCROLLBAR	= 103
    GRAPH_VIEWPORT	= 104
    GRAB_HANDLE	= 105
    GRAPH_SPLITTER_BAR	= 106
    GRAPH_LEGEND_AREA	= 107
    GRAPH_LEGEND_SCRLBAR = 108
    DATA_BINDING_STATUS	= 109
    TERNARY_TEXT	= 110
    TERNARY_BUTTON	= 111
    MULTISEG_PIPE_FLANGE = 112
    MULTISEG_PIPE_ELBOW	= 113
    MULTISEG_PIPE_PIPE	= 114
    GRAPH_LEGEND_FRAME	= 115
    SCENE_GRAPH_DISPLAY	= 116
    OVERFLOW_STATUS	= 117
    RADIX_SHADOW	= 118
    CUSTOM_COSMETIC	= 119
    TYPEDEF_CORNER	= 120
    NON_COLORABLE_DECAL	= 8000 # 121 ?
    DIGITAL_DISPLAY	= 8001
    ARRAY_INDEX	= 8002
    VARIANT_INDEX	= 8003
    LISTBOX_DISPLAY	= 8004
    DATA_DISPLAY	= 8005
    MEASURE_DATA	= 8006
    KNOTUSED4	= 8007
    TREE_LEGEND	= 8008
    COLOR_RAMP_ARRAY	= 8009
    TYPE_DEFS_CONTROL	= 8010
    CURSOR_BUTTONS	= 8011
    HIGH_COLOR	= 8012
    LOW_COLOR	= 8013
    GRAPH_CURSOR	= 8014
    GRAPH_SCALE_LEGEND	= 8015
    TABLE	= 8015
    IO_NAME_DISPLAY	= 8016
    TAB_CTRL_PAGE_SEL	= 8017
    BROWSE_BUTTON	= 8018
    GRAPH_PLOT_LEGEND	= 8019

def partIdToEnum(partId):
    if partId not in set(item.value for item in PARTID):
        return partId
    return PARTID(partId)

class DSINIT(enum.IntEnum):
    """ Part identifiers
    """
    Unknown0	= 0
    Unknown1	= 1
    DSHiliteTableTypeDesc	= 2
    Unknown3	= 3
    Unknown4	= 4
    # Points to Cluster type which consists of another Cluster and then connector types
    DSProbeTableTypeDesc	= 5
    NumDCOs		= 6
    FPdcoInfoTblOffst	= 7
    Unknown8	= 8
    Unknown9	= 9
    Unknown10	= 10
    Unknown11	= 11
    NConnectorPorts	= 12
    Unknown13	= 13
    Unknown14	= 14
    NExtraDCOInfoEntries	= 15
    Unknown16	= 16
    Unknown17	= 17
    Unknown18	= 18
    Unknown19	= 19
    Unknown20	= 20
    Unknown21	= 21
    Unknown22	= 22
    Unknown23	= 23
    Unknown24	= 24
    Unknown25	= 25
    Unknown26	= 26
    Unknown27	= 27
    Unknown28	= 28
    Unknown29	= 29
    Unknown30	= 30
    Unknown31	= 31
    Unknown32	= 32
    Unknown33	= 33
    Unknown34	= 34
    Unknown35	= 35
    Unknown36	= 36
    Unknown37	= 37
    Unknown38	= 38
    Unknown39	= 39
    Unknown40	= 40
    Unknown41	= 41
    Unknown42	= 42
    Unknown43	= 43
    Unknown44	= 44
    Unknown45	= 45
    Unknown46	= 46
    Unknown47	= 47
    Unknown48	= 48
    Unknown49	= 49
    Unknown50	= 50

def dsInitIdToEnum(dsInitId):
    if dsInitId not in set(item.value for item in DSINIT):
        return dsInitId
    return DSINIT(dsInitId)
