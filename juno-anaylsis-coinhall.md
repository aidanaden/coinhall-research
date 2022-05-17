# Junø

## Main Considerations

1. Bond breakdown -- 135th - 1 self-bond, remaing 1.3k delegated; 125th - 460 self-bond, 31K delegated
2. Staking profits -- 111.24% APR w/ 10% commission -> (120th: 337.82 JUNO; 60th: 970.42 JUNO) monthly
3. Validator POC -- Core team
4. **Dealbreakers** -- Kind of minor but Juno has aggressively been recruiting devs onto their chain and enticing them (and us) with grants see prop 23 [via keplr](https://wallet.keplr.app/#/juno/governance?detailId=23) and recent ~~FUD~~ *issue* regarding JUNO whale [prop 16](https://wallet.keplr.app/#/juno/governance?detailId=23)
5. **Recommendation** -- I overall think it's a good move seeing as how prop 23 is going + IBC chain.

## Get to know (TLDR/One-liners)

- Junø is a PoS network designed to be *the* smart contract chain of the IBC.

## What's in their ecosystem

- Charting: [JOEDAO](https://joedao.io/charts/JUNO/)
- DEX: [JunoSwap](https://junoswap.com/)
- DAO: [DAODAO](https://daodao.zone/), [RAW](https://www.rawdao.zone/)
- Explorer/Dashboard: [MintScan](https://www.mintscan.io/juno)
- NFT: [Passage3D Market](https://market.passage3d.com/)
- Other: [(de)NS](https://dens.sh/)
- Tooling: [JunoTools](https://juno.tools/)
  - API:
    - Mainnet:
      - Itastakers: [RPC](https://rpc-juno.itastakers.com/), [LCD](https://lcd-juno.itastakers.com/)
      - Omniflix: [RPC](https://rpc.juno.omniflix.co/), [LCD](https://api.juno.omniflix.co/)
    - Testnet:
      - JunoNetwork: [RPC](https://rpc.uni.junonetwork.io/), [LCD](https://api.uni.junonetwork.io/)
    - Websock details ([refer to me](https://docs.junonetwork.io/validators/relayers/hermes#configuring-hermes) -- we need our own validator first)

## Grants/Funding

- [Juno Grants](https://www.junonetwork.io/grants/)
- [Foundation-assisted delegation](https://docs.junonetwork.io/validators/official-delegations-handbook)
  - No need to request for delegations, core team will screen the **entire** set 2 weeks prior to a new delegation round. 
    - Delegation rounds are announced occurs every 6 months (check Discord/Telegram), next round on 1st July, evaluation occurs 2 weeks prior -- mid-June).
  - Prioritised based on a score in a delegation [criteria](https://docs.junonetwork.io/validators/official-delegations-handbook#official-delegation-criteria), giving high prio to development on chain (dapp/contract/tooling), active participation, and development of main codebase (those are the highest few in the list).
  - `juno190g5j8aszqhvtg7cprmev8xcxs6csra7xnk3n3`[*](https://www.mintscan.io/juno/account/juno190g5j8aszqhvtg7cprmev8xcxs6csra7xnk3n3) seems to be the foundation's wallet.
    - Sampled from the top 125 validators, (1 to 15, followed by intervals of 10). Stated address has the 7th highest frequency at 16 and has a high value (>12M JUNO).
    - Data folder: `juno-vals`[*](https://github.com/aidanaden/coinhall-research/tree/master/juno-vals) to see the raw and filtered data.

## Market Opportunity

- Charting is already kind of available on the chain, via [JOEDAO](https://joedao.io/charts/JUNO/), but I think we can do better.

I believe what we've planned for LUNA can also be ported over since its part of IBC too.

## Considerations to be a Validator

- Capital:
  - Recently, active set increased from 125 to 135 [commonwealth](https://commonwealth.im/juno/discussion/4713-increase-validator-set?comment=19836), [prop 22 (keplr link)](https://wallet.keplr.app/#/juno/governance?detailId=22). Because of this, 135th spot -- 1.3K JUNO, 125th spot -- 31K JUNO.

- **Minimum** H/W requirements:
  - 4 (v)CPU
  - 32GB RAM
  - 1TB storage (SSD/NVME)

> I *think* the safest play would be like sifchain's recommended specs of 8cpu, 32gb ram, 2tb ssd/nvme.
