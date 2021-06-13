import time


# Print iterations progress


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=2, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int) or finished steps of all steps
        total       - Required  : total iterations (Int) all steps
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    I used it in another projects.
    """
    # Decimal is calculate by divide iteration on total
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    # FilledLength calculate the length of bar in each step
    filled_length = int(length * iteration // total)

    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()


# A List of Items
items = list(range(0, 20))
length_of_items = len(items)

# Initial call to print 0% progress
print_progress_bar(0, length_of_items, prefix='Progress:', suffix='Complete', length=50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.3)
    # Update Progress Bar
    print_progress_bar(i + 1, length_of_items, prefix='Progress:', suffix='Complete', length=50)
