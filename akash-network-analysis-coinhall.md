# Akash Network

## Main Considerations

1. Bond breakdown -- Unable to determine. Explorers dont seem to show breakdown, discord does not seem to indicate that there are any foundation helping validators stay in the active set, most of them got in early BUT have very little self-bonded AKT stake so may have to ask POC if foundation contributes. (note: no minimum self-bonding amt)
2. Staking costs:
   - Minimum: 41,990 AKT delegated, ~16.8K USD @ 0.4 USD/AKT
   - Median (middle guy): 804,595 AKT delegated, ~322K @ 0.4 USD/AKT
3. Staking profits (10% comission of 32% APR):
   - Minimum: 537 USD
   - Median: 10.3K USD
4. Validator POC -- discord @ Alani I Akash#4366
5. **Dealbreaker** -- Last validator reward is ~~garbage~~ very low, median validator rewards are decent though(?) but will depend on whether foundation is willing to contribute (must enquire from POC).
6. **Recommendation** -- After taking AKT tokenomics into consideration I wouldn't really recommend but may be somewhat viable short term if foundation is willing to contribute + really desperate.

## Get to know (TLDR/One-liners)

Akash is an [**open source**](https://github.com/ovrclk/akash) Cloud platform that lets you quickly deploy a Docker container to the Cloud provider of your choice for less than the cost of AWS, right from the [**command-line**](https://docs.akash.network/guides/cli).

- Define your Docker image, CPU, Memory, and Storage in a **deploy.yaml** file.
- Set your price, receive bids from providers in seconds, and select the lowest price.
- Deploy your application without having to set up, configure, or manage servers.
- Scale your application from a single container to hundreds of deployments.

The cost of hosting your application using Akash is about one-third the cost of Amazon AWS, Google Cloud Platform (GCP), and Microsoft Azure. You can check the prices live using the [Akashlytics.com price comparison tool](https://akashlytics.com/price-compare).

## Hosting on Akash

The lifecycle of a typical application deployment is as follows:

1. The tenant describes their desired deployment in [SDL], called a [deployment](/other-resources/marketplace#deployment).
2. The tenant submits that definition to the blockchain.
3. Their submission generates an [order](/other-resources/marketplace#order) on the marketplace.
4. Providers that would like to fulfill that order [bid](/other-resources/marketplace#bid) on it.
5. After some period of time, a winning [bid](/other-resources/marketplace#bid) for the [order](/other-resources/marketplace#order) is chosen, and a [lease](/other-resources/marketplace#lease) is created.

6. Once a [lease](/other-resources/marketplace#lease) has been created, the tenant submits a [manifest](/intro-to-akash/stack-definition-language) to the provider.
7. The provider executes workloads as instructed by the [manifest](/intro-to-akash/stack-definition-language).
8. The workload is running - if it is a web application it can be visited
9. The provider or tenant eventually closes the [lease](/other-resources/marketplace#lease), shutting down the workload.

Docs for steps to hosting apps on Akash can be found [here](https://docs.akash.network/guides)

### Grants/Funding

All grants are paid in $AKT to the developer’s Akash account address. To prevent fraudulent activity, the account is linked to the developer’s accounts on Discourse, GitHub, and Discord. This award is a non-dilutive donation, and Akash’s treasury and community do not gain equity in projects with the grants. The grants must be used to deploy and run applications on Akash Network.

- Funding tiers:

  - **$100 Initiate Grant**: The purpose of this funding is to support a large number of developers in running their first apps on Akash. If a developer sends these tokens to an exchange, they will be ineligible for future funding, as well as the next tier of funding.
  - **$1,000 Seed Grant**: The Seed Grant requires a developer to create a detailed proposal for their project and share this with the community for public comment and questions. Developers are expected to open source their project for the community, publish a detailed guide, and answer questions from the community.
  - **$10,000 Incubator Grant**: The Incubator Grant is awarded only if progress is made by the developer to meet the milestones in their proposal. The developers may be asked to present their project in a recorded livestream and answer questions live from the community.
  - **$100,000 Accelerator Grant:** The Accelerator Grant is only awarded to developers that have consistently met their milestones, demonstrated improvements, and shown a willingness to remain open source and collaborate with the Akash community.

- Milestones:

  - A typical project should have 3-4 milestones and be completed within 2-4 months. Projects that complete their milestones will present to investors, advisors, and developers in the community on a scheduled Demo Day.

- Requirements:
  - Projects that apply for grants from the developer program will need to outline how their project will contribute and add value to the Akash ecosystem.
- Example recommended projects (non-exhaustive):

  - Developer tooling for Akash including SDKs and APIs.
  - Open-source developer tools (Homebrew).
  - Creator platforms (CMS, podcasting, blogging, forums, GitLab).
  - Decentralized web services (Handshake, DNS, OpenRegistry).
  - Backend as a service (Hasura on Akash).
  - Platform as a service (Heroku on Akash).
  - Open-source communications (Chat, Email).
  - Desktop deployment interface.
  - Hosted deployment interface with wallet integration.
  - App Store interface (OpenChannel on Akash).
  - Persistent storage integrations (Sia, Skynet, Filebase, Arweave, Filecoin, Storj, Coldstack).

- Free hosting for VCs that partner with Akash Network
  - Akash will be partnering with other startup funds to provide free hosting on Akash. If you are a venture capital firm, accelerator, incubator, or other startup-enabling organization interested in providing Akash developer grants to your startups, contact [partners@akash.network](mailto:partners@akash.network).

### Roadmap

View [here](https://akash.network/roadmap)

### Market Opportunity

- Potentially host infra on Akash network to save money
- Not much market opportunity since it's not an L1 (works similar to chainlink)

### Public Infrastructure

- Akash maintained RPC pool:
  - http://akash.c29r3.xyz:80/rpc
- Trusted Community RPC Nodes:
  - https://rpc.akash.forbole.com:443
  - http://akash-sentry01.skynetvalidators.com:26657
  - https://rpc.akash.smartnodes.one:443
  - full up-to-date list [here](https://raw.githubusercontent.com/ovrclk/net/master/mainnet/rpc-nodes.txt)

### Considerations to be Node Operator

- Capital: In order to become an **active** validator, you must be within the active set (top 100) + have more stake than the [last active validator](https://www.mintscan.io/akash/validators) (current bottom validator: 8,951 self-bonded + delegated)
- Minimum H/W requirements:
  - CPU - 4 Core
  - Memory - 8 GB
  - Disk - SSD
- Recommended H/W requirements:
  - CPU - 8 Core
  - Memory - 16GB
  - Disk - NVMe
- Docs for setting up [validator](https://docs.akash.network/validating/validator), [full node](https://docs.akash.network/akash-nodes/run-an-akash-node)

## References

- [Akash Network grant program](https://akash.network/blog/akash-offers-up-to-100-000-in-grants-through-new-developer-grant-program)
- [Collection of example app deployments on Akash](https://github.com/ovrclk/awesome-akash)
- [Akash Network Official docs](https://docs.akash.network/)
