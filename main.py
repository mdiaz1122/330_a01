# PERSONAL BLOG


class Blog:
    def __init__(self, header: str, about: str):
        self.entries = []           # The list containing the dictionaries for each blog post.
        self.header = header        # The title of the blog page.
        self.introduction = about   # The blog page introduction.

    def newEntry(self, date: int, time: int, title: str, text: str) -> None:
        """Creates new blog post and adds to blog entries collection.

        Args:
            date: Date of blog entry creation.
            time: Time of blog entry creation.
            title: Blog entry title.
            text: Main text of the blog entry.
        """
        # Create new BlogPost object
        # Call __newEntry blog post function in Blog Post class
        # Append returned dictionary to the list of entries (self.entries)
        pass

    def readEntry(self, title: str, all_posts: bool) -> str:
        """Reads blog post. If 'all_posts' is True, read all posts.

        Args:
            title: Title of blog post user wants to read.
            all_posts: Boolean toggle indicating whether all posts should be read.

        Returns:
            A string containing the text of the blog entry.
        """
        pass

    def deleteEntry(self, title: str) -> None:
        """Deletes an existing blog entry.

        Args:
            title: Title of blog post user wants to delete.
        """
        pass


class BlogPost:
    def __init__(self, date: int, time: int, title: str, text=None):
        self.date = date            # The date of the blog entry.
        self.time = time            # The time of the blog entry.
        self.title = title          # The title of the blog entry.
        self.body = text            # The blog entry text.

    def __newEntry(self, date: int, time: int, title: str, text: str) -> dict:
        """Creates new blog post.

        Args:
            date: Date of blog entry creation.
            time: Time of blog entry creation.
            title: Blog entry title.
            text: Main text of the blog entry.

        Returns:
            A dictionary containing the text of the blog entry as well as the date,
            time, and title of the blog post.
        """

        # Define dictionary for blog post and populate self.body with blog entry text
        # Return dictionary
        pass

    def updateEntry(self, title: str) -> dict:
        """Updates an existing blog entry.

        Args:
            title: Title of blog post user wants to read.

        Returns:
            A dictionary containing the text of the blog entry as well as the date,
            time, and title of the blog post.
        """
        # Update blog post text in dictionary.
        # Return dictionary and modify blog entries list.
        pass

