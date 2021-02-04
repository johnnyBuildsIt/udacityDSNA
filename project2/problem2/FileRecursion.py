import os


class FileRecursion:

    def find_files(self, suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
        """
        search_list = []
        contents = os.listdir(path)
        for i in contents:
            full_path = path + "/" + i
            if os.path.isfile(full_path) and full_path.endswith(suffix):
                search_list.append(full_path)
            elif os.path.isdir(full_path):
                search_list.extend(self.find_files(suffix, path + "/" + i))
        return search_list
