
# Frank, Ian and Glen’s Letters

## Learning Goals

- Practise working with libraries in python
- Practise working with command-line arguments in python


## Background

Among the fonts supported by FIGlet are those at [figlet.org/examples.html](figlet.org/examples.html)

FIGlet has been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)



## Implementation Details

In a file called `figlet.py`, there's a program that:

- Expects zero or two command-line arguments:
  - Zero if the user would like to output text in a random font.
  - Two if the user would like to output text in a specific font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.

- Prompts the user for a string of text.
- Outputs that text in the desired font.


## Usage/Examples

Your program should behave per the examples below.

```
$ python figlet.py                                                              
Input: hello, world                                                             
Output:                                                                         
 _          _ _                             _     _                             
| |__   ___| | | ___    __      _____  _ __| | __| |                            
| '_ \ / _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |                            
| | | |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |                            
|_| |_|\___|_|_|\___( )   \_/\_/ \___/|_|  |_|\__,_|                            
                    |/                                                          
```

```
$ python figlet.py -f  slant                                                     
Input: hello, world                                                             
Output:                                                                         
    __         ____                               __    __                      
   / /_  ___  / / /___       _      ______  _____/ /___/ /                      
  / __ \/ _ \/ / / __ \     | | /| / / __ \/ ___/ / __  /                       
 / / / /  __/ / / /_/ /     | |/ |/ / /_/ / /  / / /_/ /                        
/_/ /_/\___/_/_/\____( )    |__/|__/\____/_/  /_/\__,_/                         
                     |/                                                      
```

```
$ python figlet.py --font rectangles                                            
Input: hello, world                                                             
Output:                                                                         
                                                                                
 _       _ _                        _   _                                       
| |_ ___| | |___      _ _ _ ___ ___| |_| |                                      
|   | -_| | | . |_   | | | | . |  _| | . |                                      
|_|_|___|_|_|___| |  |_____|___|_| |_|___|                                      
                |_|                                                             
```

```
$ python figlet.py --font alphabet                                            
Input: Moo                                                              
Output:                                                                 

M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo 

```


