# Cascading Rainbow-- A custom Powerline segment

![woot](1.png)

### built by Mel Sawyer

[Powerline](https://powerline.readthedocs.io/en/master/) is a plugin to produce statusline segments. This is a custom segment to display the **current working directory** in a satisfying gradient of rainbow colors. All of the existing functionality of the `cwd` segment still remains (shortening directory names, adding a max depth, etc)-- this customization merely adds gradient coloring on top. I built this segment for use in a bash prompt, but it should theoretically work in vim, zsh, tmux, etc. 

## Examples
![woot](2.png)

![woot](3.png)


## Installation

Install powerline: 
```
pip install powerline-status
```
(or other installation options detailed [here](https://powerline.readthedocs.io/en/master/installation.html))


### Using pip:
```
pip install cascading-rainbow
```

## Configuration

**In order to configure powerline to use the cascading_rainbow segment, you'll need to do the following:**

Go into your powerline config directory. I copy mine into a more accessible place:
```
cp -r ~/Library/Python/3.8/lib/python/site-packages/powerline/config_files/* ~/.config/powerline  #replace with location of powerline installation on your machine
```
You should see the following directory structure:

|-- colors.json \n
|-- config.json \n
|-- colorschemes \n
|------ default.json \n
|-- themes \n
|------- shell \n
|-----------default.json \n

(You'll probably have more subdirectories than this).
#### Add the rainbow gradient to your colors.json file.
This is where you're telling powerline which colors you want to use in the output. Below are the colors I used with a couple variations. Note that output colors might look different depending on your terminal settings. Feel free to use whatever colors here you'd like! 

Add the following gradient **at the bottom of your colors.json file** 
``` 
"rainbow": [
                        [105, 141, 177, 213, 211, 209, 208, 214, 220, 214, 208, 209, 211, 213, 177, 141, 105, 69, 33, 69]
                ]
```

#### Set the color gradient to use for the `cascading_rainbow` segment
Next, add the following to your colorschemes/[colorscheme].json file. (I usually copy `default.json` into a new file, in this case `rainbow.json`, in order to keep everything separate). 
```
"cascading_rainbow":          { "fg": "black", "bg": "rainbow", "attrs": [] }
```
(if you'd like to make your text white, or bold, or use a different gradient besides `rainbow`, you can do so here.

The `blue_red` gradient that comes in the powerline installation is also nice to use with this segment:




