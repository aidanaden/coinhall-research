# Proposed new API design reference for Multi-Chain Coinhall

## Pairs API (`/dashboard` and `/pairs`)

### Current

Returns ALL pairs from ALL chains (terra classic and terra v2, ~1200-1300 total including unverified)

- Method: `GET`
- URL: `/api/v1/charts/terra/pairs`

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  [
    // ...
    {
      terra1uenpalqlmfaf4efgtqsvzpa3gh898d9h2a232g: {
        timestamp: "2021-09-05T04:09:27.479Z",
        asset0: {},
        asset1: {},
        type: "xyk",
        defaultBase: "asset1",
        dex: "Terraswap",
        unofficial: true,
      },
    },
    // ...
  ];
  ```

### Proposed

Returns pairs data based on query parameters sorted by mcap desc (similar to gecko) including usd and quote asset (native) price:

- Method: `GET`
- URL: `/api/v2/pairs` OR `/api/v2/pairs/:pair_address`
- URL Parameters:
  - `pair_address`: pair address of pair to get data for
- Query Parameters:
  - `chains`: optional, most useful for improving performance if there's 20+ chains, defaults to `Terra Classic` and `Terra 2.0` for now (will change over time as more chains are integrated)
  - `start`: for pagination, set index to start from
  - `limit`: for pagination, set how many pairs to call from start index, defaults to 120
  - `verified`: boolean to decide whether to return verified/unverified pairs, defaults to true
  - `name`: optional, to be used in search to return list of pairs with names that match the search query

**Examples**:

`/api/v2/pairs/terra1uenpalqlmfaf4efgtqsvzpa3gh898d9h2a232g`

- Returns pair data for pair address provided

`/api/v2/pairs?chains=Terra+Classic%2CTerra+2.0&verified=true&start=0&limit=120`

- Returns first 120 verified pairs from Terra Classic and Terra 2.0 (120 is 5 dashboard pages or 1 pairs page)

`/api/v2/pairs?chains=Terra+Classic%2CTerra+2.0&name=classic`

- Returns first 120 verified pairs from Terra Classic and Terra 2.0 that contains the word `classic` in their name (120 is 5 dashboard pages or 1 pairs page)

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  [
    {
      terra1uenpalqlmfaf4efgtqsvzpa3gh898d9h2a232g: {
        timestamp: "2021-09-05T04:09:27.479Z",
        asset0: {},
        asset1: {},
        type: "xyk",
        defaultBase: "asset1",
        dex: "Terraswap",
        chain: "Terra Classic",
        prices: {
          usd: {
            latest: 1.3467106592148677,
            historical: 1.0467106592148677,
          },
          native: {
            latest: 0.5123454324324324,
            historical: 0.5123454324324324,
          },
        },
      },
    },
    // 119 more...
  ];
  ```

## Historical Prices API (`/dashboard` and `/charts`)

### Current

Returns historical prices from ALL chains (terra classic and terra v2, 984 total)

- Method: `GET`
- URL: `/api/charts/terra/prices/historical`
- Query parameters:
  - `pairs`: pair address to get price (can have multiple)

**Example**:

`api/charts/terra/prices/historical?pairs=terra18g4d309jykk54l43k58fjqq8h2qdpzgdctxfwf&pairs=terra170lzdyflaamashcqkst23k9ew773dtg67tfu5m`

- Returns historical price of the pair addresses below
  - `terra18g4d309jykk54l43k58fjqq8h2qdpzgdctxfwf`
  - `terra170lzdyflaamashcqkst23k9ew773dtg67tfu5m`

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  [
    {
      terra18g4d309jykk54l43k58fjqq8h2qdpzgdctxfwf: 1.3467106592148677,
      terra170lzdyflaamashcqkst23k9ew773dtg67tfu5m: 422.22222222222223,
    },
  ];
  ```

### Proposed

Move to store prices in pairs API

## Latest Prices API (`/dashboard` and `/charts`)

### Current

Returns latest prices from ALL chains (terra classic and terra v2, 984 total)

- Method: `GET`
- URL: `/api/charts/terra/prices/latest`

**Example**:

`api/charts/terra/prices/latest`

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  {
    terra1rg9p352hcepvclfrxptpk0ua7a0tz4gcc0f0p8: 0.0013513513513513514,
    // ...
  };
  ```

### Proposed

Move to store prices in pairs API

## Candles API (`/charts`)

### Current

Returns candle data for chart page

- Method: `GET`
- URL: `/api/v1/charts/terra/candles`
- Query parameters:
  - `bars`
  - `from`
  - `interval`
  - `pairAddress`
  - `quoteAsset`
  - `to`

**Example**:

`/api/v1/charts/terra/candles?bars=320&from=1654517647&interval=1h&pairAddress=terra1m6ywlgn6wrjuagcmmezzz2a029gtldhey5k552&quoteAsset=uusd&to=1655669647`

- Returns chart data required to render chart

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  [
    {
      time: 1654516800000,
      open: 0.00517249961473,
      high: 0.00524733245443,
      low: 0.0051185787245,
      close: 0.00514423898789,
      volume: 307545.84513599996,
    },
    // ...
  ];
  ```

### Proposed

Rename API endpoint to `/api/v1/charts/:chain_name/candles` where `chain_name` is the name of the chain where the pair address is on

## Latest Prices API (`/dashboard` and `/charts`)

### Current

Returns latest prices from ALL chains (terra classic and terra v2, 984 total)

- Method: `GET`
- URL: `/api/charts/terra/prices/latest`

**Example**:

`api/charts/terra/prices/latest`

**Success response**:

- Condition: if everything is OK
- Code: `200 OK`
- Content (example):
  ```js
  {
    terra1rg9p352hcepvclfrxptpk0ua7a0tz4gcc0f0p8: 0.0013513513513513514,
    // ...
  };
  ```
