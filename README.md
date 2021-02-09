<a href="https://github.com/jacopomv/shaky/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/jacopomv/shaky?style=plastic"></a>
<a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fjacopomv%2Fshaky"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=Follow%20%40marb&style=social&url=https%3A%2F%2Ftwitter.com%2Fmarb_0x08"></a>

# Shaky 🖱️

Shaky is a simple python script that implements mouse jiggler based on [mouse](https://pypi.org/project/mouse/) Python library.

## Getting the code
Download from repository:

    $ git clone https://github.com/jacopomv/shaky
    $ cd shaky/

## Usage
    =======================================================
    =======================================================

             _____ _           _
            /  ___| |         | |
            \ `--.| |__   __ _| | ___   _
             `--. \ '_ \ / _` | |/ / | | |
            /\__/ / | | | (_| |   <| |_| |
            \____/|_| |_|\__,_|_|\_'\__, |
                                     __/ |
                                    |___/

     > shaky.py - marb.................................
    -------------------------------------------------------
    Simple tool to bill while AFK!
    =======================================================

    usage: shaky.py [-h] [-d MINUTES]

    optional arguments:
      -h, --help                            Show this help message and exit.         
      -d MINUTES, --duration MINUTES        Set the duration of the Mouse jitter in minutes.
     
     $> python shaky.py                     Default mode, it will jitter the mouse for an undefined amount of time Ctrl + C or mouse move to exit.
     $> python shaky.py -d 5                Timebased mode, the jitter will last for the indicated amount of time.
     
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
