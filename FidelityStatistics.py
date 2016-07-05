import pandas as pd

list_of_stocks = ['asdfasfas','ijr','ijh', 'fcom', 'ive', 'ewj', 'ieur', 'fsta']


def Get_Statistics_Fidelity(ETFs):
    ps_list = dict()  
    ps_list['Ticker'] = []
    ps_list['PriceSales'] = []
    ps_list['PriceEarnings'] = []
    ps_list['Dividend'] = []
    ps_list['ExpenseRatio'] = []
    
    for ticker in ETFs:
        try:
            key_statistics = pd.read_html('https://screener.fidelity.com/ftgw/etf/goto/snapshot/keyStatistics.jhtml?symbols=' + str(ticker)) 
            not_valid_test = key_statistics[3][1][8:9].tolist() 
            if len(not_valid_test) < 1:
                print(str(ticker) + ' does not have price to sales info and therefore may be missing information and will be omitted') 
            else: 
                valid_ticker = ticker 
                inputps = key_statistics[3][1][8:9].tolist() 
                inputpe = key_statistics[3][1][6:7].tolist() 
                inputdividend = key_statistics[3][1][11:12].tolist() 
                inputexpense = key_statistics[3][1][12:13].tolist() 
                ps_list['Ticker'].append(valid_ticker) 
                ps_list['PriceSales'].extend(inputps) 
                ps_list['PriceEarnings'].extend(inputpe)
                ps_list['Dividend'].extend(inputdividend)
                ps_list['ExpenseRatio'].extend(inputexpense)  
        except:
            print(str(ticker) + ': an error occured with this ticker symbol') 
    print(ps_list)          
    Table = pd.DataFrame(ps_list) 
    return(Table)
        
         
print(Get_Statistics_Fidelity(list_of_stocks))

