# Shaky 🖱️

Shaky is a python script to implement mouse jiggling based on WIN32 APIs.

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
      -h, --help                            Show this help message and exit                            
      -d MINUTES, --duration MINUTES        Set the duration of the Mouse jitter in minutes
     
     $> python shaky.py -d 5
     $> python shaky.py                     Default mode will jitter the mouse for an undefined amount of time until either Ctrl + C or mouse move is detected

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
