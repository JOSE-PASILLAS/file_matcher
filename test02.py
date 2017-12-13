IDENTICAL = -1
def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    shorter = line2 
    longer = line1
    i_character = 0
    if line1 < line2:
        shorter = line1
        longer = line2
    for i in range(0, len(shorter)):
        if shorter[i] != longer[i]:
            i_character = 1
            return (i)
    if i_character == 0:
        if len(shorter)<len(longer):
            return(len(shorter))
        else:
            return (IDENTICAL)

#print(singleline_diff("pepe","peps"))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    shorter=line2
    longer=line1
    if line1 < line2:
        shorter = line1
        longer = line2
    f_string = shorter
    if idx<0 or idx>len(shorter):
        return ("")
    if "\n" in shorter+longer or "\r" in shorter+longer:
        return ("")

    if idx > len(shorter) and idx < 0:
        return 0
    else:
        indicator = "=" * (idx) + "^"
        f_string = line1 + "\n" + indicator + "\n"+line2+"\n"
        return(f_string)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    shorter=lines1
    longer=lines2
    if shorter is not longer:
        if len(shorter)==0 and len(longer)==0:
            return (IDENTICAL, IDENTICAL)
        elif len(shorter)==0 or len(longer)==0:
            return (0,0)
        if len(lines2) < len(lines1):
            shorter=lines2
            longer=lines1
        for i in range(0, len(shorter)):#shorter.count('\n')
            a = singleline_diff(lines1[i], lines2[i])
            if a > -1:
                return(i,a)
        if a == -1 and len(shorter) == len(longer):
            return (IDENTICAL, IDENTICAL)
        else:
            return(i+1,0)
    else:
        return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename, "rt")
    #for line in openfile.readlines():
    #    print(line)
    strings=openfile.readlines()
    strings = [x.strip() for x in strings]
    return(strings)
    openfile.close()

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1=get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    dif=multiline_diff(file1, file2)
    if dif[0]>-1:
        output="Line "+str(dif[0])+":\n"
        output=output+singleline_diff_format(file1[dif[0]], file2[dif[0]], dif[1])
    else:
        output="No differences\n"
    return output



