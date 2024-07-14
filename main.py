# PERSONAL BLOG


class Blog:
    def __init__(self, header: str, about: str):
        self.entries = []           # The list containing the dictionaries for each blog post.
        self.header = header        # The title of the blog.
        self.introduction = about   # The blog page introduction.

    def newEntry(self, date: int, time: int, title: str, text: str) -> None:
        """Creates new blog post."""
        # Create new BlogPost object
        # Call newEntry blog post function
        # Append returned dictionary to the list of entries (self.entries)
        pass

    def readEntry(self, title: str) -> str:
        """Reads blog post."""
        pass

    def readAllEntries(self) -> str:
        """Reads all blog posts."""
        # uses query
        pass

    def deleteEntry(self, title: str) -> None:
        """Deletes an existing blog entry."""
        pass


class BlogPost:
    def __init__(self, date: int, time: int, title: str, text=None):
        self.date = date            # The date of the blog entry.
        self.time = time            # The time of the blog entry.
        self.title = title          # The title of the blog entry.
        self.body = text            # The blog entry text.

    def newEntry(self) -> dict:
        """Creates new blog post."""
        # Define dictionary for blog post
        # Populate self.body with blog entry text
        # Return dictionary
        pass

    def updateEntry(self, title: str) -> None:
        """Edits an existing blog entry."""
        # Update self.body and modify blog entries list...is this the right place
        # to do that?
        pass

