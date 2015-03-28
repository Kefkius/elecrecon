'''Find data heuristically about a coin from an electrum fork'''
import argparse
from electrum_recon.recon import Recon

parser = argparse.ArgumentParser(description='Find data heuristically in an electrum repo')
parser.add_argument('github_user', default='spesmilo', help='name of the github account that owns the repo')
parser.add_argument('repo_name', default='electrum', help='name of the repository')

args = parser.parse_args()


if __name__ == '__main__':
    recon = Recon(args.github_user, args.repo_name)
    recon.do_recon()
    print(recon.params)
