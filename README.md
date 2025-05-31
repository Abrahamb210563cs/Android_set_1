# Data Structures: LRU Cache and Custom HashMap Implementations

## Overview

This repository contains solutions for two common data structure problems:

1. **Q1: Least Recently Used (LRU) Cache**  
2. **Q2: Custom HashMap Implementation without built-in dictionaries**

---

## Q1: LRU Cache
### Problem Statement

Implement an LRU Cache with the following operations in **O(1)** time complexity:

- `get(key)`: Return the value of the key if it exists, otherwise return -1.
- `put(key, value)`: Insert or update the key-value pair. If the cache exceeds its capacity, evict the least recently used item.

### Approach
- Use a **doubly linked list** to track the order of usage.
- Use a **hash map** to store key-node references for O(1) access.
- The most recently used item is moved to the front of the linked list.
- When capacity is exceeded, the tail (least recently used) is removed.

## Q2: Custom HashMap
## Problem Statement
Implement a simplified HashMap without using built-in dictionary or hash map libraries. The operations should average O(1) time complexity:

put(key, value): Insert or update a key-value pair.

get(key): Return the value if the key exists, else -1.

remove(key): Remove the key-value pair if present.

## Approach
Use an array of buckets where each bucket contains a list to handle collisions (separate chaining).

A simple modulo-based hash function is used to map keys to buckets.

All operations are performed by traversing the bucket list in the worst case.