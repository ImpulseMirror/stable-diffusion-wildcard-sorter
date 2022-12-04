extension_name = "Wildcard Sorter"

def get_image_wildcard(prompt, sort_keys):
    # todo: regex parse the image prompt for the key and find the inserted value
    return wildcard_value if wildcard_value else ""

def on_ui_settings():
    options = {}

    options.update(shared.options_section(('wcs', extension_name), {
        
    }))

    # opts.add_option(ais_exif_pnginfo_choices.get_name(),
    #                 options[ais_exif_pnginfo_choices.get_name()])

def on_before_image_saved(params: ImageSaveParams):    
    
    
    return params
        
def on_image_saved(params: ImageSaveParams):
    

class WildcardSorter(scripts.Script):
    def title(self):
        return extension_name

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return []

    def process(self, p):
        pass


script_callbacks.on_ui_settings(on_ui_settings)
script_callbacks.on_before_image_saved(on_before_image_saved)
script_callbacks.on_image_saved(on_image_saved)