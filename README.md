# Web3pathPy
Program for listing all the paths between 2 wallet addresses using Python &amp; `etherscan.io` API (web3 / Blockchain)

## Description
This program connects to the `Ethereum network` using the `web3 library`, and gets the list of all accounts in the network regarding the `wallet addresses` entered by the user. Then it goes through all the accounts and checks if they are on the way between the two wallet addresses. If an account has a balance and has a connection with another wallet, it is added to the `list of paths`. Finally, the list of paths is printed and can be downloaded in the `.csv` format file. Accordingly, if 2 wallets are completely unrelated, then the program does not output transaction paths.
 - Initially, I tried to write a smart contract on solidity so that it outputs the communication paths of 2 wallets and connect this contract to web interface (JS, HTML/CSS). But unfortunately I had problems due to lack of experience in Solidity;
 - Finally, I decided to write a Python console program using the API `etherscan.io`;
 - To test the program without downloading, you can use this link: [https://repl.it/web3pathpy](https://replit.com/@arman2669/Web3pathPy#main.py)
 
 **Screen of the Program!**

 [![Testing Results][screen-img]][contributor-url]
 
 ## Acknowledgments

* [Web3 - Python](https://web3py.readthedocs.io/)
* [Ethereum network](https://etherscan.io/)
* [INFURA](https://www.infura.io/)
* [Bitquery Flow Money](https://explorer.bitquery.io/bsc/address/0x04a5a1b0f58a98f45f6cd159365591e37ed8a0ca/graph)
* [Remix](https://remix.ethereum.org/)
 
[screen-img]: https://sun9-west.userapi.com/sun9-65/s/v1/ig2/4zCP6tBq_f0_oZlWgyejvf_UARx8UsU2OfDGfGs5m_CKNAJhOK58--KXsmY7jReJGtHbWvWEutYdomV4aD2FZqCw.jpg?size=2223x1176&quality=95&type=album
[contributor-url]: https://github.com/silvermete0r
