from settings import Session
from sql_alchemy_models import User, Tag, Post


def add_some_data():
    session = Session()

    user1 = User(username='morpheus')
    user2 = User(username='Neo')
    user3 = User(username='Trinity')
    session.add(user1)
    session.add(user2)
    session.add(user3)

    tag1 = Tag(name='matrix')
    tag2 = Tag(name='questions')
    tag3 = Tag(name='answers')
    tag4 = Tag(name='rabbit')

    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.add(tag4)

    session.flush()

    post1 = Post(user_id=user2.id, title='Who am I', description='where am I?', body='What is it all about?',
                 is_published=True, tags=[tag2, tag3])

    post2 = Post(user_id=user3.id, title='Why you hardly sleep?', description='I know what are you doing...',
                 body="I know why you're here, Neo. I know what you've been doing... why you hardly sleep, why you live alone, and why night after night, you sit by your computer. You're looking for him. I know because I was once looking for the same thing. And when he found me, he told me I wasn't really looking for him. I was looking for an answer. It's the question that drives us, Neo. It's the question that brought you here. You know the question, just as I did.",
                 tags=[tag1, tag2, tag3], is_published=True)
    post3 = Post(user_id=user3.id, title="The answer is out there", description='wait...',
                 body='follow the white rabbit', tags=[tag1, tag3, tag4], is_published=True)
    post4 = Post(user_id=user1.id, title="you're feeling a bit like Alice. Hmm?",
                 description='Tumbling down the rabbit hole?',
                 body="I see it in your eyes. You have the look of a man who accepts what he sees because he is expecting to wake up. Ironically, that's not far from the truth. Do you believe in fate??",
                 tags=[tag1, tag2], is_published=True)
    post5 = Post(user_id=user3.id, title="Are you still here?", description='Neo...',
                 body='follow the white rabbit', tags=[tag1, tag4], is_published=True)

    post6 = Post(user_id=user2.id, title='Help', description='I need someboby', body='Help, not just anybody..',
                 is_published=True, tags=[tag2, tag1])

    session.add(post1)
    session.add(post2)
    session.add(post3)
    session.add(post4)
    session.add(post5)
    session.add(post6)

    session.commit()
