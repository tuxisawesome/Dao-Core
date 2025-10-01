dictionary = {"man": "Man\nThe manual viewer\nUsage: man"} #TODO: Add more man entries

def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    interactive = drivers[drivernames.index("input")]
    file_to_view = interactive.getinput("Enter the path to the file you want to view: ")
    text_to_view_as_list = dictionary.get(file_to_view,"Invalid application").splitlines()
    less_like_viewer(display,interactive,text_to_view_as_list)

def less_like_viewer(display,interactive,filepath, lines_per_page=20):
    """
    Simulates the 'less' command for viewing a text file.

    Args:
        filepath (str): The path to the text file to view.
        lines_per_page (int): The number of lines to display per "page".
    """
    lines = filepath

    total_lines = len(lines)
    current_line_index = 0

    while current_line_index < total_lines:
        # Print lines for the current page
        for i in range(current_line_index, min(current_line_index + lines_per_page, total_lines)):
            display.printline(lines[i].strip('\n'))  # Remove trailing newlines for cleaner output

        # If there are more lines, prompt the user
        if current_line_index + lines_per_page < total_lines:
            interactive.getinput("\nPress Enter to view next page, or 'q' to quit: ")
            if input().lower() == 'q':
                break
        current_line_index += lines_per_page