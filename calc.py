#!/usr/bin/env python3

from mpmath import mp, mpf
import cpuinfo
import sys
import time
from rich.progress import (
    Progress,
    MofNCompleteColumn,
    SpinnerColumn,
    TextColumn
)


print(cpuinfo.get_cpu_info()["brand_raw"])
digits = int(sys.argv[1])

# Run calculation
def calc():
    mp.dps = digits
    data = mp.nstr(mp.pi, n=digits)
    return data


# Make it look good though
with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    MofNCompleteColumn()
) as progress:
    c1 = progress.add_task(description="[green]Calculating...", total=digits)
    start = time.process_time()
    data = calc()
    while not progress.finished:
        progress.update(c1, advance=len(data)-1)
        time.sleep(0.1)

print(f"Finished calculating {len(data)-1} digits of pi in {time.process_time()-start} seconds.")