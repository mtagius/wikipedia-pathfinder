# wikipedia-pathfinder
A script to find paths through Wikipedia 

pip install beautifulsoup4
pip install httplib2
python3 main.py

TODO:
    Create Mode to search for "primary pages" (Pages with a link to the desired page in it)
    Create Mode to search for "secondary pages" (Pages with a link to any primary page in it)
    Create storage mechanism to store page lists for a desired page 
    Make the link picker favor the desired page, then primary pages, then secondary pages, then random pages.