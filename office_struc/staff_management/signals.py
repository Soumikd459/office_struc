

from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started, request_finished
from django.db.backends.signals import connection_created


@receiver(user_logged_in,sender = User)     #2nd method to connect
def login_success(sender,reqest,user,**kwargs):
    print('--------------------')
    print('sender:', sender)
    print('user password:' , user.password)
    
    ## req codeing
#user_logged_in.connect(login_success, sender= User)    # 1st method to connect

# scenarios
''' after successfully user's login you may capture many things. like if I want to capture the ip of the model ,
how many time he login ,you can count, I can.'''




@receiver(user_logged_out,sender = User)     #2nd method to connect
def log_out(sender,reqest,user,**kwargs):
    print('--------------------')
    print('sender:', sender)
    print('user password:' , User.password)
    
    ## req codeing
#user_logged_out.connect(log_out, sender= User)    # 1st method to connect


''' after log out if I want show the message '''

@receiver(user_login_failed,sender = User)     #2nd method to connect
def login_failed(sender,credentials,reqest,**kwargs):
    print('--------------------')
    print('login failed signal')
    print('sender:', sender)
    print('credentials:' , credentials)
    
    ## req codeing
#user_logged_out.connect(log_out, sender= User)    # 1st method to connect

'''the people who tried to log in but not to do so, i can capture there ip, user name. even if i want to restrict the login no
like 1 can try maximum 4 attempt ,beyond that the ip will block. I can do this here.'''


@receiver(pre_save,sender = User) # User = model class
def at_beggining_save(sender, instance, **kwargs):  #it will run before the save method.cz we set the pre_save receiver before this.
    print('--------------------')
    print('pre save signal')
    print('sender:', sender)
    print('instance:', instance)
    
# pre_save.connect(at_beggining_save, sender= User)


@receiver(post_save,sender = User) # User = model class
def at_ending_save(sender, instance,created, **kwargs):  #it will run after the save method.cz we set the pre_save receiver before this.
    if created:

        print('--------------------')
        print('post save signal')
        print('new record')
        print('sender:', sender)       '''here we can control the cache .if data updated then cache files also be update'''
        print('instance:', instance)      # if not update then old cache will remain
        print('created:', created)
    else:
        print('--------------------')
        print('post save signal')
        print('Updated record')
        print('sender:', sender)
        print('instance:', instance)
        print('created:', created)

# post_save.connect(at_ending_save, sender= User)

'''its called at the ending of the save method, if new obj is created then 1st code will run(or we can write our code ,
 what we want to do here), or if the obj is updated then 2nd code will run  '''

@receiver(pre_delete,sender = User) 
def at_begining_delete (sender, instance, **kwargs):  
        print('--------------------')
        print('pre delete signal')
        
        print('sender:', sender)      
        print('instance:', instance)      
        

@receiver(post_delete,sender = User) 
def at_ending_delete (sender, instance, **kwargs):  
        print('--------------------')
        print('post delete signal')
        print('are you sure to delete?')
        print('sender:', sender)       
        print('instance:', instance)      
        

@receiver(pre_init,sender = User) 
def at_begining_init (sender, *args, **kwargs):  
        print('--------------------')
        print('pre init signal')
                                            # before __init__ if we want to wright some code then we can do it
        print('sender:', sender)      
        print(f'Args: {args}')      
        print(f'Kwargs: {kwargs}')

@receiver(post_init,sender = User) 
def at_ending_init (sender, *args, **kwargs):  
        print('--------------------')
        print('pre init signal')
                                            # after __init__ if we want to wright some code then we can do it
        print('sender:', sender)      
        print(f'Args: {args}')      
        print(f'Kwargs: {kwargs}')