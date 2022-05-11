# crypto.com vs crypto.org

- Similar to BNB (Binance Chain - .org, BSC - .com)
- .com is EVM compatible IBC, .org is the mainnet built on Cosmos SDK
- .com (Cronos) powered by Ethermint, which allows rapid porting of apps and smart contracts from Ethereum and EVM-compatible chains. The main focus is to bridge, and support smart contracts and dapps.
- .org Chain is native blockchain solution for Crypto.com, backbone behind the Crypto.com applications. It aims to provide a fast transaction experience. 
- CRO utility token on both, exists as ERC20 as well
- Together, aimed to be the intersection of Ethereum and Cosmos

## Bridging
- Bridge between the chains using [Cronos Bridge](https://cronos.org/bridge)
[Docs](https://cronos.org/docs/bridge/webapp.html)

**Currently supported networks:**
- Crypto.org <-> Cronos
- Cosmos <-> Cronos
- Terra <-> Cronos
- Akash <-> Cronos

**Currently supported tokens:**
- CRO
- ATOM
- LUNA
- AKT

- Going from ERC20 CRO, will have to go through the crypto.com app

## Ecosystem

### Exchanges
- Crypto.com app
- [VVS Finance (.com/.org)](https://vvs.finance/)
- [MM Finance (.com)](https://mm.finance/)

### Explorers
- [Cronos Explorer (.com)](https://cronos.org/explorer)
- [Cronoscan Explorer (.com)](https://cronoscan.com/)
- [Crypto.org Explorer](https://crypto.org/explorer)
- [Mintscan](https://www.mintscan.io/crypto-org)

### Analytics
- [DeFI Lama](https://defillama.com/chain/Cronos)
- [Cronoscan](https://cronoscan.com/tokens)
- [Geckoterminal](https://geckoterminal.com/cro/tokens)
- [Dexscreener](https://dexscreener.com/cronos)

### Dev
- [Github](https://github.com/crypto-org-chain/cronos)
- [Dev docs](https://cronos.org/docs/resources/chain-integration.html#integration-guide-for-cronos-mainnet-beta)

### Grants/Funding
- [Cronos Ecosystem Grant](https://cronos.org/grants)
- [Particle B](https://www.cronoslabs.org/)

### Node 

- [Cronos Docs](https://cronos.org/docs/getting-started/cronos-mainnet.html)
- Proof of Authority (POA), validator hosting by invite only 22 validators currently [List](https://cronos.org/validators)
- Minimum - Stakespace (2.6m CRO)
- [Main (.org) Docs](https://crypto.org/docs/getting-started/mainnet.html)
- [FAQ](https://github.com/crypto-org-chain/chain-main/discussions/442)
- Active validators only receive rewards: top 100 [Active Validators](https://crypto.org/explorer/validators)
- Capital: 1.3m CRO - 366m CRO bonded 
- H/W Requirements: Minimum requirements
    - 4-core, x86_64/ARM architecture processor; 16 GB RAM; 1 TB of storage space

## Infra APIs

### Mainnet (.org)
- Tendermint/Cosmos - https://crypto.org/docs/resources/blocks-and-transactions.html#table-of-content
  - Example: https://mainnet.crypto.org:1317/cosmos/tx/v1beta1/txs/0C5E617B0577B047D78EBF5313B8B70DF69E9535E17B964303BD04947B11B660
- Crypto.org Explorer 
  - Example: https://crypto.org/explorer/api/v1/transactions/0C5E617B0577B047D78EBF5313B8B70DF69E9535E17B964303BD04947B11B660
- Mintscan
  - Example: https://api-cryptocom.cosmostation.io/v1/tx/hash/0C5E617B0577B047D78EBF5313B8B70DF69E9535E17B964303BD04947B11B660

### EVM
- JSON-RPC - https://evm.cronos.org/
  - Example: https://etherflow.quiknode.io/aHR0cHM6Ly9ldm0uY3Jvbm9zLm9yZy8=/web3/eth_getTransactionByHash/0xd67454ec590e1617db920735d0796d33c8e919e4a44a69c2e1ed405ed60b9758
- Cronos Exporer - https://cronos.org/explorer/api-docs
- CronoScan - https://cronoscan.com/apis 

## References
- [Binance Academy](https://academy.binance.com/en/articles/what-is-thorchain-rune)

