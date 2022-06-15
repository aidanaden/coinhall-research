# Kafka-GCP Consideration

## Kafka

- Functions similar to a log.
    - Messages are accessed by index/offset which increments after consumption.
    - This allows messages to be re-consumed by *other* consumers.
        - Non-zero chance that a consumer re-consumes the same message
    - As messages stay in the log, there exists a retention policy that’s configured by age or size of the log.
- Core concepts can be found [here](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.2.4/bk_storm-user-guide/content/basic-kafka-concepts.html).
- [Research on Kafka cluster/replication as it is currently a SPOF](https://github.com/aidanaden/coinhall-research/blob/master/pipeline-research/kafka-replication.md).
    - Have a Kafka instance per chain that stripes data of other chains into the other (n-k) instances of Kafka, similar to RAID 5 (illustrated in link), or
    - Round-robin replication (n replicates to n+1, wrap over).

## GCP Pub/Sub

### Understanding Pub/Sub

- Functions similar to queue.
    - Message pops from memory when subscriber acknowledges message.
    - It’s possible to [replay messages](https://cloud.google.com/pubsub/docs/replay-overview).
- Core concepts can be found [here](https://cloud.google.com/pubsub/docs/overview#core_concepts).

## [Pub/Sub vs Pub/Sub **Lite**](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite)

|  | Pub/Sub | Pub/Sub Lite |
| --- | --- | --- |
| Price [1] | ~$2000/month | - Zonal: ~$169/month <br> - Regional: ~$608/month |
| Reliability | Highest | - Zonal: Best effort <br> - Regional: Similar SLA to normal Pub/Sub |
| Resources | Managed | Pre-provisioned |
| Data replication | - ≥ 2 zones <br> - Best effort 3rd additional zone | - Zonal: No replication <br> - Regional: Async backup to 2nd zone |

## Kafka vs Pub/Sub

|  | Kafka | Pub/Sub (Lite) |
| --- | --- | --- |
| Deployment | - Cloud (Confluent) <br> - On-premise (current) | - Cloud |
| Message <br> delivery (default) | At least once | Exactly once |
| Message flow | Offset increments, <br> message remains  | Message deleted on acknowledgement |
| Message order | Within partitions / same key | Within topics |

More information can be found [here](https://cloud.google.com/architecture/migrating-from-kafka-to-pubsub#comparing_features).

## Dev

1. Migration from Kafka to Pub/Sub ([link](https://cloud.google.com/architecture/migrating-from-kafka-to-pubsub)).
2. KafkaJS manual committing for exactly-once semantics (EOS) ([link](https://kafka.js.org/docs/consuming#manual-committing)).
    1. [Java example](https://www.baeldung.com/kafka-exactly-once).
    2. librdkafka - C/C++ Kafka client to support EOS ([link](https://github.com/edenhill/librdkafka)).
    3. Blizzard’s Node.js wrap on librdkafka ([link](https://github.com/Blizzard/node-rdkafka)).
3. Pub/Sub Client ([Node.js](https://cloud.google.com/nodejs/docs/reference/pubsub/latest)) — not sure if it works with pub/sub lite.
4. [Pub/Sub Lite library](https://cloud.google.com/pubsub/lite/docs/reference/libraries) (Go/Java/Python)
5. Pub/Sub Lite API ([REST](https://cloud.google.com/pubsub/lite/docs/reference/rest))([RPC](https://cloud.google.com/pubsub/lite/docs/reference/rpc))

