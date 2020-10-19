import argparse
from os import getenv

home = getenv("HOME")

parser = argparse.ArgumentParser()
parser.add_argument("-t", help="title", action="store", type=str)
parser.add_argument("-y", help="years, TYLKO DLA FILMOW", action="store", type=str)
parser.add_argument("-s", help="sources, NIE TRZEBA ZMIENIAC", action="store", default = "BluRay, WEB-DL, WEB", type=str)
parser.add_argument("--season", help="season number, TYLKO DLA SERIALI", action="store", type=str)
parser.add_argument("--smartepisode", help="smart episode, TYLKO DLA SERIALI", action="store_true")
parser.add_argument("--maxper", help="max dowloads per week/month, DOMYSLNIE MONTH, dla seriali zmienic na WEEK", action="store", default="month")
args = parser.parse_args()

resolutions = "resolutions = 1080p"
match_sites = "match-sites = tl"
max_size = "max-size = 15GB"
max_downloads = "max-downloads = 1"

file = open(home+"/.autodl/autodl.cfg", "a")

file.write("\n")
file.write("[filter " + str(args.t) + "]" + "\n")
file.write(match_sites + "\n")
file.write(max_size + "\n")
file.write("shows = " + str(args.t) + "\n")
file.write("sources = " + str(args.s) + "\n")
if str(args.y) == "None":
    pass
else:
    file.write("years = " + str(args.y) + "\n")
file.write(resolutions + "\n")
file.write(max_downloads + "\n")
file.write("max-downloads-per = " + str(args.maxper) + "\n")
if str(args.season) == "None":
    pass
else:
    file.write("seasons = " + str(args.season) + "\n")
if str(args.smartepisode) == "False":
    pass
else:
    file.write("smart-episode = " + str(args.smartepisode) + "\n")

file.close() 
