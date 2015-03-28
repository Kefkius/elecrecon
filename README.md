# elecrecon

This is a that attempts to retrieve data heuristically about a coin by looking through its electrum fork.

## Usage

```
positional arguments:
  github_user  name of the github account that owns the repo
  repo_name    name of the repository
```

Retrieve Bitcoin's info at https://github.com/spesmilo/electrum

```
$ python electrum-recon.py spesmilo electrum

{'wif': 0, 'actual_wif': 128, 'p2sh': 5, 'p2pkh': 0}
```

`actual_wif` refers to the 'real' value of the WIF byte, which is different from
the 'assumed' WIF byte value. Usually, the WIF byte is (`p2pkh_verison` + 128) % 255, but
this is not always the case. In all cases, `actual_wif` should show the value that is actually used.
