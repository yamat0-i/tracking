import tracemalloc

from tracking import tracking


tracemalloc.start(3)

tracking.main() # target process

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top 10]")
for stat in top_stats[:1]:
    print(stat)
    for line in stat.traceback.format():
        print(line)
    print("=====")