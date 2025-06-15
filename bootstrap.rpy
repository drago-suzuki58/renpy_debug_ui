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

    except Exception as e:
        renpy.error(f"Failed to initialize Debug UI: {e}")


    config.statement_callbacks.append(debug_ui.track_say_statements)
    config.overlay_during_with = True
    config.always_shown_screens.append('debug_ui_display')
    config.top_layers.append('debug_ui_layer')
