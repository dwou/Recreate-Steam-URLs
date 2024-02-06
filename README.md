Useful if you have a lot of Steam games that aren't indexed. Happened to me when adding games from D: after reinstalling Windows.
## instructions
1) Go to https://steamcommunity.com/profiles/{YOUR_PROFILE_ID}/games?xml=1 or https://steamcommunity.com/id/{YOUR_PROFILE_ID}/games?xml=1 and download file
2) Put .py file in same directory as that file
3) Put that file name in .py file and run. Creates Windows URL file in this directory for every game in your library. It prints the files as it goes.
4) Optional: put URL files in C:\ProgramData\Microsoft\Windows\Start Menu\Programs to index them
## Notes
* Does not fetch game icon, uses default white Windows icon
* Reads XML file in a not great way and therefore will break if the XML file structure/order change
