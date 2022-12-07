from typing import Union, List

Num = Union[int, float]
AC_LINE=0
AC_PLINE=1
AC_SPLINE=2



AC_SCRIPT_FILENAME="{f}.{e}"
AC_SCRIPT_FILENAME_DATE="{f}_{d}.{e}"
AC_LINE_COMMAND="_LINE"
AC_PLINE_COMMAND="_PLINE"
AC_SPLINE_COMMAND="_SPLINE"

AC_LINE_NL="\n" # NL = Newline
AC_PLINE_NL="; ERROR"
AC_SPLINE_NL="\n\n\n"

AC_NL = (AC_LINE_NL, AC_PLINE_NL, AC_SPLINE_NL)
##AC_COMMAND_TO_INDEX = {AC_LINE_COMMAND: 1,
##                       AC_PLINE_COMMAND: 2,
##                       AC_SPLINE_COMMAND: 3}

AC_COMMANDS_NL = {AC_LINE_COMMAND: AC_LINE_NL,
                  AC_PLINE_COMMAND: AC_PLINE_NL,
                  AC_SPLINE_COMMAND: AC_SPLINE_NL}

def ac_write_to_file(
        line_commands,
        *lines,
        output_file="script",
        output_ext="scr",
        append_date=False):
##    if(len(pline_x) != len(pline_y)):
##        print("Uncorrect len")
##        return

    if(append_date): filename = AC_SCRIPT_FILENAME_DATE.format(f=output_file, d=d, e=output_ext)
    else: filename = AC_SCRIPT_FILENAME.format(f=output_file, e=output_ext)
        
    with open(filename, "w") as f:
        for index, line in enumerate(lines):
            f.write(line_commands[index])
            f.write("\n")
            for point in zip(line[0], line[1]):
                f.write("{:.8f},{:.8f}\n".format(point[0], point[1]))

            _nl = AC_COMMANDS_NL.get(line_commands[index])
            if(_nl == None): print("ERROR OCCURED")
            f.write(_nl)  
        f.write(";")

def ac_line_to_file(pline_x, pline_y,
                    line_command,
                    output_file="script",
                    output_ext="scr",
                    append_date=False):
    if(len(pline_x) != len(pline_y)):
        print("Uncorrect len")
        return

    if(append_date): filename = AC_SCRIPT_FILENAME_DATE.format(f=output_file, d=d, e=output_ext)
    else: filename = AC_SCRIPT_FILENAME.format(f=output_file, e=output_ext)
        
    with open(filename, "w") as f:
        f.write(line_command)
        f.write("\n")
        for point in zip(pline_x, pline_y):
            f.write("{:.8f},{:.8f}\n".format(point[0], point[1]))
        _nl = AC_COMMANDS_NL.get(line_command)
        if(_nl == None): print("ERROR")
        f.write(_nl)  
        f.write(";")

def ac_pline_to_file(pline_x, pline_y,
                     output_file="script",
                     output_ext="scr",
                     append_date=False):
    ac_line_to_file(pline_x, pline_y,
                    AC_PLINE_COMMAND,
                    output_file,
                    output_ext,
                    append_date)

def ac_spline_to_file(pline_x, pline_y,
                      output_file="script",
                      output_ext="scr",
                      append_date=False):
    ac_line_to_file(pline_x, pline_y,
                    AC_SPLINE_COMMAND,
                    output_file,
                    output_ext,
                    append_date)

def ac_simple_line_to_file(
        pline_x, pline_y,
        output_file="script",
        output_ext="scr",
        append_date=False):
    ac_line_to_file(pline_x, pline_y,
                    AC_LINE_COMMAND,
                    output_file,
                    output_ext,
                    append_date)

def ac_plot_to_file(pline_x, pline_y,
                    output_file="script",
                    output_ext="scr",
                    append_date=False):
    zeros = [0, 0]
    xaxis = [min(pline_x), max(pline_x)]
    yaxis = [min(pline_y), max(pline_y)]
    
    ac_write_to_file(
        [AC_SPLINE_COMMAND, AC_LINE_COMMAND, AC_LINE_COMMAND],
        [pline_x, pline_y], [xaxis, zeros], [zeros, yaxis],
        output_file=output_file, output_ext=output_ext,
        append_date=append_date)

    print("-> {}.{} {}".format(output_file, output_ext, "complite"))
          
    
if __name__=="__main__":
    print("AutoCAD module");
    x = [-5, -4, -3, -2, -1, 0, 1, 2, 3,  4,  5]
    y = [25, 16,  9,  4,  1, 0, 1, 4, 9, 16, 25]
    print(max(x))
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    zeros = [0, 0]
    xaxis = [xmin, xmax]
    yaxis = [ymin, ymax]
    #ac_spline_to_file(x, y)
    #ac_plot_to_file(x, y, "test")

##    ac_write_to_file(
##        [AC_SPLINE_COMMAND, AC_LINE_COMMAND, AC_LINE_COMMAND],
##        [x, y], [xaxis, zeros], [zeros, yaxis],
##        output_file="test1")

    ac_plot_to_file(x, y, "script")
        
