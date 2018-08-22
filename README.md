# JobApplicationHelper
JobApplicationHelper is a little python script to help you apply for jobs easier and faster. 

This script works in two ways:
- Copy/Paste
- Link opener

## How to configure
First you need to change the following lines in your text editor of choice to reflect your actual information
```
linkedInUrl   = 'https://linkedin.com/in/<user>'
portfolioUrl  = 'https://example.com/'
addressString = '742 Evergreen Terrace'
phoneString   = '5559025'
mailString    = 'example@email.com'
```
You can also change the buttons' images by modifying the following lines
```
linkedInImagePath = 'Linkedin.gif'
portfolioImagePath   = 'Portfolio.gif'
addressImagePath  = 'Address.gif'
phoneImagePath    = 'Phone.gif'
mailImagePath     = 'Mail.gif'
```
In case you want to add more buttons you can modify the `buildLayout( root )` function as follows
```
global newImage

newImage = tk.PhotoImage(file=newImage)

newButton = tk.Button(root, width=32, height=32, image=newImage, command=lambda: setClipboard(root, '<New Url>'))
newButton.grid(row = 0, column = <Column>, padx=(0,2))
```
The Column should be an Integer that represents the position in the window, in the case of the current code we should put 6 in this field so it goes at the right of the "Load" button.

## How to use

### Copy/Paste
This script creates a window with six buttons. The first five buttons allow you to put strings in your clipboard. For example, if you click the mail button your clipboard will now have the string you set as your e-mail address.

### Link Opener
The sixth button (load button) parses all urls in your clipboard and changes its label so you know how many links have been read.
After loading the urls you can click the button to open the current url in a new tab in your browser. This is helpful when you are looking at many job openings but cannot apply at the moment, just copy the url, paste it in a text editor and when you are ready to apply just copy all urls and press load.
The list should look like this, one url per line
```
http://jobsite.com/opening123
http://alldajobs.com/456
http://wannawork.com/jobs/789
```
Urls must start with `http`. You can change this by modifying the `loadButtonCallback( root )` function, specifically this line: `JOBS_ARRAY = findall('(http\S*)', jobData)`
