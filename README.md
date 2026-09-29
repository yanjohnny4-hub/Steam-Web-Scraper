# Steam-Web-Scraper
A small Python script that pulls the newest games from the Steam store and saves them as a JSON file in your Downloads folder. 

## What it collects
For each game:
| Field | Description |
| ----- | ----------- |
| Title | Game Name |
| Price | Final price as displayed (N/A if no price is shown) |
| Tags | User tags of the game |
| Platforms | Supported platforms (ex: win, mac, linux) |

## Requirements
* Python 3.7+
* requests
* lxml

Install the dependencies:
```
pip install requests lxml
```
Usage: 
```
python steam_scraper.py
```
When it finishes, you should see something like this:
```
Saved 36 games to C:\Users\YourName\Downloads\Steam_Pop_New_Releases.json
```

## Changing the output location
The file is saved to your Downloads folder by default. 
If your Downloads folder lives elsewhere (for example, inside OneDrive on Windows), set the file path accordingly:
```
out_path = Path(r'C:\Users\YourName\OneDrive\Downloads') / 'Steam_New_Releases.json'
```
## Example Output
```
[
    {
        "title": "Example Game",
        "price": "$9.99",
        "platforms": ["win", "mac"],
        "appid": "1234567"
    },
    {
        "title": "Another Game",
        "price": "Free / N/A",
        "platforms": ["win"],
        "appid": "7654321"
    }
]
```

## Disclaimer
This project is for personal and educational use. It is not affiliated with or endorsed by Valve. Respect Steam's Terms of Service and keep your request rate low.

## Author
Cai Xin (Johnny) Yan

Built with Python
