import argparse
import datetime
parser= argparse.ArgumentParser()

parser.add_argument ("--num_y" , help = "insert the number of years", type=int)
parser.add_argument ("--num_d", help = "insert the number of days", type=int)
args = parser.parse_args()
dt = datetime.datetime.now()

print("current date:", dt)

if args.num_y:
    print("given years:", args.num_y)
    print("final date:", dt.replace(year=dt.year + args.num_y))
if args.num_d:
    print("given days:", args.num_d)
    tdelta = datetime.timedelta(days = args.num_d)
    print("final date:", dt + tdelta)
else:
    print("given days:not given")
