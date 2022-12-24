# Web3pathPy
Program for listing all the paths between 2 wallet addresses using Python &amp; `etherscan.io` API (web3 / Blockchain)

## Description
This program connects to the `Ethereum network` using the `web3 library`, and gets the list of all accounts in the network regarding the `wallet addresses` entered by the user. Then it goes through all the accounts and checks if they are on the way between the two wallet addresses. If an account has a balance and has a connection with another wallet, it is added to the `list of paths`. Finally, the list of paths is printed and can be downloaded in the `.csv` format file. Accordingly, if 2 wallets are completely unrelated, then the program does not output transaction paths.
 - Initially, I tried to write a smart contract on solidity so that it outputs the communication paths of 2 wallets and connect this contract to web interface (JS, HTML/CSS). But unfortunately I had problems due to lack of experience in Solidity;
 - Finally, I decided to write a Python console program using the API `therscan.io`;
 - To test the program without downloading, you can use this link:
