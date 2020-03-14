#https://smartcities.data.gov.in/resources/digital-payments-visakhapatnam-2017-2018/api#/Resource/get_resource_39ec31e3_3f0e_4bbf_8fe4_97f028aa162d
import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get("https://api.data.gov.in/resource/64a06584-154d-46a9-9b53-80f84c08ee22?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=16")
print response.status_code
data=response.json()
print data['title']
list_of_data=data['records']
Bank_Rate=[]
Year=[]
Lending_Rate=[]

for i in range(len(list_of_data)-1):
	print "Year "+list_of_data[i]['_year']
	x=list_of_data[i]['_year'][:4]
	print x
	Year.append(int(x))
	print "RBI Bank Rate "+list_of_data[i]['reserve_bank___bank_rate']
	Bank_Rate.append(float(list_of_data[i]['reserve_bank___bank_rate']))
	print "Lending Rates "+list_of_data[i]['lending_rates']
	Lending_Rate.append(list_of_data[i]['lending_rates'])

print Year
print Bank_Rate

data_dict={'Year':Year,'RBI_Bank_Rate':Bank_Rate}
df=pd.DataFrame(data_dict,columns=['Year','RBI_Bank_Rate'])
print type(df)
plot_one=df.plot(x='Year',y='RBI_Bank_Rate',kind='line')
#plot_two=df.plot(x='Year',y='RBI_Bank_Rate',kind='scatter')
plt.ylim(5,10)
plt.xlim(2000,2015)
plt.show()





	

	

