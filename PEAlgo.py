import pandas as pd

list_of_stocks = ['ijr', 'ijh', 'fcom', 'ive', 'ewj']




def getpe(stocks):
    pe_list = dict()  
    pe_list['ticker'] = []
    pe_list['value'] = []
    for ticker in stocks:
        key_statistics = pd.read_html('https://www.google.com/finance?q=' + str(ticker) + '&ei')
        convert = key_statistics[0][1][5:6] 
        input = convert.tolist()  
        pe_list['ticker'].append(ticker) 
        pe_list['value'].extend(input) 
    return(pe_list)
        
         

list = getpe(list_of_stocks) 
df = pd.DataFrame(list) 
print(df)  

