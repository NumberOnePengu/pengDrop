from web3 import Web3
import sys
import csv
import os
import pandas as pd
import random
import requests
import threading
import time

## Step 1, find best RPCs.

# List of Ethereum RPC URLs
rpc_urls_og = [
    'https://1rpc.io/eth',
    'https://api.securerpc.com/v1',
    'https://api.zan.top/node/v1/eth/mainnet/public',
    'https://core.gashawk.io/rpc',
    'https://endpoints.omniatech.io/v1/eth/mainnet/public',
    'https://eth.api.onfinality.io/public',
    'https://eth.drpc.org',
    'https://eth.llamarpc.com',
    'https://eth.mainnet.public.blastapi.io',
    'https://eth-mainnet.g.alchemy.com/v2/demo',
    'https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7',
    'https://eth-meowrpc.com',
    'https://eth-pokt.nodies.app',
    'https://ethereum.blockpi.network/v1/rpc/public',
    'https://ethereum.publicnode.com',
    'https://main-light.eth.linkpool.io',
    'https://mainnet.eth.cloud.ava.do',
    'https://rpc.builder0x69.io',
    'https://rpc.eth.gateway.fm',
    'https://rpc.flashbots.net',
    'https://rpc.lokibuilder.xyz/wallet',
    'https://rpc.mevblocker.io',
    'https://rpc.mevblocker.io/fullprivacy',
    'https://rpc.mevblocker.io/noreverts',
    'https://rpc.notadegen.com/eth',
    'https://rpc.payload.de',
    'https://rpc.tenderly.co/fork/c63af728-a183-4cfb-b24e-a92801463484',
    'https://singapore.rpc.blxrbdn.com',
    'https://uk.rpc.blxrbdn.com',
    'https://virginia.rpc.blxrbdn.com'
]
rpc_urls = rpc_urls_og

print("RPC URLs imported:")
print(rpc_urls)
print("—")

def getBestRPCLatencyList(rpc_urls):
    def measure_latency(w3):
        try:
            start_time = time.time()
            w3.eth.get_balance("0x0000000000000000000000000000000000000000")
            latency = (time.time() - start_time) * 1000  # Latency in milliseconds
            return latency
        except Exception as e:
            return None

    # Shuffle the RPC URLs
    random.shuffle(rpc_urls)

    # Create a list to store RPC URLs and their corresponding latencies
    rpc_latency_list = []

    # Measure latency for each RPC URL
    for rpc_url in rpc_urls:
        try:
            # Use requests library to check the connection with a timeout
            response = requests.get(rpc_url, timeout=0.5)
            if response.status_code == 200:
                w3 = Web3(Web3.HTTPProvider(rpc_url))
                if w3.isConnected():
                    latency = measure_latency(w3)
                    if latency is not None:
                        rpc_latency_list.append((rpc_url, latency))
                        print(f'Connected to Ethereum node at {rpc_url}')
        except Exception as e:
            print(e)
            pass

    # Sort the list by latency in ascending order
    sorted_rpc_latency_list = sorted((rpc for rpc in rpc_latency_list if rpc[1] < 500), key=lambda x: x[1])

    return sorted_rpc_latency_list


best_rpc_latency_list = getBestRPCLatencyList(rpc_urls)

# Update the rpc_urls variable with the sorted URLs
rpc_urls = [rpc_url for rpc_url, _ in best_rpc_latency_list]

# Print the sorted list
for rpc_url, latency in best_rpc_latency_list:
    print(f'{rpc_url} — {latency:.2f}')
    
# Print the sorted URLs
print("Final RPCs:")
for rpc_url in rpc_urls:
    print(rpc_url)

print("—")

##### Threading

# Number of threads to use for parallel processing
num_threads = len(best_rpc_latency_list)

# Lock to synchronize access to the owners dictionary
owners_lock = threading.Lock()

# Checksum the contract address
contract_address = Web3.toChecksumAddress("0xbd3531da5cf5857e7cfaa92426877b022e612cf8")

# Define the ABI for the "ownerOf" function
abi = [{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"approved","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":False,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"}],"name":"CreatePenguin","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"MAX_BY_MINT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_ELEMENTS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRICE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseTokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"creatorAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"devAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"val","type":"bool"}],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reveal_timestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"walletOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"payable","type":"function"}]

# Instantiate the contract
contract = None

def initialize_contract(rpc_url):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    global contract
    contract = w3.eth.contract(address=contract_address, abi=abi)
    print(contract)
    print(f"Initialized contract with RPC URL: {rpc_url}")
    time.sleep(2)

# Dictionary to store owner counts
owners = {}

def web3_call_with_retry(function, *args):
    while True:
        try:
            result = function(*args)
            return result
        except Exception as e:
            print(f'Error: {e}')
            print('Switching to a different RPC...')

def fetch_owner_with_retry(contract, token_id):
    return web3_call_with_retry(contract.functions.ownerOf, token_id).call()

# Function to fetch owner for a range of token IDs
def fetch_owners_range(start_token_id, end_token_id):
    global rpc_urls
    global owners
    while start_token_id < end_token_id:
        if token_id_owners[start_token_id] is not None:
            start_token_id += 1
            continue
        try:
            owner = fetch_owner_with_retry(contract, start_token_id)
            with owners_lock:
                owners[owner] = owners.get(owner, 0) + 1
            print(str(start_token_id) + " " + str(owner))
            time.sleep(0.25)
            token_id_owners[start_token_id] = owner
            start_token_id += 1
        except Exception as e:
            print(e)
            try:
                print(f"Error fetching owner for token ID {start_token_id} from {rpc_urls[0]}. Removing it from rotation.")
            except Exception as e:
                pass
            if len(rpc_urls) == 0:
                print("All RPC URLs have failed. Exiting.")
                break
            rpc_urls.pop(0)  # Remove the failed RPC URL
            initialize_contract(rpc_urls[0])  # Initialize with the next available RPC URL

# Function to distribute work to threads
def distribute_work(num_threads):
    # Divide the work into chunks for each thread
    if num_threads == 0:
        best_rpc_latency_list = getBestRPCLatencyList(rpc_urls_og)
        num_threads = len(best_rpc_latency_list)
    
    if num_threads == 0:
        num_threads = 1
        
    chunk_size = len(range(8888)) // num_threads
    threads = []

    for i in range(num_threads):
        start_token_id = i * chunk_size
        end_token_id = (i + 1) * chunk_size if i < num_threads - 1 else len(range(8888))
        thread = threading.Thread(target=fetch_owners_range, args=(start_token_id, end_token_id))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Write results to a CSV file
def write_results():
    with open('nft_owners.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Address', 'Amount'])
        for address, amount in owners.items():
            writer.writerow([address, amount])

# Array to store token ID and owner address
token_id_owners = [None] * 8888  # Assuming there are 8888 tokens (0 to 8887)


# The list of contract addresses to be removed from the CSV
strings_to_remove = [
    "0x29469395eAf6f95920E59F858042f0e28D98a20B", #Blend
    "0x3eb879cc9a0Ef4C6f1d870A40ae187768c278Da2", #FloorProtocolVault
    "0x7822A2151Ad319040913D0EA4B93C64C0b49BF1B", #WrappedPenguins
    "0x89bc08BA00f135d608bc335f6B33D7a9ABCC98aF", #Arcade
    "0x4b94B38beC611A2c93188949F017806c22097e9f", #JPEGd
    "0x7FEe302A14D6B945c0EB6dA9C4426c8D75d38a73", #Fracton
    "0xae18f036459823223f5BAad8137Dd50663f96644", #Paraspace
    "0xE793eAeDC048b7441Ed61b51aCB5df107aF996c2", #JPEGd2
    "0xe5001ce56a6e8EA0875086C404ADB9D0a1ED5364", #NFTbasket
    "0xAbeA7663c472648d674bd3403D94C858dFeEF728" #NFTXv2
]

def filterCSV():
    # Load the CSV file
    df = pd.read_csv('nft_owners.csv')

    # Filter out rows that contain any of the strings in the array
    df_filtered = df[~df.isin(strings_to_remove).any(axis=1)]

    # Sort the DataFrame by the "Amount" column in descending order
    df_filtered2 = df_filtered.sort_values(by='Amount', ascending=False)
    
    # Save the filtered DataFrame to a new CSV file
    df_filtered2.to_csv('nft_owners_filtered.csv', index=False)

    print('CSV file filtered: nft_owners_filtered.csv')
    
    # Remove the 'nft_owners.csv' file
    try:
        os.remove('nft_owners.csv')
    except OSError as e:
        print(f"Error removing files: {e}")
        
total_attempts = 0

    
def main():
    # Define command-line argument for mode selection
    if len(sys.argv) < 3:
        print("Usage: python pengscan.py <mode>")
        print("Modes: eoa unfiltered organic. Recommended: organic")
        sys.exit(1)
    
    # Initialize the contract with the first RPC URL
    global rpc_urls
    initialize_contract(rpc_urls[0])

    while None in token_id_owners:
        # # Fetch owners in parallel with different RPC URLs
        distribute_work(num_threads=len(rpc_urls))  # Use the number of active RPC URLs as the number of threads
        missing_owners = [i for i in token_id_owners if i is None]

    # Check if there are any missing owners
    missing_owners = [i for i in token_id_owners if i is None]
    while len(missing_owners) > 0 and total_attempts < 5:
        print(f"Missing owners for {len(missing_owners)} token IDs. Retrying...")
        # Retry fetching owners for missing token IDs
        # Get RPCs again
        print("Getting RPCs again.")
        best_rpc_latency_list = getBestRPCLatencyList(rpc_urls)
        rpc_urls = [rpc_url for rpc_url, _ in best_rpc_latency_list]
        distribute_work(num_threads=len(rpc_urls))
        if len(rpc_urls) == 0:
            rpc_urls = [rpc_url for rpc_url, _ in best_rpc_latency_list]

    if len(missing_owners) > 0:
        print(f"Still have missing owners after 5 attempts. Missing owners for {len(missing_owners)} token IDs: {missing_owners}")
    
    write_results()
    
    filterCSV()
    
    # Mode filtering 
    # Load the CSV file
    df = pd.read_csv('nft_owners_filtered.csv')

    mode = sys.argv[1].lower()
    if mode == "unfiltered":
        # Do nothing in unfiltered mode
        pass

    elif mode == "organic":
        # Cap values in the "Amount" column at 20
        df['Amount'] = df['Amount'].apply(lambda x: min(x, 20))
        df.to_csv('nft_owners_filtered.csv', index=False)

    else:
        print("Invalid mode; assumed to be unfiltered. Supported modes: unfiltered, organic")
        sys.exit(1)
        
    numTokens = sys.argv[2]
    df = pd.read_csv('nft_owners_filtered.csv')
    total_amount = df['Amount'].sum()
    
    # Calculate the pro rata factor
    pro_rata_factor = int(numTokens) / int(total_amount)
    
    df['Tokens'] = (df['Amount'] * pro_rata_factor).astype(float)
    df.to_csv('nft_owners_filtered.csv', index=False)
    print(f'Distributed {numTokens} tokens pro rata to the "Tokens" column.')
        
    
if __name__ == "__main__":
    main()
