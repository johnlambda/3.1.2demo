import pytest

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
        topic = Topic(title, tags, description, author)
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


def test_user_create():
    user_id = 99
    num_posts = 54
    reputation = 13
    mod_status = True
    can_post = False

    test_user = User(user_id, num_posts, reputation, mod_status, can_post)

    assert(type(test_user) == User)


def test_user_post_topic_title():
    user_id = 99
    num_posts = 54
    reputation = 13
    mod_status = True
    can_post = False
    title = 'test'
    description = 'testing that users can create topics'
    tags = ['test']

    test_user = User(user_id, num_posts, reputation, mod_status, can_post)

    test_topic = test_user.post_topic(title, description, tags)

    assert(test_topic.title == title)