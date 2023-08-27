
import re

# Go to which of these is appropriate and download file as XML:
# https://steamcommunity.com/profiles/{YOUR_PROFILE_ID}/games?xml=1
# https://steamcommunity.com/id/{YOUR_PROFILE_ID}/games?xml=1

# Filename should look like this:
# steamcommunity.com_profiles_76561181234567890_games_xml=1.xml

# You'll probably want to index .url files in C:\ProgramData\Microsoft\Windows\Start Menu\Programs and make a new folder

filename = r''


illegals = r'/\:*?"<>|'

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [ i[:-1] for i in lines ]


for i,j in enumerate(lines):
    # Scan for IDs
    if r'<appID>' in j:
        # Get ID
        ID = re.search(r'>(.*?)<',j).group(1)
        # Get name
        for i2,j2 in enumerate(lines[i+1:]):
            if r'<name>' in j2:
                name = re.search(r'CDATA\[(.*?)\]\]\>',j2).group(1)
                break
        # Remove illegal characters from filename (for Windows)
        new_name = ''.join([ (i if i not in illegals else '') for i in name ])
        filename = f'{new_name}.url'
        # Write .url file
        with open(filename,'w') as f:
            print(f'\nname:     {name}')
            print(f'appID:    {ID}')
            print(f'Filename: {filename}')
            out_lines = [
                '[InternetShortcut]',
                'IDList=',
                'IconIndex=0',
                f'URL=steam://rungameid/{ID}'
            ]
            for i in out_lines:
                f.write(i+'\n')






