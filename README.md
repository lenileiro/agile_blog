# agile_blog

Work flow
## Class Comment
 - chat message sent to lobby is empty list 
  - it takes author as parameter
  - replied to assigned None
  - user messages is empty list
  ### methods
 - get_author 
 -          -return author value
 -  set_author(value)
 -          - sets author value to value
 -  get_message
 -          return user messages
 -  set_message(message,author)
 -        Append message tuple to user message and lobby chat message
 -        message tuple takes message,replied to,author ,created at  
 -        message and author are passed as parameters
 -        replied to is set by calling the replied to method
 -        firsrt replied_to function checked  if replied to was passed or None
 -        created at value is set by  calling created at method
 -  
 -  created_at
 -        return current datetime formatted as "%Y-%m-%d %H:%M:%S"
 -  replied_to
 -       return replied to value
 -  set_replied_to(value)
 -       set replied to value 
 -  to_string
 -       returns lobby chat messages

## class User
  - it takes name  as parameter
  - lobby is an instance of the Comment class passing name as the parameters
  - online statues is False by default
  - last seen is None by default
  - class received is the class name at instatiation
  ### Methods
  #### get_name
  -               return user name
  #### set_name(value)
  -               set name to value
  #### is_logged_in
  -                    check if online status is true
  -                    return a formatted string with online status and last seen value    
  #### last_logged_in_at
  -       sets last seen value to  current datetime formatted as "%Y-%m-%d %H:%M:%S"
  #### log_in
  -      sets online status to True
  -      call last logged in at method   
  #### login_error
  -       return formatted string with online status and last seen value if user is not                logged in
   #### can_edit(index,comment)
-        - call can_edit_own_comment method if class received is Moderator or User
 -        - call can_edit_lobby_comment method if class received is Admin 
  #####  can_edit_own_comment(index,comment)
  -              - takes index and comment as parameters
  -              - create mesage tuple
  -              -message tuple takes message,replied to,author ,created at 
  -              -create at value is set as the current time formated as "%Y-%m-%d %H:%M:%S"
  -              -get to comment to be replace at index from the users comment list = old comment
  -              - edit_comment = message_received(comment,old_comment.replied_to,self.name,current_time)
  -              - get index of old comment in lobby comments
  -               - remove from chat_messages the old comment
  -               -insert in to lobby editted comment
  -               -insert in to user_message editted comment     
 #####   can_edit_lobby_comment(index,comment)
  -               - takes index and comment as parameters
  -              - create mesage tuple
  -              -message tuple takes message,replied to,author ,created at 
  -              -create at value is set as the current time formated as "%Y-%m-%d %H:%M:%S"
  -              -get to comment to be replace at index from the chat comment list = old comment
  -              -remove from chat_messages the old comment
  -              - insert in to lobby editted comment
  -              
  #### can_delete(index)
  -             -  if class received is Moderator or Admin
  -             -remove message at index from the chat message
  #### to_string(value,reply)
  -                - takes value and reply_to as parameters
  -                if parameters is not empty call set_message method from Comment class pass arguments
  -                -else format string as required