import argparse
from redditfoodie import foodie

rf_parser = argparse.ArgumentParser(description='Reddit Foodie')
rf_parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')
rf_parser.add_argument('action', choices=['save', 'setw'],
                       help='Action for reddit-foodie')
rf_parser.add_argument('argument', nargs='*',
                       help='Keyword for food')

rf_args = rf_parser.parse_args()

print(rf_args.action)

if rf_args.action == 'save':
    foodie.saveimages(rf_args.argument)
elif rf_args.action == 'setw':
    foodie.setwallpaper(rf_args.argument)
else:
    print('Error')
