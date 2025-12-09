from math import ceil

def bake_goods(available_trays, *tuples_info, **orders):
    allowed = {}
    for good, trays_batch, pieces_batch in tuples_info:
        allowed[good] = (trays_batch, pieces_batch)

    sorted_orders = sorted(
        ((good, qty) for good, qty in orders.items() if good in allowed),
        key=lambda x: x[0]
    )

    baked = {}
    trays = available_trays
    all_fulfilled = True

    for good, requested in sorted_orders:
        trays_per_batch, pieces_per_batch = allowed[good]

        needed_batches = ceil(requested / pieces_per_batch)
        possible_batches = trays // trays_per_batch
        actual_batches = min(needed_batches, possible_batches)

        if actual_batches == 0:
            all_fulfilled = False
            continue

        produced = actual_batches * pieces_per_batch
        produced = min(produced, requested)  # report no more than requested

        baked[good] = produced

        trays -= actual_batches * trays_per_batch

        if actual_batches < needed_batches:
            all_fulfilled = False

        # if trays <= 0:
           # break

    if all_fulfilled:
        result = [f"All goods baked! Remaining trays: {trays}"]
    else:
        result = ["Not enough trays!"]

    if baked:
        result.append("Baked:")
        for good in sorted(baked):
            result.append(f"{good}: {baked[good]}")

    return "\n".join(result)

print(bake_goods(9, ("Croissant", 1, 12), ("Bagel", 2, 16), Croissant=24, Bagel=16))
print(bake_goods(2, ("Muffin", 1, 8), ("Scone", 1, 6), Muffin=12, Scone=6))
print(bake_goods(3, ("Cookie", 2, 10), ("Donut", 1, 5), Cookie=15, Donut=5))
print(bake_goods(15, ("Baguette", 1, 4), Croissant=5, Baguette=10, Eclair=1))
