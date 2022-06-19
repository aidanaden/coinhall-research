# Sifchain

## Main Considerations
1. Bond breakdown -- Medium article for the "Sifchain Validator Delegation Program" states 10000 ROWAN, top validator only has 100 self-bonded, lowest only has 1, the rest are delegated.
2. Last and median reward -- 5308.8, 133333.3 ROWAN (@ $0.08/ROWAN, 10% commission) -> 42.47 - 1066.66 USD, rates gotten from stakingrewards' validator APR which seems high.
3. Validator POC -- None that I've seen publicly, but they do have a delegator program.
4. **Recommendation** -- If we have enough self-bonded, it appears to be a low-hanging fruit to generate income considering that the median reward is ~10k USD at current prices.

---

## Get to know (TLDR/One-liners)
- The ""Omnichain"" -- Primarily a cross-chain DEX, connecting the IBC to ETH.
    - Personally knew of them before Gravity Bridge/Wormhole was operational.
    - Might be related to THORChain in more ways than what it operates as? (Sif and Thor are related, might be irrelevant)
- Falls short compared to THORChain since it's only limited to IBC <-> ETH while THORChain allows native asset swaps to BTC, DOT, LTC on top of ETH.


## What's in their ecosystem?
- Functions as a cross-chain DEX at the moment of writing.
- [Dashboard](https://bit.ly/3MzkoUf) with the key metrics -- TVL, ROWAN Price.
- [SifChain's sketchy API](https://data.sifchain.finance/)
- [SifChain RPC](https://rpc.sifchain.finance/)

### Grants/Funding
- None, apart from their [Validator Delegation Program](https://medium.com/sifchain-finance/sifchains-validator-delegation-program-fbf8907c557a)

### Market Opportunity
- [Roadmap](https://docs.sifchain.finance/project/roadmap) indicates Margin Trading in Q3 2022, Liquid Staking in Q4, Limit Order in 2023
- Similar to THORChain, it lacks charting in its swap interface.
- Limit order by 2023 seems a little far, and theres no details about how it would work, (IBC only or crosschain limit orders?).

## Incentives
- LP, pretty good APRs.
- Validator

### Considerations to be Node Operator
- Capital: 6.9k (next lowest 36k) to 52M ROWAN bonded
    - Active set consists of top 100 nodes by total stake, inclusive of validator's and their delegators. 
    - Validator set is refreshed on every block as opposed to THOR's 3 days for churning.
    - [Keplr's staking page](https://wallet.keplr.app/#/sifchain/stake) seems to indicate that its the top 111
- [H/W Requirements](https://github.com/Sifchain/sifchain-validators/blob/master/docs/nodes/setup.md):
    - 4 vCPU (8 vCPU Recommended).
    - 16GB RAM (32GB Recommended).
    - 1TB NVMe (2TB+ Recommended if running an archive node).
        - Types of nodes - `archive` does not prune, other 2 are `default prune` and `full prune`, difference is storage growth/month (est. 50, 10, 20 GB respectively).

## References
- [3rd party SifChain Dashboard](https://bit.ly/3MzkoUf)
- [Sifchain Roadmap](https://docs.sifchain.finance/project/roadmap)

