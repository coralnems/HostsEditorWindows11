# PySide6 Hosts Editor 🚀🐍

Welcome to the __PySide6 Hosts Editor__! This fun and simple GUI app helps you manage your system's hosts file with ease—and a splash of humor! 😎✨

## What It Does

- __Loads Your Hosts File:__  
  Reads your system's hosts file (located at `/etc/hosts` on Unix/Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows) and displays it in an easy-to-edit text area.  
  📄👀

- __Pulls & Merges Block Lists:__  
  Fetches a remote block list (by default from `https://someonewhocares.org/hosts/hosts`) and smartly merges it into your hosts file, complete with clear markers.  
  🤖➡️📋

- __Saves Changes:__  
  Writes your modifications back to the hosts file. (Remember, you'll need admin/root privileges for this part!)  
  💾🔐

## How It Works

1. __Loading:__  
   When you start the app, it reads your hosts file and displays its content for you to review and edit.  
   _"Load it up, edit away!"_ 😄

2. __Merging:__  
   Click the __Pull & Merge Block List__ button, and the app will download a remote block list, appending it to your hosts file with distinct markers.  
   _"Merge like a boss!"_ 🤓

3. __Saving:__  
   Once you're happy with your changes, hit __Save Hosts File__ to write your updates back to the system's hosts file.  
   _"Save it and wave goodbye to unwanted domains!"_ 🎉

## Prerequisites 🚦

- __Python 3.x__  
  Make sure you have Python 3 installed. 🐍

- __PySide6__  
  Install it via pip:

  
- __Requests__  
For fetching remote block lists:  


## Running the App 🚀

Clone the repository, then run the script:
git clone https://github.com/coralnems/HostsEditorWindows11
cd HostsEditorWindows11
pip install -r requirements.txt 
python HostsEditorWindows11.py

> __Note:__  
> - On __Windows__, run your command prompt as an administrator.  
> - On __Unix/Linux__, you might need to use `sudo` when saving the hosts file.

## Contributions & Issues 🤝🐛

Got suggestions, improvements, or encountered any bugs? Open an issue or submit a pull request! Let's make hosts file editing safer, funnier, and more powerful together. 😄👍

## License 📜

This project is licensed under the __MIT License__. See the LICENSE file for details.

Enjoy editing your hosts file with style—and a bit of quirky humor! 🎉😎

