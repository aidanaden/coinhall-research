# Secret Network

## Main Considerations

1. Bond breakdown -- Unable to determine. Explorers dont seem to show breakdown, discord does not seem to indicate that there are any foundation helping validators stay in the active set, most of them got in early BUT have very little self-bonded SCRT stake so may have to ask POC if foundation contributes. (note: no minimum self-bonding amt, validator calculator [here](https://www.securesecrets.org/validatorcalculator))
2. Staking costs:
   - Minimum: 343 SCRT delegated, ~705 USD @ 2.05 USD/SCRT
   - Median (middle guy): 1,155,007 SCRT delegated, 2.36M @ 2.05 USD/SCRT
3. Staking profits (5% comission of 23% APR):
   - Minimum: 8 USD
   - Median: 27K USD
4. Validator POC -- no replies on discord so far, can try contacting them in their [telegram](https://t.me/SCRTcommunity)
5. **Dealbreaker** -- Last validator reward is ~~garbage~~ very low, median validator rewards are quite good though but will depend on whether foundation is willing to contribute since it's quite a huge delegation amount (must enquire from their telegram group).
6. **Recommendation** -- Not too sure about SCRT tokenomics, but if it's possible to get the funds delegated to our validator then it should be somewhat profitable, without foundation/external support, can't recommend it. Long term might be an attractive chain to build on since they have a strong unique value proposition (built-in privacy).

## Get to know (TLDR/One-liners)

Secret Network is a blockchain-based, open-source protocol that lets anyone perform computations on encrypted data, bringing privacy to smart contracts and public blockchains.

## What's in their ecosystem?

- **Exchanges**:
  - [Secret Swap](https://www.secretswap.net/) - Front running resistant AMM
  - [Sienna Network](https://sienna.network/) - Front running resistant AMM, and more products in the future
  - [Button Swap](https://www.btn.group/secret_network/button_swap) - AMM/DEX aggregator by [btn.group](https://www.btn.group/) includes autocompounding of yield for LPs, optimized swaps and [more](https://medium.com/@secretnetwork/button-swap-yield-optimizer-guide-bacef0ad6adb)
  - [Shade Protocol](https://shadeprotocol.io/) - an array of connected privacy-preserving DeFi applications
- **Block explorers**:
  - [Secretnodes](https://secretnodes.com/) - Highly featured explorer, originally funded by the network, run by validator [Secretnodes](https://secretnodes.org/)
  - [Mintscan](https://www.mintscan.io/secret) - Popular and highly featured explorer for many chains in the Cosmos ecosystem
  - [Ping Explorer](https://ping.pub/secret) - Supports dozens of Cosmos chains and includes a basic web wallet, by [ping.pub]
  - [Secret Contracts](http://secret-contracts.com/) - Contract code verifier and explorer by [3Dgiro](https://3dgiro.com/)
- **Analytics**:
  - [Secret Analytics](https://secretanalytics.xyz/) - Analytics data collected about the Network, Bridges, and SecretSwap
  - [SmartStake Secret Analytics](https://secret.smartstake.io/) - Validator stats by [SmartStake](https://smartstake.io/)
- **Bridges**:
  - [Secret Bridges](https://bridge.scrt.network/) - Turn assets from other chains into SNIP-20 privacy tokens
    - Support for ETH and ERC-20 tokens
      - Integrated to [keyTango](https://app.keytango.io/invest) easy DeFi investment interface
    - Support for BNB and BEP-20 tokens
    - Also supported in [Citadel One](https://citadel.one/) wallet
  - [Secret Monero Bridge](https://ipfs.io/ipfs/QmNRrLDhKGZCSXAZcPU1cBTaLouhWnTi5kfWUzJB4nJbzA) - Turn your XMR into the SNIP-20 sXMR
  - [IBC bridges](https://wrap.scrt.network/) - Transfer tokens across IBC networks and wrap them in SNIP-20 tokens
    - Alternate UI for [IBC bridging](https://app.sienna.network/wrap/ibc) and [SNIP-20 wrapping](https://app.sienna.network/wrap) of IBC tokens, by [Sienna](https://sienna.network/)
  - [Shinobi Protocol](https://sbtc.ninja/) - Trustless bridge to Bitcoin. Turn your BTC into the SNIP-20 sBTC
- **Stablecoins**
  - **Silk** - Algorithmic stablecoin with transactional privacy by default

### Grants/Funding

- Funding amount:

  - as high as multi 6 figs (few hundred thousand), depending on the complexity and value to the network
  - average grant around 4-5 figs (thousands to tens of thousands).
  - grants may be split into smaller milestones and receive funding accordingly on a per-milestone basis

- Requirements:

  - all code must be open source unless there's a good reason (include in proposal)
  - license to be used must be included

- Who they're looking for:

  - individual developers
  - new and existing companies and projects
  - community members or established teams with a proven track record
  - prior work on secret network or experience in deploying eth/other blockchain apps is a big plus
  - encouraged to have a path for commercial sustainability (token or fee model)

- Example recommended projects (non-exhaustive):

  - **Dapps**:

    - DEFI:
      1.  Variable interest lending products: implementations of projects such as Compound or Aave
      2.  Algorithmic stable coin projects: Maker-type implementations
      3.  Fixed income products: fixed interest lending / borrowing products with insurance / liquidity pool to guarantee fixed payments
      4.  Advanced AMM / CFMM DEXs optimized for low slippage trading (like Curve) or multiple pools (like Balancer) to create decentralized index funds, encouraged to launch protocol with indices like Privacy Index, Data economy index etc.
      5.  Dark pools (private orderbook exchange) for privacy preserving trading: Dark Pools secret contract manages the encrypted order book in its state and can run multiple order matching methods such as Market / Limit / Stop-Loss orders, can build on SecretAuction repo, which uses a single sided orderbook.
    - Vaults:
      1.  Ocean Data Token integration: integrate Ocean Data Tokens to SecretVaults to allow trustless access to data token content
      2.  Decentralized Substack: build a decentralized content (audio, blog) monetization tool for content stored on IPFS or another decentralized storage platforms (click [here](https://blog.scrt.network/secret-vaults-programmable-access-control/) for more information)
    - Data Marketplaces:
      1.  Trustless private computations for Ocean Protocol data marketplace
      2.  Decentralized and privacy preserving machine learning use-cases (image recognition etc.)
    - Decentralized governance/DAOs:
      1.  SecretFund: build a DAO funded by block rewards of delegators participating in the DAO, delegators receive governance tokens proportional to their contribution, governance tokens determine how the funds in SecretFund are managed
      2.  SecretLaunchPad: create a crowdfunding mechanism like Polkastarter, where Secret Network participant can support launch of products built on Secret Network or Ethereum (using the bridge), can allow anonymous investments using SNIP-20s

  - **Ecosystem**:

    - Interoperability (Bridges):
      - BTC bridge
    - Oracles:
      1.  Secret Oracles: build TLS connection from validator enclaves to certain APIs to create private data feed for secret contracts (i.e. Binance and other exchange balances for decentralized credit scoring / leverage)
      2.  Public API oracles: allow Secret Network validators (or nodes) to query public APIs for on-chain secret contract based oracle, validators would reach on-chain consensus on inputs
    - Developer tools and improvements
      1.  Tooling for one-click-run-and-deploy of contracts: Remix for Secret Contracts
      2.  Create a library for running Secret Contract integration tests (like how Truffle uses Mocha/JS for Solidity)

  - **Network improvements**:
    - ML Library that can run on-chain (requires deterministic floats or fixed-point support)

### Roadmap

View [here](https://ik.imagekit.io/secretnetwork/images/Roadmap_may2022_569bd2c640_xAzAmMlkm.pdf)

### Market Opportunity

- Potential competitor to existing aggregator button swap (no charting, garbage UI) note: total DEX daily volume is US$4.3M
- Potential competitor to analytics tool Secret Analytics (~~pretty bad~~ garbage performance, no API) note: not sure how profitable it is considering how small ecosystem is (26M liquidity for both DEX)

### Public Infrastructure

- Public/Community API:
  - [https://api.scrt.network](https://api.scrt.network/) (LCD - Light Client Daemon)
  - [https://api.scrt.network:26657](https://api.scrt.network:26657/) (RPC - Remote Procedure Call)

### Considerations to be Node Operator

- Capital: In order to become an **active** validator, you must have more stake than the [bottom validator](https://www.mintscan.io/secret/validators) (current bottom validator: 19,158 self-bonded + delegated)
- Requirements:
  - Ubuntu/Debian host (with ZFS or LVM to be able to add more storage easily)
  - A public IP address
  - Open ports `TCP 26656 & 26657` _Note: If you're behind a router or firewall then you'll need to port forward on the network device._
  - Reading [Tendermint: Running in production](https://docs.tendermint.com/v0.34/tendermint-core/running-in-production.html)
  - RPC address of an already active node. You can use any node that exposes RPC services.
  - Refer to [Intel Processor Specifications](https://ark.intel.com/content/www/us/en/ark.html#@Processors) if you're unsure if your processor supports SGX
- Minimum H/W requirements:
  - 16GB RAM
  - 256GB SDD
  - 1 dedicated core of any Intel Skylake processor (Intel® 6th generation) or better (Xeon gen3 (Ice Lake) NOT supported)
  - Motherboard with support for SGX in the BIOS
- Recommended H/W requirements:
  - 32GB RAM
  - 512GB SSD
  - 2 dedicated cores of any Intel Skylake processor (Intel® 6th generation) or better (Xeon gen3 (Ice Lake) NOT supported)
  - Motherboard with support for SGX in the BIOS
- Docs for setting up [validator](https://docs.scrt.network/node-guides/join-validator-mainnet.html), [full node](https://docs.scrt.network/node-guides/run-full-node-mainnet.html), [LCD server](https://docs.scrt.network/node-guides/lcd-server-example.html)

## References

- [Secret Network grant program](https://scrt.network/blog/announcing-secret-network-grant-program)
- [Collection of resources/apps/tooling on Secret Network](https://github.com/SecretFoundation/awesome-secret)
- [Secret Network Official docs](https://docs.scrt.network/)
