import argparse

parser = argparse.ArgumentParser(
    description="This program prints the naöes of my dogs"
)
parser.add_argument('-c' , '--color' ,metavar='color', required=True,choices= {'yellow','blue'},help="the volor the search for"  )

args  = parser.parse_args()
print(args.color)