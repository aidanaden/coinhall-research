# Algorand

## Main Considerations

1. Bond breakdown -- N.A.
2. Staking costs: N.A.
3. Staking profits: None (participation rewards of 2.68%, governance rewards of 7.6% from https://www.stakingrewards.com/earn/algorand/)
4. Validator POC -- N.A. (since no profit from running validator node)
5. **Dealbreaker** -- No validator rewards, strong competition from existing charting analyics sites
6. **Recommendation** -- Can consider launching a DEX aggregator competitor with charting included (current DEX aggregator isn't good, high TVLs across the board, decent chance of getting grant since defi is a vertical the algorand foundation are interested in funding)

## Get to know (TLDR/One-liners)

Tezos is an open-source, community-governed, blockchain network capable of running complex smart contracts for asset settlement and decentralized applications (dApps) which benefit from censorship resistance, decentralization, and user-control.

- uses PoS
- runs on rust, js, go, python and more sdks
- 0 validator rewards
- many dexes, charting, apis, etc already exists, grant amounts are undisclosed

## What's in their ecosystem?

Note: vast majority of their DEXes and analytics tools are very well designed

- **Exchanges**:

  - [DFYN](https://exchange.dfyn.network/) - DEX (9M liquidity, 2M 24H volume)
  - [AlgoFI](https://app.algofi.org/) - DEX (14.5M TVL, 3.6M 24H volume, 31.3M 7D volume)
  - [Tinyman](https://app.tinyman.org/) - Largest DEX on algorand (21M liquidity, 3.6M 24H volume)
  - [AlgoDEX](https://app.algodex.com/trade/31566704) - DEX using order-book (order book stored on-chain, 106K 7D volume)
  - [Pact](https://app.pact.fi/) - DEX (14.8M TVL, 1.2M 24H volume)
  - [Alammex](https://app.alammex.com/) - DEX aggregator (no charts, no stats, displays best exchange(s) used for swap)

- **Block explorers**:

  - [AlgoExplorer](https://algoexplorer.io/) - Block explorer
  - [AlgoSearch](https://algosearch.io/) - Open-source block explorer (out-of-sync)
  - [AlgoScan](https://algoscan.app/) - Block explorer, no API access
  - [GoalSeeker](https://goalseeker.purestake.io/algorand/mainnet) - Block explorer run by PureStake

- **Analytics**:
  - [TinyChart](https://tinychart.org/) - Real-time price charting of all algorand tokens, very well designed, includes ads (**strong coinhall competitor**)
  - [AlgoChart](https://algocharts.net/) - Real-time price charting of algorand tokens, ugly version of TinyChart
  - [Algorand Metrics](https://metrics.algorand.org/) - Dashboard for algorand chain metrics run by Algorand foundation

### Grants/Funding

Undisclosed amounts, however they do provide "referral-based" grants to defi apps and have funded various dexes, aiming to fund programs by vertical (defi, gaming, nft) contact them [here](https://algorand.foundation/contact)

for liquidity support (to help boostrap liquidity for small defi dapps) email: contact@algorand.foundation

### Market Opportunity

- Potentially create a DEX aggregator to compete with existing DEX aggregator (existing aggregator doesn't include charting, APIs, etc)
- Difficult to compete on the charting front (TinyChart is literally Coinhall on algorand without swaps)

### Public Infrastructure

- Official Algorand API docs [here](https://developer.algorand.org/docs/rest-apis/restendpoints/)
- Free AlgoNode API [here](https://algonode.io/api/)

### Considerations to be Node Operator

No rewards currently for running validators, all addresses with at least 0.1 algo will receive "participation rewards".

Will begin rewarding validators with "governance rewards" in Q2 or Q3 (governor is anyone that stakes for 3 months or so)

- Capital: None - validators are not currently rewarded for mining blocks
- Recommended H/W requirements:
  - CPU - 8 core
  - Memory - 16 GB
  - Disk - 500 GB NVMe SSD
  - Internet - 1 gbps
- Docs for setting up [indexer](https://developer.algorand.org/docs/run-a-node/setup/indexer/), [full node](https://developer.algorand.org/docs/run-a-node/setup/install/)

## References

- [Algorand foundation grant program](https://algorand.foundation/grants-program)
- [Collection of Algorand resources](https://github.com/aorumbayev/awesome-algorand)
- [Algorand Developer docs](https://developer.algorand.org/docs/)
