# Instagram Automation Script

This repository contains a Python script that automates the process of logging into Instagram and posting comments on a specific post. The script uses Selenium to interact with the Instagram web interface and the idea is to automate the process of applying to the popular lottery posts and have more chances of winning.


## Video

<img src="https://github.com/WillyHad96/Instagram-Lottery-Bot/blob/main/InstagramLotteryBotVideoGIF.gif" alt="Screenrecording" width="500" height="500">




## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Google Chrome
- ChromeDriver (make sure the version matches your installed version of Chrome)
- Selenium





## Installation

1. Clone the repository:

```bash
git clone https://github.com/WillyHad96/Instagram-Lottery-Bot/tree/main.git
cd Instagram-Lottery-Bot
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Ensure that the ChromeDriver executable is in your PATH, or specify the path to the ChromeDriver in the script.





## Usage

1. Update the constants in the script:

- home_page_url: The URL of the Instagram post where you want to post comments.
- username: Your Instagram username.
- password: Your Instagram password.

2. Run the Script:
```
py InstagramLotteryBot.py
```





## Script Overview

The script performs the following steps:

1. Open Chrome: Launches a new Chrome browser and navigates to the specified Instagram post.
2. Allow Cookies: Clicks the "Allow Cookies" button if prompted.
3. Log In: Enters your Instagram credentials and logs in.
4. Click Login Button: Clicks the login button to proceed.
5. Save Login Info: Saves the login information if prompted.
6. Click Photo Comment: Clicks on the photo to open the comment section.
7. Add Comment: Adds comments to the post. Each comment starts with the "@" symbol followed by a letter from the alphabet.
8. Send Comment: Sends the comment.
9. Finish Program: Closes the browser and ends the program.


   

## Code Overview

```
# Constants
- home_page_url = "https://www.instagram.com/p/C9ShpZcKd0S/"
- username = "your_username"
- password = "your_password"

# Main Program
open_chrome()
allow_cookies()
click_login_button()
log_in()
save_login_info()

for letter in alphabet:
    for i in range(1, 4):
        add_comment(letter)
        for j in range(1, i):
            textarea.send_keys(Keys.ARROW_DOWN)
        send_comment()

finish_program()
```



## Notes

- The script uses hardcoded XPaths and CSS selectors which may need to be updated if Instagram's web interface changes.
- Be cautious with automated interactions on social media platforms to avoid violating their terms of service.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Licence

This project is licensed under the MIT License.

