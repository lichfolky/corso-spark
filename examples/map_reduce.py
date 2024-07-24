from utils import map_words, reduce_sum

print(" MAPREDUCE ".center(90, "*"), "\n")

## data1 = open("examples/files/tobenot1.txt").read()
## data2 = open("examples/files/tobenot2.txt").read()

data1 = "Nella vecchia fattoria ia ia o. Quante bestie ha zio Tobia ia ia o"
data2 = "C'è la capra capra ca ca capra. Nella vecchia fattoria ia ia o"

clusters = {"doc1": [data1], "doc2": [data2]}  # or nodes
clusters_cache = []


for cluster in clusters.items():
    print(cluster)

## MAP
print("\nMAP:\n")

for key, cluster_data in clusters.items():
    mapped_data = [*map(map_words, cluster_data)]

    # list comprehension would be more pythonic
    # mapped_data = [map_words(x) for x in cluster_data]

    clusters_cache += mapped_data

for cluster_cache in clusters_cache:
    print(cluster_cache)

## SHUFFLE
print("\nSHUFFLE:\n")

new_clusters_cache = [[], []]
for cluster_cache in clusters_cache:
    for item in cluster_cache:
        if item[0] < "m":
            new_clusters_cache[0].append(item)
        else:
            new_clusters_cache[1].append(item)

clusters_cache = new_clusters_cache

clusters_cache[0].sort()
clusters_cache[1].sort()

for cluster_cache in clusters_cache:
    print(cluster_cache)

## REDUCE
print("\nREDUCE:\n")

clusters_cache = [reduce_sum(x) for x in clusters_cache]

for cluster_cache in clusters_cache:
    print(cluster_cache)
print(90 * "*")
