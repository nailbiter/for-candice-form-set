#!/usr/bin/env python3
"""===============================================================================

        FILE: wait-till.py

       USAGE: (not intended to be directly executed)

 DESCRIPTION: 

     OPTIONS: ---
REQUIREMENTS: ---
        BUGS: ---
       NOTES: ---
      AUTHOR: Alex Leontiev (alozz1991@gmail.com)
ORGANIZATION: 
     VERSION: ---
     CREATED: 2021-08-05T10:14:13.683828
    REVISION: ---

==============================================================================="""

import click
from datetime import datetime,timedelta
import time

@click.command()
@click.argument("when")
def wait_till(when):
    when = datetime.strptime(when,"%H:%M")
    now = datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")
    assert when>=now, f"{when} should be later than {now}"
    click.echo(when-now)
    total_seconds = (when-now).total_seconds()
    click.echo(f"will wait for {total_seconds} seconds")
    time.sleep(total_seconds)


if __name__=="__main__":
    wait_till()
