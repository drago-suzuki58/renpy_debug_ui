import renpy


class DebugUI:
    def __init__(self):
        # Debug UI Configuration
        self.visible = True
        self.hotkey = "K_INSERT"
        self.font_path = "renpy_debug_ui/assets/fonts/MPLUS1p-Regular.ttf"
        self.accordions = {
            "collapsed": False,
            "readme_collapsed": True,
            "lang_collapsed": True,
            "script_collapsed": True,
            "information_collapsed": True,
            "store_explorer_collapsed": True,
            "test_prompt_collapsed": True,
        }
        self.child_accordions = {}


        # Tracking
        self.script_pos_filename = ""
        self.script_pos_lineno = 0

        self.input_messages = {
            "test_prompt": "",
        }

    # Debug UI System Methods
    def toggle_visibility(self):
        self.visible = not self.visible
        renpy.exports.restart_interaction()


    # Tracking
    def track_say_statements(self, statement_name):
        targets = [
            "say", "say-bubble", "say-nvl", "say-centered", "menu", "menu-nvl", "menu-with-caption", "menu-nvl-with-caption"
        ]
        if any(statement_name.startswith(t) for t in targets):
            filename, lineno = renpy.exports.get_filename_line()
            self.script_pos_filename = filename
            self.script_pos_lineno = lineno

    def input_prompt(self, key, prompt):
        self._input_data_key = key
        self._input_data_prompt = prompt
        self._input_temp_message = self.input_messages.get(key, "")

        renpy.exports.show_screen("debug_ui_input_prompt")

    def store_edit(self, key, value, prompt):
        self._store_edit_key = key
        self._store_edit_prompt = prompt + ":" + value
        self._store_edit_temp = value

        renpy.exports.show_screen("debug_ui_store_input_prompt")

    def set_store_value(self, var_name, new_value):
        try:
            if var_name in renpy.store.__dict__:
                old_value = getattr(renpy.store, var_name)
                old_type = type(old_value)

                if old_type == int:
                    setattr(renpy.store, var_name, int(new_value))
                elif old_type == float:
                    setattr(renpy.store, var_name, float(new_value))
                elif old_type == str:
                    setattr(renpy.store, var_name, new_value)
                elif old_type == bool:
                    setattr(renpy.store, var_name, new_value.lower() in ['true', '1', 'yes'])
                elif old_type == list:
                    import json
                    setattr(renpy.store, var_name, json.loads(new_value))
                elif old_type == dict:
                    import json
                    setattr(renpy.store, var_name, json.loads(new_value))
                else:
                    setattr(renpy.store, var_name, new_value)

                renpy.exports.restart_interaction()
        except Exception as e:
            renpy.exports.notify("Edit Error: " + str(e))
