# Image to ASCII
A command-line program to convert any image into greyscale ASCII art.

<img src="https://imgur.com/ojO31uF.png" width="auto" height="auto">

## Setup
### 1. Clone Repo
`git clone https://github.com/BSmith156/Image-to-ASCII.git`

### 2. Install Requirements
`pip install -r requirements.txt`

## Usage
`image_to_ascii.py input_file output_file [-i] [-max n]`

### Arguments
| Argument | Description |
| -------- | ----------- |
| input_file | The image file being converted. |
| output_file | The file to store the ASCII art. |
| -i | Optional. Inverts the image colour, useful when displaying the output using a light font on a dark background. |
| -max n | Optional. Sets the maximum width/height of the output to n, 0 for no maximum. Defaults to 250. |

## Authors
* [Ben Smith](https://github.com/BSmith156)
