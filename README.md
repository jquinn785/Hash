# John Quinn

# Hash Tables

The first hash function had the stats of Stats: Movie Title Keys - Linked List: Wasted Rows: 14245, Collisions: 1424714, Time: 0.034420013427734375 Movie Quote Keys - Linear Probe: Wasted Rows: 6906, Collisions: 6264415, Time: 0.5237419605255127.

The second hash function had the stats of Stats: Movie Title Keys - Linked List: Wasted Rows: 7079, Collisions: 11982, Time: 0.03260016441345215 Movie Quote Keys - Linear Probe: Wasted Rows: 7230, Collisions: 7419, Time: 0.055090904235839844

The third hash function had the stats of Stats: Movie Title Keys - Linked List: Wasted Rows: 7013, Collisions: 12036, Time: 0.0272979736328125 Movie Quote Keys - Linear Probe: Wasted Rows: 7434, Collisions: 7690, Time: 1.9518799781799316

The fourth hash function had the stats of Stats: Movie Title Keys - Linked List: Wasted Rows: 5605, Collisions: 7606, Time: 0.09565186500549316 Movie Quote Keys - Linear Probe: Wasted Rows: 7596, Collisions: 7307, Time: 2.070219039916992

The fifth hash function had the stats of Stats: Movie Title Keys - Linked List: Wasted Rows: 14999, Collisions: 112492500, Time: 0.19352006912231445 Movie Quote Keys - Linear Probe: Wasted Rows: 0, Collisions: 112492500, Time: 8.198832035064697

The best optimization that was implemented was adding multiplication/divison of the hashvalue with a large prime number. From there the optimization rate decreased with similar stats for each attempt except for the final once which did really well with the linear probe hash table but very poorly with the linked list hash table. I think that altering the index with prime numbers works well because it spreads the hash values out more and generates more unique numbers because prime numbers aren't multiples of any other number. When adding a list of prime numbers it improved the hash function even more for the linked list hash table. I think this is because there are even less patterns in number generation because a random prime number from the list was used each time. There was a very large number of collisions with the final approach with the linear probe method this indicates that the same index was being generated but eventually every key got its own row in the hash table.
