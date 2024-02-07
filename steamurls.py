
import re

# Go to which of these is appropriate and download file as XML:
# https://steamcommunity.com/profiles/{YOUR_PROFILE_ID}/games?xml=1
# https://steamcommunity.com/id/{YOUR_PROFILE_ID}/games?xml=1

# Filename should be "games.xml"; formerly:
# steamcommunity.com_profiles_76561180123456789_games_xml=1.xml

# You'll probably want to index .url files; copy to:
# C:\ProgramData\Microsoft\Windows\Start Menu\Programs


filename = r'games.xml'
illegals = r'/\:*?"<>|' # Windows 10 illegal file name chars


with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
lines = [ i[:-1] for i in lines ] # remove newlines

# Scan for IDs, create .url file for each
for i,line in enumerate(lines):
    if r'<appID>' in line:
        # Get ID
        ID = re.search(r'>(.*?)<',line).group(1)

        # Look for name by iterating over the following lines
        for i2,line2 in enumerate(lines[i+1:]):
            # get name and break at first instance
            if r'<name>' in line2:
                name = re.search(r'CDATA\[(.*?)\]\]\>',line2).group(1)
                break
            
        # Remove illegal characters from "name" for filename (for Windows)
        new_name = ''.join([ (i if i not in illegals else '') for i in name ])
        filename = f'{new_name}.url'
        
        # Write .url file
        with open(filename,'w') as f:
            print(f'appID:    {ID}')
            print(f'\nname:     {name}')
            print(f'Filename: {filename}')
            out_lines = [
                '[InternetShortcut]',
                'IDList=',
                'IconFile=C:\Windows\system32\setupapi.dll',
                'IconIndex=36',
                f'URL=steam://rungameid/{ID}'
            ]
            for i in out_lines:
                f.write(i+'\n')
