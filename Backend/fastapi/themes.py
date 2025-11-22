# Theme configurations based on your color palettes
THEMES = {
    "purple_gradient": {
        "name": "Mor Tema",
        "colors": {
            "primary": "#A855F7",
            "secondary": "#7C3AED", 
            "accent": "#C084FC",
            "background": "#F8FAFC",
            "card": "#FFFFFF",
            "text": "#1E293B",
            "text_secondary": "#64748B"
        },
        "css_classes": "theme-purple-gradient"
    }
}


def get_theme(theme_name: str = "purple_gradient"):
    return THEMES.get(theme_name, THEMES["purple_gradient"])


def get_all_themes():
    return THEMES
