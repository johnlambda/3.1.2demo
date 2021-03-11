
class User:
    def __init__(self, user_id, num_posts, reputation, mod_status, can_post):
        self.username = user_id
        self.num_posts = num_posts
        self.reputation = reputation
        self.mod_status = mod_status
        self.can_post = can_post
        self.post_topic('my first topic', ['automated'], 'this topic is automatically created for every new user')

    def post_topic(self, title, tags, description):
        author = self.username
        topic = Topic(title, tags, description, author)
        return topic

    @staticmethod
    def post_topic_static(title, tags, description, author):
        topic = Topic('hard-coded topic', tags, description, author)
        return topic


class Topic:
    def __init__(self, title, tags, description, author):
        self.title = title
        self.tags = tags
        self.description = description
        self.author = author


class Comment:
    def __init__(self, text, up_votes, down_votes, moderated):
        self.text = text
        self.up_votes = up_votes
        self.down_votes = down_votes
        self.moderated = moderated


sarah = User(99, 0, 0, True, True)
sarah.post_topic(
    "smoothies",
    ["food", "healthy"],
    "smoothies are the best. love smoothies. can't get enough smoothies.",
)


User.post_topic_static('football is cool', ['sports'], 'tom brady\'s take on football', 'tombrady99')
