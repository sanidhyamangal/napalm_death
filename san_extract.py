import summarizer # for getting a summary 
import re # for regex 
import wikipedia # to handdle wiki requests 

# function to remove garbage texts 
def remove_grabage(sent):
    return [x.strip() for x in re.split('=*= [A-Za-z ]* =*=', sent) if x.split()]

# function to get important facts 
def get_facts(disease):
    text_desc = wikipedia.page(disease).content
    text_title = wikipedia.page(disease).title 

    # facts for the above article 
    summ = summarizer.summarize(title=text_title, text=text_desc, count=30)

    # clean summ from garbage values 
    clean_list = [] # empty list for the cleaned facts

    for s in summ:
        clean_list.append(remove_grabage(s)[0].replace("\n", " "))
    
    # summ_txt = ' '.join(word.encode('utf-8') for word in clean_list[:10])
    # summ_txt = summ_txt.replace(". ", ".\n\n")
    
    return clean_list
