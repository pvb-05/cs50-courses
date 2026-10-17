# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Pros: Data load is evenly distributed across all boats, avoiding overloading of one boat.

Cons: When you need to query data by a time period (e.g. all data from 0h-1h), you have to query all boats, because the data is not sorted by time.

## Partitioning by Hour

Pros: Efficient because only one boat needs to be queried by that time period.

Cons: Uneven because the hot spot will be concentrated on one boat (other boats are empty) and can cause overload.

## Partitioning by Hash Value

Advantages:

    The data load is evenly distributed, solving the "hot spot" problem.

    Querying a specific record (when the exact timestamp is known) is very fast because you only need to calculate the hash value to identify and query a single boat.

Disadvantages:

    Like random partitioning, when querying by time range, you still have to query all boats because adjacent timestamps are unlikely to have been hashed to the same boat.
