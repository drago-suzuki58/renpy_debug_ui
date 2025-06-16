# Debug UI Config
init python:
    import sys
    import os

    try:
        module_path = os.path.join(renpy.config.gamedir, 'renpy_debug_ui')
        if module_path not in sys.path:
            sys.path.append(module_path)

        from renpy_debug_ui import DebugUI

        debug_ui = DebugUI()

        # Debug UI strings prefix
        DBG = ""

    except Exception as e:
        renpy.error("Failed to initialize Debug UI")
        renpy.error(str(e))


    config.statement_callbacks.append(debug_ui.track_say_statements)
    config.overlay_during_with = True
    config.top_layers.append('debug_ui_layer')
    try:
        config.always_shown_screens.append('debug_ui_display')
    except Exception:
        config.overlay_screens.append('debug_ui_display')
