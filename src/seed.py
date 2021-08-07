Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

test1=App_base(text='my name is pawel',status='finished')
test2=App_base(text='my name is janusz',status='finished')
test3=App_base(text='hello world',status='finished')

Session.add(test1)
Session.add(test2)
Session.add(test3)
Session.commit()