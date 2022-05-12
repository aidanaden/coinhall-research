# Stacks

## Main Considerations

1. Average miner usually loses money, only top miners are profitable (willing to mine for long durations) e.g. top miner total cost (20 BTC, 560K USD @ 28K/BTC) total reward (1,769,000 STX, 884K USD @ 0.5/STX) **Profit**: 320K/57%
2. **Dealbreaker** -- 10min block times (follows BTC blocks), scaling solutions MVP rolls out EARLIEST June (99% will delay) + miners almost always lose money (that's why there's usually only 5-10 miners at any 1 time and who tf would give btc for an altcoin............)
3. **Recommendation** -- Does not seem at all worth considering the small market size and small TVL, will survive the bear market but highly difficult to be profitable anytime soon

## Get to know (TLDR/One-liners)

Stacks is an open-source blockchain network that leverages the security and capital of Bitcoin for decentralized apps and smart contracts.

Essentially, consensus mechanism (POX) relies on bitcoin chain where miners win blocks by paying with bitcoin, probability of winning block is weighted according to amount paid (state of chain is hashed and inserted into BTC, [whitepaper](https://community.stacks.org/pox) and [docs](https://docs.stacks.co/understand-stacks/overview))

## What's in their ecosystem?

- **Exchanges**:
  - [Alex](https://app.alexlab.co/swap) - Top DEX, includes launchpad (15M TVL, 2.4M 24H volume)
  - [Arkadiko](https://app.arkadiko.finance/) - DEX, creator of USDA stablecoin (7M TVL, 500K 24H volume)
  - [LN Swap](https://www.lnswap.org/) - Native swaps between stacks and btc, no stats provided
  - [Stackswap](https://app.stackswap.org/v2/) - DEX, includes launchpad (1.5M TVL, no volume provided)
- **Block explorers**:
  - [Stacks explorer](https://explorer.stacks.co/?chain=mainnet) - Main explorer, run by foundation
  - [Syvita explorer](https://explorer.syvita.org/) - Popular community explorer, run by community group called syvita guild, run by some 15 yo bitcoiner
  - [Onstacks explorer](https://app.onstacks.com/explorer) - Explorer run by [Onstacks](https://www.onstacks.com/), company focused on building miner/dev tools
- **Analytics**:
  - [Onstacks Analytics](https://app.onstacks.com/) - Mining analytics data
  - [Stacking Analytics](https://stacking.club) - Stacking stats (basic)
  - [StacksOnChain](https://stacksonchain.com/) - Analytics for overall ecosystem, [api docs](https://xchains-ai.gitbook.io/stacks-on-chain-documentation/)
- **Bridges**:
  - [StacksBridge](https://stacksbridge.com/) - Bridge for eth <> stx nfts (only 1 project supported rn)
  - Allbridge - Launches [Q2 2022](https://cointelegraph.com/news/allbridge-to-become-the-first-token-bridge-for-the-stacks-token?utm_campaign=Building%20a%20better%20internet%20on%20Bitcoin&utm_medium=email&utm_source=Revue%20newsletter)
- **Stablecoins**
  - **xUSD** - Wrapped version of USDC on stacks
  - **USDA** - Overcollateralized "stablecoin" (has been 0.6-0.8 for literal months)

### Grants/Funding

- Funding amount:
  - up to 50K (no valuation cap, includes 3-month acceleration program)
  - up to 100K (for open source contribution or special consideration for accelerator companies)
  - more info [here](https://stacks.org/grants) and [here](https://stacks.ac/#program)

### Market Opportunity

- Potential competitor to existing charting/stats site [Novum Insights](https://stacks.novuminsights.com/) not sure how profitable it can be tho, ecosystem is really small
- Potential competitor to API provider StacksOnchain (their API expects SQL queries), can offer to be paid via delegated stacking)
- Trust Machines (new company launched by creator of Stacks) just raised 150M USD to build applications on Stacks, might end up competing w them in a some area (they prolly building a DEX that allows for native BTC stuff)

### Public Infrastructure

- Official stacks api maintained by Hiro:
  - [https://stacks-node-api.mainnet.stacks.co/extended/v1/](https://stacks-node-api.mainnet.stacks.co/extended/v1/) - [Docs](https://docs.hiro.so/api)

### Considerations to be a Miner

- Capital: Since mining requires burning BTC to receive 1000 stacks per block,
- Requirements:
  - No minimum hardware requirements (u can run on raspberry pi)
  - [Docker](https://docs.docker.com/get-docker/), [curl](https://curl.se/download.html), [jq](https://stedolan.github.io/jq/download/)
- Docs for setting up [miner](https://docs.stacks.co/nodes-and-miners/miner-mainnet), [full node](https://docs.stacks.co/nodes-and-miners/running-mainnet-node), [api node](https://docs.hiro.so/get-started/running-api-node)

## References

- [Stacks grant program](https://stacks.org/grants)
- [Stacks accelerator program](https://stacks.ac/)
- [Stacks official docs](https://docs.scrt.network/)
- [Stacks developer docs](https://docs.hiro.so/intro)
