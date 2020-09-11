 y1 = dfo.str.extractall(r'(?P<am>\d?\d)/(?P<bd>\d?\d)/(?P<cy>\d{2,4})|(?P<dm>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[.-]? ?(?:(?P<ed>\d?\d)[,-])? ?(?P<fy>\d{4})|(?P<gd>\d?\d) (?P<hm>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[.,]? (?P<jy>\d{4})[.,;\\s ]|(?P<km>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?P<md>\d\d)\w\w, (?P<ny>\d{4})|(?P<om>\d?\d)/(?P<py>\d{4})|[^\d](?P<qy>\d{4})[^\d]')
    #f = ['-'.join([m,d,y]) for x in y1 ]
    #return y1.rank(method='dense').sub(1).astype(int)
    y1 = y1.fillna(0)
    dyear1 = pd.DataFrame()
    dyear2 = pd.DataFrame()
    
    y1['cy2'] = y1['cy'].apply(lambda x: int(x)+1900 if len(str(x)) == 2 else x)
    dyear1['year'] = pd.DataFrame(y1['cy2'])
    dyear2['year'] = pd.DataFrame(y1['fy'])
    
    return dyear1

