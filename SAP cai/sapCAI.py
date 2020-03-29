import sapcai

# REQUEST_TOKEN d475521f36a9539e5e4d673bf807c3f4

# usage
request=sapcai.Request('d475521f36a9539e5e4d673bf807c3f4')
# client=sapcai.Client('d475521f36a9539e5e4d673bf807c3f4')

# dialog
def dialog():
    build=sapcai.Build('d475521f36a9539e5e4d673bf807c3f4')
    response=build.dialog({'type':'text', 'content':'explore knowledge sources option a'}, 
    'CONVERSATION_ID')
    messages=response.messages
    for message in messages:
        print(message.type)
        print(message.content)

def converse():
    response=request.converse_text('explore knowledge sources option a')
    print(response.reply)

if __name__=='__main__':
    dialog()
    #converse()