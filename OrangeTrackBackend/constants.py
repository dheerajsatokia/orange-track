from user import constants as user_constants

user_constants = user_constants
read_actions = ['retrieve', 'list']
update_actions = ['update', 'partial_update']
create_actions = ['create']
delete_actions = ['destroy']
write_actions = update_actions + read_actions + update_actions + delete_actions
