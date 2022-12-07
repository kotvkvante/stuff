material written by me for me

ac_utils.py:
	some functions for generating AutoCAD scripts

## Example:
In your project:
``` 
git clone https://github.com/kotvkvante/stuff
```
Then:
```
from stuff import ac_utils as ac

xs = [-5, -4 -3, -2, -1, 0, 1, 2, 3, 4, 5]
ys = [x**2 for x in xs]

# One line:
ac_write_to_file(
        [ac.AC_PLINE_COMMAND],
        [xs, ys],
        output_file ="my_script_1" 
    )
# Multiple lines:

y3 = [x**3 for x in xs]
yx = [x for x in xs]

ac_write_to_file(
	[ac.AC_SPLINE_COMMAND, ac.AC_SPLINE_COMMAND, ac.AC_SPLINE_COMMAND],
        [xs, ys], 
	[xs, y3], 
	[xs, yx],
        output_file="my_script_2"
    )
)
```