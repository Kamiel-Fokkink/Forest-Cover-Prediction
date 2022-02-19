import pandas as pddef transformSoilType(data):        ELUmap = {1:'2702', 2:'2703', 3:'2704', 4:'2705', 5:'2706', 6:'2717',               7:'3501', 8:'3502', 9:'4201', 10:'4703', 11:'4704', 12:'4744',               13:'4758', 14:'5101', 15:'5151', 16:'6101', 17:'6102', 18:'6731',              19:'7101', 20:'7102', 21:'7103', 22:'7201', 23:'7202', 24:'7700',              25:'7701', 26:'7702', 27:'7709', 28:'7710', 29:'7745', 30:'7746',              31:'7755', 32:'7756', 33:'7757', 34:'7790', 35:'8703', 36:'8707',              37:'8708', 38:'8771', 39:'8772', 40:'8776'}        new_cols = ['ClimaticZone' + str(i) for i in range(2,9)]    new_cols += ['GeologicZone' + str(i) for i in [1,2,5,7]]    ELUdigits = set()    for v in ELUmap.values():        ELUdigits.add(v[2:4])    new_cols += ['ELUValue' + i for i in list(ELUdigits)]        soil_cols = ['Soil_Type' + str(i) for i in range(1,41)]    soil_data = data[soil_cols]    new_df = pd.DataFrame(0, index=data['Id'], columns=new_cols)        i = 0    for index, row in soil_data.iterrows():        #i += 1        #if i ==2:        #    break        soil_type = row[row==1].index[0]        #print("At iteration" + str(i))        #print(row)        #print(soil_type)        #print(index)        ELUcode = ELUmap[int(soil_type[9:])]        #print(ELUcode)        new_df.iloc[index]['ClimaticZone'+ELUcode[0]] = 1        new_df.iloc[index]['GeologicZone'+ELUcode[1]] = 1        new_df.iloc[index]['ELUValue'+ELUcode[2:4]] = 1            return pd.merge(data.drop(columns=soil_cols), new_df, left_on=['Id'], right_index=True)