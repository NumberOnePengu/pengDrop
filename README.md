
# pengDrop

#### A tool for up-and-coming token releases or existing token teams to most fairly and efficiently tap into the worldwide, distributed community of Pudgy Penguins by generously offering token drops to holders.

#### This tool automatically scans the blockchain and creates a real-time snapshot in CSV format of all Pudgy Penguins holders with the amount of tokens they should get according to your input. Contract addresses of popular marketplaces are filtered automatically so that only legitimate Pudgy Penguins holders are included.

Pudgy Penguins are a very active crypto native community, naturally inclined to support up and coming projects. Pudgy Penguins are also one of the most diverse communities of digital identity, including figures as holders in the general direction of:

- Crypto twitter OGs like GCR (rumored to be republican candidate Vivek Ramaswamy), Cobie, Jebus911, Sisyphus, LedgerStatus, Icebergy, vxC0zy, KeyboardMonkey, etc. 
- Wealthy entrepreneurs like Mark Cuban, Luca Netz, etc.
- Athletes and entertainers like Stephen Curry, Tory Lanez, etc.
- Successful 7-8 figure poker players such as Fedor Holz, Linus Loeliger, Mario Mosböck, etc.
- DeFi founders and OGs like Bobby Ong from CoinGecko, Primo from LayerZero (and their whole team), Alex Svanevik from Nansen (and much of their team), Yishay and Barry from Dymension, etc.
- NFT OGs like NFTX, Unstoppable Domains, OpenSea, Blur, etc.
- Exchange people like the Socials from Binance, Listings from WOO, Engineering from Coinbase, etc.
- Fund owners such as Big Brain, Spencer Ventures, Kronos, LayerZero, etc.
- Innumerable X spaces hosts. 
- And thousands of other well connected people not included above. 
## Who might want to airdrop?
Here are a few hypothetical examples of some people who may consider doing it this way.
- A new token that wants to instantly be noticed by the various exchange heads and crypto infrastructure providers.
- A fresh tokenless DeFi protocol that wants to deploy and needs some direction from the resident DeFi Chad penguins.
- A GameFi project that wishes to use penguin assets and wants to thank (and incentivize) the penguin community for participating.
- A SocialFi project that wants crypto OGs to come over to theirs over the incumbents like FT or Farcaster.
- A dApp that may want the eyes of the high-profile holders within the penguin community that are otherwise unreachable.
- A new chain that wants 4,000+ instant new native coin holders.
## Suggested use

We recommend using this to distribute tokens via a snapshot, which takes 5-10 minutes to run. Claims are easily gamed by MEV bots, Blur farmers and  mercenary participants that wish to dump tokens immediately. 

Snapshotted penguin holders would generally interested in new tech so long as it pushes the boundaries of what can be done with a blockchain; the same cannot be said for extractive mercenary liquidity that would be unlocked with a buy-penguin-and-claim-and-dump system.

#### To run the file, download the .py file and open the terminal in its directory.
You must first install the required python packages. You can do this with pip. 

    pip install web3 requests pandas

The two modes are `organic` (recommended: caps at 20 penguins per wallet) and `unfiltered` (not recommended: can be abused by Blur farmers).

Then run the file with the two required arguments, `mode` of distribution, and `amount` of tokens, like this:
    
    python pengDrop.py organic 50000000
                      ^ mode ^ ^ amount ^

After the program runs, the output file will be `nft_owners_filtered.csv` in the format `Address, Amount, Tokens`. 
<img src="https://i.imgur.com/nsreODM.png">
(Amount being number of penguins, tokens being the amount of tokens to be dropped). 

## FAQ

#### How long does it take to run?

It should take about 5-10 minutes but occasionally, and especially during USA peak hours, it can take a little longer since RPCs are overloaded.

#### I have this error...

Most of the time if it's stuck, you just have to start it again.

The software is not written by a professional developer. I have accounted for most issues but it is only optimized to not make mistakes on holders and connectivity. Safety, not speed. Please run it again if you get an error. Fixes will come with time.

#### What's the best way to drop?

It is your call. This is simply a way to get all the right addresses to drop to. Previous drops have done "claim-within-date" and non-claimers' tokens have distributed to claimers.

## Acknowledgements
Thank you to tangentTen for being a second set of eyes looking through the code before publishing.
## License

Anyone can use this however they wish. 

However, just remember that copying this and replacing it with your NFT collection does not recreate the composition of the penguin community. 

