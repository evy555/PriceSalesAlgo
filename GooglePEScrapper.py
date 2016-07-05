import pandas as pd

list_of_stocks = ['ijr', 'ijh', 'fcom', 'ive', 'ewj', 'ieur', 'fsta']




def getpe_google(stocks):
    pe_list = dict()  
    pe_list['ticker'] = []
    pe_list['value'] = []
    for ticker in stocks:
        try:
            key_statistics = pd.read_html('https://www.google.com/finance?q=' + str(ticker) + '&ei')
        except:
            key_statistics = pd.read_html('https://www.google.com/finance?q=NYSEARCA%3A' + str(ticker) + '&ei')
        convert = key_statistics[0][1][5:6] 
        input = convert.tolist()  
        pe_list['ticker'].append(ticker) 
        pe_list['value'].extend(input) 
    return(pe_list)
        
         

list = getpe_google(list_of_stocks) 
df = pd.DataFrame(list) 
print(df)  

