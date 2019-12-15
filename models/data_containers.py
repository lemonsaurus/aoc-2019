class AutoResizingList(list):
    """A list that never goes out of range.

    - Items that don't exist will always be equal to 0.
    - Adding an item at an index that is larger than the length
      of the list will pad the list with zeroes to add the required
      indexes.
      """

    def _resize_list(self, new_size: int):
        """Resize the list to be large enough to accommodate an index at new_size."""
        for _ in range((new_size + 1) - len(self)):
            self.append(0)

    def __getitem__(self, key):
        if key > len(self):
            return 0
        else:
            return list.__getitem__(self, key)

    def __setitem__(self, key, item):
        if len(self) <= key:
            self._resize_list(key)

        list.__setitem__(self, key, item)
