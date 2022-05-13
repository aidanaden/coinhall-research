# Tezos

## Main Considerations

1. Bond breakdown -- Unable to determine. Explorers dont show breakdown AND doesn't show APR either (had to find from [stakingrewards](https://www.stakingrewards.com/earn/tezos/)).
2. Staking costs:
   - Minimum: 12.2K XTZ staked, ~23K USD @ 1.9 USD/XTZ
   - Median (middle guy): 235K XTZ delegated, ~445K @ 1.9 USD/XTZ
3. Staking profits (5% commission of 4.5% APR):
   - Minimum: 51 USD
   - Median: 1K USD
4. Validator POC -- can check #baking-node-support in their [discord](https://discord.com/invite/udZwhQn)
5. **Dealbreaker** -- Last validator reward is ~~garbage~~ very low, TVL of DEXes are also really really low.
6. **Recommendation** -- No evidence of foundation delegating to active bakers + 5-6 fig TVL + ultra low baking APR so cannot recommend launching on tezos in short-term

## Get to know (TLDR/One-liners)

Tezos is an open-source, community-governed, blockchain network capable of running complex smart contracts for asset settlement and decentralized applications (dApps) which benefit from censorship resistance, decentralization, and user-control.

Runs on PoS, uses "formal verification" which allows developers to mathematically prove that code performs correctly, according to its formal specification or certain properties.

Well-suited to financial smart contracts representing significant real-world value (e.g. tokenized assets, loans, etc.), which require guarantees that funds will not be lost or frozen due to bugs in the code.

## What's in their ecosystem?

- **Exchanges**:

  - [FlameDEX](https://app.flamedex.io/) - DEX on Tezos
  - [Plenty DEFI](https://www.plentydefi.com/farms) - DEX on Tezos (5-6 fig TVL)
  - [Spicy Swap](https://spicyswap.xyz/#/) - DEX on Tezos (200K TVL)
  - [Vortex Network](https://app.vortex.network/) - DEX on Tezos (unreliable, loads forever)
  - [QuipuSwap](https://quipuswap.com/farming) - DEX on Tezos (380K TVL)

- **Block explorers**:

  - [TzKT](https://tzkt.io/) - Block explorer with [API access](https://api.tzkt.io/)
  - [Better Call Dev](https://better-call.dev/) - Block explorer with [API access](https://better-call.dev/docs)
  - [TezBlock](https://tezblock.io/) - Very well designed block explorer, no API access

- **Analytics**:
  - [TzStats](https://tzstats.com/) - In-depth on-chain analytics including validator data, exchange volumes, geography data, [API access](https://tzstats.com/docs/api), etc
  - [TzFlow](https://tzflow.com/) - Mempool data analytics

### Grants/Funding

Tezos grants don't state exact funding amounts, but do state they prioritize DEFI apps and dev tooling/infra apps (according to twitter they're quite generous)

### Market Opportunity

- Potentially create a DEX aggregator (very very low volumes/TVL tho)
- Difficult to compete on the charting/API front (TzStats is very good)

### Public Infrastructure

- TzStats maintained RPC pool:
  - https://rpc.tzstats.com
    - https://rpc.edo.tzstats.com
    - https://rpc.florence.tzstats.com

List of community nodes [here](https://tezostaquito.io/docs/rpc_nodes/)

### Considerations to be Node Operator

- Capital: In order to become an **active** validator, you must have 8K tezos at MINIMUM (15K USD @ 1.88 USD/XTZ)
- Recommended H/W requirements:
  - CPU - 4 Core
  - Memory - 8+ GB
  - Disk - SSD+
  - Hardware wallet
- Docs for setting up [validator](https://wiki.tezosagora.org/use/baking/setting-up-a-secure-baker), [full node](https://opentezos.com/deploy-a-node)

## References

- [Tezos foundation grant program](https://tezos.foundation/grants/)
- [Collection of Tezos resources](http://104.248.0.185/lib/awesome-tezos)
- [Tezos Developer docs](https://opentezos.com/)
