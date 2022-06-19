# THORChain

## Main Considerations
1. Bond breakdown -- Unable to determine. Explorers dont seem to show breakdown, discord does not seem to indicate that there are any foundation helping validators stay in the active set, most of them got in early when rune was cheap(er) and have a large portion of delegations.
2. Last and median reward -- 44.00505, 192.64433 RUNE (@ $4/RUNE) -> 176 - 768 USD
3. Validator POC -- Not really, community asks the other validators/thornode devs,
4. **Dealbreaker** -- Median/Last validator reward is ~~garbage~~ very low. The requirement of a full node needing to run a node in every other chain appears to be true, just to observe what transactions are taking place there.
5. **Recommendation** -- Does not seem at all worth considering the rewards alone, dealbreaker just makes it worse imo.

---

## Get to know (TLDR/One-liners)
- Enables the exchange of any(\*) native L1 assets by acting as a vault manager -- this means that there is no need to wrap assets. It uses the LPs to perform swaps of the specified assets.
- "Like Uniswap, but multi-chain".

## What's in their ecosystem?
- Exchanges -- [THORSwap](https://thorswap.finance/)
- Analytics -- [THORChain Vision](https://thorchain.vision/console) -- Key stats and figures related to THORChain ops (data gets populated **really** slowly), Telegram bots for network/monitoring info
- Infrastructure -- [Viewblock Dashboard](https://dash.viewblock.io/d/thorchain) -- Gives info regarding the network, pools, and basic stats (daily volume, staked amount, APRs)
- Explorers -- [THORChain Dashboard](https://thorchain.net/dashboard), [Viewblock](https://viewblock.io/thorchain).
- Dev -- [Dev docs](https://dev.thorchain.org/thorchain-dev/) 
    - [cross-chain aggregation](https://dev.thorchain.org/thorchain-dev/aggregators), [midgard](https://gitlab.com/thorchain/midgard), [xchainjs](https://xchainjs.org/)
    - [THORChain RPC](https://dev.thorchain.org/thorchain-dev/wallets/connecting-to-thorchain) (Midgard - time-series info, THORNode - app-specific)

### Grants/Funding
- [Treasury/Community](https://thorchain.org/ecosystem/project-funding#treasury)

### Market Opportunity
- Charting -- Crosschain has the issue of not being able to chart in one place and THORChain. Current charting option provided by THORSwap only reflects the price of a singular asset (BTC/LUNA shows the BTC price and pool)
    - Currently only good use case for their ecosystem are DEXes, and no other types of dapps exist. Considering the nature of the chain, DaaS might be something useful so the other chain (native token) can use this data for their dapps(?)

## Incentives
- Yield generation for LPs
- Easy way to swap cross-chain
- Node Operators

### LP vs Node Operator
- Read [here](https://erikvoorhees.medium.com/an-introduction-to-thorchain-for-bitcoiners-3f621bf0028e#:~:text=THORnodes%20are%20strongly,and%20toward%20THORnodes).

### Considerations to be Node Operator
- Capital: 500K - 1M RUNE bonded 
    - Min: 450k RUNE, Avg: 740k RUNE Max: 997k RUNE for [active nodes](https://thorchain.net/nodes) at the time of writing
    - There exists 2 standby nodes with >500k
    - [Churning](https://docs.thorchain.org/thornodes/overview#churning) happens every 3 days where some nodes maybe be roated out of their status (Active -> Standby, vice versa)
    - Cannot withdraw bond when Active, wait until churned out
- H/W Requirements: Docs did not indicate the specifics and has recommended deployment to be on (presumably) dynamic resource alloaction managed services(?)
    - [Official tweet](https://twitter.com/THORChain/status/1212262485299888128) from 2020 seems to suggest 16-64 GB RAM, 1-2TB storage Linux VPS, likely similar recommendation to Sifchain's HW requirements (see below).
    - **Note**: "Full nodes - for every chain that is supported by the network, each THORNode operator will run their own full node of each chain (Bitcoin, Ethereum, Binance, etc)."


## References
- [Binance Academy](https://academy.binance.com/en/articles/what-is-thorchain-rune)
- [THORChain's docs](https://docs.thorchain.org/ecosystem)
- [THORChain's Node Operators doc](https://thorchain.org/community-roles/node-operators#docs)
- [GrassRoots Crypto - THORChain - Node Operator 101](https://www.youtube.com/watch?v=XXYXNAolPEU) 

