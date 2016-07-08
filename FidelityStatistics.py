import pandas as pd

def Get_Statistics_Fidelity(ETFs):
    ps_list = dict()  
    ps_list['Ticker'] = []
    ps_list['PriceSales'] = []
    ps_list['PriceEarnings'] = []
    ps_list['Dividend'] = []
    ps_list['ExpenseRatio'] = []
    ps_list['Net_Assets'] = [] 
    
    for ticker in ETFs:
        try:
            key_statistics = pd.read_html('https://screener.fidelity.com/ftgw/etf/goto/snapshot/keyStatistics.jhtml?symbols=' + str(ticker)) 
            not_valid_test = key_statistics[3][1][18:19].tolist() 
            if len(not_valid_test) < 1:
                print(str(ticker) + ' does not have net asset information or is a bond ETF and therefore will be omitted') 
            else: 
                valid_ticker = ticker 
                
                inputps = key_statistics[3][1][8:9].tolist() 
                inputps = [float(i) for i in inputps]
                
                inputpe = key_statistics[3][1][6:7].tolist()
                inputpe = [float(i) for i in inputpe]
                
                inputdividend = key_statistics[3][1][11:12].str.strip('%').tolist() 
                if len(inputdividend) < 1:
                    inputdividend = [0]
                else:
                    inputdividend = [float(i)/100 for i in inputdividend]
                
                inputexpense = key_statistics[3][1][12:13].str.strip('%').tolist() 
                inputexpense = [float(i) for i in inputexpense]
                if len(inputexpense) < 1:
                    inputexpense = [0] 
                
                inputassets = key_statistics[3][1][18:19].str.strip('$').tolist()
                for i in inputassets:
                    if 'M' in i:
                        i = i.strip('M')
                        i = float(i)/100
                        inputassets[0] = i  
                        inputassets = [float(i) for i in inputassets]
                    elif 'B' in i:
                        i = i.strip('B') 
                        inputassets[0] = i
                        inputassets = [float(i) for i in inputassets]
                
                ps_list['Ticker'].append(valid_ticker) 
                ps_list['PriceSales'].extend(inputps) 
                ps_list['PriceEarnings'].extend(inputpe)
                ps_list['Dividend'].extend(inputdividend)
                ps_list['ExpenseRatio'].extend(inputexpense)  
                ps_list['Net_Assets'].extend(inputassets) 
        except:
            print(str(ticker) + ': an error occured with this ticker symbol')      
    Table = pd.DataFrame(ps_list) 
    Table.set_index(['Ticker'], inplace = True)
    return(Table) 
 

