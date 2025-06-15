init python:
    class DebugUI:
        def __init__(self):
            self.visible = True
            self.hotkey = "K_INSERT"
            self.font_path = "renpy_debug_ui/assets/fonts/MPLUS1p-Regular.ttf"
            self.accordions = {
                "collapsed": False,
                "readme_collapsed": False,
                "lang_collapsed": False,
                "script_collapsed": False,
                "information_collapsed": False
            }


            self.script_pos_filename = ""
            self.script_pos_lineno = 0


        def toggle_visibility(self):
            self.visible = not self.visible
            renpy.restart_interaction()

        def track_say_statements(self, statement_name):
            targets = [
                "say", "say-bubble", "say-nvl", "say-centered", "menu", "menu-nvl", "menu-with-caption", "menu-nvl-with-caption"
            ]
            if any(statement_name.startswith(t) for t in targets):
                filename, lineno = renpy.get_filename_line()
                self.script_pos_filename = filename
                self.script_pos_lineno = lineno

    debug_ui = DebugUI()
