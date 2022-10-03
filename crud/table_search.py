def findName(self):
        name = self.search.text().lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            # if the search is *not* in the item's text *do not hide* the row
            self.table.setRowHidden(row, name not in item.text().lower())