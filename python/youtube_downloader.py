import webbrowser

url = 'https://www.youtube.com/watch?v=HivQqTtiHVw&list=RDHivQqTtiHVw&start_radio=1'

download = url[:12] + 'ss' + url[12:]

webbrowser.open(download)
