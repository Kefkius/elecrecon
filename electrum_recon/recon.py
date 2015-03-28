import re, requests

# any number of tabs/spaces
tabs_spaces = '[\t ]*'

class Recon(object):

    def __init__(self, github_user, repo_name):
        self.base_url = ''.join( ['https://raw.githubusercontent.com/', github_user,
            '/', repo_name, '/master'] )
        self.params = {}

    def do_recon(self):
        self.recon_p2pkh_and_wif()
        self.recon_p2sh()

    def recon_p2pkh_and_wif(self):
        url = ''.join( [self.base_url, '/lib/bitcoin.py'] )
        raw_file = requests.get(url).text

        re_string = ''.join([
            '^', tabs_spaces,
            'def hash_160_to_bc_address\(h160, ',
            'addrtype[ ]*=[ ]*',
            '([\d]*)',
            '\):', '$'
        ])
        re_p2pkh = re.compile(re_string, re.M)
        m = re_p2pkh.search(raw_file)
        try:
            p2pkh_version = m.group(1)
        except:
            print('could not find p2pkh')
            return
        self.params['p2pkh'] = int(p2pkh_version)

        ##################
        re_string = ''.join([
            '^', tabs_spaces,
            'def ASecretToSecret\(key, addrtype=',
#            ', addrtype=',
            '([\d]*)',
            '\):', '$'
        ])
        re_wif = re.compile(re_string, re.M)
        m = re_wif.search(raw_file)
        try:
            wif_version = m.group(1)
        except:
            print('could not find wif')
            return
        self.params['wif'] = int(wif_version)

        ###################
        re_string = ''.join([
            '.*',
            'chr\(\(addrtype\+128\)&255\):',
            '$'
        ])
        re_add_wif = re.compile(re_string, re.M|re.S)
        m = re_add_wif.search(raw_file)
        try:
            m.group()
            self.params['actual_wif'] = ( int(self.params.get('wif'))+128 ) &255
        except:
            self.params['actual_wif'] = self.params.get('wif')

    def recon_p2sh(self):
        url = ''.join( [self.base_url, '/lib/account.py'] )
        raw_file = requests.get(url).text

        re_string = ''.join([
            '^',
            tabs_spaces,
            'address = hash_160_to_bc_address\(hash_160\(redeem_script.decode\(\'hex\'\)\),', tabs_spaces,
            '([\d]*)',
            '\)', '$'
        ])
        re_p2sh = re.compile(re_string, re.M)
        m = re_p2sh.search(raw_file)
        try:
            p2sh_version = m.group(1)
        except:
            print('could not find p2sh')
            return
        self.params['p2sh'] = int(p2sh_version)
