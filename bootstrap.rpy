# Debug UI Config
init python:
    _debug_ui_visible = True
    _debug_ui_hotkey ="K_INSERT"
    _debug_ui_font_path = "renpy_debug_ui/assets/fonts/MPLUS1p-Regular.ttf"
    _debug_ui_headers = {
        "collapsed": False,
        "readme_collapsed": False,
        "lang_collapsed": False,
        "script_collapsed": False,
        "information_collapsed": False
    }

    def toggle_debug_ui():
        global _debug_ui_visible
        _debug_ui_visible = not _debug_ui_visible
        renpy.restart_interaction()

    config.overlay_during_with = True
    config.always_shown_screens.append('debug_ui_display')
    config.top_layers.append('debug_ui_layer')
