# Shaky 🖱️

Shaky is a simple python script that implements mouse jiggler based on [mouse](https://pypi.org/project/mouse/) Python library.

## Getting the code
Download from repository:

    $ git clone https://github.com/marb08/shaky/
    $ cd shaky/
    
### Install [mouse](https://pypi.org/project/mouse/) Python module

    $ pip install mouse

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
Pull requests are welcome.

## License
This script is licensed under the GNU General Public License v3.0.
For more information, please refer to the license text at: https://www.gnu.org/licenses/gpl-3.0.txt
