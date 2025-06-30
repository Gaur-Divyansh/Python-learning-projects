def get_todo(filepath):
    """
    Read a text file and return the list of todo items.
    :param filepath:
    :return:
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todo(filepath,todos_arg):
    """
    Write the todo items in the list
    :param filepath:
    :param todos_arg:
    :return:
    """
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("nothing to check")
