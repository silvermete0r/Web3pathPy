####################################
# Author: Zhalgasbayev Arman
# Team: AIturbo 
# For: BNB-chain x AITU hackathon
# Task: No.7: The best route in Web3
####################################

#importing libraries
import requests
from datetime import date
import csv
import sys


# Set the start and end wallet addresses
start_address = input('Enter the first address: ') # 0xDbAC4996C7D47247330AE55fA49713643D81b211
end_address =  input('Enter the second address: ') # 0x161371515e9584af516767cf105763c847460c2e

# Set the API endpoint and the API key
api_endpoint = 'https://api.etherscan.io/api'
api_key = 'A6FFF9PC64F5NNKY81S1HG2GX3V9HBKNFF'

# Set the API parameters
params = {
    'module': 'account',
    'action': 'txlist',
    'address': start_address,
    'sort': 'desc',
    'apikey': api_key
}

# Initialize a list to store the paths
paths = []

# Send the request to the API
response = requests.get(api_endpoint, params=params)

# Check the status code of the response
if response.status_code == 200:
    # Get the list of transactions from the response
    transactions = response.json()['result']

    # Add titles for paths data
    paths.append(['Block No.:', 'Date:', 'Value:', 'Gas:', 'Gas Price:', 'From:', 'To:'])

    # Iterate over the transactions
    for transaction in transactions:
        # Check if the transaction is to the end address
        if transaction['to'] == end_address:
            # Add the path to the list
            paths.append([transaction['blockNumber'], str(date.fromtimestamp(int(transaction['timeStamp']))), transaction['value'], transaction['gas'], transaction['gasPrice'], start_address, end_address])
        # Check if the transaction is from the end address
        elif transaction['from'] == end_address:
            # Add the path to the list
            paths.append([end_address, start_address])
else:
    # Print an error message
    print('An error occurred while retrieving the transactions.')

# Print the results
if len(paths) != 1:
    # Paths list
    print('Total paths between 2 nodes: ')
    for path in paths:
        print(path)
    # Download data as a CSV table 
    printCSV = input('Do you need a CSV file of the results? (Y/N): ')
    if(printCSV == 'Y'):
        with open("pathsResults.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(paths)
    else:
        #Terminating the program
        print('Program is finished!')
        sys.exit()
else:
    # Print if no transactions detected
    print('No transactions were detected between 2 wallets!')