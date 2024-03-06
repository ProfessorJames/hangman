class Colours:

    COLOURS = {
        'black': '\u001b[30m',
        'red': '\u001b[31m',
        'green': '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue': '\u001b[34m',
        'magenta': '\u001b[35m',
        'cyan': '\u001b[36m',
        'white': '\u001b[37m',
    }
    
    @staticmethod
    def colourize(text, color):
        colour_code = Colours.COLOURS.get(color)
        reset_code = '\u001b[0m'  
        return colour_code + text + reset_code

